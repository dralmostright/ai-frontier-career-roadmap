"""Week 5 — linear regression."""

from __future__ import annotations

from itertools import pairwise

import numpy as np
import pytest
from linear_regression import (
    LinearRegression,
    bias_variance_decomposition,
    gradient_descent_step,
    mae,
    mse,
    normal_equation,
    polynomial_features,
    r_squared,
    rmse,
    train_test_split,
)

pytestmark = pytest.mark.week(5)


@pytest.fixture
def linear_data(rng):
    """y = 3x1 - 2x2 + 5 + small noise."""
    X = rng.normal(size=(300, 2))
    y = 3.0 * X[:, 0] - 2.0 * X[:, 1] + 5.0 + rng.normal(scale=0.1, size=300)
    return X, y


class TestLossFunctions:
    def test_perfect_prediction_scores_zero(self):
        y = np.array([1.0, 2.0, 3.0])
        assert mse(y, y) == pytest.approx(0.0)
        assert mae(y, y) == pytest.approx(0.0)

    def test_known_values(self):
        y_true = np.array([0.0, 0.0, 0.0])
        y_pred = np.array([1.0, 2.0, 3.0])
        assert mse(y_true, y_pred) == pytest.approx(14 / 3)
        assert mae(y_true, y_pred) == pytest.approx(2.0)
        assert rmse(y_true, y_pred) == pytest.approx(np.sqrt(14 / 3))

    def test_mse_punishes_outliers_harder_than_mae(self):
        """Why you pick one over the other."""
        y_true = np.zeros(10)
        small = np.full(10, 1.0)
        one_big = np.concatenate([np.zeros(9), [10.0]])
        assert mse(y_true, one_big) > mse(y_true, small)
        assert mae(y_true, one_big) < mae(y_true, small)

    def test_r_squared_of_perfect_model_is_one(self, rng):
        y = rng.normal(size=50)
        assert r_squared(y, y) == pytest.approx(1.0)

    def test_r_squared_of_mean_predictor_is_zero(self, rng):
        y = rng.normal(size=50)
        assert r_squared(y, np.full(50, y.mean())) == pytest.approx(0.0, abs=1e-12)

    def test_r_squared_can_be_negative(self, rng):
        """Worse than predicting the mean. Surprises people."""
        y = rng.normal(size=50)
        assert r_squared(y, -y) < 0


class TestNormalEquation:
    def test_recovers_known_coefficients(self, linear_data):
        X, y = linear_data
        X_aug = np.column_stack([np.ones(len(X)), X])
        w = normal_equation(X_aug, y)
        np.testing.assert_allclose(w, np.array([5.0, 3.0, -2.0]), atol=0.05)

    def test_ridge_shrinks_toward_zero(self, linear_data):
        X, y = linear_data
        X_aug = np.column_stack([np.ones(len(X)), X])
        plain = normal_equation(X_aug, y, l2=0.0)
        ridged = normal_equation(X_aug, y, l2=100.0)
        assert np.linalg.norm(ridged[1:]) < np.linalg.norm(plain[1:])

    def test_ridge_survives_perfect_collinearity(self, rng):
        """X^T X is singular here. Ridge makes it invertible; that is why it exists."""
        x = rng.normal(size=100)
        X = np.column_stack([np.ones(100), x, x])  # duplicated column
        y = 2.0 * x + rng.normal(scale=0.1, size=100)
        w = normal_equation(X, y, l2=1.0)
        assert np.all(np.isfinite(w))


class TestGradientDescent:
    def test_one_step_reduces_loss(self, linear_data):
        X, y = linear_data
        X_aug = np.column_stack([np.ones(len(X)), X])
        w = np.zeros(3)
        before = mse(y, X_aug @ w)
        after = mse(y, X_aug @ gradient_descent_step(X_aug, y, w, lr=0.01))
        assert after < before

    def test_converges_to_the_closed_form_solution(self, linear_data):
        """The whole point: two methods, one answer."""
        X, y = linear_data
        closed = LinearRegression(method="normal").fit(X, y)
        iterative = LinearRegression(method="gd", learning_rate=0.05, n_iters=5000).fit(X, y)
        np.testing.assert_allclose(closed.weights_, iterative.weights_, atol=0.02)
        assert closed.intercept_ == pytest.approx(iterative.intercept_, abs=0.02)

    def test_loss_history_is_monotonically_decreasing(self, linear_data):
        X, y = linear_data
        model = LinearRegression(method="gd", learning_rate=0.01, n_iters=200).fit(X, y)
        history = model.history_
        assert len(history) == 200
        assert history[-1] < history[0]
        assert all(b <= a + 1e-9 for a, b in pairwise(history))

    def test_learning_rate_too_high_diverges(self, linear_data):
        """Instructive failure. Watch it, then never wonder about it again."""
        X, y = linear_data
        model = LinearRegression(method="gd", learning_rate=10.0, n_iters=50).fit(X, y)
        assert model.history_[-1] > model.history_[0] or not np.isfinite(model.history_[-1])


