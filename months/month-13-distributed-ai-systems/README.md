# Month 13: Distributed AI Systems

**Weeks 49-52 · Phase 5: AI Systems Engineering · Lab: `bootstrap/mlops-platform/`**

---

## The Month In One Sentence

Learn to reason quantitatively about GPUs, distributed training, and inference cost — then build an evaluation pipeline that scales.

## Why This Month Exists

Phase 5 is your home phase, and it is placed here deliberately: you arrive with
enough ML context to make infrastructure decisions meaningfully rather than
generically.

An AI Infrastructure Engineer who understands attention's memory profile is worth
several who do not. This month is where those two halves join.

The specific interview leverage: the memory arithmetic. "How much memory to train
a 7B model?" has a mechanical answer (16 bytes per parameter for Adam in fp32,
before activations — about 112GB) and that single calculation is the reason ZeRO,
LoRA, and 8-bit optimizers exist. Being able to produce it on demand, and then
explain what each technique does to it, is a strong signal.

The cost dimension is yours too. Engineers who track dollars per evaluation run
are rare and immediately trusted with budgets.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 49 | GPU and CUDA Basics | The memory and throughput arithmetic, worked and verified |
| 50 | Distributed Training Concepts | `docs/distributed_training.md` — the reference document |
| 51 | Ray for AI Workloads | `distributed_eval.py` — parallel evaluation with retries and cost accounting |
| 52 | Performance Profiling | A profiling report with a measured optimization |

**Capstone:** Distributed Evaluation Pipeline — a Ray-based system that evaluates LLM and RAG outputs in parallel, with failure isolation, cost accounting, and a scaling analysis.

## The Through-Lines

**Arithmetic before architecture.** Memory, FLOPs, and bandwidth numbers first;
design decisions follow from them.

**Profile before optimizing.** Week 18's loader-bottleneck lesson, at cluster
scale.

**Cost is a first-class metric.** Dollars per run, tracked from Week 51 onward.

**Failure is normal at scale.** Nodes die, jobs preempt, workers hang. Designing
for that is ordinary distributed-systems work and it is where you are strong.

## Time and Compute

15-20 hours per week. No large cluster needed. Ray runs locally across CPU cores; the distributed evaluation capstone is CPU-and-API-bound, not GPU-bound. Week 49-50 are largely analytical.

## Files

```text
month-13-distributed-ai-systems/
  README.md      you are here
  week-49.md     gpu and cuda basics
  week-50.md     distributed training concepts
  week-51.md     ray for ai workloads
  week-52.md     performance profiling
  capstone.md    distributed evaluation pipeline
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 49.** The arithmetic underpins everything else in Phase 5 and it is the most directly examined. Week 51 can be compressed if Ray is already familiar.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Guessing at memory instead of computing it | Surprise OOM at hour three | 16 bytes per parameter for Adam fp32. Derive it every time. |
| Optimizing before profiling | Effort spent on the wrong bottleneck | Measure. The bottleneck is rarely where you expect. |
| No cost tracking | Cannot answer 'what did that cost?' | Log tokens and dollars per unit of work from day one. |
| Ignoring stragglers | Wall clock set by the slowest shard | Measure the distribution, not the mean. |
| No failure isolation | One bad input kills a 6-hour job | Per-item error capture. A crashed item is data, not a stop condition. |

## Advancement

Before Month 14, you should be able to, without notes:

- [ ] Compute training memory for a given model size and optimizer, from first principles
- [ ] Explain ZeRO stages 1, 2, and 3 and what each shards
- [ ] Explain data, tensor, and pipeline parallelism and when each applies
- [ ] Diagnose a p99/p50 latency gap systematically
- [ ] Report cost per unit of work for a distributed job
- [ ] Point at a distributed evaluation pipeline with a scaling and cost analysis

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 14 — MLOps. The operational discipline you already have, applied to models.
