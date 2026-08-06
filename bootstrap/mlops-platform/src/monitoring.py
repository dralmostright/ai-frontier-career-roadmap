"""Production monitoring — Week 56.

The core problem: **ML systems fail silently.** A model whose accuracy has
fallen from 92% to 71% returns HTTP 200 for every request. Nothing in a
conventional monitoring stack notices.

Everything here exists to make that failure visible.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class MetricSpec:
    """A monitored metric with its alerting policy.

    `page` versus `ticket` is the decision that determines whether your
    alerting is useful or ignored. Page only for things a human must act on
    *now*. Everything else is a ticket. Alert fatigue is the failure mode, and
    it is caused by exactly one thing: paging for things that can wait.
    """

    name: str
    description: str
    kind: str
    labels: list[str]
    warning_threshold: float | None = None
    critical_threshold: float | None = None
    page: bool = False
    runbook_url: str | None = None


SYSTEM_METRICS: list[MetricSpec] = []
"""Request rate, error rate, latency percentiles, saturation, queue depth.

Familiar territory. Populate in Week 56.
"""

MODEL_METRICS: list[MetricSpec] = []
"""The ML-specific ones. This is the list most teams do not have.

- `prediction_distribution` — histogram of outputs. The leading indicator.
- `confidence_mean` / `confidence_p10` — uncertainty rising before accuracy
  visibly falls.
- `feature_drift_psi` — per feature, against the training baseline.
- `refusal_rate` — a spike means retrieval or an upstream dependency broke.
- `fallback_rate` — how often you serve the degraded path.
- `tokens_per_request`, `cost_per_request` — budget, and a signal for abuse.
- `ground_truth_accuracy` — whenever labels arrive, however delayed.
"""


class ModelMonitor:
    """Track predictions and surface degradation.

    The two-tier design that works in practice:

    - **Real-time**, on every request: prediction distribution, confidence,
      latency, cost. Available immediately, and it is what alerts fire on.
    - **Batch**, hourly or daily: drift statistics, and accuracy against
      whatever ground truth has arrived.

    Ground truth is almost always delayed — sometimes by days. Design for
    that rather than pretending you have immediate labels.
    """

    def __init__(self, model_name: str, baseline: dict[str, Any], window_size: int = 1000) -> None:
        raise NotImplementedError("Week 56")

    def record(
        self,
        features: Any,
        prediction: Any,
        confidence: float | None = None,
        latency_ms: float = 0.0,
    ) -> None:
        raise NotImplementedError("Week 56")

    def record_ground_truth(self, request_id: str, actual: Any) -> None:
        """Attach a label that arrived later."""
        raise NotImplementedError("Week 56")

    def check(self) -> list[dict[str, Any]]:
        """Evaluate every monitor and return firing alerts."""
        raise NotImplementedError("Week 56")


def define_slos(service: str) -> list[dict[str, Any]]:
    """SLOs for an ML service.

    Your background makes this section strong. The ML-specific twist: you need
    a *quality* SLO alongside the availability and latency ones, and quality
    SLOs are harder because measurement is delayed and statistical.

    Example set:

    - Availability: 99.9% of requests return a response
    - Latency: p95 under 2s, p99 under 5s
    - Quality: faithfulness at or above 0.85, measured daily on a fixed set
    - Freshness: the index is no more than 24 hours stale

    Error budgets apply the same way. A quality SLO burn is a real incident,
    and treating it as one — with the same escalation as an availability burn
    — is the thing most ML teams have not internalized.
    """
    raise NotImplementedError("Week 56")


def alert_rules() -> list[dict[str, Any]]:
    """Prometheus alerting rules.

    Principles, all of which you already apply to databases:

    - Alert on symptoms users feel, not on causes. "Error rate above 1%", not
      "CPU above 80%".
    - Every page has a runbook link. A page without one is a puzzle handed to
      someone at 3am.
    - Page only for act-now conditions. Everything else is a ticket.
    - Include a `for:` duration. Instant thresholds fire on transients.
    - Alert on the *absence* of data too. A metric that stops reporting is
      usually worse news than one that goes high.
    """
    raise NotImplementedError("Week 56")
