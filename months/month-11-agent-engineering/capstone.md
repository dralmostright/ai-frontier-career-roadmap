# Month 11 Capstone: Autonomous DBA Assistant

## Objective

Build an agent that ingests PostgreSQL telemetry, diagnoses performance
incidents, explains its reasoning with cited evidence, and recommends
remediations classified by risk — and then grade it honestly against a
purpose-built benchmark.

**This is the most important project in the course.** Treat it accordingly.

## Business Problem

Database performance incidents are expensive, and diagnosis is a bottleneck:
the people who can read a query plan and a lock chain are few and they are
usually asleep when it matters.

An agent that can do the first thirty minutes of triage — gather the telemetry,
form hypotheses, cite evidence, and hand a human a ranked set of candidate causes
with proposed fixes — is genuinely valuable, and it is valuable precisely because
a wrong answer is dangerous. That tension is what makes the safety work
interesting rather than decorative.

Be honest about the scope in the README: this triages, it does not fix. The human
stays in the loop by design, not by limitation.

## Technical Requirements

- Telemetry collectors for slow queries, index usage, table stats, locks, bloat,
  connections, replication, and configuration
- Narrow, typed, risk-classified tools with instructive errors
- An agent loop with step, token, and cost budgets and no-progress detection
- Hypothesis generation that seeks disconfirming evidence
- **Every claim cites the tool output supporting it**, validated in code
- Risk-classified recommendations, each with a rollback plan
- Approval gate for anything above ADVISORY
- Append-only audit log sufficient to reconstruct any run
- Prompt injection defense, architecturally documented
- **A benchmark of 30-50 reproducible incidents with known root causes**
- Evaluation at five runs per scenario, with variance reported
- A blast-radius analysis

## Theory Requirements

The README and design docs must explain:

1. The tool design principles and why each constraint exists.
2. The safety architecture, **without relying on the word 'prompt'** — read-only
   grants, approval gates, audit, and injection defense are structural.
3. How the benchmark was constructed and why the ground truth is trustworthy.
4. Why you report variance across runs.
5. What the agent should not be used for.

## System Design Requirements

- Read-only database role, granted `SELECT` on the stats views and nothing else
- Telemetry collection separate from reasoning separate from recommendation
- Structured diagnosis output with evidence IDs
- Approval gate as a separate component that the agent cannot bypass
- Audit log written before the action, not after
- Benchmark scenarios as data (YAML), not code

## Implementation Plan

**Days 1-2** — Telemetry and tools against a real database with a synthetic
workload.

**Day 3** — The agent loop with the diagnosis framework.

**Days 4-5** — The benchmark. 30-50 scenarios. The bulk of the value.

**Day 6** — Safety: approval gate, audit, injection defense, blast radius.

**Day 7** — The full evaluation run, five per scenario, and the write-up.

If you need an eighth day, take it from Month 12. This project is worth more.

## Evaluation Plan

| Metric | Target |
| ------ | ------ |
| Diagnostic accuracy | > 75%, with a CI, across 30-50 scenarios × 5 runs |
| Accuracy by difficulty | Reported separately for easy / medium / ambiguous |
| Evidence recall | > 0.85 — did it look at what a competent DBA would? |
| Citation accuracy | > 0.90 |
| **Unsafe recommendations** | **Zero. This is gating, not a target.** |
| Rollback coverage | 100% of mutating recommendations |
| Run-to-run variance | Reported; scenarios with high variance flagged |
| Cost per incident | Measured |
| Time to diagnosis | Compared against a human baseline (time yourself) |

## Expected Repository Structure

```text
autonomous-dba-agent/
  README.md
  docker-compose.yml
  pyproject.toml
  Makefile
  src/dba_agent/
    agent.py  telemetry.py  diagnosis.py  recommendations.py  prompts.py
    tools/
      queries.py  indexes.py  locks.py  config.py  replication.py
    safety/
      classify.py  approval.py  audit.py  injection.py
  evals/
    scenarios/*.yaml       the benchmark
    generate.py  run_eval.py
    results/
      accuracy.json  variance.json  failures.md
  tests/
  docs/
    design.md
    safety.md              risk model, gates, blast radius, red-team results
    evaluation.md          benchmark construction and results
    limitations.md
    runbook.md             what to do when the agent is wrong
```

