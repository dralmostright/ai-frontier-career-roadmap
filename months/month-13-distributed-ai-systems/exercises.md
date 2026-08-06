# Month 13 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 49 — GPU and CUDA Basics

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 49.1 | Derive the 16N rule | 45m | Medium |
| 49.2 | Build a memory calculator | 1.5h | Medium |
| 49.3 | Activation memory analysis | 1.5h | Medium |
| 49.4 | KV cache calculator | 45m | Easy |
| 49.5 | Gradient checkpointing measurement | 1.5h | Medium |
| 49.6 | Arithmetic intensity | 1.5h | Hard |
| 49.7 | Batch size sweep at inference | 1h | Medium |
| 49.8 | The technique comparison table | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 49.E1 | Profile a training step with torch.profiler and attribute time to compute, memory, and overhead | 3h | **High** — the Horace He framing, applied |
| 49.E2 | Write a simple CUDA kernel via Triton and compare against PyTorch | 3h | High — demystifies the layer below |
| 49.E3 | Model the cost of training a 7B model on rented GPUs, end to end | 2h | High — a concrete number to quote |

## Week 50 — Distributed Training Concepts

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 50.1 | Write the reference document | 3h | Hard |
| 50.2 | Compute memory for each ZeRO stage | 1h | Medium |
| 50.3 | Communication cost analysis | 1.5h | Hard |
| 50.4 | Run DDP locally on CPU | 1.5h | Medium |
| 50.5 | Pipeline bubble calculation | 1h | Medium |
| 50.6 | Checkpointing frequency analysis | 1h | Medium |
| 50.7 | Read the OPT logbook | 1.5h | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 50.E1 | Run FSDP on two local processes and verify parameter sharding | 3h | High — makes ZeRO-3 concrete |
| 50.E2 | Simulate straggler impact: inject delay into one worker, measure wall-clock | 2h | High |
| 50.E3 | Model the cost/time tradeoff for training a 7B model across cluster sizes | 2h | High — a concrete planning artifact |

## Week 51 — Ray for AI Workloads

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 51.1 | Ray tasks and actors | 1h | Easy |
| 51.2 | Shard the evaluation work | 1.5h | Medium |
| 51.3 | Retries with backoff | 1h | Medium |
| 51.4 | Failure isolation | 1.5h | Medium |
| 51.5 | Distributed rate limiting | 1.5h | Hard |
| 51.6 | Cost accounting across workers | 1h | Medium |
| 51.7 | Resumability | 1h | Medium |
| 51.8 | **The scaling curve** | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 51.E1 | Straggler mitigation: speculative re-execution of slow items | 2.5h | High |
| 51.E2 | Ray Data pipeline for a streaming evaluation over a large corpus | 2.5h | High |
| 51.E3 | Add a cost budget that halts the job when exceeded | 1.5h | **High** — a genuinely useful guardrail |

## Week 52 — Performance Profiling

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 52.1 | Profile a training step | 1.5h | Medium |
| 52.2 | Find and fix a synchronization stall | 1h | Medium |
| 52.3 | Profile inference: prefill vs decode | 1.5h | Medium |
| 52.4 | Measure tokenization overhead | 45m | Easy |
| 52.5 | The p99 investigation | 1.5h | Hard |
| 52.6 | INT8 quantization | 1.5h | Medium |
| 52.7 | `torch.compile` | 1h | Medium |
| 52.8 | Try vLLM | 1.5h | Medium |
| 52.9 | **The optimization** | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 52.E1 | Implement continuous batching and compare against static batching | 3h | **High** — the core of modern LLM serving |
| 52.E2 | INT4 quantization with the full quality/size/speed table | 2h | High |
| 52.E3 | Build a latency attribution dashboard broken down by stage | 2.5h | High — feeds Week 56 |

---

## If You Finish Early

Priority: Week 52's continuous batching (the core of modern serving), Week 49's profiler attribution exercise, Week 51's cost budget guard. All three are directly useful in Month 15.
