"""Explainability and error analysis — Week 12.

The month's payoff. A model report that says "AUC 0.87" is a number; a report
that says "AUC 0.87 overall, 0.62 on the segment that generates 40% of revenue,
and here are the twelve worst false positives with a root cause for each" is an
engineering artifact.

This is also the week where your background pays off most directly in Phase 1.
Error analysis is root-cause analysis. Bucketing failures, forming hypotheses,
and testing them is what you already do during an incident — the only new part
is the vocabulary.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
import pandas as pd
from numpy.typing import NDArray

Array = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Global explanations
# ---------------------------------------------------------------------------


def permutation_importance_report(
    model: object,
    X: pd.DataFrame,
    y: Array,
    scoring: Callable[[Array, Array], float],
    n_repeats: int = 10,
    random_state: int | None = None,
) -> pd.DataFrame:
    """Rank features by the score drop caused by shuffling them.

    Returns a frame with mean, std, and a rank per feature, sorted descending.

    State the caveat unprompted in interviews: correlated features share the
    credit, so two near-duplicate columns can both appear unimportant even
    though the information they carry is essential.
    """
    raise NotImplementedError("Week 12")


def partial_dependence(
    model: object, X: pd.DataFrame, feature: str, grid_resolution: int = 50
) -> tuple[Array, Array]:
    """Average prediction as one feature is swept across its range.

    Marginalizes over every other feature by actually setting the column to each
    grid value and re-predicting. This means it will happily evaluate the model
    at impossible combinations — age 8 with income 200k — so a PDP over
    correlated features can be misleading. Know this; it is the standard
    follow-up question.

    Returns:
        (grid_values, mean_predictions).
    """
    raise NotImplementedError("Week 12")


def individual_conditional_expectation(
    model: object, X: pd.DataFrame, feature: str, grid_resolution: int = 50, sample: int = 100
) -> tuple[Array, Array]:
    """PDP, but one line per sample instead of the average.

    Reveals heterogeneous effects that the average hides. If half your ICE
    curves slope up and half slope down, the PDP is flat and you would have
    concluded the feature does nothing.

    Returns:
        (grid_values, curves) with curves of shape (n_sampled, grid_resolution).
    """
    raise NotImplementedError("Week 12")


# ---------------------------------------------------------------------------
# Local explanations
# ---------------------------------------------------------------------------


def shapley_values_exact(
    model: object, X_background: Array, x: Array, max_features: int = 12
) -> Array:
    """Exact Shapley values by enumerating coalitions.

    Cost is O(2^d), so this is only tractable for small feature counts. Implement
    it anyway, on a 6-feature problem, because it makes the definition concrete:
    a feature's attribution is its average marginal contribution across every
    possible ordering of the features.

    Having computed it exactly once, you will understand what SHAP's fast
    approximations are approximating — and you will be able to answer "how does
    SHAP work?" with mechanism rather than vocabulary.

    Raises:
        ValueError: if the feature count exceeds ``max_features``.
    """
    raise NotImplementedError("Week 12")


def local_surrogate(
    model: object,
    X_background: pd.DataFrame,
    x: pd.Series,
    n_samples: int = 1000,
    kernel_width: float = 0.75,
) -> dict[str, float]:
    """LIME-style explanation: fit a weighted linear model near one point.

    Perturb around x, weight the perturbations by proximity, fit a sparse linear
    model, and read off its coefficients. Locally faithful, globally
    meaningless — which is the correct and frequently misunderstood framing.
    """
    raise NotImplementedError("Week 12")


# ---------------------------------------------------------------------------
# Error analysis — the section that matters most
# ---------------------------------------------------------------------------


@dataclass
class ErrorAnalysis:
    """Structured investigation of what a model gets wrong.

    The workflow, which is a postmortem in different clothing:

    1. Rank errors by loss. Look at the worst twenty individually. Actually look.
    2. Bucket them by hand into named categories.
    3. Count each bucket and estimate the score recoverable by fixing it.
    4. Fix the biggest one. Re-measure. Repeat.

    Step 1 is non-negotiable and the one people skip. Aggregate statistics never
    tell you that 30% of your false positives share a data-entry artifact.
    """

    y_true: Array
    y_pred: Array
    y_prob: Array | None = None
    X: pd.DataFrame | None = None

    def worst_errors(self, n: int = 20) -> pd.DataFrame:
        """The n highest-loss predictions, with their features.

        Read these one at a time. This is the highest-value hour of Week 12.
        """
        raise NotImplementedError("Week 12")

    def error_rate_by_slice(self, column: str, bins: int = 10) -> pd.DataFrame:
        """Error rate broken out by the values of one feature.

        A model at 90% accuracy overall might be at 55% for one segment. If that
        segment is a protected class you have a fairness problem; if it is your
        largest customer you have a business problem. Either way the aggregate
        number hid it.
        """
        raise NotImplementedError("Week 12")

    def confusion_examples(self, true_class: int, pred_class: int, n: int = 10) -> pd.DataFrame:
        """Sample rows from one cell of the confusion matrix.

        Confusing class 3 for class 5 repeatedly is a labeling problem, a feature
        problem, or a genuinely hard distinction. You can only tell by reading
        the examples.
        """
        raise NotImplementedError("Week 12")

    def calibration_by_slice(self, column: str, n_bins: int = 10) -> pd.DataFrame:
        """Calibration within each slice. Models are often calibrated overall and
        badly miscalibrated on subgroups."""
        raise NotImplementedError("Week 12")

    def summary_report(self) -> str:
        """Markdown report: headline metrics, worst slices, error buckets, and
        recommended next actions.

        This is the deliverable. Write it so an engineering manager could read it
        and know what to do next. Put it in the capstone README.
        """
        raise NotImplementedError("Week 12")


def find_label_noise(y_true: Array, y_prob: Array, threshold: float = 0.95) -> Array:
    """Flag likely mislabeled examples: confidently predicted as the other class.

    On real datasets some fraction of labels are simply wrong. Finding them is
    frequently a bigger accuracy win than any model change, and "I audited the
    labels and found 3% were wrong" is a far more interesting interview story
    than "I tried a bigger model."

    Returns:
        Indices, ordered by suspicion.
    """
    raise NotImplementedError("Week 12")


def model_card(
    model_name: str,
    metrics: dict[str, float],
    slices: pd.DataFrame,
    limitations: list[str],
    intended_use: str,
) -> str:
    """Generate a model card in markdown.

    Intended use, out-of-scope uses, training data, metrics overall and by
    slice, ethical considerations, limitations. Start producing these in Month 3
    and it becomes automatic by the time you ship the fine-tuned model in
    Month 12 — where a real model card is expected rather than admirable.
    """
    raise NotImplementedError("Week 12")
