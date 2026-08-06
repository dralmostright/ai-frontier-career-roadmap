"""Week 9 — gradient boosting.

The tests are designed to make the bagging/boosting contrast concrete: boosting
reduces bias with weak learners, and unlike a forest it will overfit if you keep
going.
"""

from __future__ import annotations

import numpy as np
import pytest
from boosting import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    early_stopping_round,
)
from metrics import accuracy

pytestmark = pytest.mark.week(9)


@pytest.fixture
def regression_data(rng):
    X = rng.uniform(-3, 3, size=(400, 2))
    y = np.sin(X[:, 0]) * 3 + X[:, 1] ** 2 * 0.5 + rng.normal(scale=0.2, size=400)
    return X[:300], y[:300], X[300:], y[300:]


@pytest.fixture
def classification_data(rng):
    X = rng.normal(size=(500, 4))
    y = ((X[:, 0] * X[:, 1] + X[:, 2] + rng.normal(scale=0.5, size=500)) > 0).astype(int)
    return X[:350], y[:350], X[350:], y[350:]


class TestGradientBoostingRegressor:
    def test_reduces_error_over_rounds(self, regression_data):
        X_tr, y_tr, _, _ = regression_data
        model = GradientBoostingRegressor(n_estimators=100, random_state=0).fit(X_tr, y_tr)
        assert model.train_scores_[-1] < model.train_scores_[0]

    def test_weak_learners_compose_into_a_strong_one(self, regression_data):
        """Depth-2 stumps individually explain almost nothing. A hundred of them fit well."""
        X_tr, y_tr, X_te, y_te = regression_data
        one = GradientBoostingRegressor(n_estimators=1, max_depth=2, random_state=0).fit(X_tr, y_tr)
        many = GradientBoostingRegressor(n_estimators=200, max_depth=2, random_state=0).fit(
            X_tr, y_tr
        )
        assert np.mean((many.predict(X_te) - y_te) ** 2) < 0.3 * np.mean(
            (one.predict(X_te) - y_te) ** 2
        )

    def test_lower_learning_rate_needs_more_rounds(self, regression_data):
        X_tr, y_tr, X_te, y_te = regression_data
        fast = GradientBoostingRegressor(n_estimators=30, learning_rate=0.3, random_state=0).fit(
            X_tr, y_tr
        )
        slow = GradientBoostingRegressor(n_estimators=30, learning_rate=0.02, random_state=0).fit(
            X_tr, y_tr
        )
        assert np.mean((slow.predict(X_te) - y_te) ** 2) > np.mean((fast.predict(X_te) - y_te) ** 2)

    def test_staged_predict_yields_one_prediction_per_round(self, regression_data):
        X_tr, y_tr, X_te, _ = regression_data
        model = GradientBoostingRegressor(n_estimators=25, random_state=0).fit(X_tr, y_tr)
        stages = list(model.staged_predict(X_te))
        assert len(stages) == 25
        np.testing.assert_allclose(stages[-1], model.predict(X_te), atol=1e-9)

    def test_too_many_rounds_overfits(self, rng):
        """The key contrast with random forests, where more trees is always safe."""
        X = rng.uniform(-2, 2, size=(120, 1))
        y = X[:, 0] + rng.normal(scale=1.0, size=120)
        X_te = rng.uniform(-2, 2, size=(400, 1))
        y_te = X_te[:, 0]

        modest = GradientBoostingRegressor(n_estimators=20, max_depth=4, random_state=0).fit(X, y)
        excessive = GradientBoostingRegressor(n_estimators=800, max_depth=4, random_state=0).fit(
            X, y
        )
        assert np.mean((excessive.predict(X_te) - y_te) ** 2) > np.mean(
            (modest.predict(X_te) - y_te) ** 2
        )

    def test_deep_base_learners_hurt(self, regression_data):
        """Boosting wants weak learners. A deep first tree leaves no residual."""
        X_tr, y_tr, X_te, y_te = regression_data
        shallow = GradientBoostingRegressor(n_estimators=60, max_depth=2, random_state=0).fit(
            X_tr, y_tr
        )
        deep = GradientBoostingRegressor(n_estimators=60, max_depth=12, random_state=0).fit(
            X_tr, y_tr
        )
        assert np.mean((shallow.predict(X_te) - y_te) ** 2) < np.mean(
            (deep.predict(X_te) - y_te) ** 2
        )

    def test_subsampling_regularizes(self, regression_data):
        X_tr, y_tr, X_te, y_te = regression_data
        full = GradientBoostingRegressor(
            n_estimators=200, max_depth=4, subsample=1.0, random_state=0
        ).fit(X_tr, y_tr)
        stochastic = GradientBoostingRegressor(
            n_estimators=200, max_depth=4, subsample=0.6, random_state=0
        ).fit(X_tr, y_tr)
        assert (
            np.mean((stochastic.predict(X_te) - y_te) ** 2)
            <= np.mean((full.predict(X_te) - y_te) ** 2) * 1.1
        )


class TestGradientBoostingClassifier:
    def test_learns_a_nonlinear_boundary(self, classification_data):
        X_tr, y_tr, X_te, y_te = classification_data
        model = GradientBoostingClassifier(n_estimators=100, random_state=0).fit(X_tr, y_tr)
        assert accuracy(y_te, model.predict(X_te)) > 0.8

    def test_probabilities_are_valid(self, classification_data):
        X_tr, y_tr, X_te, _ = classification_data
        p = (
            GradientBoostingClassifier(n_estimators=50, random_state=0)
            .fit(X_tr, y_tr)
            .predict_proba(X_te)
        )
        assert np.all((p >= 0) & (p <= 1))
        np.testing.assert_allclose(p.sum(axis=1), np.ones(len(X_te)), atol=1e-10)

    def test_built_from_regression_trees(self, classification_data):
        """A depth check: the classifier's base learners regress on gradients."""
        from decision_tree import DecisionTreeRegressor

        X_tr, y_tr, _, _ = classification_data
        model = GradientBoostingClassifier(n_estimators=10, random_state=0).fit(X_tr, y_tr)
        assert all(isinstance(t, DecisionTreeRegressor) for t in model.trees_)


class TestAdaBoost:
    def test_classifies(self, classification_data):
        X_tr, y_tr, X_te, y_te = classification_data
        model = AdaBoostClassifier(n_estimators=50, random_state=0).fit(X_tr, y_tr)
        assert accuracy(y_te, model.predict(X_te)) > 0.7

    def test_estimator_weights_reflect_accuracy(self, classification_data):
        """Better rounds get more say. That is the whole mechanism."""
        X_tr, y_tr, _, _ = classification_data
        model = AdaBoostClassifier(n_estimators=20, random_state=0).fit(X_tr, y_tr)
        assert len(model.estimator_weights_) == len(model.estimators_)
        assert all(w >= 0 for w in model.estimator_weights_)


class TestEarlyStopping:
    def test_finds_the_minimum(self):
        losses = [1.0, 0.8, 0.6, 0.5, 0.52, 0.55, 0.6, 0.7]
        assert early_stopping_round(losses, patience=2) == 3

    def test_respects_patience(self):
        losses = [1.0, 0.9, 0.91, 0.92, 0.8]
        assert early_stopping_round(losses, patience=5) == 4

    def test_higher_is_better_mode(self):
        scores = [0.5, 0.7, 0.9, 0.85, 0.84]
        assert early_stopping_round(scores, patience=2, higher_is_better=True) == 2
