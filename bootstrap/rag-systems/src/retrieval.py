"""Retrieval strategies — Week 38."""

from __future__ import annotations

from typing import Any


def dense_retrieve(
    store: Any, query: str, embedder: Any, k: int = 10, filters: dict | None = None
) -> list:
    """Embedding similarity search.

    Strong on paraphrase and conceptual similarity. Weak on exact matches:
    product codes, error numbers, table names, rare proper nouns. Embeddings
    map "ORA-01555" and "ORA-01578" close together, and they are completely
    different problems.
    """
    raise NotImplementedError("Week 38")


def lexical_retrieve(store: Any, query: str, k: int = 10, filters: dict | None = None) -> list:
    """BM25 / full-text search.

    Exactly complementary to dense retrieval: excellent on rare exact terms,
    useless on paraphrase. Postgres gives you this for free via the generated
    `tsvector` column, in the same query as the vector search.

    Always build the lexical baseline first. If your fancy embedding pipeline
    does not beat BM25, you have learned something important, and a
    surprising number of RAG systems do not.
    """
    raise NotImplementedError("Week 38")


def reciprocal_rank_fusion(result_lists: list[list], k: int = 60) -> list:
    """Fuse ranked lists by summing 1/(k + rank).

    Rank-based, so it needs no score normalization — which matters because
    cosine similarities and BM25 scores are not on comparable scales and
    normalizing them is fiddly and fragile.

    k=60 is the standard constant from the original paper. It damps the
    influence of top ranks slightly; the value is not sacred but there is
    little reason to change it.
    """
    raise NotImplementedError("Week 38")


def hybrid_retrieve(
    store: Any,
    query: str,
    embedder: Any,
    k: int = 10,
    alpha: float = 0.5,
    fusion: str = "rrf",
) -> list:
    """Dense + lexical, fused.

    Reliably beats either alone. The Week 38 finding worth reporting: run the
    per-query-category breakdown and show *where* each method wins. Dense wins
    on conceptual questions, lexical on identifier lookups, hybrid on both.
    That breakdown is a better artifact than the aggregate number.
    """
    raise NotImplementedError("Week 38")


def query_expansion(query: str, model: Any, n: int = 3) -> list[str]:
    """Generate paraphrases and retrieve for each.

    Helps with vocabulary mismatch: the user says "database is slow", the
    runbook says "elevated query latency". Costs an LLM call per query, so
    measure whether it earns the latency before shipping it.
    """
    raise NotImplementedError("Week 38")


def hyde(query: str, model: Any, embedder: Any) -> list[float]:
    """Hypothetical Document Embeddings.

    Generate a fake answer, embed *that*, and search with it. The intuition:
    a hypothetical answer lives closer in embedding space to real answers than
    the question does, because questions and answers are stylistically
    different kinds of text.

    Works well on some corpora and not others. A good ablation to run and
    report either way.
    """
    raise NotImplementedError("Week 38")


def deduplicate(results: list, threshold: float = 0.95) -> list:
    """Drop near-identical chunks from the result set.

    Overlapping chunks and boilerplate produce duplicates that waste context
    window on the same information. Cheap to fix and easy to forget.
    """
    raise NotImplementedError("Week 38")
