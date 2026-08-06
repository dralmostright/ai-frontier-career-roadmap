"""Weeks 43-44 — telemetry, diagnosis, and the benchmark.

Tests marked `db` need the lab Postgres (`make db-up`).
"""

from __future__ import annotations

import pytest
from diagnosis import Evidence, Hypothesis, explain_query_plan, format_diagnosis, score_hypotheses


@pytest.mark.week(43)
class TestDiagnosis:
    def test_hypothesis_tracks_contradicting_evidence(self):
        """The field that separates diagnosis from confirmation bias."""
        h = Hypothesis(name="missing_index", description="no index on the filter column")
        h.supporting.append("e1")
        h.contradicting.append("e2")
        assert h.supporting and h.contradicting

    def test_scoring_prefers_well_supported_hypotheses(self):
        strong = Hypothesis(name="a", description="", supporting=["e1", "e2", "e3"])
        weak = Hypothesis(name="b", description="", supporting=["e1"])
        evidence = [
            Evidence(id=f"e{i}", source="pg_stat", summary="", raw={}, captured_at="")
            for i in range(1, 4)
        ]
        ranked = score_hypotheses([weak, strong], evidence)
        assert ranked[0].name == "a"

    def test_contradicting_evidence_lowers_confidence(self):
        clean = Hypothesis(name="a", description="", supporting=["e1", "e2"])
        contested = Hypothesis(
            name="b", description="", supporting=["e1", "e2"], contradicting=["e3"]
        )
        evidence = [
            Evidence(id=f"e{i}", source="pg_stat", summary="", raw={}, captured_at="")
            for i in range(1, 4)
        ]
        ranked = score_hypotheses([contested, clean], evidence)
        assert ranked[0].name == "a"

    def test_ambiguity_is_reported_rather_than_resolved(self):
        """Two similar scores must not produce a confident single answer."""
        a = Hypothesis(name="stale_stats", description="", supporting=["e1", "e2"])
        b = Hypothesis(name="missing_index", description="", supporting=["e1", "e3"])
        evidence = [
            Evidence(id=f"e{i}", source="pg_stat", summary="", raw={}, captured_at="")
            for i in range(1, 4)
        ]
        result = format_diagnosis(score_hypotheses([a, b], evidence), evidence)
        assert result.get("ambiguous") is True
        assert len(result["candidates"]) >= 2

    def test_every_claim_cites_evidence(self):
        """**The structural guarantee.** A claim without evidence is a hallucination."""
        h = Hypothesis(name="missing_index", description="", supporting=["e1"], confidence=0.9)
        evidence = [
            Evidence(
                id="e1",
                source="pg_stat_user_tables",
                summary="seq_scan=41200",
                raw={},
                captured_at="",
            )
        ]
        result = format_diagnosis([h], evidence)
        for claim in result["claims"]:
            assert claim["evidence_ids"]
            assert all(eid in {"e1"} for eid in claim["evidence_ids"])

    def test_claims_referencing_unknown_evidence_are_rejected(self):
        h = Hypothesis(name="x", description="", supporting=["nonexistent"], confidence=0.9)
        with pytest.raises(ValueError):
            format_diagnosis([h], [])


