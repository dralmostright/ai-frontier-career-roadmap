# Month 15: Kubernetes AI Platform

**Weeks 57-60 · Phase 5: AI Systems Engineering · Lab: `bootstrap/mlops-platform/`**

---

## The Month In One Sentence

Deploy the whole stack to Kubernetes, then break it on purpose and write the postmortem.

## Why This Month Exists

The month that produces your best interview story.

Week 60's induced-failure exercise — deploy something bad deliberately, watch
what fires and what does not, execute the rollback, time it, and write the
blameless postmortem — is an artifact essentially no other candidate will have.
It is unmistakably the work of someone who has been on call.

The rest of the month is deployment engineering: hardened images, correct
resource requests and probes, async workers for batch inference, and horizontal
scaling. Familiar work with AI-specific wrinkles — model loading time makes
startup probes different, GPU resources are not divisible the way CPU is, and
inference pods have long warmup.

This month also assembles the **Database Incident Commander**: telemetry
ingestion plus RAG over runbooks plus the agent, deployed as one product. That is
Flagship #3.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 57 | Docker Hardening | Production images, small and reproducible |
| 58 | Kubernetes for AI Services | `infra/k8s/` — manifests for the whole stack |
| 59 | Scaling, Queues, and Batch Inference | `workers.py` — async batch inference at scale |
| 60 | Reliability and Incident Response | The Month 15 capstone, and **the postmortem** |

**Capstone:** Production AI Cluster — the RAG system and DBA agent deployed to Kubernetes as the Database Incident Commander, with SLOs, runbooks, and a real postmortem.

## The Through-Lines

**Liveness versus readiness.** Conflating them causes restart loops during a
transient dependency blip. For a model server with a 90-second load time, getting
the probes right is not optional.

**Resources are contracts.** Requests schedule, limits kill. For memory-heavy
inference the difference between them is the difference between throttling and
OOMKill.

**Queues absorb variance.** Async workers for batch inference decouple request
rate from processing rate.

**Test the failure path.** Week 60 is the month's point.

## Time and Compute

15-20 hours per week. kind or minikube locally. No cloud spend required. Docker Desktop or Colima needs several GB allocated.

## Files

```text
month-15-kubernetes-ai-platform/
  README.md      you are here
  week-57.md     docker hardening
  week-58.md     kubernetes for ai services
  week-59.md     scaling, queues, and batch inference
  week-60.md     reliability and incident response
  capstone.md    production ai cluster
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 60.** The induced failure and the postmortem. Do not skip it; it is the month's differentiator.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Liveness probe on a slow-starting model server | Restart loop, never becomes ready | Startup probe, or a generous initial delay. |
| No resource requests | Scheduler overcommits, pods OOMKill under load | Requests and limits, both, informed by measurement. |
| Building the image with the model baked in | 8GB image, slow deploys | Model from a volume or object store; image stays small. |
| No graceful shutdown | In-flight requests dropped on every deploy | preStop hook and a drain period. |
| Skipping the postmortem | The month's best artifact never gets written | Write it. It is the differentiator. |

## Advancement

Before Month 16, you should be able to, without notes:

- [ ] Get an 8GB image under 1GB and explain each reduction
- [ ] Set requests and limits for an inference pod and justify the numbers
- [ ] Explain liveness versus readiness for a slow-starting model server
- [ ] Design batch inference over 100M documents with failure recovery
- [ ] Write a blameless postmortem for an LLM outage
- [ ] Point at a deployed stack with runbooks and a real postmortem

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 16 — Paper Reproduction. Phase 6, and the research half of the portfolio.
