"""Chunking strategies — Week 38.

The most under-appreciated variable in a RAG system. Chunking determines what
can ever be retrieved, so it caps your recall before the embedding model gets
a say.

Week 38's job is to stop guessing and measure. Run every strategy against the
Week 39 eval set and produce the table.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Chunk:
    text: str
    start: int
    end: int
    metadata: dict[str, Any] | None = None


def fixed_size_chunks(text: str, size: int = 512, overlap: int = 64) -> list[Chunk]:
    """Split on a token count with a sliding overlap.

    The baseline. Overlap exists so that a fact straddling a boundary appears
    whole in at least one chunk. Zero overlap reliably loses those facts, and
    the loss is invisible until you measure recall.

    Count *tokens*, not characters. Characters vary by several times per token
    across languages and content types, so a character-based chunk size gives
    you wildly different context sizes for different documents.
    """
    raise NotImplementedError("Week 38")


def recursive_chunks(
    text: str,
    size: int = 512,
    overlap: int = 64,
    separators: list[str] | None = None,
) -> list[Chunk]:
    """Split on the largest natural boundary that fits.

    Try paragraph breaks, then sentences, then words, then characters. Usually
    the best default: it respects document structure without needing to
    understand it.
    """
    raise NotImplementedError("Week 38")


def semantic_chunks(text: str, model: Any, threshold: float = 0.5) -> list[Chunk]:
    """Split where consecutive sentence embeddings diverge.

    Embed each sentence, walk the document, and cut where similarity to the
    running context drops below the threshold. Produces topically coherent
    chunks of uneven size.

    Expensive at ingestion and frequently worth it. Measure rather than assume
    — on well-structured documents, recursive chunking often matches it for a
    fraction of the cost, and reporting that honestly is more valuable than
    picking the sophisticated option.
    """
    raise NotImplementedError("Week 38")


def structural_chunks(text: str, format: str = "markdown") -> list[Chunk]:
    """Split on document structure: headings, sections, code blocks, tables.

    The best strategy when the format supports it. A markdown section under
    one heading is a coherent unit by construction, and prepending the heading
    path to each chunk gives the embedding real context — "Database
    Reliability > Replication > Lag Troubleshooting" is far more retrievable
    than the section body alone.

    Never split a table or a code block. Retrieving half a table is worse than
    retrieving nothing, because it produces a confidently wrong answer.
    """
    raise NotImplementedError("Week 38")


def add_context_headers(
    chunks: list[Chunk], document_title: str, section_path: list[str] | None = None
) -> list[Chunk]:
    """Prepend document and section context to each chunk before embedding.

    A cheap, large win. A chunk reading "Increase this to 64MB if you see
    temporary files in the logs" is nearly unretrievable alone; prefixed with
    "PostgreSQL Tuning > Memory > work_mem" it becomes findable.

    Measure this as an ablation — it is usually worth several points of
    recall for essentially no cost.
    """
    raise NotImplementedError("Week 38")


def compare_strategies(documents: list[str], eval_set: Any, strategies: dict[str, Any]) -> Any:
    """**The Week 38 deliverable.**

    Run every strategy through the full pipeline and report recall@k, MRR,
    chunk count, mean chunk size, and ingestion cost.

    The output is a table you can point at, which turns "I used recursive
    chunking at 512 tokens" into "recursive at 512 beat fixed at 256 by 6
    points of recall@5 on our corpus; here is the table."
    """
    raise NotImplementedError("Week 38")
