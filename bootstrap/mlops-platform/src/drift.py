"""Drift detection — Week 56.

The world changes and the model does not. Three distinct kinds, which are
worth distinguishing precisely because they have different responses:

- **Data drift** — P(X) changes. Input distribution moves. Detectable
  immediately, no labels needed.
- **Concept drift** — P(y|X) changes. The relationship itself moves. The same
  input now has a different correct answer. Requires labels to detect.
- **Label drift** — P(y) changes. Class balance moves.

The practical asymmetry: data drift is cheap to detect and only sometimes
matters; concept drift always matters and is expensive to detect. So you
monitor data drift as a proxy and confirm with delayed labels.
"""

from __future__ import annotations

from typing import Any


def population_stability_index(baseline: Any, current: Any, bins: int = 10) -> float:
    """PSI: the standard drift statistic.

    PSI = sum (current% - baseline%) * ln(current% / baseline%)

    The conventional thresholds, worth knowing because you will be asked:

    - < 0.1 — no meaningful shift
    - 0.1 to 0.25 — moderate, investigate
    - > 0.25 — significant, act

    These are conventions from credit risk modeling, not laws. Calibrate them
    against your own data by measuring PSI during periods you know were fine.
    Saying that in an interview shows you know where the numbers come from.
    """
    raise NotImplementedError("Week 56")


def kl_drift(baseline: Any, current: Any, bins: int = 20) -> float:
    """KL divergence between the baseline and current distributions.

    Week 4's function, in production. Add smoothing: a bin that is empty in
    the baseline and populated now makes KL infinite.
    """
    raise NotImplementedError("Week 56")


def kolmogorov_smirnov_test(baseline: Any, current: Any) -> dict[str, float]:
    """KS test for continuous features. Returns statistic and p-value.

    The trap: with a large enough sample, everything is statistically
    significant. At a million requests per day the KS test flags drift
    constantly, and none of it matters. Use effect size, not p-value, as the
    alerting condition — this is a mistake teams make repeatedly.
    """
    raise NotImplementedError("Week 56")


def embedding_drift(baseline_embeddings: Any, current_embeddings: Any) -> dict[str, float]:
    """Drift in embedding space, for text and image inputs.

    Compare centroid distance and average pairwise similarity. This is how you
    detect that the questions people are asking your RAG system have shifted —
    which is the leading indicator that your corpus no longer covers the need.
    """
    raise NotImplementedError("Week 56")


class DriftDetector:
    """Monitor a set of features against a training baseline.

    Store the baseline *with the model version*, not separately. A model and
    its baseline must move together, or a rollback leaves you comparing the
    old model against the new model's baseline — which produces nonsense drift
    alerts at the worst possible moment.
    """

    def __init__(
        self, baseline: dict[str, Any], method: str = "psi", threshold: float = 0.25
    ) -> None:
        raise NotImplementedError("Week 56")

    def check(self, current: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError("Week 56")

    def report(self) -> str:
        """Which features drifted, by how much, and what to do about it.

        Include the "what to do" column. A drift dashboard nobody knows how to
        act on gets ignored within two weeks.
        """
        raise NotImplementedError("Week 56")
