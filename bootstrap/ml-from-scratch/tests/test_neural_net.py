"""Weeks 13-16 — the MLP end to end, plus regularization and diagnosis.

The capstone test is ``test_trains_mnist_subset_to_high_accuracy``. When that
passes, you have built a working deep learning framework in NumPy.
"""

from __future__ import annotations

import numpy as np
import pytest
from neural_net import MLP, iterate_minibatches
from regularization import (
    EarlyStopping,
    ablation_study,
    diagnose_fit,
    elastic_net_penalty,
    gaussian_noise_augmentation,
    generalization_gap,
    l1_penalty,
    l2_penalty,
    label_smoothing,
    mixup,
    overfit_single_batch,
)


@pytest.fixture
def spiral(rng):
    """Two interleaved spirals — not linearly separable, small enough to be fast."""
    n = 300
    theta = np.sqrt(rng.random(n)) * 3 * np.pi
    r = theta + rng.normal(scale=0.3, size=n)
    a = np.column_stack([r * np.cos(theta), r * np.sin(theta)])
    b = np.column_stack([-r * np.cos(theta), -r * np.sin(theta)])
    X = np.vstack([a, b]) / 10.0
    y = np.concatenate([np.zeros(n, dtype=int), np.ones(n, dtype=int)])
    return X, y


# ---------------------------------------------------------------------------
# Week 13
# ---------------------------------------------------------------------------


@pytest.mark.week(13)
class TestMinibatching:
    def test_covers_every_sample_once_per_epoch(self, rng):
        X = np.arange(100).reshape(-1, 1).astype(float)
        y = np.arange(100)
        seen = np.concatenate([yb for _, yb in iterate_minibatches(X, y, 16, rng=rng)])
        np.testing.assert_array_equal(np.sort(seen), np.arange(100))

    def test_handles_a_ragged_final_batch(self, rng):
        X = np.zeros((100, 2))
        y = np.zeros(100)
        sizes = [len(xb) for xb, _ in iterate_minibatches(X, y, 32, rng=rng)]
        assert sizes == [32, 32, 32, 4]

    def test_shuffles_between_epochs(self, rng):
        X = np.arange(50).reshape(-1, 1).astype(float)
        y = np.arange(50)
        first = next(iter(iterate_minibatches(X, y, 10, rng=rng)))[1]
        second = next(iter(iterate_minibatches(X, y, 10, rng=rng)))[1]
        assert not np.array_equal(first, second)


@pytest.mark.week(13)
class TestMLP:
    def test_learns_xor(self):
        """The problem a perceptron cannot solve. One hidden layer is enough."""
        X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
        y = np.array([0, 1, 1, 0])
        model = MLP([2, 8, 2]).fit(
            X, y, epochs=2000, batch_size=4, learning_rate=0.05, verbose=False
        )
        np.testing.assert_array_equal(model.predict(X), y)

    def test_learns_a_nonlinear_boundary(self, spiral):
        X, y = spiral
        model = MLP([2, 32, 32, 2]).fit(X, y, epochs=400, learning_rate=0.01, verbose=False)
        assert np.mean(model.predict(X) == y) > 0.9

    def test_records_history(self, spiral):
        X, y = spiral
        model = MLP([2, 16, 2]).fit(
            X, y, epochs=30, validation_data=(X, y), learning_rate=0.01, verbose=False
        )
        assert len(model.history_["train_loss"]) == 30
        assert len(model.history_["val_loss"]) == 30

    def test_loss_decreases(self, spiral):
        X, y = spiral
        history = MLP([2, 16, 2]).fit(X, y, epochs=100, learning_rate=0.01, verbose=False).history_
        assert history["train_loss"][-1] < history["train_loss"][0]

    def test_proba_is_normalized(self, spiral):
        X, y = spiral
        p = MLP([2, 16, 2]).fit(X, y, epochs=20, verbose=False).predict_proba(X)
        np.testing.assert_allclose(p.sum(axis=1), np.ones(len(y)), atol=1e-9)


# ---------------------------------------------------------------------------
# Week 16 — penalties, regularizers, diagnosis
# ---------------------------------------------------------------------------


@pytest.mark.week(16)
class TestPenalties:
    def test_l1_and_l2_of_known_weights(self):
        params = [np.array([3.0, -4.0])]
        assert l1_penalty(params, 1.0) == pytest.approx(7.0)
        assert l2_penalty(params, 1.0) == pytest.approx(25.0)

    def test_elastic_net_is_the_sum(self):
        params = [np.array([3.0, -4.0])]
        assert elastic_net_penalty(params, 1.0, 1.0) == pytest.approx(32.0)

    def test_penalties_scale_with_strength(self):
        params = [np.array([1.0, 2.0])]
        assert l2_penalty(params, 2.0) == pytest.approx(2 * l2_penalty(params, 1.0))


@pytest.mark.week(16)
class TestEarlyStopping:
    def test_stops_after_patience(self):
        stopper = EarlyStopping(patience=3)
        losses = [1.0, 0.8, 0.85, 0.86, 0.87, 0.88]
        stopped_at = next((i for i, loss in enumerate(losses) if stopper(loss, i)), None)
        assert stopped_at == 4

    def test_does_not_stop_while_improving(self):
        stopper = EarlyStopping(patience=2)
        assert not any(stopper(loss, i) for i, loss in enumerate([1.0, 0.9, 0.8, 0.7, 0.6]))

    def test_tracks_the_best_epoch(self):
        stopper = EarlyStopping(patience=5)
        for i, loss in enumerate([1.0, 0.5, 0.9, 0.95, 1.1]):
            stopper(loss, i)
        assert stopper.best_epoch_ == 1
        assert stopper.best_score_ == pytest.approx(0.5)

    def test_restores_the_best_weights(self):
        """Stopping at epoch 5 while keeping epoch 5's weights wastes the peak."""
        stopper = EarlyStopping(patience=2, restore_best=True)
        params = [np.array([1.0])]

        stopper(0.5, 0, [np.array([42.0])])
        stopper(0.9, 1, [np.array([1.0])])
        stopper(0.95, 2, [np.array([2.0])])
        stopper.restore(params)
        assert params[0][0] == pytest.approx(42.0)

    def test_min_delta_ignores_noise(self):
        stopper = EarlyStopping(patience=2, min_delta=0.01)
        results = [stopper(loss, i) for i, loss in enumerate([1.0, 0.999, 0.998, 0.997])]
        assert results[-1] is True, "sub-threshold improvements should not reset patience"


