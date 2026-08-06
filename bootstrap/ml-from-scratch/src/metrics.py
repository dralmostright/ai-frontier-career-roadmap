"""Classification metrics — Week 6, extended in Week 11.

Accuracy is almost always the wrong metric and it is the one everybody reaches
for first. On a 0.1% positive rate, predicting "negative" forever scores 99.9%.
Every metric in this module exists because accuracy failed someone.

Implement each from the confusion matrix rather than calling sklearn. The point
is that when an interviewer asks "how would you evaluate this?", you reason from
the four cells instead of recalling a function name.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def confusion_matrix(y_true: Array, y_pred: Array, n_classes: int | None = None) -> Array:
    """Rows are true classes, columns predicted. Binary: [[TN, FP], [FN, TP]].

    Fix this layout in your head. A large share of metric bugs are a transposed
    confusion matrix, and they produce numbers that are wrong in a way that is
    hard to place.
    """
    raise NotImplementedError("Week 6")


def accuracy(y_true: Array, y_pred: Array) -> float:
    raise NotImplementedError("Week 6")


def precision(y_true: Array, y_pred: Array) -> float:
    """TP / (TP + FP). Of the things you flagged, how many were real?

    Optimize this when acting on a positive is expensive: blocking a
    transaction, paging an engineer, or having your DBA agent recommend an index
    rebuild at peak load.
    """
    raise NotImplementedError("Week 6")


def recall(y_true: Array, y_pred: Array) -> float:
    """TP / (TP + FN). Of the real things, how many did you catch?

    Optimize this when missing a positive is expensive: cancer screening, fraud,
    or replication lag going unnoticed until the replica is an hour behind.
    """
    raise NotImplementedError("Week 6")


def f1_score(y_true: Array, y_pred: Array) -> float:
    """Harmonic mean of precision and recall.

    Harmonic, not arithmetic, so a model scoring 1.0 and 0.0 gets F1 = 0 rather
    than 0.5. Be able to say why that is the desirable behavior.
    """
    raise NotImplementedError("Week 6")


def fbeta_score(y_true: Array, y_pred: Array, beta: float = 1.0) -> float:
    """Weighted harmonic mean. beta > 1 favors recall, beta < 1 favors precision.

    Choosing beta is where you encode the actual business cost ratio. Doing that
    explicitly, rather than defaulting to F1, is a strong interview signal.
    """
    raise NotImplementedError("Week 6")


def specificity(y_true: Array, y_pred: Array) -> float:
    """TN / (TN + FP). Recall for the negative class."""
    raise NotImplementedError("Week 6")


def roc_curve(y_true: Array, y_score: Array) -> tuple[Array, Array, Array]:
    """Returns (fpr, tpr, thresholds), sweeping every threshold.

    Implement by sorting scores descending and accumulating counts — O(n log n).
    The naive loop over candidate thresholds is O(n²) and will not finish on a
    real dataset.
    """
    raise NotImplementedError("Week 6")


def roc_auc(y_true: Array, y_score: Array) -> float:
    """Area under the ROC curve.

    The interpretation worth knowing: the probability that a randomly chosen
    positive is ranked above a randomly chosen negative. That reading makes it
    obvious why AUC is threshold-independent, and why it is insensitive to class
    imbalance — which is sometimes exactly the problem.
    """
    raise NotImplementedError("Week 6")


def precision_recall_curve(y_true: Array, y_score: Array) -> tuple[Array, Array, Array]:
    """Returns (precision, recall, thresholds)."""
    raise NotImplementedError("Week 6")


def average_precision(y_true: Array, y_score: Array) -> float:
    """Area under the PR curve (PR-AUC).

    **The interview question.** ROC-AUC's baseline is 0.5 regardless of class
    balance, because the false positive rate carries the huge negative count in
    its denominator. At a 0.1% positive rate a model can look excellent by
    ROC-AUC while its precision is 2%. PR-AUC's baseline is the positive rate
    itself, so it exposes that immediately.

    Rule: heavy imbalance and you care about the positive class → PR-AUC.
    """
    raise NotImplementedError("Week 6")


def classification_report(y_true: Array, y_pred: Array) -> dict[str, dict[str, float]]:
    """Per-class precision, recall, F1, support, plus macro and weighted averages.

    Macro averaging treats every class equally; weighted averaging treats every
    *sample* equally. On imbalanced data they differ substantially, and reporting
    the flattering one without saying which is a small dishonesty that
    interviewers notice.
    """
    raise NotImplementedError("Week 6")


def matthews_corrcoef(y_true: Array, y_pred: Array) -> float:
    """MCC: balanced even under heavy skew. Range [-1, 1].

    Uses all four confusion-matrix cells, which F1 does not — F1 ignores true
    negatives entirely. Worth knowing as the answer to "is there one number I
    can trust on imbalanced data?"
    """
    raise NotImplementedError("Week 6")


def find_optimal_threshold(
    y_true: Array,
    y_score: Array,
    metric: str = "f1",
    cost_fp: float = 1.0,
    cost_fn: float = 1.0,
) -> tuple[float, float]:
    """Sweep thresholds; return (best_threshold, best_score).

    With ``cost_fp`` and ``cost_fn``, minimize expected cost rather than
    maximize a metric. This is what you actually do in production, and framing
    threshold selection as cost minimization separates you from candidates who
    say "we used 0.5."
    """
    raise NotImplementedError("Week 6")
