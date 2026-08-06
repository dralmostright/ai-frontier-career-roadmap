"""Evaluation, cross-validation, and calibration — Week 11.

Week 6 gave you metrics. This module is about trusting them.

Three things separate a professional evaluation from a hobbyist one:

1. **Cross-validation**, so your estimate isn't an artifact of one lucky split.
2. **Confidence intervals**, so "0.84 versus 0.86" is a claim you can defend.
3. **Calibration**, so a predicted probability of 0.7 means the event happens
   70% of the time.

Calibration is the one people skip and the one that matters most when a
downstream system consumes the probability — which is exactly what happens when
your DBA agent decides whether a 0.7-confidence diagnosis justifies paging
someone.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Cross-validation
# ---------------------------------------------------------------------------


def k_fold_split(
    n_samples: int, n_splits: int = 5, shuffle: bool = True, random_state: int | None = None
) -> Iterator[tuple[Array, Array]]:
    """Yield (train_indices, val_indices) for each fold."""
    raise NotImplementedError("Week 11")


def stratified_k_fold_split(
    y: Array, n_splits: int = 5, shuffle: bool = True, random_state: int | None = None
) -> Iterator[tuple[Array, Array]]:
    """K-fold preserving class proportions in every fold.

    Mandatory for imbalanced data. With a 1% positive rate and 5 folds of 200
    rows, plain k-fold will hand you a fold with zero positives, and the metric
    for that fold is undefined or zero. This is not hypothetical; it happens
    constantly.
    """
    raise NotImplementedError("Week 11")


def time_series_split(n_samples: int, n_splits: int = 5) -> Iterator[tuple[Array, Array]]:
    """Expanding-window splits: always train on the past, validate on the future.

    Fold 1 trains on [0, k) and validates on [k, 2k). Fold 2 trains on [0, 2k),
    and so on. Never shuffle time series. The Week 10 leakage lesson, applied to
    the split strategy itself.
    """
    raise NotImplementedError("Week 11")


def group_k_fold_split(groups: Array, n_splits: int = 5) -> Iterator[tuple[Array, Array]]:
    """K-fold keeping all rows of a group on the same side of the split.

    Necessary whenever rows are not independent: multiple queries from one
    database instance, multiple readings from one patient, multiple rows per
    customer. Splitting a group across train and validation leaks.
    """
    raise NotImplementedError("Week 11")


def cross_validate(
    model_factory: Callable[[], object],
    X: Array,
    y: Array,
    cv: int = 5,
    scoring: dict[str, Callable[[Array, Array], float]] | None = None,
    stratified: bool = True,
    random_state: int | None = None,
) -> dict[str, Array]:
    """Fit and score across folds.

    Take a *factory*, not a fitted model. Reusing one instance across folds
    means fold 2 starts from fold 1's parameters, which quietly invalidates the
    entire exercise.

    Returns:
        Metric name to per-fold scores.
    """
    raise NotImplementedError("Week 11")


def nested_cross_validate(
    model_factory: Callable[..., object],
    param_grid: dict[str, list],
    X: Array,
    y: Array,
    outer_cv: int = 5,
    inner_cv: int = 3,
) -> dict[str, object]:
    """Hyperparameter selection inside, performance estimation outside.

    The honest way to report a score for a tuned model. Tuning on the same folds
    you report from is optimistic by a few points, which is roughly the margin
    that separates competition ranks and the margin people quietly exploit.
    """
    raise NotImplementedError("Week 11")


# ---------------------------------------------------------------------------
# Uncertainty
# ---------------------------------------------------------------------------


def bootstrap_metric_ci(
    y_true: Array,
    y_pred: Array,
    metric: Callable[[Array, Array], float],
    n_resamples: int = 2000,
    confidence: float = 0.95,
    rng: np.random.Generator | None = None,
) -> tuple[float, float, float]:
    """Point estimate and confidence interval for any metric.

    Use this every time you report a number, starting now. "AUC 0.84
    [0.81, 0.87]" is a result. "AUC 0.84" is a number.

    Returns:
        (point_estimate, lower, upper).
    """
    raise NotImplementedError("Week 11")


def paired_bootstrap_test(
    y_true: Array,
    y_pred_a: Array,
    y_pred_b: Array,
    metric: Callable[[Array, Array], float],
    n_resamples: int = 2000,
    rng: np.random.Generator | None = None,
) -> dict[str, float]:
    """Is model A actually better than model B?

    Resample the *same* rows for both models — that pairing removes the
    variance from which rows you happened to draw, and it is why a paired test
    is far more sensitive than comparing two independent intervals.

    You will use this constantly from Week 39 onward, when "does this chunking
    strategy beat that one?" becomes a question you have to answer honestly.

    Returns:
        Keys ``difference``, ``ci_lower``, ``ci_upper``, ``p_value``.
    """
    raise NotImplementedError("Week 11")


def learning_curve(
    model_factory: Callable[[], object],
    X: Array,
    y: Array,
    train_sizes: Array | None = None,
    cv: int = 5,
) -> tuple[Array, Array, Array]:
    """Score versus training set size.

    The most useful diagnostic plot in classical ML, because it answers "would
    more data help?" — a question that otherwise gets answered by guessing.

    - Both curves low and converged → underfitting. More data won't help; use a
      bigger model or better features.
    - Large gap between them → overfitting. More data will help.
    - Validation still rising at the right edge → collect more data.

    Returns:
        (train_sizes, train_scores, val_scores).
    """
    raise NotImplementedError("Week 11")


# ---------------------------------------------------------------------------
# Calibration
# ---------------------------------------------------------------------------


def calibration_curve(
    y_true: Array, y_prob: Array, n_bins: int = 10, strategy: str = "uniform"
) -> tuple[Array, Array, Array]:
    """Bin predictions and compare mean predicted probability to observed rate.

    A perfectly calibrated model lies on the diagonal. Above it means
    underconfident, below means overconfident.

    ``strategy="quantile"`` uses equal-count bins instead of equal-width, which
    matters when predictions cluster — the usual case, where 90% of predictions
    land in the lowest uniform bin and the plot tells you nothing.

    Returns:
        (mean_predicted, observed_fraction, bin_counts).
    """
    raise NotImplementedError("Week 11")


def expected_calibration_error(y_true: Array, y_prob: Array, n_bins: int = 10) -> float:
    """ECE: bin-count-weighted mean gap between confidence and accuracy.

    A single number for calibration quality. Report it alongside AUC whenever
    the probability itself gets consumed downstream rather than just ranked.
    """
    raise NotImplementedError("Week 11")


def brier_score(y_true: Array, y_prob: Array) -> float:
    """Mean squared error of predicted probabilities.

    A proper scoring rule: it is minimized only by reporting your true belief.
    It decomposes into calibration plus refinement, which is a satisfying result
    worth reading about once.
    """
    raise NotImplementedError("Week 11")


@dataclass
class PlattScaling:
    """Fit a 1-D logistic regression mapping scores to calibrated probabilities.

    Works well for SVMs and boosted trees, both of which produce systematically
    distorted probabilities. Fit it on a *held-out* calibration set, never on
    the training data — otherwise you are calibrating against the same
    overconfidence you are trying to fix.
    """

    a_: float = field(init=False, default=1.0)
    b_: float = field(init=False, default=0.0)

    def fit(self, scores: Array, y: Array) -> PlattScaling:
        raise NotImplementedError("Week 11")

    def transform(self, scores: Array) -> Array:
        raise NotImplementedError("Week 11")


@dataclass
class IsotonicCalibration:
    """Non-parametric calibration via a monotonic step function.

    More flexible than Platt scaling and more prone to overfitting on small
    calibration sets. The rule of thumb: Platt below ~1,000 calibration
    examples, isotonic above.
    """

    x_: Array = field(init=False, repr=False)
    y_: Array = field(init=False, repr=False)

    def fit(self, scores: Array, y: Array) -> IsotonicCalibration:
        raise NotImplementedError("Week 11")

    def transform(self, scores: Array) -> Array:
        raise NotImplementedError("Week 11")


# ---------------------------------------------------------------------------
# Imbalanced data
# ---------------------------------------------------------------------------


def class_weights(y: Array, strategy: str = "balanced") -> dict[int, float]:
    """Per-class loss weights, inversely proportional to frequency."""
    raise NotImplementedError("Week 11")


def resample(
    X: Array, y: Array, strategy: str = "undersample", rng: np.random.Generator | None = None
) -> tuple[Array, Array]:
    """Rebalance by under- or over-sampling.

    Three things to know and be able to say:

    - Resampling changes the base rate, so predicted probabilities become
      miscalibrated. You must recalibrate afterward or correct the intercept.
    - Only ever resample the *training* fold. Resampling before splitting puts
      copies of the same row on both sides — a leak that produces near-perfect
      validation scores.
    - Class weighting usually works as well as resampling and does not
      duplicate data. Prefer it unless you have a reason.
    """
    raise NotImplementedError("Week 11")
