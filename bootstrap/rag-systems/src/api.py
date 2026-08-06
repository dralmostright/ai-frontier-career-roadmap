"""RAG service — Week 40.

FastAPI, streaming, observability, and cost accounting. The Month 10 capstone
artifact.
"""

from __future__ import annotations

from typing import Any


def create_app(config: Any) -> Any:
    """Build the FastAPI application.

    Endpoints:

    - `POST /query` — ask a question, get a grounded answer with citations
    - `POST /query/stream` — same, server-sent events
    - `POST /ingest` — add documents
    - `GET /health` — liveness; is the process up?
    - `GET /ready` — readiness; is the DB reachable and the index warm?
    - `GET /metrics` — Prometheus

    The liveness/readiness distinction matters and most people conflate them.
    Liveness failing means restart me. Readiness failing means stop sending me
    traffic but do not restart me. Getting this wrong produces restart loops
    during a transient database blip — which you have almost certainly seen.
    """
    raise NotImplementedError("Week 40")


def instrument(app: Any) -> None:
    """Add metrics, tracing, and structured logging.

    Metrics worth having, chosen because they map to real failure modes:

    - `rag_query_duration_seconds` — histogram, split by stage (embed,
      retrieve, rerank, generate). The split is what makes it debuggable.
    - `rag_retrieval_score` — histogram of top-1 similarity. A drifting
      distribution is your early warning that the corpus and the queries have
      diverged.
    - `rag_refusal_total` — counter. A sudden spike means retrieval broke.
    - `rag_tokens_total`, `rag_cost_usd_total` — by model.
    - `rag_context_truncated_total` — you are silently dropping context.

    Log the trace id, question hash, retrieved chunk ids, scores, and cost for
    every query. When someone reports a bad answer three days later, that log
    line is the only way to reconstruct what happened.
    """
    raise NotImplementedError("Week 40")


class ResponseCache:
    """Cache by (question, retrieval-config, model) hash.

    Two distinct wins: cost during development, where you re-run the same
    evaluation dozens of times, and latency in production for repeated
    questions.

    Invalidate on ingestion. A cached answer from before the corpus changed is
    a stale answer served with full confidence, which is worse than a slow
    one.
    """

    def __init__(self, backend: str = "memory", ttl_seconds: int = 3600) -> None:
        raise NotImplementedError("Week 40")

    def get(self, key: str) -> Any | None:
        raise NotImplementedError("Week 40")

    def set(self, key: str, value: Any) -> None:
        raise NotImplementedError("Week 40")
