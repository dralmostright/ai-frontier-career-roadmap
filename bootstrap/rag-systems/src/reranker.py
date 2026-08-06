"""Reranking — Week 38.

Retrieve broadly with a cheap method, then rerank precisely with an expensive
one. Retrieve 50, rerank, keep 5.

The distinction to be able to explain, because it is a common interview
question:

- **Bi-encoder** (retrieval): embeds query and document *separately*. Document
  embeddings are precomputed, so search is a fast vector operation. Fast and
  less accurate, because the two never interact.
- **Cross-encoder** (reranking): processes query and document *together*
  through a transformer, so attention runs across both. Far more accurate and
  far too slow to run over a whole corpus — it cannot be precomputed.

That is the entire reason for the two-stage architecture.
"""

from __future__ import annotations


class CrossEncoderReranker:
    """Score (query, chunk) pairs jointly.

    Typically the single largest quality improvement available in a RAG
    pipeline, and it costs latency proportional to the number of candidates.
    Measure the tradeoff: reranking 50 candidates might add 200ms and 8 points
    of nDCG, which is usually worth it — but you should know both numbers
    rather than assuming.
    """

    def __init__(
        self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2", batch_size: int = 32
    ) -> None:
        raise NotImplementedError("Week 38")

    def rerank(self, query: str, chunks: list, top_k: int = 5) -> list:
        raise NotImplementedError("Week 38")


class LLMReranker:
    """Use an LLM to rank candidates.

    More accurate still, and much more expensive. Justifiable for low-volume,
    high-stakes retrieval; not for interactive search at scale.

    Watch for position bias, exactly as in Week 36's judge: models favor
    items appearing early in the list. Shuffle and average, or accept a biased
    ranking knowingly.
    """

    def __init__(self, model: str = "claude-haiku-4-5-20251001", batch_size: int = 10) -> None:
        raise NotImplementedError("Week 38")

    def rerank(self, query: str, chunks: list, top_k: int = 5) -> list:
        raise NotImplementedError("Week 38")


def lost_in_the_middle_reorder(chunks: list) -> list:
    """Place the strongest chunks at the start and end of the context.

    Models attend more to the beginning and end of a long context than to the
    middle — a well-documented and counterintuitive effect. Ordering results
    best-first is therefore *not* optimal; interleaving so the top results sit
    at both ends measurably improves answer quality.

    A free improvement, and a good detail to mention in an interview because
    it shows you read the literature rather than only the tutorials.
    """
    raise NotImplementedError("Week 38")
