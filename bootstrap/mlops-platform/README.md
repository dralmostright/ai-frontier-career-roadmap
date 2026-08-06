# mlops-platform

**Weeks 53-60 · Months 14, 15 · Capstones: Full MLOps Pipeline, Production AI Cluster**

Train, evaluate, register, deploy, monitor. The phase where fifteen years of
production operations stops being background and becomes the differentiator.

---

## Why This Lab Exists

Most ML engineers are visibly weak here. They can train a model and cannot tell
you their rollback procedure, their error budget, or what page fires when
quality degrades. You can, because you have been on call.

Months 14-15 are where you should score highest in this entire course, and
where a system design interview should feel like describing your day job with
different nouns.

The one thing to guard against: assuming the ML-specific parts are the same as
the systems parts. They are not. A model does not fail loudly — it degrades
silently while returning 200s. That difference is the whole subject.

---

## Layout

```text
mlops-platform/
  src/
    tracking.py    W53  experiment records, lineage
    registry.py    W54  model versioning, staging, promotion, rollback
    pipeline.py    W55  train -> eval -> gate -> register -> deploy
    monitoring.py  W56  quality, drift, and system metrics
    drift.py       W56  data and prediction drift detection
    serving.py     W57-59  the production service
    workers.py     W59  async batch inference
  infra/
    docker/        W57  hardened images
    k8s/           W58  manifests, probes, HPA, resources
    github/        W55  CI/CD workflows
    runbooks/      W60  what to do at 3am
  tests/
```

---

## What Makes ML Ops Different

The table to have ready for a system design interview:

| | Traditional service | ML service |
| --- | --- | --- |
| Failure mode | Loud: 500s, timeouts | **Silent: confident wrong answers** |
| Correctness | Deterministic, testable | Statistical, only measurable in aggregate |
| Regression detection | Unit tests catch it pre-merge | Needs an eval set and a quality gate |
| Rollback unit | Code version | Code **and** model **and** data version |
| Degradation cause | Code change | Code change, or the world changed |
| Latency profile | Stable | Varies with input size and content |
| Cost | Roughly fixed per request | Varies per request; can be 100x |

The silent-failure row is the whole reason drift monitoring exists. A model
whose accuracy has fallen from 92% to 71% returns HTTP 200 for every request
and no conventional alert fires.

---

## The Metrics That Matter

**System** — you already know these: request rate, error rate, p50/p95/p99
latency, saturation, queue depth.

**Model** — the ones most teams do not have:

| Metric | Catches |
| ------ | ------- |
| Prediction distribution | The model's output shifting without an input change |
| Confidence distribution | Growing uncertainty before accuracy visibly drops |
| Input feature drift (PSI, KL) | The world changing under the model |
| Delayed ground-truth accuracy | Actual quality, whenever labels arrive |
| Refusal / fallback rate | Retrieval or upstream breakage |
| Token usage and cost per request | Budget, and prompt-injection attempts |

**The alert that matters most** is not "accuracy dropped" — you usually cannot
know that in real time. It is "the prediction distribution moved more than N
standard deviations from the training baseline," which is available
immediately and is a leading indicator.

---

## The Quality Gate

Week 55's deliverable, and the single most valuable thing in this lab.

A CI job that runs the eval suite on every PR touching model code, compares
against the current production baseline, and **fails the build** on a
regression beyond threshold.

```yaml
# infra/github/eval-gate.yml
- run: python -m src.pipeline evaluate --baseline production
  # exits non-zero if faithfulness drops > 2% or p95 latency rises > 20%
```

Most teams do not have this. Having it — with a CI log showing it catching a
real regression — is a concrete, verifiable artifact that separates your
portfolio from a folder of notebooks.

---

## Milestones

| Week | You can... |
| ---- | ---------- |
| 53 | Say what belongs in an experiment record, and reproduce a run from it |
| 54 | Roll back a bad model in under five minutes, and prove it |
| 55 | Block a regressing PR automatically |
| 56 | Detect drift before users report a problem |
| 57 | Ship a hardened image under 1GB |
| 58 | Set correct requests/limits and probes for an inference pod |
| 59 | Run async batch inference over a large corpus |
| 60 | Hand someone a runbook and have them resolve an incident without you |

---

## Week 60: The Induced Failure

The exercise that produces your best interview story.

Break your own system on purpose. Deploy a deliberately bad model. Watch what
fires and what does not. Execute the rollback and time it. Then write the
postmortem — blameless, with a timeline, contributing factors, and action
items.

Put that postmortem in the repository. No other candidate will have one, and
it is unmistakably the work of someone who has done this for real.

---

## Interview Drills

| Week | Drill |
| ---- | ----- |
| 53 | What belongs in an experiment record? Why each field? |
| 54 | A model is misbehaving at 2am. Walk me through the rollback. |
| 55 | What tests gate a model deployment? Which are ML-specific? |
| 56 | Design alerting for a production LLM feature. What pages, what emails? |
| 57 | Your image is 8GB. Get it under 1GB. |
| 58 | Requests vs limits for a GPU inference pod. What happens if you get it wrong? |
| 59 | Design batch inference over 100M documents. Include cost and failure recovery. |
| 60 | Write the postmortem for an LLM outage. |
