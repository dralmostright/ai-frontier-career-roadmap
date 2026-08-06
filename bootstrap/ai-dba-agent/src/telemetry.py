"""PostgreSQL telemetry collection — Week 43.

The agent's sensory input. Every collector here maps to a view a DBA actually
checks during an incident, which is exactly why this project is credible
coming from you and would not be coming from someone else.

All queries are read-only and bounded. The agent connects with a role that has
`SELECT` on the stats views and nothing else.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class TelemetrySnapshot:
    """A point-in-time view of database health.

    Snapshot-based rather than streaming, deliberately: incidents are
    diagnosed by comparing a bad moment to a normal one, and a snapshot pair
    is the simplest thing that supports that.
    """

    captured_at: datetime
    slow_queries: list[dict[str, Any]]
    index_usage: list[dict[str, Any]]
    table_stats: list[dict[str, Any]]
    locks: list[dict[str, Any]]
    connections: dict[str, Any]
    replication: list[dict[str, Any]]
    settings: dict[str, str]
    bgwriter: dict[str, Any]


def collect_slow_queries(
    conn: Any, limit: int = 20, min_mean_ms: float = 100.0
) -> list[dict[str, Any]]:
    """Top queries from `pg_stat_statements`.

    Order by `total_exec_time`, not `mean_exec_time`. A query taking 5ms and
    running 2 million times is a bigger problem than one taking 8 seconds
    twice, and sorting by mean hides it completely. This is the kind of
    judgment the agent needs encoded in its tools rather than left to the
    model.

    Return `calls`, `total_exec_time`, `mean_exec_time`, `stddev_exec_time`,
    `rows`, and the cache hit ratio. High stddev is itself a signal — it
    usually means plan instability or parameter-dependent performance.
    """
    raise NotImplementedError("Week 43")


def collect_index_usage(conn: Any) -> list[dict[str, Any]]:
    """From `pg_stat_user_indexes` and `pg_index`.

    Identify unused indexes (`idx_scan = 0`), duplicate indexes, and indexes
    whose leading column is already covered by another. Unused indexes are
    pure write amplification and wasted space.

    Caveat the agent must respect: `idx_scan` accumulates since the last stats
    reset. An index that looks unused may simply be newer than the counter.
    Always report `stats_reset` alongside — an agent that recommends dropping
    an index based on a counter reset an hour ago is worse than no agent.
    """
    raise NotImplementedError("Week 43")


def collect_table_stats(conn: Any) -> list[dict[str, Any]]:
    """From `pg_stat_user_tables`: scan counts, tuple counts, vacuum times.

    The key ratio is `seq_scan` against `seq_tup_read`. High sequential scans
    on a large table is the classic missing-index signature. But a sequential
    scan on a 200-row lookup table is correct and optimal, so size must be part
    of the judgment — another piece of domain knowledge that belongs in the
    tool, not the prompt.

    Also return `n_dead_tup`, `last_autovacuum`, and `autovacuum_count` for
    the bloat and vacuum-starvation scenarios.
    """
    raise NotImplementedError("Week 43")


def collect_locks(conn: Any) -> list[dict[str, Any]]:
    """Blocking chains from `pg_locks` joined to `pg_stat_activity`.

    Return the full chain, not just the blocked queries. The blocked query is
    the symptom; the blocker at the head of the chain is the cause, and it is
    frequently an idle-in-transaction session that nobody is looking at.

    Include `state`, `wait_event_type`, `wait_event`, and transaction age.
    `idle in transaction` with an age over a few minutes is one of the most
    common real-world causes of a database "outage".
    """
    raise NotImplementedError("Week 43")


def collect_bloat(conn: Any, threshold_pct: float = 20.0) -> list[dict[str, Any]]:
    """Table and index bloat via `pgstattuple`.

    `pgstattuple` scans the whole relation, which is expensive on large tables.
    Use `pgstattuple_approx` above a size threshold, and *say in the output*
    which one was used — an approximation reported as exact is the kind of
    detail that makes downstream reasoning wrong.
    """
    raise NotImplementedError("Week 43")


def collect_connections(conn: Any) -> dict[str, Any]:
    """Connection counts by state, against `max_connections`.

    Break out active, idle, and idle-in-transaction. Long-lived idle-in-
    transaction sessions hold locks and block vacuum, which makes them a cause
    of two other incident classes rather than merely a connection-count issue.
    """
    raise NotImplementedError("Week 43")


def collect_replication(conn: Any) -> list[dict[str, Any]]:
    """Replica lag and slot status from `pg_stat_replication`.

    Report write, flush, and replay lag separately — they diagnose different
    problems. Replay lag with low write lag means the replica is receiving WAL
    and cannot apply it, usually because a long-running query on the replica is
    blocking apply.

    Also check `pg_replication_slots` for inactive slots. An inactive slot
    retains WAL indefinitely and will fill the disk, which is a slow-motion
    outage that nobody notices until it is urgent.
    """
    raise NotImplementedError("Week 43")


def collect_settings(conn: Any, relevant_only: bool = True) -> dict[str, str]:
    """Configuration from `pg_settings`.

    Filter to the parameters that matter for performance diagnosis:
    `shared_buffers`, `work_mem`, `maintenance_work_mem`,
    `effective_cache_size`, `random_page_cost`, `max_connections`,
    `autovacuum_*`, `max_wal_size`, `checkpoint_completion_target`.

    Dumping all 350 settings wastes context and buries the signal.
    """
    raise NotImplementedError("Week 43")


def snapshot(conn: Any) -> TelemetrySnapshot:
    """Collect everything at once."""
    raise NotImplementedError("Week 43")


def diff_snapshots(before: TelemetrySnapshot, after: TelemetrySnapshot) -> dict[str, Any]:
    """What changed between two snapshots?

    Often the most informative single input. "Query 7's mean time went from
    12ms to 4,100ms and its plan changed" localizes an incident far faster
    than any absolute measurement, and it is how a human would actually
    approach it.
    """
    raise NotImplementedError("Week 43")
