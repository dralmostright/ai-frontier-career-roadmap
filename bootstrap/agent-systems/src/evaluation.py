"""Agent evaluation — Week 44.

Harder than evaluating a single output, because the trajectory matters as much
as the answer. An agent that guesses correctly without looking at the evidence
is not a working agent; it is a lucky one.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Scenario:
    """A test case with a known ground truth.

    `root_cause` is the answer. `required_evidence` is what the agent should
    have looked at. `unsafe_actions` are things it must never propose.

    That third field is the one that makes this a safety evaluation rather
    than only an accuracy one.
    """

    id: str
    description: str
    setup: dict[str, Any]
    root_cause: str
    acceptable_diagnoses: list[str]
    required_evidence: list[str]
    unsafe_actions: list[str]
    difficulty: str = "medium"


@dataclass
class ScenarioResult:
    scenario_id: str
    correct: bool
    diagnosis: str
    steps_taken: int
    evidence_cited: list[str]
    evidence_recall: float
    unsafe_proposed: list[str]
    tokens: int
    cost_usd: float
    elapsed_s: float


def score_outcome(scenario: Scenario, diagnosis: str, judge: Any = None) -> bool:
    """Did the agent reach an acceptable conclusion?

    Use `acceptable_diagnoses`, not exact string match. "Missing index on
    users.email" and "sequential scan because users.email is unindexed" are
    the same diagnosis expressed differently, and a string comparison would
    call the second one wrong.
    """
    raise NotImplementedError("Week 44")


def score_trajectory(scenario: Scenario, run: Any) -> dict[str, float]:
    """Was the *path* sensible, not just the destination?

    Metrics:

    - **Evidence recall.** What fraction of `required_evidence` did it
      actually examine? An agent reaching the right answer without looking at
      the evidence got lucky, and it will not be lucky on the next incident.
    - **Tool precision.** Fraction of tool calls that contributed. Low
      precision means it is flailing.
    - **Step efficiency.** Steps taken versus the minimum needed.
    - **Redundancy.** Repeated identical calls.
    """
    raise NotImplementedError("Week 44")


def score_safety(scenario: Scenario, run: Any) -> dict[str, Any]:
    """Did it ever propose something unsafe?

    The metric that gates deployment. One unsafe recommendation in a hundred
    scenarios is a blocker, not a rounding error, and reporting it as such is
    the whole point of running this.

    Also check: did every mutating recommendation carry a rollback plan? Did
    every recommendation cite evidence?
    """
    raise NotImplementedError("Week 44")


class AgentEvaluator:
    """Run scenarios, aggregate, and report.

    **Run every scenario N times.** Agents are stochastic; a single successful
    run proves nothing. Report mean and variance, and treat high variance as a
    finding in its own right — an agent that solves a scenario 3 times out of
    5 is not a 60%-accurate agent, it is an unreliable one, and those are
    different problems.

    Almost nobody does this. Doing it and reporting it honestly is a strong
    differentiator for the Month 11 capstone.
    """

    def __init__(self, scenarios: list[Scenario], runs_per_scenario: int = 5) -> None:
        raise NotImplementedError("Week 44")

    def evaluate(self, agent: Any) -> Any:
        raise NotImplementedError("Week 44")

    def report(self, results: Any) -> str:
        """Markdown report for the capstone README.

        Must include: accuracy with a confidence interval, per-difficulty
        breakdown, evidence recall, unsafe-recommendation count, run-to-run
        variance, mean cost per incident, and a taxonomy of failures.

        That last one — the failure taxonomy — is what makes the project read
        as engineering rather than a demo.
        """
        raise NotImplementedError("Week 44")

    def compare_configurations(self, agents: dict[str, Any]) -> Any:
        """Ablations: with and without reflection, different models, different
        tool sets, different step budgets.

        The Month 11 ablation table. "Reflection added 40% to cost and 2
        points of accuracy" is a real finding, and reporting it when the
        answer is unflattering is what makes the rest credible.
        """
        raise NotImplementedError("Week 44")
