"""The agent loop — Week 42.

Think, act, observe, repeat, until done or out of budget.

The loop is not the hard part; it is thirty lines. The hard parts are
termination, budgets, error recovery, and knowing when reflection helps.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class StopReason(StrEnum):
    COMPLETED = "completed"
    MAX_STEPS = "max_steps"
    BUDGET_EXCEEDED = "budget_exceeded"
    AWAITING_APPROVAL = "awaiting_approval"
    ERROR = "error"
    NO_PROGRESS = "no_progress"


@dataclass
class Step:
    """One iteration, recorded in full.

    Keep the whole trajectory. You need it for the audit log, for evaluation,
    and for debugging — and when an agent reaches a bizarre conclusion, the
    trajectory is the only way to find out where it went wrong.
    """

    index: int
    thought: str | None
    tool_name: str | None
    tool_arguments: dict[str, Any] | None
    observation: Any
    tokens_used: int = 0
    cost_usd: float = 0.0
    elapsed_ms: float = 0.0


@dataclass
class AgentRun:
    """A complete run."""

    task: str
    steps: list[Step] = field(default_factory=list)
    final_answer: str | None = None
    stop_reason: StopReason | None = None
    total_tokens: int = 0
    total_cost_usd: float = 0.0
    total_elapsed_s: float = 0.0


class Agent:
    """A ReAct-style agent with budgets and safety gates.

    Args:
        model: LLM client.
        registry: Available tools.
        system_prompt: Role, constraints, and output contract.
        max_steps: Hard iteration cap.
        max_tokens: Token budget for the whole run.
        max_cost_usd: Dollar budget. Enforce it; an agent in a loop is a bill.
        reflect_every: Insert a self-critique step every N iterations. 0
            disables it.

    **On termination**, which is where naive implementations fail:

    - A step cap alone is insufficient — the agent burns the whole budget on a
      task it finished at step 3.
    - Detect no-progress: the same tool with the same arguments twice in a row
      means it is stuck. Stop, or force a different approach.
    - Give it an explicit way to say "I cannot determine this." Without one,
      an agent will invent an answer rather than admit failure, and that is
      the worst possible behavior for a diagnostic tool.

    **On reflection**, since the interview question is "when does it help?":
    it helps when the agent can *verify* something — re-reading a query plan,
    checking whether the evidence supports the conclusion. It is theater when
    the agent merely re-asserts its previous answer more confidently. Measure
    it before believing in it; it doubles your token cost.
    """

    def __init__(
        self,
        model: Any,
        registry: Any,
        system_prompt: str,
        max_steps: int = 12,
        max_tokens: int = 100_000,
        max_cost_usd: float = 1.0,
        reflect_every: int = 0,
    ) -> None:
        raise NotImplementedError("Week 42")

    def run(self, task: str, context: dict[str, Any] | None = None) -> AgentRun:
        raise NotImplementedError("Week 42")

    def step(self, state: Any) -> Step:
        """One iteration: call the model, parse, execute, observe."""
        raise NotImplementedError("Week 42")

    def _detect_no_progress(self, steps: list[Step], window: int = 3) -> bool:
        """Is it looping?

        Repeated identical tool calls, or repeated observations. Catch it and
        either force a different approach or stop honestly.
        """
        raise NotImplementedError("Week 42")

    def _handle_tool_error(self, step: Step, error: str) -> str:
        """Turn a failure into something the model can act on.

        Retry transient errors with backoff. For permanent ones, return an
        instructive message rather than a stack trace. Never retry a
        destructive action automatically.
        """
        raise NotImplementedError("Week 42")


def build_system_prompt(
    role: str,
    tools: list[Any],
    constraints: list[str],
    output_format: str | None = None,
) -> str:
    """Assemble the system prompt.

    What a good agent prompt contains:

    - The role and its scope, including what is explicitly out of scope
    - Available tools and when to use each
    - Hard constraints ("never recommend an action you cannot justify with
      observed evidence")
    - The evidence requirement: every claim cites the tool output supporting it
    - Explicit permission to say "I don't know"
    - The output contract, ideally a schema

    The evidence requirement is the one that most improves output quality for
    a diagnostic agent, and it is what makes the DBA assistant trustworthy
    rather than merely fluent.
    """
    raise NotImplementedError("Week 42")
