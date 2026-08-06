"""Weeks 13-14 — layers, losses, and gradient verification.

Every layer gets gradient-checked. This is the discipline that makes Month 8
tractable: when you implement attention in Week 29, you will check it the same
way, and you will find your bug in ten minutes instead of three days.
"""

from __future__ import annotations

import numpy as np
import pytest
from backprop import (
    activation_statistics,
    check_gradient_flow,
    clip_gradients,
    gradient_check_layer,
    gradient_check_network,
    gradient_norms,
    numerical_gradient,
    relative_error,
)
from neural_net import (
    GELU,
    BatchNorm1d,
    BCELoss,
    CrossEntropyLoss,
    Dropout,
    LayerNorm,
    Linear,
    MSELoss,
    ReLU,
    Sequential,
    Sigmoid,
    Softmax,
    Tanh,
)

# ---------------------------------------------------------------------------
# Week 13 — forward passes
# ---------------------------------------------------------------------------


@pytest.mark.week(13)
class TestForward:
    def test_linear_output_shape(self, rng):
        layer = Linear(4, 7)
        assert layer.forward(rng.normal(size=(9, 4))).shape == (9, 7)

    def test_relu_clamps_negatives(self):
        out = ReLU().forward(np.array([[-2.0, -0.1, 0.0, 3.0]]))
        np.testing.assert_allclose(out, np.array([[0.0, 0.0, 0.0, 3.0]]))

    def test_sigmoid_range(self, rng):
        out = Sigmoid().forward(rng.normal(scale=10, size=(20, 5)))
        assert np.all((out > 0) & (out < 1))

    def test_tanh_is_zero_centered(self):
        assert Tanh().forward(np.zeros((1, 1)))[0, 0] == pytest.approx(0.0)

    def test_gelu_is_smooth_and_near_relu_for_large_inputs(self):
        gelu = GELU().forward(np.array([[-5.0, 0.0, 5.0]]))
        assert gelu[0, 0] == pytest.approx(0.0, abs=1e-3)
        assert gelu[0, 1] == pytest.approx(0.0, abs=1e-6)
        assert gelu[0, 2] == pytest.approx(5.0, abs=1e-3)

    def test_softmax_rows_sum_to_one(self, rng):
        out = Softmax().forward(rng.normal(size=(6, 4)))
        np.testing.assert_allclose(out.sum(axis=-1), np.ones(6), atol=1e-12)

    def test_sequential_composes(self, rng):
        net = Sequential(Linear(4, 8), ReLU(), Linear(8, 3))
        assert net.forward(rng.normal(size=(5, 4))).shape == (5, 3)

    def test_he_initialization_preserves_activation_variance(self, rng):
        """Why initialization is not a detail: signal must survive depth."""
        x = rng.normal(size=(512, 128))
        for _ in range(6):
            x = ReLU().forward(Linear(128, 128, init="he").forward(x))
        assert 0.3 < x.std() < 3.0

    def test_bad_initialization_collapses_the_signal(self, rng):
        x = rng.normal(size=(512, 128))
        for _ in range(6):
            layer = Linear(128, 128, init="he")
            layer.W *= 0.1  # deliberately too small
            x = ReLU().forward(layer.forward(x))
        assert x.std() < 0.05


# ---------------------------------------------------------------------------
# Week 14 — gradients
# ---------------------------------------------------------------------------


@pytest.mark.week(14)
class TestNumericalTools:
    def test_numerical_gradient_of_a_quadratic(self):
        x = np.array([1.0, 2.0, 3.0])
        grad = numerical_gradient(lambda v: float(np.sum(v**2)), x)
        np.testing.assert_allclose(grad, 2 * x, atol=1e-6)

    def test_numerical_gradient_does_not_mutate_its_input(self):
        x = np.array([1.0, 2.0])
        numerical_gradient(lambda v: float(np.sum(v**2)), x)
        np.testing.assert_array_equal(x, np.array([1.0, 2.0]))

    def test_relative_error_of_identical_arrays_is_zero(self, rng):
        a = rng.normal(size=10)
        assert np.max(relative_error(a, a.copy())) < 1e-12

    def test_relative_error_scales_correctly(self):
        """Absolute error would call these equally wrong. Relative error doesn't."""
        big = relative_error(np.array([1000.0]), np.array([1001.0]))
        small = relative_error(np.array([0.001]), np.array([0.002]))
        assert big < small


