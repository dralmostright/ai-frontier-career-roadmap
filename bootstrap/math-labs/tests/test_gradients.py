"""Tests for Week 3 scalar autodiff.

Every gradient here is checked two ways: against a hand-derived analytic value,
and against a central finite difference. If your implementation passes both, it
is right.
"""

from __future__ import annotations

import math

import pytest
from autodiff_scalar import (
    Value,
    binary_cross_entropy,
    cross_entropy,
    gradient_check,
    mse_loss,
    numerical_gradient,
    softmax,
)

pytestmark = pytest.mark.week(3)


class TestForward:
    def test_add(self):
        assert (Value(2.0) + Value(3.0)).data == pytest.approx(5.0)

    def test_add_scalar(self):
        assert (Value(2.0) + 3.0).data == pytest.approx(5.0)
        assert (3.0 + Value(2.0)).data == pytest.approx(5.0)

    def test_mul(self):
        assert (Value(2.0) * Value(3.0)).data == pytest.approx(6.0)

    def test_sub_and_div(self):
        assert (Value(7.0) - Value(3.0)).data == pytest.approx(4.0)
        assert (Value(6.0) / Value(3.0)).data == pytest.approx(2.0)

    def test_pow(self):
        assert (Value(3.0) ** 2).data == pytest.approx(9.0)

    def test_activations(self):
        assert Value(0.0).tanh().data == pytest.approx(0.0)
        assert Value(0.0).sigmoid().data == pytest.approx(0.5)
        assert Value(-2.0).relu().data == pytest.approx(0.0)
        assert Value(2.0).relu().data == pytest.approx(2.0)
        assert Value(1.0).exp().data == pytest.approx(math.e)
        assert Value(math.e).log().data == pytest.approx(1.0)

    def test_log_of_nonpositive_raises(self):
        with pytest.raises(ValueError):
            Value(0.0).log()


class TestBackwardAnalytic:
    """Gradients you should be able to state without thinking."""

    def test_add_routes_gradient_unchanged(self):
        a, b = Value(2.0), Value(3.0)
        (a + b).backward()
        assert a.grad == pytest.approx(1.0)
        assert b.grad == pytest.approx(1.0)

    def test_mul_swaps_operands(self):
        a, b = Value(2.0), Value(3.0)
        (a * b).backward()
        assert a.grad == pytest.approx(3.0)
        assert b.grad == pytest.approx(2.0)

    def test_pow(self):
        a = Value(3.0)
        (a**2).backward()
        assert a.grad == pytest.approx(6.0)  # 2 * 3

    def test_gradient_accumulates_for_reused_nodes(self):
        """The += case. y = x*x means dy/dx = 2x, not x."""
        x = Value(3.0)
        (x * x).backward()
        assert x.grad == pytest.approx(6.0)

    def test_diamond_graph(self):
        """x -> a, x -> b, y = a + b. Gradients from both paths must sum."""
        x = Value(2.0)
        a = x * 3.0
        b = x * 5.0
        (a + b).backward()
        assert x.grad == pytest.approx(8.0)

    def test_chain_of_three(self):
        # y = ((x + 1) * 2) ** 2, at x = 3  ->  y = 64, dy/dx = 32
        x = Value(3.0)
        y = ((x + 1.0) * 2.0) ** 2
        y.backward()
        assert y.data == pytest.approx(64.0)
        assert x.grad == pytest.approx(32.0)

    def test_tanh_derivative(self):
        x = Value(0.5)
        y = x.tanh()
        y.backward()
        assert x.grad == pytest.approx(1 - math.tanh(0.5) ** 2)

    def test_sigmoid_derivative(self):
        x = Value(0.7)
        y = x.sigmoid()
        y.backward()
        s = 1 / (1 + math.exp(-0.7))
        assert x.grad == pytest.approx(s * (1 - s))

    def test_relu_derivative_both_sides(self):
        pos = Value(2.0)
        pos.relu().backward()
        assert pos.grad == pytest.approx(1.0)

        neg = Value(-2.0)
        neg.relu().backward()
        assert neg.grad == pytest.approx(0.0)

    def test_exp_is_its_own_derivative(self):
        x = Value(1.5)
        x.exp().backward()
        assert x.grad == pytest.approx(math.exp(1.5))


class TestZeroGrad:
    def test_gradients_accumulate_across_backward_calls(self):
        x = Value(3.0)
        y = x * 2.0
        y.backward()
        y.backward()
        assert x.grad == pytest.approx(4.0), "two backward calls should sum to 2+2"

    def test_zero_grad_resets(self):
        x = Value(3.0)
        y = x * 2.0
        y.backward()
        y.zero_grad()
        assert x.grad == pytest.approx(0.0)


class TestTopologicalSort:
    def test_parents_come_before_children(self):
        a = Value(1.0, label="a")
        b = Value(2.0, label="b")
        c = a + b
        d = c * a
        order = d.topological_sort()
        assert order.index(a) < order.index(c)
        assert order.index(c) < order.index(d)

    def test_includes_every_ancestor_once(self):
        a = Value(1.0)
        b = a * a
        c = b + a
        order = c.topological_sort()
        assert len(order) == len(set(id(n) for n in order))
        assert a in order and b in order and c in order


