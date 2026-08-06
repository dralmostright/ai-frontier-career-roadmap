"""Feature engineering and leakage prevention — Week 10.

The most valuable week in Phase 1, and the one that maps most directly onto
work you already do. Leakage is a data-lineage bug. You have spent years
reasoning about which data was written when and by whom; that is exactly the
skill required here.

**The rule that prevents nearly all leakage:** every transformation that learns
something from data (a mean, a scale, a category vocabulary, a target encoding)
must learn it from the *training fold only*, then apply it unchanged to
validation and test. The moment you call `.fit()` on data that includes your
validation set, your validation score becomes a lie.

The `Transformer` protocol below enforces the fit/transform split. Use it for
everything. In Week 39 the same discipline stops you from tuning a RAG system
on its own eval set.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

import numpy as np
import pandas as pd
from numpy.typing import NDArray

Array = NDArray[np.float64]


class Transformer(Protocol):
    """Anything that learns from training data and applies to new data.

    Two methods, deliberately separate. If a class only has `transform`, it
    cannot leak. If it has `fit`, it can, and the separation is what lets you
    audit it.
    """

    def fit(self, X: pd.DataFrame, y: Array | None = None) -> Transformer: ...
    def transform(self, X: pd.DataFrame) -> pd.DataFrame: ...


@dataclass
class StandardScaler:
    """Zero mean, unit variance, using training statistics only."""

    mean_: Array = field(init=False, repr=False)
    scale_: Array = field(init=False, repr=False)

    def fit(self, X: pd.DataFrame, y: Array | None = None) -> StandardScaler:
        raise NotImplementedError("Week 10")

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Week 10")

    def fit_transform(self, X: pd.DataFrame, y: Array | None = None) -> pd.DataFrame:
        raise NotImplementedError("Week 10")


@dataclass
class OneHotEncoder:
    """Categorical to indicator columns.

    Two production concerns most tutorials skip:

    - **Unseen categories.** Test data will contain a category absent from
      training. Decide the policy (drop, or an explicit "unknown" column) and
      make it explicit, because the silent default is a crash at 2am.
    - **High cardinality.** 10,000 distinct values becomes 10,000 columns. Use
      ``min_frequency`` to bucket the tail into "other".
    """

    handle_unknown: str = "ignore"
    min_frequency: int | None = None

    categories_: dict[str, list] = field(init=False, default_factory=dict)

    def fit(self, X: pd.DataFrame, y: Array | None = None) -> OneHotEncoder:
        raise NotImplementedError("Week 10")

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Week 10")


@dataclass
class TargetEncoder:
    """Replace a category with the mean target for that category.

    Powerful and dangerous. Naively computing the mean over the full training
    set leaks the row's own target into its own feature, which produces
    spectacular validation scores and a model that fails in production.

    Two mitigations, both required:

    - **Out-of-fold encoding.** Compute each row's encoding from the other folds.
    - **Smoothing.** Shrink rare categories toward the global mean, or a category
      appearing once gets encoded as its single target value.

    If you can explain this failure mode clearly in an interview, you will be
    ahead of most candidates — it is a specific, common, expensive bug.
    """

    smoothing: float = 10.0
    n_folds: int = 5
    random_state: int | None = None

    mapping_: dict[str, dict] = field(init=False, default_factory=dict)
    global_mean_: float = field(init=False, default=0.0)

    def fit(self, X: pd.DataFrame, y: Array | None = None) -> TargetEncoder:
        raise NotImplementedError("Week 10")

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Week 10")

    def fit_transform(self, X: pd.DataFrame, y: Array) -> pd.DataFrame:
        """Out-of-fold encoding. **Must** differ from fit-then-transform.

        If your `fit_transform` returns the same thing as `fit().transform()`,
        you have not implemented out-of-fold encoding and you are leaking.
        There is a test for exactly this.
        """
        raise NotImplementedError("Week 10")


@dataclass
class MissingValueImputer:
    """Impute with a training-set statistic, plus an optional indicator column.

    The indicator matters. Missingness is frequently informative — a null
    `last_login` means something different from a null `middle_name`. Throwing
    that signal away by imputing silently is a common, quiet loss of accuracy.
    """

    strategy: str = "median"
    add_indicator: bool = True

    statistics_: dict[str, float] = field(init=False, default_factory=dict)

    def fit(self, X: pd.DataFrame, y: Array | None = None) -> MissingValueImputer:
        raise NotImplementedError("Week 10")

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Week 10")


@dataclass
class Pipeline:
    """Chain transformers so the fit/transform discipline is structural.

    The reason pipelines exist is not tidiness. It is that a pipeline makes it
    *impossible* to accidentally fit on validation data during cross-validation,
    because the whole pipeline is refit inside each fold. Manual preprocessing
    followed by cross-validation is the single most common way a leaderboard
    score turns out to be fiction.
    """

    steps: list[tuple[str, Transformer]]

    def fit(self, X: pd.DataFrame, y: Array | None = None) -> Pipeline:
        raise NotImplementedError("Week 10")

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Week 10")

    def fit_transform(self, X: pd.DataFrame, y: Array | None = None) -> pd.DataFrame:
        raise NotImplementedError("Week 10")


# ---------------------------------------------------------------------------
# Feature construction
# ---------------------------------------------------------------------------


def add_datetime_features(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Expand a timestamp into hour, day of week, month, and is-weekend.

    Encode cyclical features as sine/cosine pairs. Hour 23 and hour 0 are
    adjacent in reality and maximally distant as integers; the model cannot
    know that unless you tell it.
    """
    raise NotImplementedError("Week 10")