class TestLinearRegression:
    def test_predict_shape(self, linear_data):
        X, y = linear_data
        assert LinearRegression().fit(X, y).predict(X).shape == (300,)

    def test_score_on_clean_data_is_near_one(self, linear_data):
        X, y = linear_data
        assert LinearRegression().fit(X, y).score(X, y) > 0.99

    def test_intercept_can_be_disabled(self, rng):
        X = rng.normal(size=(100, 2))
        y = 3.0 * X[:, 0] + 50.0
        model = LinearRegression(fit_intercept=False).fit(X, y)
        assert model.intercept_ == pytest.approx(0.0)
        assert model.score(X, y) < 0.9, "without an intercept it cannot fit the offset"

    def test_l1_produces_exact_zeros(self, rng):
        """L1's constant-magnitude gradient pushes weights all the way to zero."""
        X = rng.normal(size=(200, 10))
        y = 3.0 * X[:, 0] + rng.normal(scale=0.1, size=200)  # only feature 0 matters
        model = LinearRegression(method="gd", l1=0.5, learning_rate=0.05, n_iters=3000).fit(X, y)
        assert np.sum(np.abs(model.weights_) < 1e-6) >= 5

    def test_l2_shrinks_without_zeroing(self, rng):
        X = rng.normal(size=(200, 10))
        y = 3.0 * X[:, 0] + rng.normal(scale=0.1, size=200)
        model = LinearRegression(method="gd", l2=0.5, learning_rate=0.05, n_iters=3000).fit(X, y)
        assert np.sum(np.abs(model.weights_) < 1e-6) == 0


class TestPolynomialFeatures:
    def test_shape(self, rng):
        X = rng.normal(size=(50, 1))
        assert polynomial_features(X, degree=3).shape[1] >= 3

    def test_high_degree_overfits(self, rng):
        """The canonical demonstration. Produce the plot for your write-up."""
        X = rng.uniform(-1, 1, size=(20, 1))
        y = (X[:, 0] ** 2 + rng.normal(scale=0.2, size=20)).ravel()
        X_test = rng.uniform(-1, 1, size=(200, 1))
        y_test = (X_test[:, 0] ** 2).ravel()

        def fit_score(degree):
            model = LinearRegression().fit(polynomial_features(X, degree), y)
            train = model.score(polynomial_features(X, degree), y)
            test = model.score(polynomial_features(X_test, degree), y_test)
            return train, test

        low_train, low_test = fit_score(2)
        high_train, high_test = fit_score(15)
        assert high_train >= low_train
        assert high_test < low_test


class TestSplitting:
    def test_sizes(self, linear_data, rng):
        X, y = linear_data
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, rng=rng)
        assert len(X_tr) == 225 and len(X_te) == 75
        assert len(y_tr) == 225 and len(y_te) == 75

    def test_no_rows_are_lost_or_duplicated(self, linear_data, rng):
        X, y = linear_data
        X_tr, X_te, _, _ = train_test_split(X, y, rng=rng)
        combined = np.vstack([X_tr, X_te])
        assert len(np.unique(combined, axis=0)) == len(np.unique(X, axis=0))

    def test_actually_shuffles(self, rng):
        """An unshuffled split on ordered data is a silent disaster."""
        X = np.arange(100).reshape(-1, 1).astype(float)
        y = X.ravel()
        _, _, y_tr, _ = train_test_split(X, y, test_size=0.2, rng=rng)
        assert not np.array_equal(y_tr, np.sort(y_tr))


class TestBiasVariance:
    def test_complex_model_has_higher_variance(self, rng):
        """The decomposition you must be able to explain."""
        X = rng.uniform(-1, 1, size=(60, 1))
        y = (X[:, 0] ** 2 + rng.normal(scale=0.1, size=60)).ravel()

        simple = bias_variance_decomposition(
            lambda: LinearRegression(), polynomial_features(X, 1), y, n_trials=30, rng=rng
        )
        complex_ = bias_variance_decomposition(
            lambda: LinearRegression(), polynomial_features(X, 12), y, n_trials=30, rng=rng
        )
        assert complex_["variance"] > simple["variance"]
        assert complex_["bias_squared"] < simple["bias_squared"]
