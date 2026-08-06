"""Model registry — Week 54.

Versioning, lineage, staging, promotion, and — the part that matters at 2am —
rollback.

The requirement people miss: **a model version is not just weights.** It is
weights plus the code that produced them plus the data plus the config plus the
evaluation results. Rolling back weights alone can produce a model that no
longer matches its serving code, which is a worse outage than the one you were
fixing.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class ModelVersion:
    """A registered model version and everything needed to reproduce or revert it."""

    name: str
    version: int
    stage: str
    artifact_uri: str
    created_at: datetime
    git_sha: str
    git_dirty: bool
    config: dict[str, Any]
    dataset_version: str
    metrics: dict[str, float]
    eval_run_id: str | None = None
    parent_version: int | None = None
    notes: str = ""
    tags: dict[str, str] = field(default_factory=dict)


class ModelRegistry:
    """Versioned model store with staged promotion.

    Stages: `none` -> `staging` -> `production` -> `archived`.

    Rules worth enforcing in code rather than in a wiki:

    - Promotion to production requires a passing eval run. No exceptions, no
      "just this once."
    - Exactly one production version at a time, per model name.
    - The previous production version is retained and immediately
      re-promotable. That is your rollback.
    - Every transition is logged with who, when, and why.
    """

    def __init__(self, backend: str = "local", uri: str | Path | None = None) -> None:
        raise NotImplementedError("Week 54")

    def register(
        self, name: str, artifact: Path, metrics: dict[str, float], **metadata: Any
    ) -> ModelVersion:
        raise NotImplementedError("Week 54")

    def promote(self, name: str, version: int, stage: str, actor: str, reason: str) -> ModelVersion:
        """Promote a version. Refuses production without a passing eval run."""
        raise NotImplementedError("Week 54")

    def get_production(self, name: str) -> ModelVersion | None:
        raise NotImplementedError("Week 54")

    def rollback(self, name: str, actor: str, reason: str) -> ModelVersion:
        """Revert production to the previous version.

        **Time this.** Under five minutes, executable by someone who did not
        build the system, following only the runbook. If it takes longer or
        needs you specifically, it is not a rollback procedure — it is a hope.

        Test it on a schedule, not only when you need it. An untested rollback
        is an untested code path, and it will fail exactly when you are least
        able to debug it.
        """
        raise NotImplementedError("Week 54")

    def lineage(self, name: str, version: int) -> dict[str, Any]:
        """Full provenance: data, code, config, parent version, eval run.

        The question this answers is "why does the model behave this way?",
        asked three months later by someone who was not there.
        """
        raise NotImplementedError("Week 54")

    def compare(self, name: str, version_a: int, version_b: int) -> dict[str, Any]:
        """Diff two versions: metrics, config, data, code."""
        raise NotImplementedError("Week 54")
