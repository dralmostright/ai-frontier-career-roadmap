"""Week 8 — bagging and random forests.

The tests are ordered to build the argument: bootstrap works, bagging reduces
variance, feature subsampling decorrelates, and decorrelation is what makes the
averaging pay off.
"""

from __future__ import annotations

import numpy as np
import pytest
from decision_tree import DecisionTreeClassifier
from metrics import accuracy
from random_forest import (
    RandomForestClassifier,
    RandomForestRegressor,
    bootstrap_sample,
    permutation_importance,
)

pytestmark = pytest.mark.week(8)


@pytest.fixture
def noisy(rng):
    X = rng.normal(size=(500, 8))
    y = ((X[:, 0] + X[:, 1] - X[:, 2] + rng.normal(scale=1.2, size=500)) > 0).astype(int)
    return X, y


@pytest.fixture
def split(noisy, rng):
    X, y = noisy
    idx = rng.permutation(len(y))
    train, test = idx[:350], idx[350:]
    return X[train], y[train], X[test], y[test]


class TestBootstrap:
    def test_output_size_matches_input(self, noisy, rng):
        X, y = noisy
        X_boot, y_boot, _ = bootstrap_sample(X, y, rng)
        assert len(X_boot) == len(X) and len(y_boot) == len(y)

    def test_samples_with_replacement(self, noisy, rng):
        X, y = noisy
        X_boot, _, _ = bootstrap_sample(X, y, rng)
        assert len(np.unique(X_boot, axis=0)) < len(X)

    def test_oob_fraction_approaches_one_over_e(self, noisy, rng):
        """(1 - 1/n)^n -> 1/e ≈ 0.368. Be able to derive this."""
        X, y = noisy
        fractions = [len(bootstrap_sample(X, y, rng)[2]) / len(X) for _ in range(40)]
        assert np.mean(fractions) == pytest.approx(1 / np.e, abs=0.02)

    def test_oob_indices_are_genuinely_out_of_bag(self, rng):
        X = np.arange(200).reshape(-1, 1).astype(float)
        y = np.zeros(200)
        X_boot, _, oob = bootstrap_sample(X, y, rng)
        in_bag = set(X_boot.ravel().tolist())
        assert not (set(X[oob].ravel().tolist()) & in_bag)