class TestNumericalGradient:
    def test_matches_known_derivative(self):
        # d/dx x^2 at x=3 is 6
        assert numerical_gradient(lambda x: x**2, 3.0) == pytest.approx(6.0, abs=1e-6)

    def test_on_sin(self):
        assert numerical_gradient(math.sin, 1.0) == pytest.approx(math.cos(1.0), abs=1e-6)

    def test_central_beats_forward_difference(self):
        """Central difference is O(h^2); forward is O(h). Verify it."""
        h = 1e-4
        exact = 6.0
        central = numerical_gradient(lambda x: x**2, 3.0, h=h)
        forward = ((3.0 + h) ** 2 - 3.0**2) / h
        assert abs(central - exact) < abs(forward - exact)


class TestGradientCheck:
    def test_passes_on_correct_implementation(self):
        def f(a, b):
            return (a * b + a.tanh()) * b

        inputs = [Value(0.4), Value(-1.3)]
        passed, errors = gradient_check(f, inputs)
        assert passed, f"relative errors: {errors}"

    @pytest.mark.parametrize(
        "f",
        [
            lambda a, b: a * b,
            lambda a, b: (a + b) ** 3,
            lambda a, b: (a * b).tanh(),
            lambda a, b: a.sigmoid() * b.relu(),
            lambda a, b: (a * a + b * b) ** 0.5,
            lambda a, b: (a.exp() + b.exp()).log(),
        ],
    )
    def test_across_expression_shapes(self, f):
        passed, errors = gradient_check(f, [Value(0.6), Value(1.1)])
        assert passed, f"relative errors: {errors}"


class TestLosses:
    def test_mse_gradient(self):
        p = Value(5.0)
        mse_loss(p, 3.0).backward()
        assert p.grad == pytest.approx(4.0)  # 2 * (5 - 3)

    def test_mse_is_zero_at_the_target(self):
        assert mse_loss(Value(3.0), 3.0).data == pytest.approx(0.0)

    def test_bce_forward(self):
        loss = binary_cross_entropy(Value(0.9), 1.0)
        assert loss.data == pytest.approx(-math.log(0.9), abs=1e-9)

    def test_bce_penalizes_confident_and_wrong(self):
        confident_wrong = binary_cross_entropy(Value(0.01), 1.0)
        confident_right = binary_cross_entropy(Value(0.99), 1.0)
        assert confident_wrong.data > 10 * confident_right.data

    def test_bce_does_not_produce_nan_at_the_extremes(self):
        """Clamping matters. Without it this is inf, and then everything is NaN."""
        loss = binary_cross_entropy(Value(0.0), 1.0)
        assert math.isfinite(loss.data)

    def test_sigmoid_bce_gradient_is_p_minus_y(self):
        """The cancellation you must be able to derive."""
        logit = Value(0.8)
        p = logit.sigmoid()
        binary_cross_entropy(p, 1.0).backward()
        expected = (1 / (1 + math.exp(-0.8))) - 1.0
        assert logit.grad == pytest.approx(expected, abs=1e-6)

    def test_softmax_sums_to_one(self):
        probs = softmax([Value(1.0), Value(2.0), Value(3.0)])
        assert sum(p.data for p in probs) == pytest.approx(1.0)

    def test_softmax_is_shift_invariant(self):
        a = softmax([Value(1.0), Value(2.0), Value(3.0)])
        b = softmax([Value(101.0), Value(102.0), Value(103.0)])
        for x, y in zip(a, b, strict=True):
            assert x.data == pytest.approx(y.data)

    def test_softmax_survives_large_logits(self):
        """Without the max-subtraction trick this overflows to nan."""
        probs = softmax([Value(1000.0), Value(1001.0)])
        assert all(math.isfinite(p.data) for p in probs)
        assert sum(p.data for p in probs) == pytest.approx(1.0)

    def test_cross_entropy_gradient_is_p_minus_onehot(self):
        logits = [Value(1.0), Value(2.0), Value(3.0)]
        cross_entropy(logits, target_index=1).backward()

        exps = [math.exp(v) for v in (1.0, 2.0, 3.0)]
        total = sum(exps)
        expected = [e / total for e in exps]
        expected[1] -= 1.0

        for logit, want in zip(logits, expected, strict=True):
            assert logit.grad == pytest.approx(want, abs=1e-6)


class TestEndToEnd:
    def test_gradient_descent_fits_a_line(self):
        """The whole point of the file: does it actually optimize?

        Fit y = 2x + 1 from four points using only this engine.
        """
        w, b = Value(0.0), Value(0.0)
        data = [(1.0, 3.0), (2.0, 5.0), (3.0, 7.0), (4.0, 9.0)]

        for _ in range(500):
            loss = Value(0.0)
            for x, y in data:
                loss = loss + mse_loss(w * x + b, y)
            loss = loss * (1.0 / len(data))

            w.zero_grad()
            b.zero_grad()
            loss.backward()

            w.data -= 0.01 * w.grad
            b.data -= 0.01 * b.grad

        assert w.data == pytest.approx(2.0, abs=0.05)
        assert b.data == pytest.approx(1.0, abs=0.1)
