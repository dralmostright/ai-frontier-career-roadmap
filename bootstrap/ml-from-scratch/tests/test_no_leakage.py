"""Week 10 — leakage tests.

This file is the deliverable for Week 10, and it is a template you should carry
into every project for the rest of the course. Leakage does not announce itself:
it looks like a great validation score. The only defense is a test suite that
asserts the discipline.

The single most important test here is
``TestTargetEncoder::test_fit_transform_must_differ_from_fit_then_transform``.
If out-of-fold encoding is not implemented, that test fails and every model
built on top of the encoder is producing fiction.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest
from features import (
    MissingValueImputer,
    OneHotEncoder,
    Pipeline,
    StandardScaler,
    TargetEncoder,
    detect_target_leakage,
    detect_train_test_contamination,
    temporal_split_check,
)

pytestmark = pytest.mark.week(10)


@pytest.fixture
def frame(rng):
    n = 400
    return pd.DataFrame(
        {
            "numeric": rng.normal(loc=10.0, scale=3.0, size=n),
            "category": rng.choice(["a", "b", "c"], size=n),
            "with_nulls": np.where(rng.random(n) < 0.2, np.nan, rng.normal(size=n)),
            "timestamp": pd.date_range("2026-01-01", periods=n, freq="h"),
        }
    )


@pytest.fixture
def target(rng):
    return (rng.random(400) < 0.3).astype(int)


# ---------------------------------------------------------------------------
# The core discipline: fit on train, apply to test
# ---------------------------------------------------------------------------


class TestFitTransformSeparation:
    def test_scaler_uses_training_statistics_only(self, frame):
        """Transforming test data must not recompute the mean."""
        train, test = frame.iloc[:300], frame.iloc[300:]
        scaler = StandardScaler().fit(train[["numeric"]])

        scaled_test = scaler.transform(test[["numeric"]])
        expected = (test[["numeric"]] - train["numeric"].mean()) / train["numeric"].std(ddof=0)
        np.testing.assert_allclose(scaled_test.to_numpy(), expected.to_numpy(), atol=1e-6)

    def test_scaled_test_data_is_not_exactly_zero_mean(self, frame):
        """If it is, you refit on the test set. That is the bug."""
        train, test = frame.iloc[:300], frame.iloc[300:]
        scaled = StandardScaler().fit(train[["numeric"]]).transform(test[["numeric"]])
        assert abs(scaled["numeric"].mean()) > 1e-8

    def test_encoder_vocabulary_comes_from_training_only(self, frame):
        train = frame.iloc[:300].copy()
        test = frame.iloc[300:].copy()
        train.loc[train.index[:5], "category"] = "a"
        test.loc[test.index[:5], "category"] = "unseen_category"

        encoder = OneHotEncoder(handle_unknown="ignore").fit(train[["category"]])
        encoded = encoder.transform(test[["category"]])
        assert not any("unseen_category" in str(c) for c in encoded.columns)

    def test_unseen_category_does_not_crash(self, frame):
        train, test = frame.iloc[:300].copy(), frame.iloc[300:].copy()
        test.loc[test.index[0], "category"] = "brand_new"
        encoder = OneHotEncoder(handle_unknown="ignore").fit(train[["category"]])
        encoder.transform(test[["category"]])  # must not raise

    def test_imputer_uses_training_median(self, frame):
        train = frame.iloc[:300]
        imputer = MissingValueImputer(strategy="median").fit(train[["with_nulls"]])
        assert imputer.statistics_["with_nulls"] == pytest.approx(
            train["with_nulls"].median(), abs=1e-9
        )


# ---------------------------------------------------------------------------
# Target encoding — the highest-risk transformation in the module
# ---------------------------------------------------------------------------


class TestTargetEncoder:
    def test_fit_transform_must_differ_from_fit_then_transform(self, frame, target):
        """**The critical test.**

        `fit_transform` must use out-of-fold encoding, so a row's own target
        never contributes to its own feature value. If these two paths agree,
        out-of-fold encoding is not implemented and you are leaking.
        """
        encoder = TargetEncoder(n_folds=5, random_state=0)
        oof = encoder.fit_transform(frame[["category"]], target)
        in_fold = (
            TargetEncoder(n_folds=5, random_state=0)
            .fit(frame[["category"]], target)
            .transform(frame[["category"]])
        )
        assert not np.allclose(oof.to_numpy(), in_fold.to_numpy())

    def test_encoding_does_not_perfectly_predict_the_target(self, rng):
        """With a unique category per row, naive encoding reproduces the target
        exactly. Out-of-fold encoding must not."""
        n = 300
        df = pd.DataFrame({"id_like": [f"cat_{i}" for i in range(n)]})
        y = (rng.random(n) < 0.5).astype(int)

        encoded = TargetEncoder(n_folds=5, random_state=0).fit_transform(df, y)
        correlation = np.corrcoef(encoded.iloc[:, 0].to_numpy(), y)[0, 1]
        assert abs(correlation) < 0.3, "the encoder is leaking the target"

    def test_smoothing_pulls_rare_categories_toward_the_global_mean(self, rng):
        df = pd.DataFrame({"cat": ["common"] * 200 + ["rare"]})
        y = np.concatenate([(rng.random(200) < 0.3).astype(int), [1]])

        strong = TargetEncoder(smoothing=100.0, n_folds=5, random_state=0).fit(df, y)
        weak = TargetEncoder(smoothing=0.01, n_folds=5, random_state=0).fit(df, y)

        global_mean = y.mean()
        strong_rare = strong.transform(pd.DataFrame({"cat": ["rare"]})).iloc[0, 0]
        weak_rare = weak.transform(pd.DataFrame({"cat": ["rare"]})).iloc[0, 0]
        assert abs(strong_rare - global_mean) < abs(weak_rare - global_mean)


# ---------------------------------------------------------------------------
# Pipelines
# ---------------------------------------------------------------------------


class TestPipeline:
    def test_chains_transformers(self, frame):
        pipe = Pipeline([("impute", MissingValueImputer()), ("scale", StandardScaler())])
        result = pipe.fit(frame[["with_nulls"]]).transform(frame[["with_nulls"]])
        assert not result.isna().any().any()

    def test_refitting_inside_folds_prevents_leakage(self, frame, target):
        """A pipeline exists so cross-validation cannot accidentally see the
        validation fold during preprocessing."""
        train, test = frame.iloc[:300], frame.iloc[300:]
        pipe = Pipeline([("scale", StandardScaler())])
        pipe.fit(train[["numeric"]])
        first = pipe.transform(test[["numeric"]]).to_numpy()

        pipe.transform(test[["numeric"]])  # must not mutate fitted state
        second = pipe.transform(test[["numeric"]]).to_numpy()
        np.testing.assert_allclose(first, second)


# ---------------------------------------------------------------------------
# Detection
# ---------------------------------------------------------------------------


class TestLeakageDetection:
    def test_flags_a_feature_that_is_the_target(self, frame, target):
        contaminated = frame.copy()
        contaminated["leaked"] = target.astype(float)
        flagged = detect_target_leakage(contaminated.drop(columns=["timestamp"]), target)
        assert any(name == "leaked" for name, _ in flagged)

    def test_does_not_flag_honest_features(self, frame, target):
        flagged = detect_target_leakage(frame.drop(columns=["timestamp"]), target)
        assert not flagged

    def test_finds_exact_duplicates_across_splits(self, frame):
        train = frame.iloc[:300]
        test = pd.concat([frame.iloc[300:], frame.iloc[:20]])  # 20 rows leaked in
        report = detect_train_test_contamination(train, test)
        assert report["exact_duplicates"] >= 20

    def test_clean_split_reports_no_contamination(self, frame):
        report = detect_train_test_contamination(frame.iloc[:300], frame.iloc[300:])
        assert report["exact_duplicates"] == 0

    def test_temporal_split_check_accepts_a_sound_split(self, frame):
        train_idx = np.arange(300)
        test_idx = np.arange(300, 400)
        assert temporal_split_check(frame, "timestamp", train_idx, test_idx)

    def test_temporal_split_check_rejects_a_random_split(self, frame, rng):
        """A random split on time series lets the model learn from the future."""
        shuffled = rng.permutation(400)
        assert not temporal_split_check(frame, "timestamp", shuffled[:300], shuffled[300:])
