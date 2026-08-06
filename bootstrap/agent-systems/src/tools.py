"""Tool definitions and the registry — Week 41.

Tools are the agent's entire interface to the world. Everything the agent can
do, and every mistake it can make, passes through this file.

The framing that matters: you are not designing an API for a careful engineer.
You are designing one for a capable, well-meaning, occasionally confidently
wrong actor who will call your tool with arguments you did not anticipate. If
you have ever granted database permissions, you already have the right
instincts — apply them.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Protocol


class RiskLevel(StrEnum):
    """Risk tier, which determines the approval gate.

    Classifying every tool forces the safety conversation to happen at design
    time rather than after an incident.
    """

    READ = "read"
    ADVISORY = "advisory"
    REVERSIBLE = "reversible"
    DESTRUCTIVE = "destructive"


@dataclass
class ToolResult:
    """A tool's return value.

    Structured, not a bare string. `success` lets the loop distinguish "the
    tool failed" from "the tool succeeded and found nothing", which are
    completely different situations that a string return conflates.

    `truncated` matters more than it looks: silently truncating a result and
    letting the model reason over a partial view produces confident wrong
    conclusions. Tell it.
    """

    success: bool
    content: Any
    error: str | None = None
    truncated: bool = False
    row_count: int | None = None
    elapsed_ms: float | None = None
    metadata: dict[str, Any] | None = None


class Tool(Protocol):
    """The tool contract."""

    name: str
    description: str
    risk: RiskLevel

    def schema(self) -> dict[str, Any]:
        """JSON Schema for the arguments.

        Generate from a Pydantic model rather than hand-writing it. Hand-
        written schemas drift from the implementation, and a drifted schema
        means the model is being told the wrong thing about your tool.
        """
        ...

    def execute(self, **kwargs: Any) -> ToolResult: ...


def tool(
    name: str | None = None,
    risk: RiskLevel = RiskLevel.READ,
    timeout_s: float = 30.0,
    max_rows: int = 100,
) -> Any:
    """Decorator turning a typed function into a Tool.

    Derives the schema from type hints, enforces the timeout and row limit,
    catches exceptions and converts them into instructive errors, and records
    timing.

    **Write good error messages.** Compare:

        "psycopg.errors.UndefinedTable: relation 'user' does not exist"
        "Table 'user' not found. Did you mean 'users'? Call list_tables()
         to see available tables."

    The first makes the model flail; the second lets it recover in one step.
    Error message quality measurably changes agent success rates, and it is
    the cheapest improvement available to you.
    """
    raise NotImplementedError("Week 41")


class ToolRegistry:
    """Holds the available tools and renders them for the model.

    Responsibilities:

    - Register and look up tools by name.
    - Emit provider-format tool definitions.
    - Enforce risk policy: refuse to execute above the configured tier
      without approval.
    - Validate arguments against the schema *before* execution.
    - Record every call for the audit log.
    """

    def __init__(self, max_risk: RiskLevel = RiskLevel.READ, audit_log: Any = None) -> None:
        raise NotImplementedError("Week 41")

    def register(self, tool_obj: Tool) -> None:
        raise NotImplementedError("Week 41")

    def to_schemas(self, provider: str = "anthropic") -> list[dict[str, Any]]:
        """Render tool definitions for the model.

        Descriptions matter enormously — they are the only documentation the
        model gets. State what the tool does, when to use it, when *not* to,
        and what it returns. A vague description produces a tool that is
        called at the wrong times.
        """
        raise NotImplementedError("Week 41")

    def execute(self, name: str, arguments: dict[str, Any], approved: bool = False) -> ToolResult:
        """Validate, check risk policy, execute, and audit.

        Never `eval`, never string-interpolate arguments into a query.
        Parameterized queries only. The model is an untrusted input source and
        should be treated exactly the way you would treat a web form.
        """
        raise NotImplementedError("Week 41")


def validate_arguments(
    schema: dict[str, Any], arguments: dict[str, Any]
) -> tuple[bool, str | None]:
    """Check arguments against the schema before execution.

    Models hallucinate parameters, omit required ones, and pass strings where
    integers belong. Catching that here and returning a clear message lets the
    model self-correct; letting it reach your code produces a stack trace it
    cannot act on.
    """
    raise NotImplementedError("Week 41")


def truncate_result(content: Any, max_rows: int = 100, max_chars: int = 8000) -> tuple[Any, bool]:
    """Bound a result to fit the context window.

    Truncate informatively: "showing 100 of 4,312 rows" tells the model its
    view is partial and lets it narrow the query. Silent truncation produces
    confident conclusions drawn from 2% of the data.

    Returns:
        (content, was_truncated).
    """
    raise NotImplementedError("Week 41")
