# Week 43: Database Diagnostic Tools

## Outcome

By Sunday your agent has real diagnostic tools reading real telemetry from a real database, and a hypothesis framework that seeks disconfirming evidence rather than confirming it.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**This is the week where your fifteen years become an asset nobody can
replicate quickly.**

Every collector maps to a view a DBA actually checks during an incident, and the
judgment embedded in each one is what makes the agent good. Two examples worth
noticing:

Ordering slow queries by `total_exec_time` rather than `mean_exec_time`, because
a 5ms query run two million times is a bigger problem than an 8-second query run
twice. Sorting by mean hides the N+1 pattern completely.

Reporting `stats_reset` alongside `idx_scan`, because an index that looks unused
may simply be newer than the counter — and an agent that recommends dropping an
index based on a counter reset an hour ago is worse than no agent.

That kind of judgment belongs in the tools, not in the prompt, and encoding it is
the differentiated work.

The hypothesis framework matters too. `contradicting` evidence is what separates
diagnosis from confirmation bias, which is exactly the failure mode a junior
engineer has during an incident.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 9 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The telemetry surface**
   1. pg_stat_statements: the most useful view in PostgreSQL
   2. pg_stat_user_tables and _indexes
   3. pg_locks joined to pg_stat_activity
   4. pg_stat_replication and replication slots
   5. pgstattuple, and when to use the approximate version
2. **Judgment encoded in tools**
   1. total_exec_time over mean_exec_time
   2. stats_reset as a caveat on every counter
   3. Table size as context for a sequential scan
   4. Approximation flags in the output
3. **Query plans**
   1. Reading EXPLAIN ANALYZE: time, not rows
   2. Estimate versus actual as the strongest signal
   3. Sequential scans, nested loops, disk spills
   4. Explaining a plan to a non-DBA
4. **Hypothesis-driven diagnosis**
   1. Generate several candidates, not one
   2. Seek disconfirming evidence deliberately
   3. Scoring by support and contradiction
   4. Reporting ambiguity rather than resolving it falsely
5. **Snapshot diffing**
   1. Comparing a bad moment to a normal one
   2. Why the diff is often more informative than the absolute state

## Required Free Resources

- **Primary:** PostgreSQL EXPLAIN documentation — https://www.postgresql.org/docs/current/using-explain.html
- **Primary:** pg_stat_statements documentation — https://www.postgresql.org/docs/current/pgstatstatements.html
- Use The Index, Luke — https://use-the-index-luke.com/ — for the plan-reading material
- PgHero source — https://github.com/ankane/pghero — prior art worth reading; your agent covers a superset
- PostgreSQL wiki, Slow Query Questions — https://wiki.postgresql.org/wiki/Slow_Query_Questions — the ground truth for incident scenarios

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=43
```

1. **`collect_slow_queries`** (1.5h) — Ordered by total_exec_time. Include stddev — high variance means plan instability.
2. **`collect_index_usage`** (1.5h) — With stats_reset. Detect unused and duplicate indexes.
3. **`collect_table_stats`** (1h) — seq_scan against size. A seq scan on 200 rows is correct.
4. **`collect_locks`** (1.5h) — The full blocking chain, not just the blocked queries.
5. **`collect_bloat`, `collect_connections`, `collect_replication`, `collect_settings`** (2h) — Filter settings to the relevant ones; 350 rows wastes context.
6. **`snapshot` and `diff_snapshots`** (1.5h) — The diff is often the most informative single input.
7. **`generate_hypotheses` and `KNOWN_PATTERNS`** (2h) — Encode your domain knowledge as signatures with ruled-out-by conditions.
8. **`gather_evidence` seeking disconfirmation** (1.5h) — 'Is there an index the planner is ignoring?' distinguishes stale stats from a missing index.
9. **`explain_query_plan`** (2h) — The Week 43 interview drill, as a function. Also the spin-out project.
10. **`format_diagnosis` with evidence validation** (1h) — Reject any claim without a valid evidence ID. Enforced in code.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
a
i
-
d
b
a
-
a
g
e
n
t
/
s
r
c
/
t
e
l
e
m
e
t
r
y
.
p
y


b
o
o
t
s
t
r
a
p
/
a
i
-
d
b
a
-
a
g
e
n
t
/
s
r
c
/
d
i
a
g
n
o
s
i
s
.
p
y


b
o
o
t
s
t
r
a
p
/
a
i
-
d
b
a
-
a
g
e
n
t
/
s
r
c
/
t
o
o
l
s
/
```

## Tests To Write

`tests/test_dba_agent.py` week-43 blocks. The evidence-validation tests are the structural guarantee; the plan-explanation tests check the domain reasoning.

## Portfolio Artifact

The telemetry and diagnosis layer, plus — if you do the stretch — the standalone Query Plan Explainer as its own repository.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *Explain this bad query plan to someone who is not a DBA.* Use a real plan with a row-estimate gap. Two minutes, no jargon, ending with the specific fix.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Spin the query plan explainer out as a standalone tool with a small web UI: paste `EXPLAIN ANALYZE` output, get a plain-language explanation with the problem node highlighted and a suggested fix. This is Flagship #9, it is genuinely useful to people, small self-contained tools get shared in a way monoliths do not, and it might get actual users — which is its own signal.
