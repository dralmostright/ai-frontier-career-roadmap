"""Neural networks from scratch — Weeks 13-16.

A miniature deep learning framework in NumPy. Layers, losses, optimizers, and a
training loop, with the same API shape as PyTorch so that Month 5 feels like a
port rather than a new language.

**Why build this.** When PyTorch produces a NaN, or your GPU sits at 30%
utilization, or the loss plateaus at exactly ln(num_classes), the engineers who
diagnose it quickly are the ones who know what the framework is doing
underneath. Two weeks here buys you seventeen months of not being confused.

Design note: everything is array-based, unlike `math-labs/autodiff_scalar.py`
which was scalar. The concepts are identical; only the shapes change. If a
gradient here confuses you, re-derive it on scalars first.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Base classes
# ---------------------------------------------------------------------------


class Layer(ABC):
    """A differentiable transformation.

    The contract every layer honors:

    - ``forward(x)`` returns the output and caches whatever the backward pass
      needs. That cache is why training uses far more memory than inference,
      and it is the thing gradient checkpointing trades away in Week 49.
    - ``backward(grad_output)`` takes dL/d(output) and returns dL/d(input),
      accumulating parameter gradients along the way.

    The shapes are the hard part, not the calculus. dL/d(input) always has the
    shape of the input; dL/d(W) always has the shape of W. When a derivation
    stalls, write the shapes down first and the transposes place themselves.
    """

    def __init__(self) -> None:
        self.training = True

    @abstractmethod
    def forward(self, x: Array) -> Array: ...

    @abstractmethod
    def backward(self, grad_output: Array) -> Array: ...

    def parameters(self) -> list[Array]:
        return []

    def gradients(self) -> list[Array]:
        return []

    def train(self) -> None:
        self.training = True

    def eval(self) -> None:
        """Switch to inference mode.

        Dropout stops dropping; BatchNorm uses running statistics. Forgetting to
        call this before evaluation is a classic bug that shows up as
        validation metrics that are noisy and slightly too low.
        """
        self.training = False

    def __call__(self, x: Array) -> Array:
        return self.forward(x)


# ---------------------------------------------------------------------------
# Week 13: layers and activations
# ---------------------------------------------------------------------------


class Linear(Layer):
    """Fully connected layer: y = xW + b.

    Gradients (derive these on paper before implementing):
        dL/dW = x^T @ grad_output
        dL/db = sum(grad_output, axis=0)
        dL/dx = grad_output @ W^T

    Initialization is not a detail. Zeros make every neuron identical forever
    (the symmetry never breaks). Large values saturate activations. Use He
    initialization for ReLU (std = sqrt(2/fan_in)) and Xavier/Glorot for tanh
    (std = sqrt(1/fan_in)); both keep activation variance roughly constant
    across depth, which is exactly what prevents vanishing and exploding
    signals in the forward pass.
    """

    def __init__(self, in_features: int, out_features: int, init: str = "he") -> None:
        raise NotImplementedError("Week 13")

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")


class ReLU(Layer):
    """max(0, x). Gradient is 1 where x > 0, else 0.

    Why it beat sigmoid: the gradient does not saturate for positive inputs, so
    signal survives depth. Its failure mode — dead ReLUs, where a large negative
    bias makes a unit output zero forever with zero gradient — is a good
    interview follow-up. LeakyReLU exists to fix it.
    """

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")


class Sigmoid(Layer):
    """1/(1+e^-x). Gradient is s(1-s), maximum 0.25 at x=0.

    That 0.25 ceiling is the vanishing gradient problem, quantitatively: stack
    ten sigmoid layers and the gradient reaching layer one is at most 0.25^10 ≈
    1e-6. Be able to produce that calculation on demand.
    """

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")


class Tanh(Layer):
    """Zero-centered, gradient 1 - tanh². Better than sigmoid for hidden layers
    because the zero-centering keeps gradient signs mixed rather than uniform."""

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")


class GELU(Layer):
    """Gaussian Error Linear Unit — the activation in every modern transformer.

    x * Φ(x), usually via the tanh approximation. Smooth everywhere, unlike
    ReLU. Implement it here and you will recognize it in Week 30.
    """

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")


class Softmax(Layer):
    """Softmax over the last axis.

    The Jacobian is dense: every output depends on every input. In practice you
    almost never need it, because fusing softmax with cross-entropy collapses
    the whole thing to ``p - y``. Implement the standalone version once to see
    why the fusion is worth it.
    """

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")


class Sequential(Layer):
    """A stack of layers. Forward runs in order; backward runs in reverse.

    That reversal *is* backpropagation. Once you have written these six lines,
    the algorithm stops being intimidating.
    """

    def __init__(self, *layers: Layer) -> None:
        raise NotImplementedError("Week 13")

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 13")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 14")

    def parameters(self) -> list[Array]:
        raise NotImplementedError("Week 13")

    def gradients(self) -> list[Array]:
        raise NotImplementedError("Week 14")

    def train(self) -> None:
        raise NotImplementedError("Week 16")

    def eval(self) -> None:
        raise NotImplementedError("Week 16")


# ---------------------------------------------------------------------------
# Week 14: losses
# ---------------------------------------------------------------------------


class Loss(ABC):
    @abstractmethod
    def forward(self, predictions: Array, targets: Array) -> float: ...

    @abstractmethod
    def backward(self) -> Array: ...

    def __call__(self, predictions: Array, targets: Array) -> float:
        return self.forward(predictions, targets)


class MSELoss(Loss):
    """Mean squared error. dL/dpred = 2(pred - target)/n."""

    def forward(self, predictions: Array, targets: Array) -> float:
        raise NotImplementedError("Week 14")

    def backward(self) -> Array:
        raise NotImplementedError("Week 14")


class CrossEntropyLoss(Loss):
    """Softmax + negative log likelihood, fused.

    Takes raw logits, not probabilities. The fusion gives numerical stability
    (via log-sum-exp) and the clean gradient ``(p - y)/n``. This is exactly why
    PyTorch's ``CrossEntropyLoss`` warns against applying softmax first — and
    now you know the reason rather than the rule.

    Sanity check to internalize: an untrained classifier over C classes should
    report a loss near ln(C). 2.30 for 10 classes, 6.91 for 1000. If your
    initial loss is far from that, something is wrong before training even
    starts. This single check will save you hours in Month 5 and Month 8.
    """

    def forward(self, logits: Array, targets: Array) -> float:
        raise NotImplementedError("Week 14")

    def backward(self) -> Array:
        raise NotImplementedError("Week 14")


class BCELoss(Loss):
    """Binary cross entropy from logits. Same fusion argument as above."""

    def forward(self, logits: Array, targets: Array) -> float:
        raise NotImplementedError("Week 14")

    def backward(self) -> Array:
        raise NotImplementedError("Week 14")


# ---------------------------------------------------------------------------
# Week 16: regularization layers
# ---------------------------------------------------------------------------


class Dropout(Layer):
    """Randomly zero activations during training.

    Use *inverted* dropout: scale surviving activations by 1/(1-p) at training
    time so that inference needs no adjustment at all. Every framework does it
    this way, and knowing why is a decent interview question.

    Must be a no-op when ``self.training`` is False.
    """

    def __init__(self, p: float = 0.5) -> None:
        raise NotImplementedError("Week 16")

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 16")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 16")


class BatchNorm1d(Layer):
    """Normalize each feature across the batch, then scale and shift.

    Two modes, and conflating them is a classic bug: training uses batch
    statistics and updates a running average; evaluation uses that running
    average. A model that performs well in training mode and badly in eval mode
    almost always has a BatchNorm problem.

    Why it works is still debated — the original "internal covariate shift"
    explanation has been largely displaced by "it smooths the loss landscape."
    Saying that you know the explanation is contested is a better answer than
    confidently reciting the original paper.
    """

    def __init__(self, num_features: int, momentum: float = 0.1, eps: float = 1e-5) -> None:
        raise NotImplementedError("Week 16")

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 16")

    def backward(self, grad_output: Array) -> Array:
        """The gnarliest derivation in this file. Do it on paper, carefully.

        The subtlety: the batch mean and variance both depend on every input in
        the batch, so each input's gradient has three routes to travel. Getting
        this right and gradient-checking it is the strongest possible evidence
        that you understand backpropagation.
        """
        raise NotImplementedError("Week 16")


class LayerNorm(Layer):
    """Normalize across features within each sample, independent of the batch.

    The transformer's choice, and the reason matters: batch statistics are
    unusable for variable-length sequences and for batch size 1 at inference.
    LayerNorm has neither problem. You will reimplement this in Week 30 — build
    it here first.
    """

    def __init__(self, normalized_shape: int, eps: float = 1e-5) -> None:
        raise NotImplementedError("Week 16")

    def forward(self, x: Array) -> Array:
        raise NotImplementedError("Week 16")

    def backward(self, grad_output: Array) -> Array:
        raise NotImplementedError("Week 16")


# ---------------------------------------------------------------------------
# Model wrapper and training loop
# ---------------------------------------------------------------------------


@dataclass
class MLP:
    """Multi-layer perceptron with a scikit-learn-flavored interface.

    The Month 4 capstone deliverable: this must train MNIST to >95% test
    accuracy using nothing but NumPy and the code in this file.
    """

    layer_sizes: list[int]
    activation: str = "relu"
    dropout: float = 0.0
    batch_norm: bool = False

    network_: Sequential = field(init=False, repr=False)
    history_: dict[str, list[float]] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        raise NotImplementedError("Week 13")

    def fit(
        self,
        X: Array,
        y: Array,
        epochs: int = 100,
        batch_size: int = 32,
        learning_rate: float = 0.01,
        optimizer: str = "adam",
        validation_data: tuple[Array, Array] | None = None,
        early_stopping_patience: int | None = None,
        verbose: bool = True,
    ) -> MLP:
        """Train. Record per-epoch train and validation loss in ``history_``.

        Plot that history every single time. A loss curve answers "is the
        learning rate wrong", "am I overfitting", and "has it converged"
        instantly, and every one of those questions costs an hour to answer
        without it.
        """
        raise NotImplementedError("Week 13")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 13")

    def predict_proba(self, X: Array) -> Array:
        raise NotImplementedError("Week 13")


def iterate_minibatches(
    X: Array,
    y: Array,
    batch_size: int,
    shuffle: bool = True,
    rng: np.random.Generator | None = None,
):
    """Yield (X_batch, y_batch).

    Shuffle every epoch, not once. Fixed batch composition correlates the
    gradient noise across epochs and measurably hurts convergence.
    """
    raise NotImplementedError("Week 13")
