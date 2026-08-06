"""Week 15 — optimizers and learning rate schedules.

Each test isolates the specific failure the next optimizer in the sequence was
invented to fix. Read them in order and the "why Adam?" answer writes itself.
"""

from __future__ import annotations

from itertools import pairwise

import numpy as np
import pytest
from optimizers import (
    SGD,
    Adam,
    AdamW,
    CosineAnnealingLR,
    ReduceLROnPlateau,
    RMSProp,
    StepLR,
    WarmupCosineLR,
    compare_optimizers,
    lr_range_test,
)

pytestmark = pytest.mark.week(15)


def quadratic(w: np.ndarray, curvature: np.ndarray) -> tuple[float, np.ndarray]:
    """f(w) = 0.5 * sum(curvature * w^2). Minimum at the origin."""
    return 0.5 * float(np.sum(curvature * w**2)), curvature * w


def run(optimizer_cls, curvature, steps=300, start=None, **kwargs):
    w = (np.array([1.0, 1.0]) if start is None else start.copy()).astype(float)
    params = [w]
    opt = optimizer_cls(params, **kwargs)
    trace = []
    for _ in range(steps):
        _, grad = quadratic(w, curvature)
        opt.step([grad])
        trace.append(float(np.linalg.norm(w)))
    return w, trace


class TestSGD:
    def test_converges_on_a_well_conditioned_problem(self):
        w, _ = run(SGD, np.array([1.0, 1.0]), lr=0.1)
        assert np.linalg.norm(w) < 0.01

    def test_struggles_in_an_ill_conditioned_ravine(self):
        """Curvature ratio 100:1. Plain SGD crawls. This is momentum's reason to exist."""
        w, _ = run(SGD, np.array([100.0, 1.0]), steps=200, lr=0.005)
        assert np.linalg.norm(w) > 0.1

    def test_momentum_accelerates_through_the_ravine(self):
        plain, _ = run(SGD, np.array([100.0, 1.0]), steps=200, lr=0.005)
        with_momentum, _ = run(SGD, np.array([100.0, 1.0]), steps=200, lr=0.005, momentum=0.9)
        assert np.linalg.norm(with_momentum) < np.linalg.norm(plain)

    def test_nesterov_runs_and_converges(self):
        w, _ = run(SGD, np.array([1.0, 1.0]), lr=0.05, momentum=0.9, nesterov=True)
        assert np.linalg.norm(w) < 0.05

    def test_weight_decay_pulls_toward_the_origin(self):
        w = np.array([5.0, 5.0])
        opt = SGD([w], lr=0.1, weight_decay=0.5)
        for _ in range(50):
            opt.step([np.zeros(2)])  # no data gradient — only decay acts
        assert np.linalg.norm(w) < 5.0

    def test_too_large_a_learning_rate_diverges(self):
        w, _ = run(SGD, np.array([1.0, 1.0]), steps=50, lr=5.0)
        assert np.linalg.norm(w) > 10.0 or not np.all(np.isfinite(w))


class TestRMSProp:
    def test_converges(self):
        w, _ = run(RMSProp, np.array([1.0, 1.0]), steps=800, lr=0.05)
        assert np.linalg.norm(w) < 0.05

    def test_handles_wildly_different_gradient_scales(self):
        """Per-parameter steps: the point of the second moment."""
        sgd_w, _ = run(SGD, np.array([1000.0, 0.01]), steps=400, lr=1e-4)
        rms_w, _ = run(RMSProp, np.array([1000.0, 0.01]), steps=400, lr=0.02)
        assert abs(rms_w[1]) < abs(sgd_w[1])


class TestAdam:
    def test_converges(self):
        w, _ = run(Adam, np.array([1.0, 1.0]), steps=800, lr=0.05)
        assert np.linalg.norm(w) < 0.02

    def test_bias_correction_is_present(self):
        """Without it, m and v start at zero and the first steps are absurdly small.

        With bias correction, step one moves roughly `lr`. Without, far less.
        Implement it both ways, plot the first 200 steps, and put the figure in
        your Week 15 write-up.
        """
        w = np.array([1.0])
        opt = Adam([w], lr=0.1)
        before = w.copy()
        opt.step([np.array([1.0])])
        assert abs(float(before - w)) == pytest.approx(0.1, rel=0.2)

    def test_beats_sgd_on_an_ill_conditioned_problem(self):
        sgd_w, _ = run(SGD, np.array([100.0, 1.0]), steps=300, lr=0.005)
        adam_w, _ = run(Adam, np.array([100.0, 1.0]), steps=300, lr=0.05)
        assert np.linalg.norm(adam_w) < np.linalg.norm(sgd_w)

    def test_step_counter_advances(self):
        w = np.array([1.0])
        opt = Adam([w], lr=0.01)
        for _ in range(5):
            opt.step([np.array([1.0])])
        assert opt.t == 5


