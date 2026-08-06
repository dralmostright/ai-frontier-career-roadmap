"""Logistic regression — Week 6.

Linear regression's classifier sibling, and the direct ancestor of the softmax
layer at the top of every language model.

The derivation you must own: with a sigmoid output and a log-loss objective,
dL/dz = p - y, where z is the logit. Every messy term cancels. The same
cancellation happens for softmax + cross entropy, which is why frameworks fuse
those two operations into one and warn you not to apply softmax before
`CrossEntropyLoss`.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def sigmoid(z: Array | float) -> Array | float:
    """1 / (1 + e^-z), computed stably.

    The naive form overflows for z < -700. The standard fix branches on sign and
    uses e^z / (1 + e^z) for negative z. Do it — three lines, and it is the
    difference between a robust implementation and one that emits warnings on
    real data.
    """
    raise NotImplementedError("Week 6")


def log_loss(y_true: Array, y_prob: Array, eps: float = 1e-15) -> float:
    """Binary cross entropy. Clip probabilities into [eps, 1-eps] first."""
    raise NotImplementedError("Week 6")


@dataclass
class LogisticRegression:
    """Binary classifier trained by gradient descent.

    Args:
        learning_rate: Step size.
        n_iters: Maximum full-batch steps.
        l2: Ridge penalty on the weights, not the intercept.
        class_weight: None or "balanced". Balanced reweights the loss inversely
            to class frequency, which matters enormously for the imbalanced
            problems in Week 11.
        tol: Stop early when the loss improves by less than this.
    """

    learning_rate: float = 0.1
    n_iters: int = 1000
    l2: float = 0.0
    class_weight: str | None = None
    tol: float = 1e-7

    weights_: Array = field(init=False, repr=False)
    intercept_: float = field(init=False, default=0.0)
    history_: list[float] = field(init=False, default_factory=list)

    def fit(self, X: Array, y: Array) -> LogisticRegression:
        """Fit. y must contain only 0 and 1."""
        raise NotImplementedError("Week 6")

    def predict_proba(self, X: Array) -> Array:
        """P(y=1|x), shape (n_samples,)."""
        raise NotImplementedError("Week 6")

    def predict(self, X: Array, threshold: float = 0.5) -> Array:
        """Hard labels.

        0.5 is a default, not a law. It is optimal only when false positives and
        false negatives cost the same *and* the model is calibrated. Neither is
        usually true. Week 11 covers choosing it properly.
        """
        raise NotImplementedError("Week 6")

    def decision_function(self, X: Array) -> Array:
        """Raw logits, before the sigmoid."""
        raise NotImplementedError("Week 6")


@dataclass
class SoftmaxRegression:
    """Multiclass logistic regression.

    This is exactly the final layer of a neural classifier, and of a language
    model at each position — the only difference there is that the vocabulary
    has 50,000 classes instead of three.
    """

    learning_rate: float = 0.1
    n_iters: int = 1000
    l2: float = 0.0

    weights_: Array = field(init=False, repr=False)
    intercept_: Array = field(init=False, repr=False)
    classes_: Array = field(init=False, repr=False)

    def fit(self, X: Array, y: Array) -> SoftmaxRegression:
        raise NotImplementedError("Week 6")

    def predict_proba(self, X: Array) -> Array:
        """Shape (n_samples, n_classes), each row summing to 1."""
        raise NotImplementedError("Week 6")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 6")


def softmax(logits: Array, axis: int = -1) -> Array:
    """Stable softmax. Subtract the max along ``axis`` before exponentiating."""
    raise NotImplementedError("Week 6")


def one_hot(y: Array, n_classes: int | None = None) -> Array:
    """Integer labels to one-hot rows, shape (n_samples, n_classes)."""
    raise NotImplementedError("Week 6")