## README Requirements

Above the fold: one sentence, **the accuracy number with its confidence
interval**, the zero-unsafe-recommendations claim, and a demo GIF of the agent
diagnosing an incident.

Then:

- **The problem** — why database triage is a bottleneck
- **Architecture diagram**
- **Results table** — accuracy by difficulty, evidence recall, citation accuracy,
  safety, variance, cost
- **The benchmark** — how it was built, why the ground truth is trustworthy, the
  incident taxonomy
- **Safety architecture** — read-only grants, risk classification, approval
  gates, audit, injection defense, blast radius. **This section is the
  differentiator.**
- **The failure taxonomy** — where it fails and why, by category
- **Red-team results** if you did the stretch
- **What this should not be used for**
- **Interview talking points**

Lead with the number and the safety claim. The combination — measured accuracy
*and* a real safety architecture — is what no other agent project has.

## Demo Requirements

A recorded 3-minute walkthrough: inject an incident, run the agent, show it
gathering telemetry, forming hypotheses, citing evidence, and producing a
risk-classified recommendation that requires approval. Then show the audit log
reconstructing the run.

Also `make demo` for a text version.

## Blog Post Requirement

**Post #4 is due this month, and it is the highest-value post in the plan.**

Working title: "I Built an AI Agent for the Domain I Know Best. Here's Where It
Failed."

The angle nobody else can write: a domain expert honestly assessing an agent in
their own field, with a benchmark, an accuracy number, and a specific account of
the failure modes. Lead with the failures. An honest negative-tinged post from
someone with real expertise gets shared by exactly the people who hire.

## Interview Story

> "I built an agent for the domain I've worked in for fifteen years, so I could
> actually grade it. It diagnoses 82% of incidents correctly across 40 scenarios,
> five runs each — and I report the variance, because three-out-of-five isn't
> 60% accuracy, it's unreliability. Evidence recall is 0.91. It has never
> proposed an unsafe action, which is enforced by a read-only grant and an
> approval gate rather than by prompting. The 18% it misses are almost all the
> ambiguous cases where two causes are plausible, and I can show you the
> taxonomy."

90 seconds. Every clause is a claim you can back with data. This is the story
that gets you the interview.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 11 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 9 | A real problem you have lived. |
| Technical execution | 9 | Tools, loop, diagnosis, safety — all of it working. |
| Evaluation rigor | 10 | **Target 10.** The benchmark with variance is the whole point. |
| Code quality | 8 | Clean separation, tested, safety components isolated. |
| Documentation | 10 | **Target 10.** The safety document is unique. |
| Reproducibility | 9 | The benchmark must be rerunnable by someone else. |
| Error analysis | 10 | **Target 10.** The failure taxonomy is the credibility. |
| Portfolio readiness | 10 | **Flagship #1.** Top of the resume. |

**Overall target: 9.0+. This is the flagship. Anything below 9 gets another week.**

## Stretch Goals

1. **Red-team write-up.** Injection attempts in SQL comments and table names,
   what worked, and what you changed. Nearly unheard of in an agent project.
2. **A non-LLM baseline.** Rule-based heuristics on the same benchmark. If the
   baseline wins on some scenario classes, say so — that is a finding, and it is
   the kind of honesty that makes the rest believable.
3. **MCP server.** Expose the tools; make them usable from any client.
4. **Oracle collectors** alongside PostgreSQL, broadening the claim.
5. **The configuration ablation** — reflection on/off, model size, tool set, step
   budget — as a table.

## Limitations To State Honestly

State these plainly and prominently:

- The benchmark is synthetic. Real incidents are messier, involve multiple
  simultaneous causes, and arrive with incomplete telemetry.
- Ground truth is established by the scenario generator, which means the agent is
  graded against the causes I chose to inject, not against the full space of
  database problems.
- 30-50 scenarios is a small benchmark. Confidence intervals are wide.
- The agent triages; it does not fix. Every mutating action requires a human.
- It has been tested against PostgreSQL only.
- Diagnostic accuracy on ambiguous scenarios is substantially lower than the
  headline number, and the headline number should not be quoted without the
  breakdown.
- Prompt injection defense is architectural and tested against the attacks I
  thought of. That is not the same as being secure.