@pytest.mark.week(14)
class TestLayerGradients:
    @pytest.mark.parametrize(
        "layer_factory",
        [
            lambda: Linear(5, 3),
            lambda: ReLU(),
            lambda: Sigmoid(),
            lambda: Tanh(),
            lambda: GELU(),
            lambda: Softmax(),
        ],
        ids=["linear", "relu", "sigmoid", "tanh", "gelu", "softmax"],
    )
    def test_gradient_check(self, layer_factory, rng):
        layer = layer_factory()
        x = rng.normal(size=(6, 5))
        errors = gradient_check_layer(layer, x)
        for name, err in errors.items():
            assert err < 1e-6, f"{name} gradient is wrong (relative error {err:.2e})"

    def test_linear_input_gradient_shape(self, rng):
        layer = Linear(5, 3)
        x = rng.normal(size=(6, 5))
        layer.forward(x)
        assert layer.backward(rng.normal(size=(6, 3))).shape == x.shape

    def test_relu_gradient_is_zero_where_input_was_negative(self):
        layer = ReLU()
        layer.forward(np.array([[-1.0, 2.0, -3.0]]))
        grad = layer.backward(np.ones((1, 3)))
        np.testing.assert_allclose(grad, np.array([[0.0, 1.0, 0.0]]))

    def test_sigmoid_gradient_peaks_at_zero(self):
        """Max 0.25. Stack ten of these and the gradient is 1e-6 — vanishing,
        quantified."""
        layer = Sigmoid()
        layer.forward(np.array([[0.0]]))
        assert layer.backward(np.ones((1, 1)))[0, 0] == pytest.approx(0.25)


@pytest.mark.week(14)
class TestLosses:
    def test_mse_forward_and_backward(self):
        loss = MSELoss()
        value = loss.forward(np.array([[3.0]]), np.array([[1.0]]))
        assert value == pytest.approx(4.0)
        assert loss.backward()[0, 0] == pytest.approx(4.0)

    def test_cross_entropy_initial_loss_is_ln_c(self, rng):
        """The single most useful sanity check in deep learning.

        Untrained, uniform logits over C classes must give ln(C). 2.303 for 10
        classes. If your training run starts far from this, stop and debug
        before touching hyperparameters.
        """
        logits = np.zeros((100, 10))
        targets = rng.integers(0, 10, size=100)
        assert CrossEntropyLoss().forward(logits, targets) == pytest.approx(np.log(10), abs=1e-9)

    def test_cross_entropy_gradient_is_p_minus_y(self, rng):
        logits = rng.normal(size=(4, 5))
        targets = np.array([0, 2, 4, 1])
        loss = CrossEntropyLoss()
        loss.forward(logits, targets)
        grad = loss.backward()

        exp = np.exp(logits - logits.max(axis=1, keepdims=True))
        probs = exp / exp.sum(axis=1, keepdims=True)
        expected = probs.copy()
        expected[np.arange(4), targets] -= 1.0
        expected /= 4
        np.testing.assert_allclose(grad, expected, atol=1e-10)

    def test_cross_entropy_survives_extreme_logits(self):
        """The fused log-sum-exp form is why this doesn't overflow."""
        value = CrossEntropyLoss().forward(np.array([[1000.0, -1000.0]]), np.array([0]))
        assert np.isfinite(value)

    def test_bce_gradient_check(self, rng):
        logits = rng.normal(size=(8, 1))
        targets = rng.integers(0, 2, size=(8, 1)).astype(float)
        loss = BCELoss()
        loss.forward(logits, targets)
        analytic = loss.backward()
        numeric = numerical_gradient(
            lambda z: loss.forward(z.reshape(8, 1), targets), logits.ravel()
        )
        np.testing.assert_allclose(analytic.ravel(), numeric, atol=1e-6)


@pytest.mark.week(14)
class TestNetworkGradients:
    def test_end_to_end_gradient_check(self, rng):
        net = Sequential(Linear(4, 6), Tanh(), Linear(6, 3))
        x = rng.normal(size=(5, 4))
        y = rng.integers(0, 3, size=5)
        errors = gradient_check_network(net, CrossEntropyLoss(), x, y)
        for name, err in errors.items():
            assert err < 1e-6, f"{name}: {err:.2e}"

    def test_backward_runs_layers_in_reverse(self, rng):
        """That reversal is backpropagation. Nothing more."""
        order = []

        class Tracer(ReLU):
            def __init__(self, tag):
                super().__init__()
                self.tag = tag

            def backward(self, grad_output):
                order.append(self.tag)
                return super().backward(grad_output)

        net = Sequential(Tracer("first"), Tracer("second"), Tracer("third"))
        net.forward(rng.normal(size=(2, 3)))
        net.backward(np.ones((2, 3)))
        assert order == ["third", "second", "first"]


