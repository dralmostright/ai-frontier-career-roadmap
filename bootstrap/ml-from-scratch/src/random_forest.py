"""Bagging and random forests — Week 8.

Two independent ideas, and the interview value lies in separating them:

1. **Bagging.** Train each tree on a bootstrap sample. Averaging models trained
   on different data reduces variance without increasing bias.
2. **Feature subsampling.** Consider only a random subset of features at each
   split. This *decorrelates* the trees, and decorrelation is what makes the
   averaging effective — averaging k identical models reduces nothing.

Bagging alone gives a bagged forest. Bagging plus feature subsampling gives a
random forest, which is meaningfully better. Knowing that the second idea is the
load-bearing one is the depth an interviewer is probing for.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

import numpy as np
from decision_tree import DecisionTreeClassifier, DecisionTreeRegressor
from numpy.typing import NDArray

Array = NDArray[np.float64]


def bootstrap_sample(X: Array, y: Array, rng: np.random.Generator) -> tuple[Array, Array, Array]:
    """Sample n rows with replacement.

    About 36.8% of rows are left out of any given bootstrap — the limit of
    (1 - 1/n)^n is 1/e. Those out-of-bag rows are a free validation set, an
    elegant property worth being able to derive on the spot.

    Returns:
        (X_boot, y_boot, oob_indices).
    """
    raise NotImplementedError("Week 8")


@dataclass
class RandomForestClassifier:
    """A forest of decorrelated trees.

    Args:
        n_estimators: Number of trees. More is monotonically better for accuracy
            and linearly worse for latency; it does not overfit. Contrast with
            boosting, where more rounds *does* overfit.
        max_features: Features per split. "sqrt" is the classification default
            and the setting that does the decorrelating.
        bootstrap: Set False to get a forest that differs only by feature
            subsampling — a useful ablation for your write-up.
        oob_score: Compute the out-of-bag accuracy estimate.
    """

    n_estimators: int = 100
    criterion: str = "gini"
    max_depth: int | None = None
    min_samples_split: int = 2
    min_samples_leaf: int = 1
    max_features: int | str | None = "sqrt"
    bootstrap: bool = True
    oob_score: bool = False
    random_state: int | None = None

    trees_: list[DecisionTreeClassifier] = field(init=False, default_factory=list)
    oob_score_: float = field(init=False, default=float("nan"))
    feature_importances_: Array = field(init=False, repr=False)

    def fit(self, X: Array, y: Array) -> RandomForestClassifier:
        raise NotImplementedError("Week 8")

    def predict(self, X: Array) -> Array:
        """Majority vote across trees."""
        raise NotImplementedError("Week 8")

    def predict_proba(self, X: Array) -> Array:
        """Average the per-tree probabilities.

        Averaging probabilities beats majority voting because voting discards
        confidence. Verify it empirically — it is a good, cheap ablation.
        """
        raise NotImplementedError("Week 8")

    def _compute_oob_score(self, X: Array, y: Array) -> float:
        """Score each row using only the trees that never saw it."""
        raise NotImplementedError("Week 8")


@dataclass
class RandomForestRegressor:
    """Regression forest.

    ``max_features`` defaults to all features here rather than sqrt — a
    convention difference worth knowing and being able to justify.
    """

    n_estimators: int = 100
    max_depth: int | None = None
    min_samples_split: int = 2
    min_samples_leaf: int = 1
    max_features: int | str | None = None
    bootstrap: bool = True
    random_state: int | None = None

    trees_: list[DecisionTreeRegressor] = field(init=False, default_factory=list)

    def fit(self, X: Array, y: Array) -> RandomForestRegressor:
        raise NotImplementedError("Week 8")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 8")


def permutation_importance(
    model: object,
    X: Array,
    y: Array,
    scoring: Callable[[Array, Array], float] | None = None,
    n_repeats: int = 10,
    rng: np.random.Generator | None = None,
) -> tuple[Array, Array]:
    """Shuffle one feature, measure how much the score drops.

    Model-agnostic and far more trustworthy than a tree's built-in importances,
    which are biased toward high-cardinality features. Preferring this, and
    being able to say why, is a Week 12 talking point that starts here.

    The caveat to state unprompted: correlated features split the credit, so two
    duplicated features can both look unimportant.

    Returns:
        (mean_importance, std_importance), each shape (n_features,).
    """
    raise NotImplementedError("Week 8")
