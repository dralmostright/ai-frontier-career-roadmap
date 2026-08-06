"""Decision trees — Week 7.

Recursive partitioning: find the split that most reduces impurity, recurse on
each side, stop when a criterion is met. That is the whole algorithm.

Trees matter here for three reasons. They are the base learner for random
forests (Week 8) and gradient boosting (Week 9), which remain the strongest
models for tabular data. They are the cleanest illustration of overfitting — an
unconstrained tree memorizes the training set perfectly and generalizes badly.
And the split criterion is `information_gain` from Week 4, which makes the link
between information theory and ML concrete rather than decorative.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


@dataclass
class Node:
    """A node. Internal nodes carry a feature and threshold; leaves carry a value."""

    feature_index: int | None = None
    threshold: float | None = None
    left: Node | None = None
    right: Node | None = None
    value: float | Array | None = None
    n_samples: int = 0
    impurity: float = 0.0

    @property
    def is_leaf(self) -> bool:
        return self.value is not None


@dataclass
class DecisionTreeClassifier:
    """CART classifier.

    Args:
        criterion: "gini" or "entropy". They rarely disagree; gini avoids a
            logarithm, which is why most libraries default to it. Resist
            inventing a deeper justification in an interview.
        max_depth: Depth limit. The most effective single regularizer.
        min_samples_split: Refuse to split a node smaller than this.
        min_samples_leaf: Refuse a split producing a child smaller than this.
        max_features: Features considered per split. None uses all. This is the
            knob that turns bagging into a random forest in Week 8.
    """

    criterion: str = "gini"
    max_depth: int | None = None
    min_samples_split: int = 2
    min_samples_leaf: int = 1
    max_features: int | str | None = None
    random_state: int | None = None

    root_: Node | None = field(init=False, default=None)
    n_classes_: int = field(init=False, default=0)
    feature_importances_: Array = field(init=False, repr=False)

    def fit(self, X: Array, y: Array) -> DecisionTreeClassifier:
        raise NotImplementedError("Week 7")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 7")

    def predict_proba(self, X: Array) -> Array:
        """Class distribution at the reached leaf.

        These are badly calibrated for deep trees: a pure leaf reports
        probability 1.0 on the strength of three samples. Week 11 fixes it.
        """
        raise NotImplementedError("Week 7")

    def _best_split(self, X: Array, y: Array) -> tuple[int | None, float | None, float]:
        """Find the (feature, threshold) with the greatest impurity decrease.

        The naive version tries every midpoint of every feature: O(n·d) impurity
        evaluations per node, each O(n), so O(n²d). Sort each feature once and
        update class counts incrementally as the threshold sweeps — that gets
        you to O(n·d·log n), which is how real implementations work. Doing this
        yourself is the most instructive hour of Week 7.

        Returns:
            (feature_index, threshold, impurity_decrease). Feature is None when
            no split improves on the current node.
        """
        raise NotImplementedError("Week 7")

    def depth(self) -> int:
        raise NotImplementedError("Week 7")

    def n_leaves(self) -> int:
        raise NotImplementedError("Week 7")

    def print_tree(self, feature_names: list[str] | None = None) -> str:
        """Render the tree as indented text.

        Interpretability is a genuine selling point of trees. Print one, trace a
        single prediction through it by hand, and you will never again describe
        a tree as a black box.
        """
        raise NotImplementedError("Week 7")


@dataclass
class DecisionTreeRegressor:
    """CART regressor. Splits minimize variance; leaves predict the mean."""

    max_depth: int | None = None
    min_samples_split: int = 2
    min_samples_leaf: int = 1
    max_features: int | str | None = None
    random_state: int | None = None

    root_: Node | None = field(init=False, default=None)

    def fit(self, X: Array, y: Array) -> DecisionTreeRegressor:
        raise NotImplementedError("Week 7")

    def predict(self, X: Array) -> Array:
        raise NotImplementedError("Week 7")


def gini(y: Array) -> float:
    """1 - sum p_i²."""
    raise NotImplementedError("Week 7")


def entropy(y: Array) -> float:
    """-sum p_i log2 p_i. The same function as Week 4."""
    raise NotImplementedError("Week 7")


def variance_reduction(y: Array, left: Array, right: Array) -> float:
    """Weighted variance decrease. The regression analogue of information gain."""
    raise NotImplementedError("Week 7")
