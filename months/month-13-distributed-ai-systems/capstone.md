# Month 13 Capstone: Distributed Evaluation Pipeline

## Objective

Turn evaluation from a bottleneck into infrastructure. Build a distributed pipeline that runs your Month 10 and Month 11 evaluation suites in a fraction of the time, with retries, failure isolation, cost tracking, and a measured scaling curve.

## Business Problem

Evaluation is the bottleneck in LLM development. Your Month 11 benchmark at 40
scenarios × 5 runs is 200 agent invocations; your Month 10 eval is 200 questions
with judge calls on each. Run serially, both take hours, which means you run them
rarely, which means regressions go unnoticed.

Making evaluation fast makes it routine, and routine evaluation is what a quality
gate in CI requires. That is the actual business case and it is a good one.

## Technical Requirements

- Ray-based parallel execution over a sharded work list
- Retries with exponential backoff for transient failures
- Failure isolation: per-item error capture, reported as part of the result
- Distributed rate limiting against API quotas
- Resumability: kill it halfway and restart without redoing work
- Cost accounting: tokens and dollars per item and per run
- **A cost budget that halts the job cleanly when exceeded**
- Result aggregation with the same metrics as the serial version
- **A scaling curve**: speedup and cost against worker count, with the plateau explained
- Runs both the Month 10 RAG eval and the Month 11 agent benchmark

## Theory Requirements

The README must explain:

1. Why evaluation is the bottleneck, with your serial timings.
2. Where the scaling plateaus and why — Amdahl, rate limits, or straggler-bound.
3. How failure isolation works and why silently dropping failures biases results.
4. The cost model: dollars per evaluation run, and where the money goes.

## System Design Requirements

- Work list sharding with bounded in-flight items
- A rate limiter actor shared across workers
- Persistent completion state for resumability
- Result aggregation identical to the serial path, verified by test
- Clean shutdown on budget exhaustion or signal

## Implementation Plan

**Day 1** — Ray fundamentals and a first parallel run.

**Day 2** — Reliability: retries, isolation, timeouts.

**Day 3** — Rate limiting and cost accounting.

**Day 4** — Resumability and the budget guard.

**Day 5** — Wire in both evaluation suites; verify results match the serial path.

**Day 6** — The scaling study and the write-up.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Results match serial execution | Exactly, verified by test |
| Speedup at 16 workers | Reported, with the plateau explained |
| Failure isolation | One poisoned input does not kill the job |
| Resumability | Killed at 50%, restarts and completes correctly |
| Rate limiting | Stays under quota with all workers running |
| Cost per run | Measured and reported |
| Budget guard | Halts cleanly and reports partial results |

## Expected Repository Structure

```text
distributed-llm-eval/
  README.md
  pyproject.toml
  Makefile
  src/
    runner.py  shard.py  ratelimit.py  retry.py  cost.py  aggregate.py
  suites/
    rag_eval.py  agent_bench.py
  tests/
  results/
    scaling.json  cost.json
  docs/
    design.md  scaling_analysis.md  limitations.md
```

## README Requirements

Above the fold: one sentence, the headline speedup and cost, and `make eval`.

Then: why evaluation is the bottleneck with your serial numbers; architecture
diagram; **the scaling curve** with the plateau explained; the cost model; the
reliability features and why each exists; the verification that distributed
results match serial; limitations.

**Lead with the numbers.** "50,000 evaluations: 14 hours serially, 22 minutes
distributed, $6.40" is the whole pitch and it belongs in the first line.

## Demo Requirements

`make demo` runs a 200-item evaluation across 8 workers, printing progress, the failure count, wall-clock time, and total cost, then the aggregated metrics.

## Blog Post Requirement

Optional. The angle: the scaling analysis. 'Why My Evaluation Pipeline Stopped Getting Faster at 12 Workers' — a specific, diagnosed plateau is more interesting than a speedup claim.

## Interview Story

> "Evaluating our benchmark serially took fourteen hours, which meant we ran it
> weekly. Distributed it takes twenty-two minutes and costs about six dollars, so
> now it runs on every pull request. It plateaus at twelve workers because we hit
> the API rate limit, not because of coordination overhead — here's the curve."

45 seconds, with a diagnosed plateau rather than a bare speedup.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 13 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 8 | A real bottleneck with your own numbers. |
| Technical execution | 8 | Reliability features are the substance. |
| Evaluation rigor | 8 | Scaling curve with the plateau diagnosed. |
| Code quality | 8 | Clean, tested, resumable. |
| Documentation | 8 | The scaling analysis is the interesting part. |
| Reproducibility | 8 | `make eval` works. |
| Error analysis | 8 | Failure modes captured and reported, not dropped. |
| Portfolio readiness | 8 | **Flagship #7.** The cost report is the distinguishing detail. |

**Overall target: 8.0+.**

## Stretch Goals

1. **Straggler mitigation** with speculative re-execution; measure the p99
   wall-clock improvement.
2. **Ray Data streaming** for evaluation over a corpus too large to shard upfront.
3. **A cost dashboard** showing spend by suite, model, and day.
4. **Multi-node**: run across two machines and report what changed.

## Limitations To State Honestly

- Tested on a single machine with multiple workers; multi-node adds network
  and scheduling complexity not measured here.
- The plateau is rate-limit bound for API-based suites, so the scaling curve is
  specific to my quota.
- Cost figures are for the models and prices at time of writing.
- No GPU scheduling; the suites here are API- and CPU-bound.
