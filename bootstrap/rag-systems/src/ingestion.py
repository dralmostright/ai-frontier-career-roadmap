"""Document ingestion — Week 37."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def load_documents(source: Path, formats: list[str] | None = None) -> list[dict[str, Any]]:
    """Load documents and extract metadata.

    Metadata is not optional. Source, title, author, timestamp, and any
    permission scope must be captured at ingestion — retrofitting it later
    means reprocessing the whole corpus, and permission scope in particular is
    what makes the system deployable at a real company.
    """
    raise NotImplementedError("Week 37")


def clean_text(text: str, remove_boilerplate: bool = True) -> str:
    """Normalize whitespace, strip navigation and boilerplate, fix encoding.

    Unglamorous and high-leverage. Headers, footers, and cookie banners
    repeated across every page become the most "similar" content in your
    corpus and pollute every retrieval.
    """
    raise NotImplementedError("Week 37")


def deduplicate_documents(documents: list[dict], threshold: float = 0.95) -> tuple[list[dict], int]:
    """Remove exact and near-duplicate documents.

    Real corpora are full of duplicates: versioned copies, mirrors, forwarded
    emails. Duplicates crowd out diverse results in the top-k and make your
    retrieval look worse than it is.

    Returns:
        (kept, removed_count).
    """
    raise NotImplementedError("Week 37")


def embed_batch(
    texts: list[str], model: Any, batch_size: int = 32, normalize: bool = True
) -> list[list[float]]:
    """Embed in batches.

    Normalize to unit length at ingestion time so cosine similarity reduces to
    a dot product, which is meaningfully cheaper at query time and lets
    pgvector use the simpler operator.
    """
    raise NotImplementedError("Week 37")


class IngestionPipeline:
    """Load, clean, dedupe, chunk, embed, store — resumably.

    Make it resumable. Ingesting 100k documents takes hours, and something
    will fail at hour two. Track processed document ids and skip them on
    restart. This is ordinary batch-job discipline and it is routinely absent
    from ML pipelines.
    """

    def __init__(
        self, store: Any, embedder: Any, chunker: Any, state_path: Path | None = None
    ) -> None:
        raise NotImplementedError("Week 37")

    def run(self, source: Path, resume: bool = True) -> dict[str, Any]:
        raise NotImplementedError("Week 37")
