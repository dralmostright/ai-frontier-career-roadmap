"""Week 11 — cross-validation, uncertainty, and calibration."""

from __future__ import annotations

import numpy as np
import pytest
from evaluation import (
    IsotonicCalibration,
    PlattScaling,
    bootstrap_metric_ci,
    brier_score,
    calibration_curve,
    class_weights,
    cross_validate,
    expected_calibration_error,
    group_k_fold_split,
    k_fold_split,
    learning_curve,
    paired_bootstrap_test,
    resample,
    stratified_k_fold_split,
    time_series_split,
)
from logistic_regression import LogisticRegression
from metrics import accuracy, roc_auc

pytestmark = pytest.mark.week(11)


@pytest.fixture
def data(rng):
    X = rng.normal(size=(400, 4))
    y = ((X[:, 0] + X[:, 1] + rng.normal(scale=0.8, size=400)) > 0).astype(int)
    return X, y


@pytest.fixture
def skewed(rng):
    """5% positive rate."""
    y = (rng.random(500) < 0.05).astype(int)
    X = rng.normal(size=(500, 3)) + y[:, None]
    return X, y


class TestSplitters:
    def test_k_fold_covers_every_row_exactly_once(self):
        seen = np.zeros(100, dtype=int)
        for _, val in k_fold_split(100, n_splits=5, random_state=0):
            seen[val] += 1
        np.testing.assert_array_equal(seen, np.ones(100, dtype=int))

    def test_k_fold_train_and_val_are_disjoint(self):
        for train, val in k_fold_split(100, n_splits=5, random_state=0):
            assert not set(train.tolist()) & set(val.tolist())

    def test_stratified_preserves_class_ratio(self, skewed):
        _, y = skewed
        overall = y.mean()
        for _, val in stratified_k_fold_split(y, n_splits=5, random_state=0):
            assert y[val].mean() == pytest.approx(overall, abs=0.03)

    def test_plain_k_fold_can_produce_an_empty_class(self, rng):
        """Why stratification is mandatory on imbalanced data."""
        y = np.zeros(200, dtype=int)
        y[:4] = 1  # 2% positive
        empty_folds = sum(
            1 for _, val in k_fold_split(200, n_splits=10, random_state=3) if y[val].sum() == 0
        )
        assert empty_folds > 0

    def test_time_series_split_never_trains_on_the_future(self):
        for train, val in time_series_split(100, n_splits=5):
            assert train.max() < val.min()

    def test_time_series_windows_expand(self):
        sizes = [len(train) for train, _ in time_series_split(100, n_splits=5)]
        assert sizes == sorted(sizes)

    def test_group_k_fold_keeps_groups_together(self, rng):
        groups = np.repeat(np.arange(20), 5)
        for train, val in group_k_fold_split(groups, n_splits=4):
            assert not set(groups[train].tolist()) & set(groups[val].tolist())


class TestCrossValidate:
    def test_returns_one_score_per_fold(self, data):
        X, y = data
        results = cross_validate(
            lambda: LogisticRegression(n_iters=300), X, y, cv=5, scoring={"acc": accuracy}
        )
        assert len(results["acc"]) == 5

    def test_scores_are_plausible(self, data):
        X, y = data
        results = cross_validate(
            lambda: LogisticRegression(n_iters=500), X, y, cv=5, scoring={"acc": accuracy}
        )
        assert 0.6 < np.mean(results["acc"]) < 1.0

    def test_uses_a_fresh_model_per_fold(self, data):
        """Reusing one fitted instance silently invalidates the whole exercise."""
        X, y = data
        created = []

        def factory():
            model = LogisticRegression(n_iters=100)
            created.append(model)
            return model

        cross_validate(factory, X, y, cv=5, scoring={"acc": accuracy})
        assert len(created) == 5
        assert len({id(m) for m in created}) == 5


