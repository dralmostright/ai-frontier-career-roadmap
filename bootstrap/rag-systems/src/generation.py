"""Grounded generation — Week 39.

Turning retrieved context into an answer that is faithful, cited, and honest
about what it does not know.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class GroundedAnswer:
    """An answer plus the evidence for it."""

    text: str
    citations: list[int]
    refused: bool = False
    refusal_reason: str | None = None
    context_used: list[int] | None = None
    tokens: int = 0
    cost_usd: float = 0.0


def build_prompt(
    question: str, chunks: list, max_context_tokens: int = 4000, instructions: str | None = None
) -> str:
    """Assemble the generation prompt.

    What a good RAG prompt does:

    - Delimits the context explicitly, so the model can distinguish retrieved
      material from instructions. This is also your prompt-injection boundary:
      state that content inside the block is data, never instructions.
    - Numbers the chunks so the model can cite them.
    - Requires a citation for every factual claim.
    - Explicitly permits refusal: "if the context does not contain the answer,
      say so." Without this line, models confabulate rather than decline, and
      this single sentence measurably reduces hallucination.
    - Budgets the context. Truncate by relevance, and log when you do.
    """
    raise NotImplementedError("Week 39")


def generate_grounded(
    question: str, chunks: list, model: Any, temperature: float = 0.0
) -> GroundedAnswer:
    """Generate with citations.

    Temperature 0 for factual retrieval. Sampling adds variety, and variety is
    not a virtue when the job is reporting what a document says.
    """
    raise NotImplementedError("Week 39")


def extract_citations(answer: str) -> tuple[str, list[int]]:
    """Parse citation markers out of the answer text.

    Returns the clean text and the cited chunk indices. Validate them: models
    cite chunk 7 when you supplied five. An out-of-range citation is a
    correctness bug worth surfacing rather than silently dropping.
    """
    raise NotImplementedError("Week 39")


def should_refuse(question: str, chunks: list, threshold: float = 0.3) -> tuple[bool, str | None]:
    """Decide whether to answer at all, before generating.

    Cheap pre-check on retrieval scores. If the best chunk is barely relevant,
    refuse without paying for a generation call.

    The tradeoff is explicit and you should measure both directions: raising
    the threshold cuts hallucination and increases unnecessary refusals. Which
    error is worse depends entirely on the application, and being able to say
    that — and show the curve — is the mature answer.
    """
    raise NotImplementedError("Week 39")
