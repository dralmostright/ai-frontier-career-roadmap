# ai-dba-agent

**Weeks 43-44 · Month 11 · ⭐ THE FLAGSHIP**

An LLM agent that diagnoses PostgreSQL performance incidents from telemetry,
explains its reasoning with cited evidence, and proposes remediations
classified by risk.

This is the single most important project in the course. If one thing on your
resume gets you an interview, it is this.

---

## Why This Project Wins

The applicant pool is saturated with agents that summarize PDFs and call three
tools. Yours is different in one structural way: **you know the ground truth.**

That means you can do the thing almost nobody else can — build the benchmark,
grade the agent, and report honestly where it fails. An agent without an
evaluation is a demo. An agent with a domain-expert-constructed benchmark is
engineering.

Everything in this project should be pointed at that difference.

---

## What It Does

```text
synthetic incident  ->  telemetry ingestion  ->  agent loop  ->  diagnosis
                                                      |
                                      tools: pg_stat_statements, EXPLAIN,
                                      index usage, locks, bloat, config,
                                      replication lag
                                                      |
                                      -> risk-classified recommendations
                                      -> cited evidence for every claim
                                      -> human approval gate for mutations
                                      -> audit log
```

**Read-only by default.** The agent connects with a role that has no write
privileges. Not "the agent is instructed not to write" — it *cannot*, enforced
by the grant. Any mutating action is a recommendation that a human approves and
executes.

---

## Layout

```text
ai-dba-agent/
  src/
    agent.py           the DBA agent, built on agent-systems
    telemetry.py       collectors: pg_stat_statements, locks, bloat, config
    diagnosis.py       hypothesis generation and evidence assembly
    recommendations.py risk-classified remediation with rollback plans
    prompts.py         system prompt, few-shot examples, output schema
    tools/
      queries.py       slow queries, plans, statement stats
      indexes.py       usage, missing, unused, bloat
      locks.py         blocking chains, wait events
      config.py        settings inspection and sanity checks
      replication.py   lag and slot inspection
  evals/
    scenarios/         the benchmark — one YAML per incident
    generate.py        synthetic incident generator
    run_eval.py        the harness
    results/
  docs/
    design.md          architecture and the decisions behind it
    safety.md          risk model, approval gates, blast radius
    evaluation.md      benchmark construction and results
    limitations.md     what it cannot do, stated plainly
  tests/
```

---

## The Benchmark

**This is the deliverable.** Build 30-50 synthetic incidents with known root
causes. Each one is a YAML scenario: database setup, workload, the true root
cause, acceptable diagnoses, the evidence a competent DBA would examine, and
the actions that would be unsafe.

Incident classes to cover, drawn from what actually pages people:

| Class | Example |
| ----- | ------- |
| Missing index | Sequential scan on a large, frequently-filtered table |
| Unused index | Write amplification from indexes nothing reads |
| Stale statistics | Planner picks a nested loop for 2M rows |
| Bloat | 40% dead tuples after a bulk delete, autovacuum starved |
| Lock contention | Long transaction blocking a queue of writers |
| Connection exhaustion | No pooler, connections at max_connections |
| Bad plan from a parameter | Generic plan chosen for a skewed distribution |
| N+1 query pattern | Application issuing 10k single-row lookups |
| Replication lag | Long-running query on the replica blocking apply |
| Config mismatch | work_mem too low, causing repeated disk sorts |
| Checkpoint storm | Too-small max_wal_size causing constant checkpoints |
| Autovacuum not keeping up | Transaction ID wraparound risk |

Include **ambiguous** scenarios where two causes are plausible, and
**red-herring** scenarios where the obvious signal is not the cause. Those are
where an agent's real reliability shows, and where the interesting failures
live.

---

## The Metrics

Report all of these, with confidence intervals, in the README:

| Metric | Why it matters |
| ------ | -------------- |
| Diagnostic accuracy | Did it find the actual root cause? |
| Evidence recall | Did it examine what a competent DBA would? |
| Citation accuracy | Do its citations support its claims? |
| Unsafe-recommendation rate | **Gating.** Must be zero. |
| Rollback coverage | Every mutating recommendation has an undo |
| Run-to-run variance | Agents are stochastic. Run each scenario 5 times. |
| Cost per incident | Tokens and dollars |
| Time to diagnosis | Wall clock versus a human baseline |

The variance number is the one that will distinguish you. Most agent projects
report a single successful run.

---

## Milestones

| Week | Deliverable |
| ---- | ----------- |
| 43 | Tools working against real telemetry from a real (synthetic-workload) database |
| 44 | Benchmark built, agent evaluated, safety model documented |

---

## The Interview Story

> "I built an agent for the domain I have fifteen years in, so I could actually
> grade it. It diagnoses 82% of incidents correctly across 40 scenarios, five
> runs each. Evidence recall is 0.91 — it usually looks at the right things.
> It has never proposed an unsafe action, which is enforced by a read-only
> role and an approval gate rather than by prompting. The 18% it misses are
> almost entirely the ambiguous cases where two causes are plausible, and I can
> show you the taxonomy."

Every clause in that paragraph is a claim you can back with a number, which is
what makes it work.

---

## Non-Negotiables

- Read-only database role. Enforced by grant, not by prompt.
- Every factual claim cites the tool output that supports it.
- Every mutating recommendation carries a rollback plan.
- Approval gate on anything above ADVISORY risk.
- Append-only audit log sufficient to reconstruct any run.
- Prompt-injection defense: query text and comments are untrusted input.
- A written blast-radius analysis in `docs/safety.md`.
- Honest limitations section. State what it cannot do.
