# Month 14 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 53 — Experiment Tracking

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 53.1 | Design the record schema | 1h | Medium |
| 53.2 | `ExperimentTracker` with full capture | 1.5h | Medium |
| 53.3 | Stand up MLflow | 1h | Easy |
| 53.4 | Log 10 real runs | 1.5h | Medium |
| 53.5 | `compare_runs` | 1h | Medium |
| 53.6 | Dataset hashing and lineage | 1.5h | Medium |
| 53.7 | `lineage` traversal | 1h | Medium |
| 53.8 | The six-months-later test | 45m | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 53.E1 | Wire tracking into the Month 13 distributed eval so every run is recorded | 2h | High |
| 53.E2 | Build a run-comparison report generator with significance tests | 2.5h | High — reuses Week 11 |
| 53.E3 | Set up DVC for the instruction dataset with a remote | 2h | Medium |

## Week 54 — Model Registry and Versioning

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 54.1 | `ModelVersion` with full provenance | 1h | Easy |
| 54.2 | `ModelRegistry.register` | 1h | Medium |
| 54.3 | `promote` with the eval gate | 1.5h | Medium |
| 54.4 | Single-production-version enforcement | 45m | Easy |
| 54.5 | **`rollback`** | 1.5h | Medium |
| 54.6 | Write the rollback runbook | 1h | Medium |
| 54.7 | **Test the rollback with a stranger** | 1h | Medium |
| 54.8 | `lineage` and `compare` | 1h | Medium |
| 54.9 | Shadow deployment | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 54.E1 | Canary deployment with an automated quality-based rollback trigger | 3h | **High** — the automated version of the 2am procedure |
| 54.E2 | Model version tagging on every prediction, traceable in logs | 2h | High |
| 54.E3 | A scheduled rollback drill that runs weekly in CI | 2h | **High** — nobody does this and it is exactly your instinct |

## Week 55 — CI/CD for ML

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 55.1 | The base CI workflow | 1h | Easy |
| 55.2 | Data validation tests | 1.5h | Medium |
| 55.3 | **The eval gate workflow** | 2.5h | Hard |
| 55.4 | Threshold selection | 1h | Medium |
| 55.5 | Fast subset versus full suite | 1h | Medium |
| 55.6 | Behavioral tests | 1.5h | Medium |
| 55.7 | **Catch a real regression** | 1.5h | Medium |
| 55.8 | Automated promotion on pass | 1h | Medium |
| 55.9 | Score against the ML Test Score rubric | 1h | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 55.E1 | Automated rollback triggered by a post-deploy quality signal | 3h | High |
| 55.E2 | A PR comment bot that posts the eval diff on every pull request | 2.5h | **High** — makes quality visible where decisions happen |
| 55.E3 | Data drift detection as a CI check on the training set | 2h | Medium |

## Week 56 — Monitoring and Drift

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 56.1 | **Design the metric set before reading examples** | 1.5h | Medium |
| 56.2 | `ModelMonitor` with real-time and batch tiers | 1.5h | Medium |
| 56.3 | `population_stability_index` | 1h | Medium |
| 56.4 | `kolmogorov_smirnov_test` and the significance trap | 1h | Medium |
| 56.5 | `embedding_drift` | 1h | Medium |
| 56.6 | `DriftDetector` with the baseline stored alongside the model version | 1.5h | Medium |
| 56.7 | `define_slos` | 1h | Medium |
| 56.8 | `alert_rules` | 1.5h | Medium |
| 56.9 | Grafana dashboards | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 56.E1 | Simulate a silent degradation and verify your monitoring catches it before the accuracy metric would | 2.5h | **Highest** — proves the leading indicator works |
| 56.E2 | Delayed ground truth pipeline: join labels as they arrive and backfill accuracy | 3h | High |
| 56.E3 | Automated drift-triggered retraining, with a human approval gate | 3h | High |

---

## If You Finish Early

Priority: Week 56's silent-degradation simulation (proves the leading indicator works), Week 54's scheduled rollback drill, Week 55's PR comment bot. All three are things your background makes obvious and nobody else's portfolio has.
