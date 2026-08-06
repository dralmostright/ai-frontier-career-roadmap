"""Week 7 — decision trees."""

from __future__ import annotations

import numpy as np
import pytest
from decision_tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    entropy,
    gini,
    variance_reduction,
)
from metrics import accuracy

pytestmark = pytest.mark.week(7)


@pytest.fixture
def axis_aligned(rng):
    """A problem trees solve perfectly: label depends on axis-aligned thresholds."""
    X = rng.uniform(0, 10, size=(400, 2))
    y = ((X[:, 0] > 5) ^ (X[:, 1] > 5)).astype(int)  # XOR of two thresholds
    return X, y


@pytest.fixture
def noisy(rng):
    X = rng.normal(size=(300, 5))
    y = (X[:, 0] + X[:, 1] + rng.normal(scale=1.5, size=300) > 0).astype(int)
    return X, y


class TestImpurity:
    def test_pure_node_is_zero(self):
        pure = np.array([1, 1, 1, 1])
        assert gini(pure) == pytest.approx(0.0)
        assert entropy(pure) == pytest.approx(0.0)

    def test_balanced_binary_node(self):
        balanced = np.array([0, 0, 1, 1])
        assert gini(balanced) == pytest.approx(0.5)
        assert entropy(balanced) == pytest.approx(1.0)

    def test_maximum_impurity_for_k_classes(self):
        uniform = np.array([0, 1, 2, 3])
        assert gini(uniform) == pytest.approx(0.75)
        assert entropy(uniform) == pytest.approx(2.0)

    def test_impurity_increases_with_mixing(self):
        assert gini(np.array([0] * 9 + [1])) < gini(np.array([0] * 5 + [1] * 5))

    def test_variance_reduction_of_a_perfect_split(self):
        y = np.array([1.0, 1.0, 5.0, 5.0])
        assert variance_reduction(y, np.array([1.0, 1.0]), np.array([5.0, 5.0])) > 0
        assert variance_reduction(y, y, np.array([])) == pytest.approx(0.0, abs=1e-12)


class TestDecisionTreeClassifier:
    def test_fits_axis_aligned_data_perfectly(self, axis_aligned):
        X, y = axis_aligned
        assert accuracy(y, DecisionTreeClassifier().fit(X, y).predict(X)) > 0.99

    def test_unconstrained_tree_memorizes_the_training_set(self, noisy):
        """Why trees overfit — demonstrated, not asserted."""
        X, y = noisy
        assert accuracy(y, DecisionTreeClassifier().fit(X, y).predict(X)) == pytest.approx(1.0)

    def test_max_depth_prevents_memorization(self, noisy):
        X, y = noisy
        shallow = DecisionTreeClassifier(max_depth=3).fit(X, y)
        assert accuracy(y, shallow.predict(X)) < 0.99
        assert shallow.depth() <= 3

    def test_min_samples_leaf_is_respected(self, noisy):
        X, y = noisy
        tree = DecisionTreeClassifier(min_samples_leaf=25).fit(X, y)

        def check(node):
            if node.is_leaf:
                assert node.n_samples >= 25
            else:
                check(node.left)
                check(node.right)

        check(tree.root_)

    def test_deeper_trees_have_more_leaves(self, noisy):
        X, y = noisy
        assert (
            DecisionTreeClassifier(max_depth=2).fit(X, y).n_leaves()
            < DecisionTreeClassifier(max_depth=6).fit(X, y).n_leaves()
        )

    def test_proba_rows_sum_to_one(self, noisy):
        X, y = noisy
        p = DecisionTreeClassifier(max_depth=4).fit(X, y).predict_proba(X)
        np.testing.assert_allclose(p.sum(axis=1), np.ones(len(y)), atol=1e-12)

    def test_deep_tree_probabilities_are_overconfident(self, noisy):
        """Pure leaves report 1.0 on the strength of two samples. Week 11 fixes it."""
        X, y = noisy
        p = DecisionTreeClassifier().fit(X, y).predict_proba(X)
        assert np.mean(np.max(p, axis=1) > 0.99) > 0.9

    def test_single_class_input_produces_a_leaf(self):
        X = np.array([[1.0], [2.0], [3.0]])
        tree = DecisionTreeClassifier().fit(X, np.array([1, 1, 1]))
        assert tree.root_.is_leaf

    def test_criteria_usually_agree(self, noisy):
        """Gini and entropy rarely differ. Say that, not something deeper."""
        X, y = noisy
        g = DecisionTreeClassifier(criterion="gini", max_depth=4).fit(X, y)
        e = DecisionTreeClassifier(criterion="entropy", max_depth=4).fit(X, y)
        agreement = np.mean(g.predict(X) == e.predict(X))
        assert agreement > 0.9

    def test_max_features_makes_trees_differ(self, noisy):
        """The knob that turns bagging into a random forest in Week 8."""
        X, y = noisy
        a = DecisionTreeClassifier(max_features=1, random_state=1, max_depth=5).fit(X, y)
        b = DecisionTreeClassifier(max_features=1, random_state=2, max_depth=5).fit(X, y)
        assert not np.array_equal(a.predict(X), b.predict(X))

    def test_print_tree_returns_readable_text(self, noisy):
        X, y = noisy
        text = DecisionTreeClassifier(max_depth=2).fit(X, y).print_tree()
        assert isinstance(text, str) and len(text.splitlines()) >= 3


class TestDecisionTreeRegressor:
    def test_fits_a_step_function(self, rng):
        X = rng.uniform(0, 10, size=(300, 1))
        y = np.where(X[:, 0] < 5, 1.0, 10.0)
        pred = DecisionTreeRegressor(max_depth=3).fit(X, y).predict(X)
        assert np.mean((pred - y) ** 2) < 0.1

    def test_predictions_are_piecewise_constant(self, rng):
        """Trees cannot extrapolate or interpolate smoothly. Know this limitation."""
        X = rng.uniform(0, 10, size=(200, 1))
        y = X[:, 0] * 2.0
        pred = DecisionTreeRegressor(max_depth=3).fit(X, y).predict(X)
        assert len(np.unique(np.round(pred, 6))) <= 8

    def test_cannot_extrapolate(self, rng):
        X = rng.uniform(0, 10, size=(200, 1))
        y = X[:, 0] * 2.0
        tree = DecisionTreeRegressor(max_depth=5).fit(X, y)
        far = tree.predict(np.array([[1000.0]]))[0]
        assert far < 25.0, "a tree clamps to its training range; it never extrapolates"