@pytest.mark.week(16)
class TestAugmentation:
    def test_label_smoothing_shapes_and_sums(self):
        smoothed = label_smoothing(np.array([0, 2]), n_classes=3, smoothing=0.1)
        assert smoothed.shape == (2, 3)
        np.testing.assert_allclose(smoothed.sum(axis=1), np.ones(2))

    def test_label_smoothing_reduces_the_target_mass(self):
        smoothed = label_smoothing(np.array([1]), n_classes=4, smoothing=0.2)
        assert smoothed[0, 1] == pytest.approx(0.8)
        assert np.all(smoothed[0, [0, 2, 3]] > 0)

    def test_mixup_stays_inside_the_convex_hull(self, rng):
        X = rng.normal(size=(64, 5))
        y = rng.integers(0, 3, size=64)
        X_mixed, _ = mixup(X, y, alpha=0.2, rng=rng)
        assert X_mixed.shape == X.shape
        assert X_mixed.max() <= X.max() + 1e-9
        assert X_mixed.min() >= X.min() - 1e-9

    def test_gaussian_noise_preserves_the_mean(self, rng):
        X = rng.normal(size=(2000, 4))
        noisy = gaussian_noise_augmentation(X, sigma=0.1, rng=rng)
        np.testing.assert_allclose(noisy.mean(axis=0), X.mean(axis=0), atol=0.02)
        assert noisy.std() > X.std()


@pytest.mark.week(16)
class TestDiagnosis:
    def test_detects_overfitting(self):
        result = diagnose_fit([0.9, 0.5, 0.2, 0.05], [0.9, 0.7, 0.75, 0.9])
        assert result["diagnosis"] == "overfitting"

    def test_detects_underfitting(self):
        result = diagnose_fit([0.9, 0.85, 0.84, 0.84], [0.91, 0.86, 0.85, 0.85])
        assert result["diagnosis"] == "underfitting"

    def test_detects_a_healthy_run(self):
        result = diagnose_fit([0.9, 0.4, 0.15, 0.10], [0.92, 0.45, 0.18, 0.13])
        assert result["diagnosis"] in {"healthy", "good_fit"}

    def test_returns_actionable_recommendations(self):
        result = diagnose_fit([0.9, 0.5, 0.2, 0.05], [0.9, 0.7, 0.75, 0.9])
        assert isinstance(result["recommendations"], list)
        assert result["recommendations"]

    def test_generalization_gap_tracking(self):
        stats = generalization_gap([0.5, 0.3, 0.1, 0.02], [0.5, 0.35, 0.4, 0.6])
        assert stats["final_gap"] > stats["max_gap"] - 1e-9
        assert stats["epoch_of_divergence"] >= 1

    def test_overfit_single_batch_succeeds_on_a_working_model(self, rng):
        """**Run this before every training run for the rest of the course.**

        A correct model memorizes 8 examples. If it cannot, the bug is in your
        code, not your hyperparameters.
        """
        X = rng.normal(size=(8, 4))
        y = rng.integers(0, 2, size=8)
        result = overfit_single_batch(lambda: MLP([4, 32, 2]), X, y, max_epochs=800)
        assert result["converged"]
        assert result["final_loss"] < 0.01


@pytest.mark.week(16)
@pytest.mark.slow
class TestAblation:
    def test_produces_a_comparison_table(self, spiral):
        """The Week 16 deliverable: what each regularizer actually bought."""
        X, y = spiral

        def train(config):
            model = MLP(
                [2, 64, 64, 2],
                dropout=config.get("dropout", 0.0),
                batch_norm=config.get("bn", False),
            ).fit(X[:400], y[:400], epochs=150, verbose=False)
            return {
                "train": float(np.mean(model.predict(X[:400]) == y[:400])),
                "val": float(np.mean(model.predict(X[400:]) == y[400:])),
            }

        table = ablation_study(
            base_config={},
            variations={"dropout": {"dropout": 0.3}, "batchnorm": {"bn": True}},
            train_fn=train,
        )
        assert len(table) >= 3


@pytest.mark.week(16)
@pytest.mark.slow
class TestCapstone:
    def test_trains_mnist_subset_to_high_accuracy(self):
        """**The Month 4 capstone gate.**

        Nothing but NumPy and the code in this lab. Uses sklearn's digits
        dataset (8x8, 1797 samples) so it runs in seconds; swap in full MNIST
        for the actual capstone deliverable and target >95% test accuracy.
        """
        from sklearn.datasets import load_digits

        digits = load_digits()
        X = digits.data / 16.0
        y = digits.target

        split = 1400
        model = MLP([64, 128, 64, 10], dropout=0.2).fit(
            X[:split],
            y[:split],
            epochs=200,
            batch_size=64,
            learning_rate=0.01,
            optimizer="adam",
            validation_data=(X[split:], y[split:]),
            verbose=False,
        )
        assert np.mean(model.predict(X[split:]) == y[split:]) > 0.93
