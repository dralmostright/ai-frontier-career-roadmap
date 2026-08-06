"""Gradient boosting — Week 9.

Fit a weak model. Look at what it got wrong. Fit another model to *that*. Repeat.
The general form: each new tree is fit to the negative gradient of the loss with
respect to the current predictions — which for squared error is simply the
residual, and for log loss is (y - p).

Bagging versus boosting, the answer to have ready:

|              | Bagging                   | Boosting                        |
| ------------ | ------------------------- | ------------------------------- |
| Trees are    | independent, parallel     | sequential, each fixes the last |
| Reduces      | variance                  | bias                            |
| Base model   | deep (low bias, high var) | shallow stumps (high bias)      |
| More trees   | never overfits            | eventually overfits             |
| Tuning       | forgiving                 | sensitive to the learning rate  |

Gradient boosting on tabular data still beats deep learning in most cases. Say
that out loud in an interview when it is true — it shows you choose models on
evidence rather than fashion.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

import numpy as np
from decision_tree import DecisionTreeRegressor
from numpy.typing import NDArray

Array = NDArray[np.float64]


@dataclass
class GradientBoostingRegressor:
    """Gradient boosting for squared error.

    Args:
        n_estimators: Boosting rounds.
        learning_rate: Shrinkage. Each tree's contribution is scaled by this.
            Lower means more rounds and better generalization — the classic
            tradeoff, and the single most important hyperparameter here.
        max_depth: Keep it small (2-5). Boosting wants weak learners; a deep
            tree fits the residual perfectly and leaves nothing for round two.
        subsample: Fraction of rows per round. Below 1.0 gives stochastic
            gradient boosting, which adds regularization for free.
    """

    n_estimators: int = 100
    learning_rate: float = 0.1
    max_depth: int = 3
    min_samples_leaf: int = 1
    subsample: float = 1.0
    random_state: int | None = None

    trees_: list[DecisionTreeRegressor] = field(init=False, default_factory=list)
    init_prediction_: float = field(init=False, default=0.0)
    train_scores_: list[float] = field(init=False, default_factory=list)

    def fit(self, X: Array, y: Array) -> GradientBoostingRegressor:
        """Initialize with the mean, then fit each tree to the running residuals."""
        raise NotImplementedError("Week 9")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 9")

    def staged_predict(self, X: Array) -> Iterator[Array]:
        """Yield predictions after each round.

        This is how you find the optimal number of rounds: plot validation error
        against round index and take the minimum. Unlike a random forest, more
        rounds are not free.
        """
        raise NotImplementedError("Week 9")


@dataclass
class GradientBoostingClassifier:
    """Gradient boosting for binary log loss.

    The trees still fit real-valued targets — they regress on the gradient of the
    log loss, which is (y - p). Predictions accumulate in log-odds space and a
    sigmoid converts at the end. Being able to explain that a classifier is built
    out of regression trees is a good depth check.
    """

    n_estimators: int = 100
    learning_rate: float = 0.1
    max_depth: int = 3
    subsample: float = 1.0
    random_state: int | None = None

    trees_: list[DecisionTreeRegressor] = field(init=False, default_factory=list)
    init_log_odds_: float = field(init=False, default=0.0)

    def fit(self, X: Array, y: Array) -> GradientBoostingClassifier:
        raise NotImplementedError("Week 9")

    def predict_proba(self, X: Array) -> Array:
        raise NotImplementedError("Week 9")

    def predict(self, X: Array, threshold: float = 0.5) -> Array:
        raise NotImplementedError("Week 9")


@dataclass
class AdaBoostClassifier:
    """AdaBoost, for contrast.

    Reweights *samples* rather than fitting residuals: misclassified points get
    heavier each round. It predates gradient boosting and is a special case of
    it (exponential loss). Implement it once so that "AdaBoost is gradient
    boosting with exponential loss" becomes something you have verified rather
    than something you repeat.
    """

    n_estimators: int = 50
    learning_rate: float = 1.0
    random_state: int | None = None

    estimators_: list[object] = field(init=False, default_factory=list)
    estimator_weights_: list[float] = field(init=False, default_factory=list)

    def fit(self, X: Array, y: Array) -> AdaBoostClassifier:
        raise NotImplementedError("Week 9")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 9")


def early_stopping_round(
    val_scores: list[float], patience: int = 10, higher_is_better: bool = False
) -> int:
    """Return the best round index, stopping after `patience` rounds without gain.

    You will reuse this in Week 19 for neural network training and Week 48 for
    fine-tuning. Same idea every time.
    """
    raise NotImplementedError("Week 9")
