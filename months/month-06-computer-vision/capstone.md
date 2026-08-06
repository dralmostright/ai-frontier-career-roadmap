# Month 06 Capstone: Image Classification Service

## Objective

Ship a model. Train a classifier, serve it behind FastAPI, containerize it, and measure its latency properly — percentiles, batching curve, and saturation point.

## Business Problem

Pick something with a plausible use: defect detection on a manufacturing
dataset, plant disease classification, or document type classification. Avoid
generic CIFAR-10 — a stated use case lets you reason about the cost of errors,
which is what makes the threshold and latency decisions meaningful.

State in the README who uses this, what decision the prediction drives, and what
a false positive and a false negative each cost.

## Technical Requirements

- A trained model (fine-tuned pretrained backbone is fine and realistic)
- FastAPI service: `/predict`, `/predict/batch`, `/health`, `/ready`, `/metrics`
- Warmup at startup
- Dynamic batching with a configurable window
- Containerized, multi-stage build, image size reported and minimized
- Latency: p50/p95/p99 under load, not a single-threaded timing
- The latency-versus-batch-size curve, with the throughput knee identified
- A load test finding the saturation point
- A model card: intended use, out-of-scope use, metrics overall and by slice, limitations
- Tests, including a test that batched and single inference agree

## Theory Requirements

The README must explain:

1. Why you chose this architecture, including the CNN-versus-ViT reasoning for
   your data scale.
2. What warmup is and why the first requests are slow.
3. The batching tradeoff, with your measured numbers.
4. Why you report percentiles rather than the mean.

## System Design Requirements

- Separate model loading from request handling
- Async request handling with a batching queue
- Health versus readiness, correctly distinguished
- Prometheus metrics: request rate, latency histogram, batch size distribution
- Graceful shutdown that drains in-flight requests

## Implementation Plan

**Days 1-2** — Train the model. Reuse the Month 5 pipeline; do not rebuild it.

**Day 3** — The service, with warmup.

**Day 4** — Dynamic batching. This is the interesting engineering.

**Day 5** — Measurement: percentiles, the batching curve, the load test.

**Day 6** — Containerize, model card, README.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Model accuracy | Stated, with a baseline comparison |
| p99 latency, batch 1 | Measured and reported |
| Throughput at the knee | Measured; report the batch size |
| Batched vs single predictions | Identical, verified by a test |
| Container image | Under 1.5GB, size reported |
| Saturation point | Found by load test |
| `docker compose up` from a clean clone | Works |

## Expected Repository Structure

```text
image-classification-service/
  README.md
  Dockerfile
  docker-compose.yml
  pyproject.toml
  Makefile
  src/service/
    api.py
    inference.py
    batching.py
    metrics.py
  src/training/
    train.py
    export.py
  tests/
  loadtest/
    locustfile.py
  docs/
    model_card.md
    design.md
    latency.md
    limitations.md
```

## README Requirements

Above the fold: one sentence, the latency table (p50/p95/p99 and throughput),
and `docker compose up`.

Then: the problem and error costs; architecture diagram; the latency-versus-batch
curve; the saturation point; key decisions with rejected alternatives; the model
card link; limitations.

**Lead with the latency table.** Accuracy on a vision dataset impresses nobody;
a measured p99 and a batching curve show you have deployed something.

## Demo Requirements

`docker compose up` then `make demo` posts ten images and prints predictions with per-request latency, followed by a batched run showing the throughput difference.

## Blog Post Requirement

Optional. If written, the angle is the batching measurement: 'Dynamic Batching Took My Inference Service from 12 to 180 Requests Per Second.' Concrete, useful, and it has a number in the title.

## Interview Story

> "Throughput went from 12 to 180 requests a second when I added dynamic
> batching, at the cost of about 8ms of added p50 latency. Here's the curve, and
> here's the batch size where the GPU saturates."

30 seconds, and the numbers do the work.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 6 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 7 | A stated use case with error costs. |
| Technical execution | 8 | Batching is the interesting part. |
| Evaluation rigor | 8 | Percentiles, curve, saturation point. |
| Code quality | 8 | Service and training cleanly separated. |
| Documentation | 8 | Latency table above the fold; model card present. |
| Reproducibility | 8 | `docker compose up` works. |
| Error analysis | 7 | Misclassification review plus slice analysis. |
| Portfolio readiness | 7 | First deployed artifact. Medium weight. |

**Overall target: 7.5+, with the latency measurement genuinely rigorous.**

## Stretch Goals

1. **INT8 quantization** with the full tradeoff table. Real, concrete, previews
   Week 52.
2. **ONNX Runtime comparison** against native PyTorch.
3. **A simple web UI** for the demo. Cheap, and it makes the README GIF possible.
4. **Autoscaling on queue depth** with docker compose replicas.

## Limitations To State Honestly

- Single-node, single-GPU. No horizontal scaling or model sharding.
- Batching adds latency to every request; the window is a fixed tradeoff.
- No authentication, rate limiting, or input validation beyond image decoding.
- The model is fine-tuned on a modest dataset and will not generalize outside it.
