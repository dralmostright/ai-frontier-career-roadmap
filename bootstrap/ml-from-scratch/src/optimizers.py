"""Optimizers — Week 15.

Five optimizers, each fixing a specific failure of the one before it. Learn them
as a sequence of problems and solutions rather than a list of formulas, and the
interview question "why Adam?" becomes easy.

    SGD          → slow through ravines, oscillates across the steep direction
    Momentum     → accumulates velocity; damps oscillation, accelerates descent
    RMSProp      → per-parameter step sizes from a running squared-gradient average
    Adam         → momentum + RMSProp + bias correction
    AdamW        → Adam with weight decay decoupled from the gradient

AdamW is what actually trains modern transformers. Knowing *why* the decoupling
matters — that L2-in-the-loss gets divided by the same adaptive denominator as
the gradient, so it stops being a constant-strength penalty — is a genuinely
discriminating question.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


class Optimizer(ABC):
    """Base optimizer.

    Holds references to the parameter arrays and mutates them in place, exactly
    as PyTorch does. Understanding that ``optimizer.step()`` mutates tensors the
    model still holds references to is worth a minute of thought — it is why
    ``optimizer.zero_grad()`` is a separate call and why forgetting it silently
    accumulates.
    """

    def __init__(self, parameters: list[Array], lr: float = 0.01) -> None:
        self.parameters = parameters
        self.lr = lr
        self.t = 0

    @abstractmethod
    def step(self, gradients: list[Array]) -> None: ...

    def zero_grad(self, gradients: list[Array]) -> None:
        for g in gradients:
            g.fill(0.0)


@dataclass
class SGD(Optimizer):
    """Plain stochastic gradient descent, with optional momentum and Nesterov.

    w -= lr * g

    Its weakness is geometric: in a ravine (high curvature one way, low the
    other) it bounces across the steep direction while creeping along the
    shallow one. Momentum exists to fix exactly that.

    Momentum: v = mu*v + g; w -= lr*v. Think of a ball rolling downhill — it
    accumulates speed in consistent directions and averages away oscillation.

    Nesterov evaluates the gradient at the *look-ahead* position w - lr*mu*v,
    which lets it start slowing before it overshoots. Marginal but real.
    """

    def __init__(
        self,
        parameters: list[Array],
        lr: float = 0.01,
        momentum: float = 0.0,
        nesterov: bool = False,
        weight_decay: float = 0.0,
    ) -> None:
        raise NotImplementedError("Week 15")

    def step(self, gradients: list[Array]) -> None:
        raise NotImplementedError("Week 15")


@dataclass
class RMSProp(Optimizer):
    """Per-parameter learning rates from an exponentially averaged squared gradient.

    s = rho*s + (1-rho)*g²;  w -= lr * g / (sqrt(s) + eps)

    Parameters with consistently large gradients get small steps and vice versa.
    This matters enormously when features are on wildly different scales, or
    when embedding rows for rare tokens receive gradient far less often than
    common ones.

    ``eps`` inside versus outside the sqrt is a real implementation difference
    between frameworks. Pick one, document it, and know it exists.
    """

    def __init__(
        self, parameters: list[Array], lr: float = 0.001, rho: float = 0.9, eps: float = 1e-8
    ) -> None:
        raise NotImplementedError("Week 15")

    def step(self, gradients: list[Array]) -> None:
        raise NotImplementedError("Week 15")


@dataclass
class Adam(Optimizer):
    """Adaptive Moment Estimation. The default for almost everything.

        m = b1*m + (1-b1)*g              first moment  (momentum)
        v = b2*v + (1-b2)*g²             second moment (RMSProp)
        m_hat = m / (1 - b1^t)           bias correction
        v_hat = v / (1 - b2^t)
        w -= lr * m_hat / (sqrt(v_hat) + eps)

    **Bias correction is not optional.** m and v start at zero, so early
    estimates are biased toward zero; without correction the first few hundred
    steps take absurdly small steps. Implement Adam without it, plot the first
    200 steps, then add it and plot again. That comparison is the Week 15
    deliverable and it makes the correction term memorable rather than
    mysterious.

    The honest caveat, worth raising unprompted: Adam converges faster and
    frequently generalizes slightly worse than well-tuned SGD with momentum.
    Vision papers often report SGD; language models almost universally use Adam
    or AdamW.
    """

    def __init__(
        self,
        parameters: list[Array],
        lr: float = 0.001,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-8,
        weight_decay: float = 0.0,
    ) -> None:
        raise NotImplementedError("Week 15")

    def step(self, gradients: list[Array]) -> None:
        raise NotImplementedError("Week 15")


@dataclass
class AdamW(Optimizer):
    """Adam with decoupled weight decay. What actually trains transformers.

    The difference from Adam-with-weight_decay is one line and it matters:

        Adam:   g = g + wd * w      then adapt      (decay gets divided by sqrt(v))
        AdamW:  w -= lr * wd * w    separately      (decay stays constant strength)

    In Adam, folding L2 into the gradient means the penalty passes through the
    adaptive denominator, so parameters with large gradient history get decayed
    less — the opposite of the intent. AdamW applies decay directly to the
    weights and keeps it uniform.

    This is a favorite interview question precisely because most people use
    AdamW without knowing what the W is for.
    """

    def __init__(
        self,
        parameters: list[Array],
        lr: float = 0.001,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-8,
        weight_decay: float = 0.01,
    ) -> None:
        raise NotImplementedError("Week 15")

    def step(self, gradients: list[Array]) -> None:
        raise NotImplementedError("Week 15")


# ---------------------------------------------------------------------------
# Learning rate schedules
# ---------------------------------------------------------------------------


class LRScheduler(ABC):
    """Adjust the learning rate over training.

    The schedule frequently matters more than the optimizer. A well-scheduled
    SGD beats an unscheduled Adam more often than people expect.
    """

    def __init__(self, optimizer: Optimizer, base_lr: float) -> None:
        self.optimizer = optimizer
        self.base_lr = base_lr
        self.step_count = 0

    @abstractmethod
    def get_lr(self) -> float: ...

    def step(self) -> None:
        self.step_count += 1
        self.optimizer.lr = self.get_lr()


class StepLR(LRScheduler):
    """Multiply the learning rate by gamma every `step_size` epochs."""

    def __init__(self, optimizer, base_lr: float, step_size: int, gamma: float = 0.1) -> None:
        raise NotImplementedError("Week 15")

    def get_lr(self) -> float:
        raise NotImplementedError("Week 15")


class CosineAnnealingLR(LRScheduler):
    """Cosine decay from base_lr to eta_min over T_max steps.

    The modern default for transformer training. Smooth, no hyperparameter
    cliff, and it spends the end of training at a very small learning rate,
    which empirically finds flatter minima.
    """

    def __init__(self, optimizer, base_lr: float, T_max: int, eta_min: float = 0.0) -> None:
        raise NotImplementedError("Week 15")

    def get_lr(self) -> float:
        raise NotImplementedError("Week 15")


class WarmupCosineLR(LRScheduler):
    """Linear warmup, then cosine decay. What every LLM is trained with.

    Why warmup: at initialization Adam's second-moment estimate is unreliable,
    so early full-size steps can move parameters somewhere the model never
    recovers from. Warming up over the first few hundred to few thousand steps
    avoids that. Skipping warmup on a transformer is one of the reliable ways
    to make training diverge, and you will see it happen in Week 35 if you try.
    """

    def __init__(
        self, optimizer, base_lr: float, warmup_steps: int, total_steps: int, eta_min: float = 0.0
    ) -> None:
        raise NotImplementedError("Week 15")

    def get_lr(self) -> float:
        raise NotImplementedError("Week 15")


class ReduceLROnPlateau:
    """Drop the learning rate when a monitored metric stops improving.

    Reactive rather than scheduled. Useful when you cannot predict the total
    step count in advance.
    """

    def __init__(
        self,
        optimizer: Optimizer,
        mode: str = "min",
        factor: float = 0.1,
        patience: int = 10,
        min_lr: float = 0.0,
    ) -> None:
        raise NotImplementedError("Week 15")

    def step(self, metric: float) -> None:
        raise NotImplementedError("Week 15")


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------


def lr_range_test(
    model_factory,
    X: Array,
    y: Array,
    min_lr: float = 1e-7,
    max_lr: float = 10.0,
    n_steps: int = 100,
) -> tuple[Array, Array]:
    """Sweep the learning rate exponentially upward and record the loss.

    Leslie Smith's LR finder. The loss falls, reaches a minimum, then explodes.
    Pick roughly one order of magnitude below the explosion point.

    Ten minutes here replaces a day of guessing, and "I ran an LR range test" is
    a much better interview answer than "I used 3e-4 because everyone does."

    Returns:
        (learning_rates, losses) for plotting on a log-x axis.
    """
    raise NotImplementedError("Week 15")


def compare_optimizers(
    loss_surface: str = "rosenbrock", n_steps: int = 500
) -> dict[str, list[tuple[float, float]]]:
    """Run every optimizer on a 2-D test surface and return their trajectories.

    Plot them overlaid. Rosenbrock's banana-shaped valley shows momentum's value
    immediately; a saddle point shows why plain SGD stalls; an ill-conditioned
    quadratic shows what adaptive methods buy.

    Three plots, one figure, and the Week 15 write-up is done.

    Returns:
        Optimizer name to list of (x, y) positions.
    """
    raise NotImplementedError("Week 15")