class TestUncertainty:
    def test_ci_brackets_the_point_estimate(self, data):
        X, y = data
        model = LogisticRegression(n_iters=500).fit(X, y)
        point, lo, hi = bootstrap_metric_ci(y, model.predict(X), accuracy, n_resamples=500)
        assert lo <= point <= hi

    def test_ci_narrows_with_more_data(self, rng):
        small_y = (rng.random(50) < 0.5).astype(int)
        large_y = (rng.random(5000) < 0.5).astype(int)
        _, lo_s, hi_s = bootstrap_metric_ci(small_y, small_y, accuracy, n_resamples=500)
        _, lo_l, hi_l = bootstrap_metric_ci(large_y, large_y, accuracy, n_resamples=500)
        assert (hi_l - lo_l) <= (hi_s - lo_s)

    def test_paired_test_detects_a_real_difference(self, data):
        X, y = data
        good = LogisticRegression(n_iters=1000).fit(X, y).predict_proba(X)
        bad = np.clip(good + np.random.default_rng(0).normal(scale=0.3, size=len(y)), 0, 1)
        result = paired_bootstrap_test(y, good, bad, roc_auc, n_resamples=500)
        assert result["difference"] > 0
        assert result["p_value"] < 0.05

    def test_paired_test_finds_no_difference_between_identical_models(self, data):
        X, y = data
        p = LogisticRegression(n_iters=500).fit(X, y).predict_proba(X)
        result = paired_bootstrap_test(y, p, p.copy(), roc_auc, n_resamples=500)
        assert result["difference"] == pytest.approx(0.0, abs=1e-9)
        assert result["p_value"] > 0.5

    def test_learning_curve_shapes(self, data):
        X, y = data
        sizes, train, val = learning_curve(lambda: LogisticRegression(n_iters=300), X, y, cv=3)
        assert len(sizes) == len(train) == len(val)
        assert sizes[0] < sizes[-1]

    def test_learning_curve_validation_improves_with_data(self, data):
        X, y = data
        _, _, val = learning_curve(lambda: LogisticRegression(n_iters=500), X, y, cv=3)
        assert val[-1] >= val[0]


class TestCalibration:
    @pytest.fixture
    def overconfident(self, rng):
        """Predictions pushed toward 0 and 1 — the classic tree/boosting signature."""
        y = (rng.random(2000) < 0.5).astype(int)
        base = np.clip(rng.normal(loc=0.5 + 0.25 * (2 * y - 1), scale=0.15), 0.01, 0.99)
        sharpened = np.clip((base - 0.5) * 2.5 + 0.5, 0.001, 0.999)
        return y, base, sharpened

    def test_curve_shapes(self, overconfident):
        y, base, _ = overconfident
        pred, obs, counts = calibration_curve(y, base, n_bins=10)
        assert len(pred) == len(obs) == len(counts)

    def test_quantile_strategy_balances_bin_counts(self, rng):
        """Uniform bins are useless when predictions cluster."""
        y = (rng.random(2000) < 0.1).astype(int)
        probs = np.clip(rng.beta(2, 20, size=2000), 0, 1)
        _, _, uniform = calibration_curve(y, probs, n_bins=10, strategy="uniform")
        _, _, quantile = calibration_curve(y, probs, n_bins=10, strategy="quantile")
        assert np.std(quantile) < np.std(uniform)

    def test_ece_is_low_for_a_calibrated_model(self, rng):
        probs = rng.random(5000)
        y = (rng.random(5000) < probs).astype(int)  # calibrated by construction
        assert expected_calibration_error(y, probs, n_bins=10) < 0.05

    def test_ece_is_high_for_an_overconfident_model(self, overconfident):
        y, base, sharpened = overconfident
        assert expected_calibration_error(y, sharpened) > expected_calibration_error(y, base)

    def test_brier_score_bounds(self, rng):
        y = (rng.random(500) < 0.5).astype(int)
        assert brier_score(y, y.astype(float)) == pytest.approx(0.0)
        assert brier_score(y, 1.0 - y) == pytest.approx(1.0)

    def test_platt_scaling_improves_calibration(self, overconfident):
        y, _, sharpened = overconfident
        calibrated = PlattScaling().fit(sharpened[:1000], y[:1000]).transform(sharpened[1000:])
        before = expected_calibration_error(y[1000:], sharpened[1000:])
        after = expected_calibration_error(y[1000:], calibrated)
        assert after < before

    def test_isotonic_improves_calibration(self, overconfident):
        y, _, sharpened = overconfident
        calibrated = (
            IsotonicCalibration().fit(sharpened[:1000], y[:1000]).transform(sharpened[1000:])
        )
        assert expected_calibration_error(y[1000:], calibrated) < expected_calibration_error(
            y[1000:], sharpened[1000:]
        )

    def test_calibration_preserves_ranking(self, overconfident):
        """Calibration should change probabilities, not the ordering — so AUC is
        unchanged. A frequent surprise."""
        y, _, sharpened = overconfident
        calibrated = PlattScaling().fit(sharpened, y).transform(sharpened)
        assert roc_auc(y, calibrated) == pytest.approx(roc_auc(y, sharpened), abs=1e-6)


class TestImbalance:
    def test_class_weights_are_inversely_proportional(self, skewed):
        _, y = skewed
        weights = class_weights(y)
        assert weights[1] > weights[0]

    def test_undersampling_balances_the_classes(self, skewed, rng):
        X, y = skewed
        _, y_res = resample(X, y, strategy="undersample", rng=rng)
        assert y_res.mean() == pytest.approx(0.5, abs=0.05)

    def test_oversampling_grows_the_minority(self, skewed, rng):
        X, y = skewed
        _, y_res = resample(X, y, strategy="oversample", rng=rng)
        assert len(y_res) > len(y)
        assert y_res.mean() == pytest.approx(0.5, abs=0.05)
