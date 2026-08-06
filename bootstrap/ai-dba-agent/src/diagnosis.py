"""Hypothesis generation and evidence assembly — Week 43.

The reasoning layer between telemetry and recommendation.

The design principle: **the agent must never assert anything it did not
observe.** Every claim carries a pointer to the tool output that supports it.
That constraint is what makes a diagnostic agent trustworthy, and it is
enforced structurally here rather than requested in the prompt.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Evidence:
    """One observation, with provenance.

    `raw` is kept so a human can verify the interpretation. An agent that
    summarizes away the underlying data cannot be audited.
    """

    id: str
    source: str
    summary: str
    raw: Any
    captured_at: str


@dataclass
class Hypothesis:
    """A candidate explanation, with support and contradiction.

    `contradicting` is the field that separates diagnosis from confirmation
    bias. An agent that only collects supporting evidence will confidently
    diagnose the first plausible cause, which is exactly the failure mode a
    junior engineer has during an incident.
    """

    name: str
    description: str
    supporting: list[str] = field(default_factory=list)
    contradicting: list[str] = field(default_factory=list)
    confidence: float = 0.0
    ruled_out: bool = False
    ruled_out_reason: str | None = None


KNOWN_PATTERNS: dict[str, dict[str, Any]] = {}
"""Incident signatures. Populate this in Week 43.

Each entry names the signals that indicate a cause and the checks that would
rule it out. This is your domain knowledge, encoded — and encoding it is more
valuable than hoping the model has absorbed it from pretraining.

Example shape:

    "missing_index": {
        "signals": ["high seq_scan on a large table",
                    "query filters on an unindexed column",
                    "EXPLAIN shows Seq Scan with a high row estimate"],
        "ruled_out_by": ["the table is small enough that a seq scan is optimal",
                         "an index exists but the planner rejects it",
                         "the filter is not selective enough to help"],
        "confounders": ["stale statistics can cause a seq scan even with an index"],
    }
"""


def generate_hypotheses(snapshot: Any, symptom: str | None = None) -> list[Hypothesis]:
    """Propose candidate causes from the telemetry.

    Generate several. An agent that commits to one hypothesis and gathers
    confirming evidence is doing confirmation bias with extra steps — and it
    will be confidently wrong on exactly the ambiguous scenarios that matter.
    """
    raise NotImplementedError("Week 43")


def gather_evidence(hypothesis: Hypothesis, tools: Any) -> list[Evidence]:
    """Run the checks that would confirm or refute a hypothesis.

    Deliberately seek disconfirming evidence too. "Is there already an index
    that the planner is not using?" is as important as "is there no index?",
    and it distinguishes a missing index from stale statistics — two problems
    with completely different fixes.
    """
    raise NotImplementedError("Week 43")


def score_hypotheses(hypotheses: list[Hypothesis], evidence: list[Evidence]) -> list[Hypothesis]:
    """Rank by evidential support.

    Be honest about ambiguity. If two hypotheses score similarly, say so
    rather than picking one. "Either stale statistics or a missing index; here
    is the check that would distinguish them" is a better answer than a
    confident coin flip, and it is what a good engineer would say.
    """
    raise NotImplementedError("Week 43")


def explain_query_plan(plan: dict[str, Any], audience: str = "engineer") -> str:
    """Translate `EXPLAIN ANALYZE` output into prose.

    The Week 43 interview drill — "explain a bad query plan to a non-DBA" —
    made into a function. This is also the natural spin-out project (Flagship
    #9, the Query Plan Explainer): small, self-contained, immediately useful,
    and the kind of tool that gets shared.

    What a good explanation identifies:

    - The node consuming the most time, not the most rows
    - Row estimate versus actual — a large gap means stale statistics, and
      this is the single most useful signal in a plan
    - Sequential scans on large tables
    - Nested loops with a high outer-row count
    - Sorts and hashes spilling to disk (`work_mem` too small)
    - The specific, actionable fix
    """
    raise NotImplementedError("Week 43")


def format_diagnosis(hypotheses: list[Hypothesis], evidence: list[Evidence]) -> dict[str, Any]:
    """Assemble the final structured diagnosis.

    Every claim references an evidence id. Validate that before returning: if
    a claim has no supporting evidence id, it is a hallucination and must not
    ship. Enforcing this in code rather than trusting the prompt is the whole
    design.
    """
    raise NotImplementedError("Week 43")
