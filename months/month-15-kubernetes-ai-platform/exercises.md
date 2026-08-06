# Month 15 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 57 — Docker Hardening

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 57.1 | Measure the naive image | 30m | Easy |
| 57.2 | Multi-stage build | 1.5h | Medium |
| 57.3 | Slim base and CPU wheels | 1h | Medium |
| 57.4 | Model weights out of the image | 1h | Medium |
| 57.5 | Layer ordering for cache | 45m | Easy |
| 57.6 | Non-root and read-only filesystem | 1h | Medium |
| 57.7 | Pin base image digests | 30m | Easy |
| 57.8 | Graceful shutdown | 1h | Medium |
| 57.9 | Vulnerability scan in CI | 1h | Medium |
| 57.10 | Document the reduction | 45m | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 57.E1 | Build a distroless image and measure the further reduction | 2h | High |
| 57.E2 | Reproducible builds: same source, byte-identical image | 3h | High — hard, and a strong claim |
| 57.E3 | Image signing with cosign and verification in the cluster | 2.5h | Medium |

## Week 58 — Kubernetes for AI Services

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 58.1 | Stand up a kind cluster | 1h | Easy |
| 58.2 | Deploy the RAG API | 1.5h | Medium |
| 58.3 | **Probes, correctly** | 1.5h | Hard |
| 58.4 | Resource requests and limits | 1.5h | Medium |
| 58.5 | Trigger an OOMKill deliberately | 45m | Easy |
| 58.6 | PersistentVolumeClaim for model weights | 1h | Medium |
| 58.7 | Postgres in-cluster or as an external service | 1h | Medium |
| 58.8 | HorizontalPodAutoscaler | 1.5h | Medium |
| 58.9 | Rolling update with graceful drain | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 58.E1 | Queue-depth autoscaling with KEDA | 2.5h | **High** — the right signal for inference |
| 58.E2 | Set up a GPU node in kind (or document the real-cluster equivalent) | 2h | Medium |
| 58.E3 | Helm chart for the whole stack | 2.5h | High — makes it genuinely deployable by someone else |

## Week 59 — Scaling, Queues, and Batch Inference

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 59.1 | Queue and worker skeleton | 1.5h | Medium |
| 59.2 | Idempotent processing | 1h | Medium |
| 59.3 | Retries and dead-letter | 1.5h | Medium |
| 59.4 | Checkpointing | 1h | Medium |
| 59.5 | Backpressure | 1h | Medium |
| 59.6 | Progress tracking | 45m | Easy |
| 59.7 | **Cost estimation** | 1h | Medium |
| 59.8 | Worker autoscaling on queue depth | 1.5h | Medium |
| 59.9 | Run it on a real corpus | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 59.E1 | Continuous batching in the serving layer; compare against static | 3h | **High** — Week 52's stretch, deployed |
| 59.E2 | Priority queues: interactive requests preempt batch work | 2.5h | High — a real multi-tenancy requirement |
| 59.E3 | Spot-instance tolerance: handle worker preemption mid-item | 2.5h | High — the cost lever for batch work |

## Week 60 — Reliability and Incident Response

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 60.1 | Define SLIs and SLOs for the stack | 1.5h | Medium |
| 60.2 | Graceful degradation | 1.5h | Medium |
| 60.3 | Circuit breakers | 1h | Medium |
| 60.4 | Write four runbooks | 2h | Medium |
| 60.5 | Assemble the Incident Commander | 2h | Hard |
| 60.6 | **Induce a failure** | 1.5h | Medium |
| 60.7 | **Respond to it** | 1h | Medium |
| 60.8 | **Write the postmortem** | 1.5h | Medium |
| 60.9 | Implement the action items | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 60.E1 | A second induced failure of a different class — data corruption rather than model quality | 2.5h | **High** — two postmortems is a pattern, not a stunt |
| 60.E2 | Chaos testing: randomly kill pods during a load test | 2h | High |
| 60.E3 | A game-day exercise with someone else responding from your runbooks | 3h | **Highest** — the real test of the documentation |

---

## If You Finish Early

Priority: Week 60's game day (the real test of the runbooks), Week 60's second postmortem, Week 59's priority queues. Phase 5 ends here — check Gate G5 before advancing to the research phase.
