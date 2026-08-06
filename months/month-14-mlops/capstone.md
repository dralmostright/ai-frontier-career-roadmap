# Month 14 Capstone: Full MLOps Pipeline

## Objective

Build the pipeline that turns a model into an operated system: tracked experiments, a versioned registry with tested rollback, CI with a quality gate, and production monitoring designed for silent failure.

## Business Problem

The Month 10 RAG system and Month 11 agent both work and neither is operable.
There is no way to tell whether a change made them worse, no way to roll back a
bad deploy, and no signal if quality degrades in production.

That is the actual state of most deployed ML systems, and closing it is what this
month is for. Frame the README that way: this is the operational layer that most
AI projects never get.

## Technical Requirements

- Experiment tracking with full lineage: data, code, config, cost
- A model registry with staged promotion and an eval gate on production
- **A tested, timed rollback** with a runbook a stranger can follow
- CI: lint, types, unit, integration, data validation
- **A quality gate that blocks a regressing PR**, with a CI log proving it
- Behavioral tests: invariance, directional, minimum functionality
- Production monitoring: system, model, cost, and quality metrics
- Drift detection with the baseline versioned alongside the model
- SLOs with error budgets, including a quality SLO
- Alerts where every page has a runbook
- Grafana dashboards readable at 3am

## Theory Requirements

The README must explain:

1. Why ML systems fail silently and what you monitor because of it.
2. Why a model version must include code, data, and config.
3. How the regression threshold was chosen, from the eval's confidence interval.
4. Which alerts page and which ticket, and the reasoning.

## System Design Requirements

- Pipeline stages as independently runnable steps
- Registry as the single source of truth for what is deployed
- Monitoring baselines stored with the model version
- Runbooks in the repository, next to the code they describe
- Everything reproducible from config

## Implementation Plan

**Day 1** — Tracking and lineage across existing runs.

**Day 2** — Registry, promotion, and the rollback. Time it.

**Day 3** — CI pipeline and data validation.

**Day 4** — The quality gate. Then break something and prove it catches it.

**Day 5** — Monitoring, drift, and dashboards.

**Day 6** — SLOs, alerts, runbooks.

**Day 7** — README, and the induced-failure exercise if you are doing it now
rather than in Week 60.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Every run traceable to data, code, config | Yes, verified by a lineage test |
| Rollback time | Measured; target under 5 minutes |
| Rollback executed by someone else from the runbook | Yes, and note what they got stuck on |
| Quality gate catches a real regression | **Yes, with the CI log** |
| Drift detection catches a simulated shift | Yes, with the detection lag measured |
| Every alert has a runbook | 100% |
| Dashboards | Two, readable, with the SLO burn visible |

## Expected Repository Structure

```text
ml-reliability-platform/
  README.md
  Makefile
  pyproject.toml
  .github/workflows/
    ci.yml  eval-gate.yml  nightly.yml  rollback-drill.yml
  src/platform/
    tracking.py  registry.py  pipeline.py  monitoring.py  drift.py  validate.py
  infra/
    grafana/  prometheus/  runbooks/
  tests/
    unit/  integration/  behavioral/  data/
  docs/
    design.md  slos.md  runbooks.md  incident_response.md  limitations.md
```

## README Requirements

Above the fold: one sentence, **the CI log screenshot showing the quality gate
catching a regression**, and the measured rollback time.

Then: why ML systems fail silently; architecture diagram; the pipeline stages;
the quality gate with its threshold derivation; the registry and rollback with
the measured time; the monitoring metric set and why each metric; the SLOs and
error budgets; the alert catalogue with page-versus-ticket reasoning; the
runbooks; limitations.

**Lead with the caught regression.** It is proof rather than description, and it
is the thing most ML projects cannot show.

## Demo Requirements

`make demo` runs the full pipeline: trains, evaluates, gates, registers, deploys to a local service, sends traffic, and shows the dashboards. Then `make demo-regression` pushes a degraded model and shows the gate blocking it.

## Blog Post Requirement

**Post #5 is due this month.** Working title: "SLOs for LLM Systems: Applying
Database Reliability Practice to AI."

This is the post only you can write. Error budgets, quality SLOs, blameless
postmortems, and runbooks applied to a system whose failure mode is confident
wrongness. The ML audience has not internalized this framing and the SRE audience
has not applied it here.

## Interview Story

> "The eval gate blocks any PR that drops faithfulness by more than two points.
> It's caught three regressions so far — here's the CI log for one of them, a
> chunking change that looked harmless. Rollback is under four minutes and I've
> had someone who didn't build the system execute it from the runbook."

45 seconds, and both claims are verifiable.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 14 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 9 | The silent-failure framing is correct and well-argued. |
| Technical execution | 8 | Every stage working and wired together. |
| Evaluation rigor | 9 | **The quality gate with a caught regression.** |
| Code quality | 8 | Clean, tested, config-driven. |
| Documentation | 9 | Runbooks and SLOs. Your strongest documentation of the course. |
| Reproducibility | 9 | `make demo` runs the whole thing. |
| Error analysis | 8 | Failure modes and the incident response document. |
| Portfolio readiness | 9 | **Flagship #8.** Infrastructure managers will notice this one. |

**Overall target: 8.5+. This should be one of your best-scoring capstones.**

## Stretch Goals

1. **The scheduled rollback drill** running weekly in CI.
2. **Automated rollback** triggered by a post-deploy quality signal.
3. **The PR comment bot** posting eval diffs.
4. **Delayed ground truth** pipeline with accuracy backfill.

## Limitations To State Honestly

- Single-environment. A real setup would have dev, staging, and production with
  separate registries.
- The quality gate uses a fast subset on PRs; a subtle regression could pass and
  be caught only by the nightly full run.
- Drift thresholds are conventional values, calibrated on limited history.
- Ground truth for the quality SLO is delayed and partial.
- Runbooks are tested by one other person, which is better than zero and less
  than a real on-call rotation.