class TestRandomForestClassifier:
    def test_beats_a_single_tree_on_noisy_data(self, split):
        """The headline claim. If this fails, the ensemble isn't doing anything."""
        X_tr, y_tr, X_te, y_te = split
        tree = DecisionTreeClassifier(random_state=0).fit(X_tr, y_tr)
        forest = RandomForestClassifier(n_estimators=100, random_state=0).fit(X_tr, y_tr)
        assert accuracy(y_te, forest.predict(X_te)) > accuracy(y_te, tree.predict(X_te))

    def test_more_trees_never_hurts(self, split):
        """Contrast with boosting, where more rounds eventually overfits."""
        X_tr, y_tr, X_te, y_te = split
        scores = [
            accuracy(
                y_te,
                RandomForestClassifier(n_estimators=n, random_state=0)
                .fit(X_tr, y_tr)
                .predict(X_te),
            )
            for n in (5, 25, 100)
        ]
        assert scores[2] >= scores[0] - 0.02

    def test_feature_subsampling_decorrelates_the_trees(self, split):
        """The load-bearing idea. Bagging alone leaves the trees too similar."""
        X_tr, y_tr, X_te, _ = split

        def pairwise_agreement(max_features):
            forest = RandomForestClassifier(
                n_estimators=20, max_features=max_features, random_state=0
            ).fit(X_tr, y_tr)
            preds = np.array([t.predict(X_te) for t in forest.trees_])
            agreements = [
                np.mean(preds[i] == preds[j])
                for i in range(len(preds))
                for j in range(i + 1, len(preds))
            ]
            return float(np.mean(agreements))

        assert pairwise_agreement("sqrt") < pairwise_agreement(None)

    def test_probability_averaging_beats_majority_voting(self, split):
        """Voting discards confidence. Averaging keeps it."""
        X_tr, y_tr, X_te, y_te = split
        forest = RandomForestClassifier(n_estimators=50, random_state=0).fit(X_tr, y_tr)
        by_vote = accuracy(y_te, forest.predict(X_te))
        by_proba = accuracy(y_te, (forest.predict_proba(X_te)[:, 1] >= 0.5).astype(int))
        assert by_proba >= by_vote - 0.01

    def test_oob_score_approximates_test_accuracy(self, split):
        """A free validation set, and a genuinely elegant property."""
        X_tr, y_tr, X_te, y_te = split
        forest = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=0)
        forest.fit(X_tr, y_tr)
        assert forest.oob_score_ == pytest.approx(accuracy(y_te, forest.predict(X_te)), abs=0.08)

    def test_proba_is_normalized(self, split):
        X_tr, y_tr, X_te, _ = split
        p = (
            RandomForestClassifier(n_estimators=20, random_state=0)
            .fit(X_tr, y_tr)
            .predict_proba(X_te)
        )
        np.testing.assert_allclose(p.sum(axis=1), np.ones(len(X_te)), atol=1e-12)

    def test_forest_probabilities_are_better_calibrated_than_a_tree(self, split):
        """Averaging many overconfident trees produces something usable."""
        X_tr, y_tr, X_te, _ = split
        tree_p = DecisionTreeClassifier(random_state=0).fit(X_tr, y_tr).predict_proba(X_te)
        forest_p = (
            RandomForestClassifier(n_estimators=100, random_state=0)
            .fit(X_tr, y_tr)
            .predict_proba(X_te)
        )
        assert np.mean(np.max(forest_p, axis=1)) < np.mean(np.max(tree_p, axis=1))

    def test_reproducible_with_a_fixed_seed(self, split):
        X_tr, y_tr, X_te, _ = split
        a = RandomForestClassifier(n_estimators=20, random_state=42).fit(X_tr, y_tr)
        b = RandomForestClassifier(n_estimators=20, random_state=42).fit(X_tr, y_tr)
        np.testing.assert_array_equal(a.predict(X_te), b.predict(X_te))


class TestRandomForestRegressor:
    def test_beats_a_single_tree(self, rng):
        X = rng.uniform(-3, 3, size=(400, 3))
        y = X[:, 0] ** 2 + X[:, 1] + rng.normal(scale=0.5, size=400)
        X_te, y_te = X[300:], y[300:]
        X_tr, y_tr = X[:300], y[:300]

        from decision_tree import DecisionTreeRegressor

        tree_mse = np.mean(
            (DecisionTreeRegressor(random_state=0).fit(X_tr, y_tr).predict(X_te) - y_te) ** 2
        )
        forest_mse = np.mean(
            (
                RandomForestRegressor(n_estimators=100, random_state=0)
                .fit(X_tr, y_tr)
                .predict(X_te)
                - y_te
            )
            ** 2
        )
        assert forest_mse < tree_mse


class TestPermutationImportance:
    def test_ranks_the_real_features_first(self, noisy, rng):
        X, y = noisy  # only features 0, 1, 2 matter
        forest = RandomForestClassifier(n_estimators=50, random_state=0).fit(X, y)
        means, _ = permutation_importance(forest, X, y, scoring=accuracy, n_repeats=5, rng=rng)
        assert set(np.argsort(means)[-3:]) == {0, 1, 2}

    def test_irrelevant_features_score_near_zero(self, noisy, rng):
        X, y = noisy
        forest = RandomForestClassifier(n_estimators=50, random_state=0).fit(X, y)
        means, _ = permutation_importance(forest, X, y, scoring=accuracy, n_repeats=5, rng=rng)
        assert np.all(means[3:] < 0.03)

    def test_correlated_duplicates_split_the_credit(self, rng):
        """The caveat to state unprompted in an interview."""
        X = rng.normal(size=(400, 3))
        X = np.column_stack([X, X[:, 0]])  # column 3 duplicates column 0
        y = (X[:, 0] + rng.normal(scale=0.3, size=400) > 0).astype(int)
        forest = RandomForestClassifier(n_estimators=50, random_state=0).fit(X, y)
        means, _ = permutation_importance(forest, X, y, scoring=accuracy, n_repeats=5, rng=rng)
        assert means[0] < 0.35 and means[3] < 0.35