@pytest.mark.week(43)
class TestPlanExplanation:
    def test_identifies_the_dominant_node(self):
        plan = {
            "Node Type": "Nested Loop",
            "Actual Total Time": 4100.0,
            "Plans": [
                {
                    "Node Type": "Seq Scan",
                    "Relation Name": "users",
                    "Actual Total Time": 3950.0,
                    "Plan Rows": 100,
                    "Actual Rows": 1_000_000,
                },
                {
                    "Node Type": "Index Scan",
                    "Actual Total Time": 12.0,
                    "Plan Rows": 1,
                    "Actual Rows": 1,
                },
            ],
        }
        explanation = explain_query_plan(plan)
        assert "Seq Scan" in explanation or "sequential scan" in explanation.lower()
        assert "users" in explanation

    def test_flags_a_row_estimate_gap(self):
        """Estimated 100, actual 1,000,000. The strongest signal in a plan."""
        plan = {
            "Node Type": "Seq Scan",
            "Relation Name": "events",
            "Plan Rows": 100,
            "Actual Rows": 1_000_000,
            "Actual Total Time": 2000.0,
        }
        explanation = explain_query_plan(plan)
        assert "estimate" in explanation.lower() or "statistics" in explanation.lower()

    def test_flags_a_disk_spill(self):
        plan = {
            "Node Type": "Sort",
            "Sort Method": "external merge",
            "Sort Space Used": 84120,
            "Actual Total Time": 900.0,
        }
        explanation = explain_query_plan(plan)
        assert "work_mem" in explanation or "disk" in explanation.lower()

    def test_non_dba_audience_avoids_jargon(self):
        plan = {
            "Node Type": "Seq Scan",
            "Relation Name": "users",
            "Plan Rows": 100,
            "Actual Rows": 1_000_000,
            "Actual Total Time": 2000.0,
        }
        plain = explain_query_plan(plan, audience="non-technical")
        assert "Seq Scan" not in plain


@pytest.mark.week(44)
class TestBenchmark:
    def test_scenarios_declare_ground_truth_and_unsafe_actions(self):
        from generate import ALL_GENERATORS

        assert len(ALL_GENERATORS) >= 7
        for generator in ALL_GENERATORS:
            scenario = generator()
            assert scenario.root_cause
            assert scenario.acceptable_diagnoses
            assert scenario.required_evidence
            assert isinstance(scenario.unsafe_actions, list)

    def test_bloat_scenario_marks_vacuum_full_unsafe(self):
        """The safety trap: VACUUM FULL takes an exclusive lock."""
        from generate import bloat_scenario

        unsafe = " ".join(bloat_scenario().unsafe_actions).upper()
        assert "VACUUM FULL" in unsafe

    def test_work_mem_scenario_marks_a_global_increase_unsafe(self):
        """work_mem is per-operation and multiplies by connection count."""
        from generate import work_mem_scenario

        unsafe = " ".join(work_mem_scenario().unsafe_actions).lower()
        assert "global" in unsafe or "postgresql.conf" in unsafe

    def test_stale_statistics_scenario_is_distinguishable_from_missing_index(self):
        """The discriminating scenario: the index exists, the planner ignores it."""
        from generate import stale_statistics_scenario

        scenario = stale_statistics_scenario()
        assert "index" in " ".join(scenario.red_herrings or []).lower()

    def test_ambiguous_scenario_accepts_multiple_diagnoses(self):
        from generate import ambiguous_scenario

        assert len(ambiguous_scenario().acceptable_diagnoses) >= 2


@pytest.mark.week(43)
@pytest.mark.db
class TestTelemetryLive:
    def test_collectors_run_against_a_real_database(self, database_url):
        import psycopg
        from telemetry import snapshot

        with psycopg.connect(database_url) as conn:
            snap = snapshot(conn)
        assert snap.captured_at is not None
        assert isinstance(snap.settings, dict)

    def test_slow_queries_sorted_by_total_not_mean_time(self, database_url):
        """A 5ms query run 2M times beats an 8s query run twice."""
        import psycopg
        from telemetry import collect_slow_queries

        with psycopg.connect(database_url) as conn:
            rows = collect_slow_queries(conn, limit=10, min_mean_ms=0.0)
        totals = [r["total_exec_time"] for r in rows]
        assert totals == sorted(totals, reverse=True)

    def test_index_usage_reports_stats_reset_time(self, database_url):
        """An index isn't unused if the counter was reset an hour ago."""
        import psycopg
        from telemetry import collect_index_usage

        with psycopg.connect(database_url) as conn:
            rows = collect_index_usage(conn)
        if rows:
            assert "stats_reset" in rows[0]
