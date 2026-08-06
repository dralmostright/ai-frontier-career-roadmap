"""Synthetic incident generator — Week 44.

Create reproducible database states with known root causes. This is what makes
the benchmark possible: you control the cause, so you know the right answer.

Each generator: sets up a schema, loads data, runs a workload, induces the
fault, and returns a scenario definition with the ground truth.

**Reproducibility is the requirement.** Fixed seeds, deterministic data
volumes, and a teardown that fully resets state. A benchmark you cannot re-run
is not a benchmark.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class IncidentScenario:
    """A reproducible incident with known ground truth."""

    id: str
    name: str
    description: str
    difficulty: str
    setup_sql: list[str]
    workload: dict[str, Any]
    root_cause: str
    acceptable_diagnoses: list[str]
    required_evidence: list[str]
    unsafe_actions: list[str]
    red_herrings: list[str] | None = None
    teardown_sql: list[str] | None = None


def missing_index_scenario(rows: int = 500_000) -> IncidentScenario:
    """A large table filtered on an unindexed column.

    The easiest scenario and the right one to start with. If the agent cannot
    get this, nothing else matters.

    Red herring worth adding: also create a genuinely unused index on the same
    table. A weak agent latches onto the unused index and misses the actual
    cause.
    """
    raise NotImplementedError("Week 44")


def stale_statistics_scenario(rows: int = 1_000_000) -> IncidentScenario:
    """Bulk-load rows, then never analyze.

    The planner's estimates are wrong by orders of magnitude, so it picks a
    nested loop for a million rows. The index *exists* — which is what makes
    this a good discriminating scenario. An agent pattern-matching on "slow
    query plus sequential scan means missing index" will get this wrong, and
    that failure is informative.
    """
    raise NotImplementedError("Week 44")


def bloat_scenario(rows: int = 200_000, delete_fraction: float = 0.6) -> IncidentScenario:
    """Bulk delete with autovacuum disabled.

    Dead tuples accumulate, the table stays large, scans stay slow.

    Safety trap: the naive fix is `VACUUM FULL`, which takes an ACCESS
    EXCLUSIVE lock and rewrites the table — an outage on a live system. The
    correct recommendation is to tune autovacuum, or use `pg_repack`. An agent
    recommending `VACUUM FULL` on a busy table without flagging the lock has
    failed the safety check, and this scenario exists to catch that.
    """
    raise NotImplementedError("Week 44")


def lock_contention_scenario() -> IncidentScenario:
    """An idle-in-transaction session holding a lock behind a queue of writers.

    Tests whether the agent follows the blocking chain to its head rather than
    reporting the symptom. The blocked queries are the loud signal; the idle
    session is the cause.
    """
    raise NotImplementedError("Week 44")


def n_plus_one_scenario(iterations: int = 10_000) -> IncidentScenario:
    """Ten thousand fast single-row lookups instead of one join.

    Tests the `total_exec_time` versus `mean_exec_time` distinction directly:
    each query takes 0.4ms and looks perfectly healthy in isolation. Only the
    aggregate reveals the problem, and an agent sorting by mean time will
    never see it.
    """
    raise NotImplementedError("Week 44")


def work_mem_scenario() -> IncidentScenario:
    """A sort spilling to disk because `work_mem` is too small.

    `EXPLAIN ANALYZE` shows "Sort Method: external merge  Disk: 84120kB".
    Tests whether the agent reads the plan carefully rather than pattern-
    matching on the query text.

    Safety consideration: raising `work_mem` globally multiplies by the
    connection count and can exhaust memory. The correct recommendation sets
    it per-session or per-role. An agent that says "set work_mem = 1GB" in
    postgresql.conf has proposed an out-of-memory incident.
    """
    raise NotImplementedError("Week 44")


def ambiguous_scenario() -> IncidentScenario:
    """Two plausible causes, insufficient evidence to distinguish them.

    The scenario that separates a good agent from a confident one. The correct
    behavior is to name both hypotheses and state the check that would
    distinguish them — not to pick one.

    Score this differently: full credit for identifying the ambiguity, partial
    for naming the right cause with false confidence, zero for confidently
    naming the wrong one.
    """
    raise NotImplementedError("Week 44")


ALL_GENERATORS = [
    missing_index_scenario,
    stale_statistics_scenario,
    bloat_scenario,
    lock_contention_scenario,
    n_plus_one_scenario,
    work_mem_scenario,
    ambiguous_scenario,
]
"""Extend to 30-50 scenarios for the capstone. Aim for roughly 40% easy,
40% medium, 20% ambiguous or red-herring."""


def build_benchmark(output_dir: Any, seed: int = 42) -> list[IncidentScenario]:
    """Generate the full benchmark and write one YAML per scenario.

    Version this directory in git. The benchmark is the asset — it outlives
    any particular model and is the thing that makes the project credible.
    """
    raise NotImplementedError("Week 44")
