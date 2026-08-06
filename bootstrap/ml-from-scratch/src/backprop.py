"""Backpropagation and gradient verification — Week 14.

Backpropagation is the chain rule applied in reverse topological order, with
intermediate results cached so nothing is computed twice. That sentence is the
whole algorithm. Everything else is bookkeeping about shapes.

This module holds the verification tooling. `gradient_check` is the most
valuable function in the entire bootstrap workspace: a wrong gradient does not
crash, it just trains to a worse optimum, and you will spend four days blaming
the learning rate. Check every gradient you write, here and in Weeks 29 and 30.
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from neural_net import Layer, Loss
from numpy.typing import NDArray

Array = NDArray[np.float64]


def numerical_gradient(f: Callable[[Array], float], x: Array, h: float = 1e-5) -> Array:
    """Central-difference gradient of a scalar function at x.

    Perturb each element independently: (f(x+h) - f(x-h)) / 2h. Cost is O(n)
    forward passes, which is why this is a debugging tool and not a training
    method — and why reverse-mode autodiff, which gets all n partials in one
    backward pass, was such a consequential idea.

    Operate on a copy. Mutating the caller's array while probing it produces a
    bug that is genuinely unpleasant to find.
    """
    raise NotImplementedError("Week 14")


def relative_error(analytic: Array, numeric: Array, eps: float = 1e-12) -> Array:
    """|a - n| / max(|a|, |n|, eps), elementwise.

    Use relative, not absolute, error. Gradient magnitudes span many orders of
    magnitude and an absolute threshold either passes everything or fails
    everything.

    Interpretation:
        < 1e-7   correct
        1e-7-1e-4  suspicious; fine for tanh/softmax chains, not for a Linear
        > 1e-4   a bug
        > 1e-2   badly wrong
    """
    raise NotImplementedError("Week 14")


def gradient_check_layer(
    layer: Layer, x: Array, tolerance: float = 1e-6, h: float = 1e-5
) -> dict[str, float]:
    """Verify one layer's input and parameter gradients.

    Procedure: forward, backward with a random upstream gradient, then compare
    each analytic gradient to a finite-difference estimate of the same quantity.

    Run this on every layer you write. It takes two minutes and it is the
    difference between "my network doesn't learn and I don't know why" and
    "layer 3's bias gradient is wrong."

    Returns:
        Max relative error per checked tensor, keyed by name.
    """
    raise NotImplementedError("Week 14")


def gradient_check_network(
    network: Layer,
    loss_fn: Loss,
    x: Array,
    y: Array,
    tolerance: float = 1e-6,
) -> dict[str, float]:
    """End-to-end check on a full network.

    Use float64 and a small batch. In float32 the finite-difference estimate is
    dominated by rounding noise and the check reports failures that are not
    real — which is why PyTorch's ``gradcheck`` also insists on double precision.
    """
    raise NotImplementedError("Week 14")


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------


def gradient_norms(network: Layer) -> dict[str, float]:
    """Per-parameter gradient L2 norms.

    Log these every N steps for the rest of the course. The shape of this
    diagnostic tells you what is wrong faster than the loss curve does:

    - Norms shrinking geometrically with depth → vanishing gradients.
    - Norms in the thousands → exploding; clip them.
    - Norms at exactly zero → dead units, or a detached graph.
    - One layer orders of magnitude above the rest → that layer is the problem.
    """
    raise NotImplementedError("Week 14")


def check_gradient_flow(network: Layer, threshold: float = 1e-7) -> dict[str, str]:
    """Classify each layer's gradient health as ok / vanishing / exploding / dead.

    Returns:
        Layer name to diagnosis.
    """
    raise NotImplementedError("Week 14")


def activation_statistics(network: Layer, x: Array) -> dict[str, dict[str, float]]:
    """Mean, std, and dead-unit fraction per layer, on a forward pass.

    Healthy: roughly zero mean, std near 1, dead fraction under 10%. Std
    collapsing toward zero with depth means your initialization is too small;
    std growing means it is too large. This is the diagnostic that makes He and
    Xavier initialization feel like engineering instead of folklore.
    """
    raise NotImplementedError("Week 14")


def clip_gradients(network: Layer, max_norm: float) -> float:
    """Rescale all gradients so their global L2 norm is at most ``max_norm``.

    Clip by *global* norm, not per-parameter — per-parameter clipping changes
    the gradient's direction, while global clipping only changes its length.
    That distinction matters and is worth stating in an interview.

    Standard practice for transformers (max_norm=1.0). You will use it in
    Weeks 19, 32, and 35.

    Returns:
        The pre-clipping global norm, for logging.
    """
    raise NotImplementedError("Week 14")
