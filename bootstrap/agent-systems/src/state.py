"""Agent state and context management — Week 42.

The agent's working memory. The hard constraint is the context window: a long
investigation accumulates more observations than fit, and how you handle that
determines whether the agent stays coherent or quietly loses the thread.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Message:
    role: str
    content: Any
    tokens: int = 0
    step: int | None = None
    pinned: bool = False


class ConversationState:
    """Message history with a token budget.

    Four strategies when the context fills, with different failure modes:

    - **Truncate oldest.** Simple, and it discards the original task
      statement, which is the worst possible thing to forget. Always pin the
      system prompt and the task.
    - **Summarize the middle.** Keep the head and tail verbatim, compress the
      middle. Costs an LLM call and loses detail, but preserves the arc.
    - **Externalize.** Write observations to a scratchpad and keep only
      references in context. Best for long investigations; requires the agent
      to know how to read back.
    - **Selective retention.** Score observations by relevance to the current
      hypothesis and keep the top ones. Most sophisticated; hardest to get
      right.

    Start with pinning plus truncate-oldest. Move to externalization when the
    DBA agent starts running long.
    """

    def __init__(self, max_tokens: int = 100_000, reserve_for_response: int = 4_000) -> None:
        raise NotImplementedError("Week 42")

    def append(self, message: Message) -> None:
        raise NotImplementedError("Week 42")

    def render(self) -> list[dict[str, Any]]:
        """Produce the message list, applying the budget policy."""
        raise NotImplementedError("Week 42")

    def token_count(self) -> int:
        raise NotImplementedError("Week 42")

    def compact(self, summarizer: Any = None) -> int:
        """Reduce the context. Returns tokens reclaimed.

        Never compact away the system prompt or the original task. Log every
        compaction — an agent that mysteriously changes behavior at step 15
        is usually one that just lost the first half of its context.
        """
        raise NotImplementedError("Week 42")


@dataclass
class Scratchpad:
    """External working memory outside the context window.

    Findings, ruled-out hypotheses, and pending questions. Two benefits: it
    keeps the context small, and it makes the agent's reasoning inspectable
    after the fact.

    `ruled_out` is the underrated field. An agent that does not record what it
    has eliminated will re-check the same hypothesis three times, which is
    both the main source of wasted steps and the main cause of loop detection
    firing.
    """

    findings: list[dict[str, Any]] = field(default_factory=list)
    ruled_out: list[dict[str, Any]] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)

    def record_finding(self, claim: str, evidence_ref: str, confidence: float) -> None:
        raise NotImplementedError("Week 42")

    def rule_out(self, hypothesis: str, reason: str, evidence_ref: str) -> None:
        raise NotImplementedError("Week 42")

    def render(self) -> str:
        """Compact text summary for injection into the prompt."""
        raise NotImplementedError("Week 42")