class TestAdamW:
    def test_converges(self):
        w, _ = run(AdamW, np.array([1.0, 1.0]), steps=800, lr=0.05, weight_decay=0.0)
        assert np.linalg.norm(w) < 0.02

    def test_decoupled_decay_differs_from_l2_in_the_gradient(self):
        """The whole point of the W, and a favorite interview question.

        Adam divides the L2 term by sqrt(v), so decay strength varies per
        parameter. AdamW applies it directly to the weights, keeping it uniform.
        With a large, uneven gradient history the two diverge measurably.
        """
        adam_w = np.array([1.0, 1.0])
        adamw_w = np.array([1.0, 1.0])
        adam = Adam([adam_w], lr=0.01, weight_decay=0.1)
        adamw = AdamW([adamw_w], lr=0.01, weight_decay=0.1)

        for _ in range(100):
            grad = np.array([10.0, 0.001])  # deliberately lopsided
            adam.step([grad.copy()])
            adamw.step([grad.copy()])

        assert not np.allclose(adam_w, adamw_w, atol=1e-4)

    def test_decay_shrinks_weights_with_no_gradient(self):
        w = np.array([1.0, 1.0])
        opt = AdamW([w], lr=0.1, weight_decay=0.1)
        for _ in range(50):
            opt.step([np.zeros(2)])
        assert np.linalg.norm(w) < 1.0


class TestSchedulers:
    def test_step_lr_decays_at_the_boundary(self):
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = StepLR(opt, base_lr=0.1, step_size=10, gamma=0.5)
        for _ in range(10):
            sched.step()
        assert opt.lr == pytest.approx(0.05)

    def test_cosine_anneals_to_the_minimum(self):
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = CosineAnnealingLR(opt, base_lr=0.1, T_max=100, eta_min=0.001)
        for _ in range(100):
            sched.step()
        assert opt.lr == pytest.approx(0.001, abs=1e-4)

    def test_cosine_is_monotonically_decreasing(self):
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = CosineAnnealingLR(opt, base_lr=0.1, T_max=100)
        rates = []
        for _ in range(100):
            sched.step()
            rates.append(opt.lr)
        assert all(b <= a + 1e-12 for a, b in pairwise(rates))

    def test_warmup_ramps_up_then_decays(self):
        """The schedule every LLM is trained with. Skipping warmup diverges."""
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = WarmupCosineLR(opt, base_lr=0.1, warmup_steps=100, total_steps=1000)

        rates = []
        for _ in range(1000):
            sched.step()
            rates.append(opt.lr)

        assert rates[0] < rates[50] < rates[99]
        assert rates[99] == pytest.approx(0.1, rel=0.05)
        assert rates[-1] < rates[99]

    def test_warmup_starts_near_zero(self):
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = WarmupCosineLR(opt, base_lr=0.1, warmup_steps=100, total_steps=1000)
        sched.step()
        assert opt.lr < 0.01

    def test_reduce_on_plateau_fires_after_patience(self):
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = ReduceLROnPlateau(opt, mode="min", factor=0.5, patience=3)
        for loss in [1.0, 0.9, 0.9, 0.9, 0.9, 0.9]:
            sched.step(loss)
        assert opt.lr < 0.1

    def test_reduce_on_plateau_does_not_fire_while_improving(self):
        opt = SGD([np.array([1.0])], lr=0.1)
        sched = ReduceLROnPlateau(opt, mode="min", factor=0.5, patience=2)
        for loss in [1.0, 0.8, 0.6, 0.4, 0.2]:
            sched.step(loss)
        assert opt.lr == pytest.approx(0.1)


@pytest.mark.slow
class TestDiagnostics:
    def test_lr_range_test_shape(self, rng):
        """Ten minutes of this replaces a day of guessing at learning rates."""
        X = rng.normal(size=(200, 4))
        y = (X[:, 0] > 0).astype(int)

        from neural_net import MLP

        rates, losses = lr_range_test(lambda: MLP([4, 8, 2]), X, y, n_steps=40)
        assert len(rates) == len(losses) == 40
        assert rates[0] < rates[-1]

    def test_optimizer_comparison_returns_trajectories(self):
        """Plot these overlaid on Rosenbrock. One figure, and Week 15 is written."""
        trajectories = compare_optimizers("rosenbrock", n_steps=200)
        assert {"sgd", "momentum", "adam"} <= {k.lower() for k in trajectories}
        for path in trajectories.values():
            assert len(path) == 200
