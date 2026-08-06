"""Experiment runner — Week 66.

Configuration, seeds, ablations, and result collection. Built so that a
reviewer can rerun any number in your report from the config alone.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ExperimentSpec:
    """A pre-registered experiment.

    Fill in `hypothesis` and `falsifier` **before** running anything. This is
    the discipline that stops you from retroactively deciding that whatever
    happened is what you predicted — which is the most common way honest
    people produce dishonest research.
    """

    name: str
    hypothesis: str
    falsifier: str
    independent_variable: str
    levels: list[Any]
    control_variables: dict[str, Any]
    metrics: list[str]
    baselines: list[str]
    seeds: list[int] = field(default_factory=lambda: [0, 1, 2, 3, 4])
    notes: str = ""


@dataclass
class RunResult:
    spec_name: str
    level: Any
    seed: int
    metrics: dict[str, float]
    duration_s: float
    config: dict[str, Any]
    artifacts: dict[str, str] = field(default_factory=dict)


class ExperimentRunner:
    """Run an experiment across levels and seeds, resumably.

    Requirements:

    - **Resumable.** A sweep takes hours and something will fail. Persist
      completed runs and skip them on restart.
    - **Seeded.** Every run's seed is recorded and reproducible in isolation.
    - **Environment-captured.** Snapshot per run, using Week 20's function.
    - **Cost-tracked.** Tokens, dollars, GPU-hours.
    - **Failure-recording.** A crashed run is data. Record it rather than
      silently dropping it — silently dropped failures bias your results
      toward configurations that happen to be stable.
    """

    def __init__(self, spec: ExperimentSpec, output_dir: Path, resume: bool = True) -> None:
        raise NotImplementedError("Week 66")

    def run(self, train_fn: Any) -> list[RunResult]:
        raise NotImplementedError("Week 66")

    def results_frame(self) -> Any:
        """Results as a DataFrame: one row per (level, seed)."""
        raise NotImplementedError("Week 66")


def ablate(base_config: dict[str, Any], components: list[str], train_fn: Any) -> Any:
    """Remove one component at a time and measure the effect.

    The ablation is what turns "my system works" into "component X causes the
    effect." Without it a result is an observation; with it, it is a finding.

    Run each ablation across all seeds too. An ablation with one seed is not
    evidence, and single-seed ablations are unfortunately common in published
    work — which is a reasonable thing to note in your Week 61 critiques.
    """
    raise NotImplementedError("Week 66")


def sensitivity_analysis(
    base_config: dict[str, Any], parameter: str, values: list[Any], train_fn: Any
) -> Any:
    """How much does the result depend on one hyperparameter?

    A finding that only holds at one learning rate is a fragile finding.
    Checking this before you publish, and reporting it, is what makes the
    result trustworthy.
    """
    raise NotImplementedError("Week 66")