def add_aggregation_features(
    df: pd.DataFrame, group_by: str, agg_column: str, aggs: list[str]
) -> pd.DataFrame:
    """Group statistics as features (mean, std, count per group).

    Same leakage hazard as target encoding: compute the aggregate on training
    rows only, then join it onto validation and test.
    """
    raise NotImplementedError("Week 10")


def add_interaction_features(df: pd.DataFrame, pairs: list[tuple[str, str]]) -> pd.DataFrame:
    """Products and ratios of feature pairs.

    Linear models cannot discover interactions; trees can but need depth to do
    it. Constructing the two or three interactions you know are real, from
    domain knowledge, often beats a deeper model.
    """
    raise NotImplementedError("Week 10")


# ---------------------------------------------------------------------------
# Leakage detection
# ---------------------------------------------------------------------------


def detect_target_leakage(
    X: pd.DataFrame, y: Array, threshold: float = 0.95
) -> list[tuple[str, float]]:
    """Flag features suspiciously predictive of the target on their own.

    A single feature with 0.99 AUC is almost never a great feature. It is
    usually the target in disguise, a post-outcome field, or an identifier that
    correlates with how the data was collected.

    Returns:
        (feature_name, single_feature_auc) pairs above the threshold.
    """
    raise NotImplementedError("Week 10")


def detect_train_test_contamination(
    X_train: pd.DataFrame, X_test: pd.DataFrame, id_columns: list[str] | None = None
) -> dict[str, int]:
    """Find rows present in both splits.

    Exact duplicates, and near-duplicates on the identifier columns. This is
    embarrassingly common with scraped or logged data, and it inflates test
    scores in a way that survives every other check.

    Returns:
        Keys ``exact_duplicates``, ``id_overlaps``, ``fuzzy_matches``.
    """
    raise NotImplementedError("Week 10")


def temporal_split_check(
    df: pd.DataFrame, time_column: str, train_idx: Array, test_idx: Array
) -> bool:
    """Assert every training timestamp precedes every test timestamp.

    For any problem with a time dimension, a random split lets the model learn
    from the future. The resulting offline score is not merely optimistic — it
    is measuring a task the model will never face.

    Returns:
        True if the split is temporally sound.
    """
    raise NotImplementedError("Week 10")
