"""Experiment tracking — Week 20, extended in Week 53.

Start with a local JSONL logger. Add MLflow when you outgrow it. Do not start
with MLflow — building the simple version first teaches you what an
experiment record needs to contain, which is the actual lesson.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


class ExperimentTracker:
    """Records one run: config, metrics, artifacts, environment.

    What belongs in a run record, which is a Week 53 interview question:

    - The exact config, including defaults that were not overridden
    - Git SHA and whether the tree was dirty
    - Environment snapshot
    - Metrics over time, not just the final value
    - Artifact paths (checkpoints, plots, predictions)
    - Wall-clock time and, from Month 10, estimated cost
    - A one-line human note on *why* this run exists

    That last field is the one everybody omits and everybody later wishes
    they had.
    """

    def __init__(self, run_dir: Path, name: str, config: dict[str, Any] | None = None) -> None:
        raise NotImplementedError("Week 20")

    def log_metrics(self, metrics: dict[str, float], step: int) -> None:
        raise NotImplementedError("Week 20")

    def log_artifact(self, path: Path, kind: str = "checkpoint") -> None:
        raise NotImplementedError("Week 20")

    def log_note(self, text: str) -> None:
        raise NotImplementedError("Week 20")

    def finish(self, status: str = "completed") -> None:
        raise NotImplementedError("Week 20")


def compare_runs(run_dirs: list[Path], metric: str = "val_loss") -> Any:
    """Tabulate runs side by side: config diffs and final metrics.

    Returns a DataFrame sorted by the metric, with columns for only the
    hyperparameters that actually varied. Constant columns are noise.
    """
    raise NotImplementedError("Week 20")


def plot_training_curves(run_dirs: list[Path], metrics: list[str] | None = None) -> Any:
    """Overlay curves from multiple runs.

    Plot the loss curve after every single run for the rest of the course.
    It answers three questions instantly that each cost an hour otherwise.
    """
    raise NotImplementedError("Week 20")
