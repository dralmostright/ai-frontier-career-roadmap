"""pgvector-backed vector store — Week 37.

Your home turf. Most candidates reach for a hosted vector service and cannot
explain what it does; you are going to build it on Postgres and be able to
discuss index build times, recall tuning, bloat, and query plans.

Schema sketch:

    CREATE TABLE labs.documents (
        id          bigserial PRIMARY KEY,
        source      text NOT NULL,
        title       text,
        metadata    jsonb NOT NULL DEFAULT '{}',
        created_at  timestamptz NOT NULL DEFAULT now()
    );

    CREATE TABLE labs.chunks (
        id          bigserial PRIMARY KEY,
        document_id bigint REFERENCES labs.documents(id) ON DELETE CASCADE,
        ordinal     int NOT NULL,
        content     text NOT NULL,
        token_count int,
        embedding   vector(384),
        tsv         tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED
    );

The generated `tsvector` column is what makes hybrid retrieval cheap: lexical
and dense search hit the same table in one query, with no second system to
keep in sync. That is a real architectural advantage of doing this on Postgres
and it is worth saying out loud in an interview.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Chunk:
    """A retrievable unit with its provenance."""

    id: int | None
    document_id: int
    ordinal: int
    content: str
    embedding: list[float] | None = None
    metadata: dict[str, Any] | None = None
    score: float | None = None


class PgVectorStore:
    """Vector store on PostgreSQL.

    Args:
        dsn: Connection string.
        dimension: Embedding dimension. Must match your model exactly — a
            mismatch is a runtime error at insert time, which is the good
            case; the bad case is silently truncating.
        distance: "cosine", "l2", or "inner_product". Cosine for normalized
            embeddings, which is almost always what you want.
    """

    def __init__(self, dsn: str, dimension: int = 384, distance: str = "cosine") -> None:
        raise NotImplementedError("Week 37")

    def create_schema(self) -> None:
        """Create tables, extensions, and the tsvector column."""
        raise NotImplementedError("Week 37")

    def create_index(self, kind: str = "hnsw", **params: Any) -> dict[str, Any]:
        """Build the ANN index.

        **Build it after loading the data, not before.** IVFFlat clusters the
        vectors it can see at build time; an index built on an empty table has
        no clusters and silently degrades to a sequential scan. This is a real
        production mistake and a good detail to have opinions about.

        HNSW parameters: `m` (connections per node, default 16) and
        `ef_construction` (build-time search width, default 64). Higher is
        better recall and slower builds.

        IVFFlat: `lists` ≈ rows/1000 up to 1M rows, sqrt(rows) beyond.

        Returns:
            Build time, index size, and the parameters used. Record these —
            "the index took 40 minutes and 3GB for 2M chunks" is the kind of
            concrete number that makes a design discussion real.
        """
        raise NotImplementedError("Week 37")

    def upsert_chunks(self, chunks: list[Chunk], batch_size: int = 500) -> int:
        """Insert or update chunks in batches.

        Batch the inserts. Row-at-a-time insertion of 100k chunks takes
        hours; `execute_values` with a batch of 500 takes minutes. You know
        this already — most ML engineers do not.
        """
        raise NotImplementedError("Week 37")

    def search(
        self,
        query_embedding: list[float],
        k: int = 10,
        filters: dict[str, Any] | None = None,
        probes: int | None = None,
    ) -> list[Chunk]:
        """Dense similarity search with optional metadata filtering.

        **The filtering problem, which is the interesting part.** Filtering
        after the ANN search breaks top-k: you request 10, the index returns
        10, the filter removes 7, and you serve 3 results while relevant
        documents sit unretrieved. Filtering before requires the filter
        columns to be indexed and the planner to cooperate.

        pgvector supports both patterns. Know which you are getting, and know
        how to check — `EXPLAIN ANALYZE` is right there. This is where your
        background is a genuine advantage over other candidates.

        `probes` (IVFFlat) or `ef_search` (HNSW) trades recall for latency at
        query time. Sweep it and plot the curve; that plot belongs in your
        capstone README.
        """
        raise NotImplementedError("Week 37")

    def hybrid_search(
        self,
        query_embedding: list[float],
        query_text: str,
        k: int = 10,
        alpha: float = 0.5,
        filters: dict[str, Any] | None = None,
    ) -> list[Chunk]:
        """Dense + lexical in one SQL statement, fused by reciprocal rank.

        One query, one system, no synchronization problem. Compare against
        running two systems and merging in the application layer — the
        Postgres version is simpler to operate and that is a legitimate
        architectural argument to make.
        """
        raise NotImplementedError("Week 38")

    def explain_search(self, query_embedding: list[float], k: int = 10) -> str:
        """Return `EXPLAIN ANALYZE` for the search query.

        Confirm the index is actually being used. A sequential scan over 2M
        vectors still returns correct results — just slowly — so this failure
        is invisible without looking. Include the plan in your README; no
        other RAG portfolio project will have one.
        """
        raise NotImplementedError("Week 37")

    def index_health(self) -> dict[str, Any]:
        """Index size, bloat estimate, scan counts, and last vacuum.

        Straight from your DBA background, and directly reusable as a tool for
        the Month 11 agent. Vector indexes bloat under heavy updates like any
        other index, and nobody building RAG systems thinks about it.
        """
        raise NotImplementedError("Week 37")


def benchmark_recall(
    store: PgVectorStore,
    queries: list[list[float]],
    ground_truth: list[list[int]],
    parameter_sweep: dict[str, list],
) -> Any:
    """Measure recall against exact search across index parameters.

    Compute exact nearest neighbors by brute force, then measure what fraction
    the ANN index returns at each setting. Plot recall against latency.

    That curve is the artifact. It turns "I used HNSW" into "at ef_search=40
    we hit 0.97 recall at 8ms p95, and going to 100 bought 0.3 points for 3x
    the latency."
    """
    raise NotImplementedError("Week 37")
