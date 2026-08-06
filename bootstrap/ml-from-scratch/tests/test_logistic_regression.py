"""Week 6 — logistic and softmax regression."""

from __future__ import annotations

import numpy as np
import pytest
from logistic_regression import (
    LogisticRegression,
    SoftmaxRegression,
    log_loss,
    one_hot,
    sigmoid,
    softmax,
)
from metrics import accuracy

pytestmark = pytest.mark.week(6)


@pytest.fixture
def separable(rng):
    """Two well-separated Gaussian blobs."""
    n = 200
    X = np.vstack([rng.normal(loc=-2.0, size=(n, 2)), rng.normal(loc=2.0, size=(n, 2))])
    y = np.concatenate([np.zeros(n), np.ones(n)])
    return X, y


@pytest.fixture
def three_class(rng):
    n = 150
    X = np.vstack(
        [
            rng.normal(loc=[-3, 0], scale=0.8, size=(n, 2)),
            rng.normal(loc=[0, 3], scale=0.8, size=(n, 2)),
            rng.normal(loc=[3, 0], scale=0.8, size=(n, 2)),
        ]
    )
    y = np.repeat([0, 1, 2], n)
    return X, y


class TestSigmoid:
    def test_known_values(self):
        assert sigmoid(0.0) == pytest.approx(0.5)
        assert sigmoid(100.0) == pytest.approx(1.0, abs=1e-9)
        assert sigmoid(-100.0) == pytest.approx(0.0, abs=1e-9)

    def test_no_overflow_at_the_extremes(self):
        """The naive form warns and returns nan below about -745."""
        values = sigmoid(np.array([-1000.0, -800.0, 0.0, 800.0, 1000.0]))
        assert np.all(np.isfinite(values))
        assert np.all((values >= 0.0) & (values <= 1.0))

    def test_symmetry(self, rng):
        z = rng.normal(size=20)
        np.testing.assert_allclose(sigmoid(z) + sigmoid(-z), np.ones(20), atol=1e-12)


class TestLogLoss:
    def test_confident_and_correct_is_near_zero(self):
        assert log_loss(np.array([1.0]), np.array([0.999])) < 0.01

    def test_confident_and_wrong_is_large(self):
        assert log_loss(np.array([1.0]), np.array([0.001])) > 5.0

    def test_clipping_prevents_infinity(self):
        assert np.isfinite(log_loss(np.array([1.0, 0.0]), np.array([0.0, 1.0])))

    def test_uniform_guessing_is_ln_two(self):
        y = np.array([0.0, 1.0, 0.0, 1.0])
        assert log_loss(y, np.full(4, 0.5)) == pytest.approx(np.log(2))


class TestLogisticRegression:
    def test_separates_two_blobs(self, separable):
        X, y = separable
        model = LogisticRegression(learning_rate=0.5, n_iters=2000).fit(X, y)
        assert accuracy(y, model.predict(X)) > 0.98

    def test_probabilities_are_bounded(self, separable):
        X, y = separable
        p = LogisticRegression().fit(X, y).predict_proba(X)
        assert np.all((p >= 0.0) & (p <= 1.0))
        assert p.shape == (len(y),)

    def test_loss_decreases(self, separable):
        X, y = separable
        history = LogisticRegression(learning_rate=0.1, n_iters=500).fit(X, y).history_
        assert history[-1] < history[0]

    def test_threshold_changes_the_prediction(self, separable):
        X, y = separable
        model = LogisticRegression().fit(X, y)
        assert model.predict(X, threshold=0.1).sum() >= model.predict(X, threshold=0.9).sum()

    def test_decision_function_agrees_with_proba(self, separable):
        X, y = separable
        model = LogisticRegression().fit(X, y)
        np.testing.assert_allclose(
            sigmoid(model.decision_function(X)), model.predict_proba(X), atol=1e-10
        )

    def test_l2_shrinks_the_weights(self, separable):
        X, y = separable
        plain = LogisticRegression(l2=0.0, n_iters=1000).fit(X, y)
        ridged = LogisticRegression(l2=10.0, n_iters=1000).fit(X, y)
        assert np.linalg.norm(ridged.weights_) < np.linalg.norm(plain.weights_)

    def test_balanced_weights_help_recall_on_skewed_data(self, rng):
        n = 2000
        X = rng.normal(size=(n, 2))
        y = ((X[:, 0] + rng.normal(scale=0.5, size=n)) > 2.2).astype(float)

        plain = LogisticRegression(n_iters=1500).fit(X, y)
        balanced = LogisticRegression(class_weight="balanced", n_iters=1500).fit(X, y)

        recall_plain = plain.predict(X)[y == 1].mean()
        recall_balanced = balanced.predict(X)[y == 1].mean()
        assert recall_balanced >= recall_plain

    def test_rejects_non_binary_targets(self, rng):
        X = rng.normal(size=(20, 2))
        with pytest.raises((ValueError, AssertionError)):
            LogisticRegression().fit(X, np.array([0, 1, 2] * 6 + [0, 1]))


class TestSoftmax:
    def test_rows_sum_to_one(self, rng):
        probs = softmax(rng.normal(size=(10, 5)), axis=-1)
        np.testing.assert_allclose(probs.sum(axis=-1), np.ones(10), atol=1e-12)

    def test_shift_invariance(self, rng):
        logits = rng.normal(size=(4, 6))
        np.testing.assert_allclose(softmax(logits), softmax(logits + 100.0), atol=1e-12)

    def test_survives_large_logits(self):
        probs = softmax(np.array([[1000.0, 1001.0, 999.0]]))
        assert np.all(np.isfinite(probs))
        assert probs.sum() == pytest.approx(1.0)

    def test_preserves_order(self, rng):
        logits = rng.normal(size=8)
        assert np.array_equal(np.argsort(logits), np.argsort(softmax(logits)))


class TestOneHot:
    def test_shape_and_content(self):
        encoded = one_hot(np.array([0, 2, 1]), n_classes=3)
        np.testing.assert_array_equal(encoded, np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]))

    def test_infers_class_count(self):
        assert one_hot(np.array([0, 1, 2, 3])).shape == (4, 4)


class TestSoftmaxRegression:
    def test_classifies_three_blobs(self, three_class):
        X, y = three_class
        model = SoftmaxRegression(learning_rate=0.5, n_iters=2000).fit(X, y)
        assert accuracy(y, model.predict(X)) > 0.95

    def test_proba_shape_and_normalization(self, three_class):
        X, y = three_class
        p = SoftmaxRegression(n_iters=500).fit(X, y).predict_proba(X)
        assert p.shape == (len(y), 3)
        np.testing.assert_allclose(p.sum(axis=1), np.ones(len(y)), atol=1e-10)

    def test_binary_case_matches_logistic_regression(self, separable):
        """A two-class softmax is logistic regression. Confirm it."""
        X, y = separable
        binary = LogisticRegression(learning_rate=0.3, n_iters=2000).fit(X, y)
        multi = SoftmaxRegression(learning_rate=0.3, n_iters=2000).fit(X, y)
        np.testing.assert_array_equal(binary.predict(X), multi.predict(X))