@pytest.mark.week(14)
class TestDiagnostics:
    def test_gradient_norms_reported_per_layer(self, rng):
        net = Sequential(Linear(4, 6), ReLU(), Linear(6, 2))
        loss = CrossEntropyLoss()
        loss.forward(net.forward(rng.normal(size=(8, 4))), rng.integers(0, 2, size=8))
        net.backward(loss.backward())
        norms = gradient_norms(net)
        assert len(norms) >= 2
        assert all(v >= 0 for v in norms.values())

    def test_detects_vanishing_gradients(self, rng):
        """Twelve sigmoid layers. The gradient does not reach layer one."""
        layers = []
        for _ in range(12):
            layers += [Linear(16, 16), Sigmoid()]
        net = Sequential(*layers, Linear(16, 2))

        loss = CrossEntropyLoss()
        loss.forward(net.forward(rng.normal(size=(8, 16))), rng.integers(0, 2, size=8))
        net.backward(loss.backward())

        diagnosis = check_gradient_flow(net)
        assert any(v == "vanishing" for v in diagnosis.values())

    def test_activation_statistics_reported(self, rng):
        net = Sequential(Linear(8, 16), ReLU(), Linear(16, 4))
        stats = activation_statistics(net, rng.normal(size=(64, 8)))
        for layer_stats in stats.values():
            assert {"mean", "std"} <= layer_stats.keys()

    def test_clip_gradients_bounds_the_global_norm(self, rng):
        net = Sequential(Linear(4, 6), ReLU(), Linear(6, 2))
        loss = CrossEntropyLoss()
        loss.forward(net.forward(rng.normal(size=(8, 4)) * 100), rng.integers(0, 2, size=8))
        net.backward(loss.backward())

        clip_gradients(net, max_norm=1.0)
        total = np.sqrt(sum(float(np.sum(g**2)) for g in net.gradients()))
        assert total <= 1.0 + 1e-6

    def test_clipping_preserves_direction(self, rng):
        """Global-norm clipping rescales; per-parameter clipping would rotate."""
        net = Sequential(Linear(4, 3))
        loss = MSELoss()
        loss.forward(net.forward(rng.normal(size=(8, 4)) * 50), rng.normal(size=(8, 3)))
        net.backward(loss.backward())

        before = [g.copy() for g in net.gradients()]
        clip_gradients(net, max_norm=0.5)
        after = net.gradients()

        flat_before = np.concatenate([g.ravel() for g in before])
        flat_after = np.concatenate([g.ravel() for g in after])
        cosine = (
            flat_before @ flat_after / (np.linalg.norm(flat_before) * np.linalg.norm(flat_after))
        )
        assert cosine == pytest.approx(1.0, abs=1e-9)


# ---------------------------------------------------------------------------
# Week 16 — regularization layers
# ---------------------------------------------------------------------------


@pytest.mark.week(16)
class TestRegularizationLayers:
    def test_dropout_is_a_noop_in_eval_mode(self, rng):
        layer = Dropout(p=0.5)
        layer.eval()
        x = rng.normal(size=(100, 20))
        np.testing.assert_allclose(layer.forward(x), x)

    def test_dropout_zeros_roughly_p_of_activations(self, rng):
        layer = Dropout(p=0.5)
        layer.train()
        out = layer.forward(rng.normal(size=(500, 100)))
        assert np.mean(out == 0.0) == pytest.approx(0.5, abs=0.05)

    def test_inverted_dropout_preserves_the_expected_value(self, rng):
        """Scaling at train time is why inference needs no adjustment."""
        layer = Dropout(p=0.5)
        layer.train()
        x = np.ones((2000, 50))
        assert layer.forward(x).mean() == pytest.approx(1.0, abs=0.05)

    def test_batchnorm_normalizes_in_training_mode(self, rng):
        layer = BatchNorm1d(8)
        layer.train()
        out = layer.forward(rng.normal(loc=5.0, scale=3.0, size=(200, 8)))
        np.testing.assert_allclose(out.mean(axis=0), np.zeros(8), atol=1e-6)
        np.testing.assert_allclose(out.std(axis=0), np.ones(8), atol=1e-3)

    def test_batchnorm_uses_running_stats_in_eval_mode(self, rng):
        layer = BatchNorm1d(8)
        layer.train()
        for _ in range(50):
            layer.forward(rng.normal(loc=5.0, scale=3.0, size=(64, 8)))
        layer.eval()
        out = layer.forward(rng.normal(loc=5.0, scale=3.0, size=(64, 8)))
        assert abs(float(out.mean())) < 0.5

    def test_batchnorm_gradient_check(self, rng):
        """The hardest derivation in the lab. Three gradient paths per input."""
        layer = BatchNorm1d(4)
        layer.train()
        errors = gradient_check_layer(layer, rng.normal(size=(16, 4)))
        for name, err in errors.items():
            assert err < 1e-5, f"{name}: {err:.2e}"

    def test_layernorm_normalizes_per_sample(self, rng):
        """Across features, not across the batch — which is why transformers use it."""
        layer = LayerNorm(16)
        out = layer.forward(rng.normal(loc=3.0, scale=2.0, size=(10, 16)))
        np.testing.assert_allclose(out.mean(axis=1), np.zeros(10), atol=1e-6)

    def test_layernorm_is_batch_size_independent(self, rng):
        """The property BatchNorm lacks, and the reason for the transformer's choice."""
        layer = LayerNorm(16)
        x = rng.normal(size=(8, 16))
        full = layer.forward(x)
        single = layer.forward(x[:1])
        np.testing.assert_allclose(single[0], full[0], atol=1e-9)

    def test_layernorm_gradient_check(self, rng):
        errors = gradient_check_layer(LayerNorm(6), rng.normal(size=(8, 6)))
        for name, err in errors.items():
            assert err < 1e-5, f"{name}: {err:.2e}"
