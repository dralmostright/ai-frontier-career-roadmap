"""Linear regression — Week 5.

The simplest supervised model, and the one every later model generalizes. A
transformer is, at its final layer, a linear model over learned features.

Two routes to the same answer:

- **Normal equation.** w = (X^T X)^-1 X^T y. Exact, O(d^3), fails when X^T X is
  singular. Use `np.linalg.lstsq` (SVD-based) rather than inverting — forming
  an explicit inverse is slower and numerically worse, and knowing that is a
  real signal in an interview.
- **Gradient descent.** Iterative, O(nd) per step, scales to any d, and is the
  only option once the model stops being linear.

Implement both. Verify they agree. Then construct the case where the normal
equation breaks and gradient descent does not.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


@dataclass
class LinearRegression:
    """Ordinary and regularized least squares.

    Args:
        method: "normal" (closed form) or "gd" (gradient descent).
        learning_rate: Step size for gradient descent.
        n_iters: Number of gradient descent steps.
        l2: Ridge penalty. Shrinks weights toward zero smoothly.
        l1: Lasso penalty. Drives weights exactly to zero (sparsity). Requires
            method="gd" — there is no closed form.
        fit_intercept: Whether to fit a bias term. Never penalize the intercept;
            doing so makes predictions depend on the units of y.
    """

    method: str = "normal"
    learning_rate: float = 0.01
    n_iters: int = 1000
    l2: float = 0.0
    l1: float = 0.0
    fit_intercept: bool = True

    weights_: Array = field(init=False, repr=False)
    intercept_: float = field(init=False, default=0.0)
    history_: list[float] = field(init=False, default_factory=list)

    def fit(self, X: Array, y: Array) -> LinearRegression:
        """Fit on (n_samples, n_features) and (n_samples,).

        Record the loss at each gradient-descent step in ``history_``. Plotting
        it is how you diagnose a learning rate, and building that habit now pays
        off for the next seventy weeks.
        """
        raise NotImplementedError("Week 5")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 5")

    def score(self, X: Array, y: Array) -> float:
        """R^2. Note it can be negative — a model worse than predicting the mean."""
        raise NotImplementedError("Week 5")


def mse(y_true: Array, y_pred: Array) -> float:
    """Mean squared error. Penalizes large errors quadratically, so it is
    sensitive to outliers. That is a property, not a defect — but know which
    you want before you pick it."""
    raise NotImplementedError("Week 5")


def mae(y_true: Array, y_pred: Array) -> float:
    """Mean absolute error. Robust to outliers, non-differentiable at zero."""
    raise NotImplementedError("Week 5")


def rmse(y_true: Array, y_pred: Array) -> float:
    """Root MSE. Same units as y, which is why you report it to stakeholders."""
    raise NotImplementedError("Week 5")


def r_squared(y_true: Array, y_pred: Array) -> float:
    """1 - SS_res / SS_tot. The fraction of variance explained."""
    raise NotImplementedError("Week 5")


def normal_equation(X: Array, y: Array, l2: float = 0.0) -> Array:
    """Closed-form solution, with optional ridge.

    Use `np.linalg.lstsq`, not `np.linalg.inv`. Forming an explicit inverse
    squares the condition number for no benefit.

    Ridge adds l2 * I to X^T X, which guarantees invertibility even under
    perfect collinearity. That numerical guarantee is the original reason ridge
    regression exists; the generalization benefit came second.
    """
    raise NotImplementedError("Week 5")


def gradient_descent_step(X: Array, y: Array, w: Array, lr: float, l2: float = 0.0) -> Array:
    """One step. Derive the gradient by hand first: dL/dw = (2/n) X^T (Xw - y).

    Note the 2/n. Dropping the 2 is harmless — it folds into the learning rate.
    Dropping the 1/n is not, because then the correct learning rate depends on
    the batch size. That is precisely why batch size and learning rate are
    coupled in Week 15.
    """
    raise NotImplementedError("Week 5")


def polynomial_features(X: Array, degree: int) -> Array:
    """Expand to polynomial terms. The cheapest way to demonstrate overfitting.

    Fit degrees 1, 3, 9, and 15 to twenty noisy points and plot all four. The
    degree-15 curve threading every point is the clearest picture of variance
    you will ever produce. Put it in your Week 5 write-up.
    """
    raise NotImplementedError("Week 5")


def train_test_split(
    X: Array, y: Array, test_size: float = 0.2, rng: np.random.Generator | None = None
) -> tuple[Array, Array, Array, Array]:
    """Shuffle and split. Returns (X_train, X_test, y_train, y_test).

    Shuffling matters. Data ordered by anything correlated with the target
    produces a test set that is not exchangeable with the training set, and the
    resulting generalization estimate is meaningless.
    """
    raise NotImplementedError("Week 5")


def bias_variance_decomposition(
    model_factory: Callable[[], object],
    X: Array,
    y: Array,
    n_trials: int = 50,
    rng: np.random.Generator | None = None,
) -> dict[str, float]:
    """Empirically decompose expected error into bias², variance, and noise.

    Train the same model on many bootstrap samples. For each test point, measure
    how far the *average* prediction sits from the truth (bias) and how much
    predictions move across trials (variance).

    Being able to *show* this decomposition, rather than recite the definition,
    is what a 9/10 answer to "explain bias-variance" looks like.

    Returns:
        Keys ``bias_squared``, ``variance``, ``total_error``.
    """
    raise NotImplementedError("Week 5")
