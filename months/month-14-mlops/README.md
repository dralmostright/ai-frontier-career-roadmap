# Month 14: MLOps

**Weeks 53-56 · Phase 5: AI Systems Engineering · Lab: `bootstrap/mlops-platform/`**

---

## The Month In One Sentence

Apply the operational discipline you already have to a class of system that fails silently.

## Why This Month Exists

**This should be your highest-scoring month in the entire course.**

Experiment tracking is configuration management. A model registry is artifact
versioning with a promotion workflow. Rollback is rollback. Monitoring, alerting,
SLOs, error budgets, and runbooks are your professional native language.

The one genuinely new thing — and it is the thing that makes ML ops different —
is that **ML systems fail silently**. A model whose accuracy has fallen from 92%
to 71% returns HTTP 200 for every request. Nothing in a conventional monitoring
stack notices. Everything in Week 56 exists to make that failure visible.

The interview leverage here is large and underused. Most ML engineers cannot
describe their rollback procedure, their error budget, or what pages at 3am. You
can. Make sure the portfolio shows it.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 53 | Experiment Tracking | `tracking.py` — a real experiment record with lineage |
| 54 | Model Registry and Versioning | `registry.py` — versioning, promotion, and a timed rollback |
| 55 | CI/CD for ML | `.github/workflows/` — including the quality gate |
| 56 | Monitoring and Drift | `monitoring.py`, `drift.py`, dashboards, and the alert set |

**Capstone:** Full MLOps Pipeline — train → evaluate → gate → register → deploy → monitor, wired together, with a quality gate that has caught a real regression.

## The Through-Lines

**Silent failure is the defining difference.** Design monitoring for a system
whose failure mode is confident wrongness.

**A model version is not just weights.** Weights plus code plus data plus config
plus eval results. Rolling back weights alone can leave a model that no longer
matches its serving path.

**The quality gate is the artifact.** A CI job that blocks a regressing PR is the
single most valuable piece of ML infrastructure most teams do not have.

**Test the rollback.** An untested rollback is an untested code path, and it will
fail exactly when you are least able to debug it.

## Time and Compute

15-20 hours per week. No GPU. Docker for the service stack. `make services-up` brings up MLflow, Prometheus, and Grafana.

## Files

```text
month-14-mlops/
  README.md      you are here
  week-53.md     experiment tracking
  week-54.md     model registry and versioning
  week-55.md     ci/cd for ml
  week-56.md     monitoring and drift
  capstone.md    full mlops pipeline
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 55.** The quality gate is the month's most distinctive artifact. Week 53 can be compressed since Week 20 covered much of it.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Versioning weights only | Rollback produces a model that does not match its code | Version code, data, config, and eval results together. |
| Untested rollback | Fails at 2am, when you need it | Test it on a schedule. Time it. |
| Alerting on causes, not symptoms | Pages nobody acts on | Alert on what users feel. CPU is a dashboard, not a page. |
| No quality gate | Regressions ship | Eval in CI, blocking on threshold breach. |
| Drift alerts with no action | Dashboard ignored within two weeks | Every alert needs a runbook and a decision. |
| Statistical significance as the alert condition | Constant firing at scale | Alert on effect size, not p-value. |

## Advancement

Before Month 15, you should be able to, without notes:

- [ ] Say what belongs in an experiment record and why each field
- [ ] Walk through a model rollback at 2am, from alert to resolution
- [ ] Name the tests that should gate a model deployment
- [ ] Design alerting for a production LLM feature, distinguishing pages from tickets
- [ ] Explain why ML systems fail silently and what you monitor because of it
- [ ] Point at a pipeline where a quality gate caught a real regression

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 15 — Kubernetes AI Platform. Deploy the whole stack and be the person on call for it.
