# Week 51: Ray for AI Workloads

## Outcome

By Sunday you have a Ray-based evaluation pipeline with sharded work, retries, failure isolation, and per-item cost tracking — and a measured scaling curve.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Distributed evaluation is a better fit for your situation than distributed
training: it is genuinely useful, it runs on CPUs and API calls, and it is a real
bottleneck in LLM work. Evaluating 50,000 samples serially takes hours; done
right it takes minutes.

The engineering content is ordinary distributed-systems work — sharding, retries,
backpressure, failure isolation, result aggregation — which is why you should be
good at it. The AI-specific parts are rate limiting against API quotas and cost
accounting.

Failure isolation is the detail that matters. One malformed input should not kill
a six-hour job. Capture per-item errors, continue, and report the failure rate as
part of the result. Silently dropping failures biases your results toward inputs
that happen to work.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Ray basics**
   1. Tasks and actors, and when each fits
   2. The object store and zero-copy sharing
   3. Placement groups and resource requests
2. **Parallel evaluation patterns**
   1. Sharding a work list
   2. Backpressure: bounded in-flight work
   3. Result aggregation and ordering
3. **Reliability**
   1. Retries with exponential backoff
   2. Failure isolation: a crashed item is data
   3. Idempotency and resumability
   4. Timeouts, and why a hung worker is worse than a failed one
4. **Rate limiting**
   1. Token buckets against API quotas
   2. Distributed rate limiting across workers
   3. Handling 429s gracefully
5. **Cost accounting**
   1. Tokens and dollars per item
   2. Aggregating across workers
   3. Cost per evaluation run as a reported metric
6. **Scaling analysis**
   1. Speedup against worker count
   2. Where it plateaus and why
   3. Amdahl's law in practice

## Required Free Resources

- **Primary:** Ray Core documentation — https://docs.ray.io/en/latest/ray-core/walkthrough.html
- **Primary:** Ray Data — https://docs.ray.io/en/latest/data/data.html — the right abstraction for batch evaluation
- Ray patterns and anti-patterns — https://docs.ray.io/en/latest/ray-core/patterns/index.html — read this properly
- 'Ray: A Distributed Framework for Emerging AI Applications' — https://arxiv.org/abs/1712.05889

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=51
```

1. **Ray tasks and actors** (1h) — Both patterns on a toy workload. Understand when each fits.
2. **Shard the evaluation work** (1.5h) — Your Week 39 RAG eval or Week 44 agent benchmark as the workload.
3. **Retries with backoff** (1h) — Transient failures only. Never retry a non-idempotent operation.
4. **Failure isolation** (1.5h) — Per-item error capture. Report the failure rate as part of the result.
5. **Distributed rate limiting** (1.5h) — A token bucket actor. Verify you stay under quota with 16 workers.
6. **Cost accounting across workers** (1h) — Aggregate tokens and dollars. Report cost per run.
7. **Resumability** (1h) — Persist completed item IDs. Kill the job halfway and restart it.
8. ****The scaling curve**** (1.5h) — 1, 2, 4, 8, 16 workers. Speedup and cost. Identify where it plateaus and explain why.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
m
l
o
p
s
-
p
l
a
t
f
o
r
m
/
s
r
c
/
d
i
s
t
r
i
b
u
t
e
d
_
e
v
a
l
.
p
y
```

## Tests To Write

Add: a test that a job resumes correctly after being killed halfway, processing each item exactly once; and a test that the rate limiter holds under concurrent workers.

## Portfolio Artifact

`src/distributed_eval.py` and the scaling curve with cost. Both feed the capstone.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (30 min).** Recorded: *Design a job scheduler for a shared GPU cluster.* Queueing, fairness, preemption, gang scheduling, and what happens when a job hangs.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Add a hard cost budget: the job tracks spend and halts cleanly when it exceeds a configured ceiling, reporting what completed. This is a small piece of code and a genuinely valuable guardrail — anyone who has watched an unbounded evaluation loop run overnight against a metered API will recognize why it matters.
