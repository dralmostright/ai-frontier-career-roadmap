# Week 59: Scaling, Queues, and Batch Inference

## Outcome

By Sunday you have a queue-backed batch inference system with workers, retries, dead-letter handling, progress tracking, and a cost estimate for a large corpus.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Design batch inference over 100 million documents" is a standard system design
question and it is mostly a distributed-systems question, which is why you should
be good at it.

The real content: work partitioning, idempotency (because retries will happen),
checkpointing so a failure at 80% does not restart from zero, dead-letter queues
for permanently-failing items, backpressure so you do not overwhelm a downstream
service, and cost estimation before you start rather than after.

That last one matters. Estimating the cost of a 100M-document job before running
it — tokens per document, cost per token, total — is the kind of thing that
prevents an expensive surprise, and it is a habit most people acquire the hard
way.

Continuous batching from Week 52 belongs here too, applied at the serving layer.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Queue-based architecture**
   1. Producer, queue, worker pool, result sink
   2. Why queues absorb rate variance
   3. At-least-once delivery, and why idempotency is required
2. **Work partitioning**
   1. Chunking a large corpus into units
   2. Balancing shard size against overhead
   3. Ordering guarantees, and when you do not need them
3. **Reliability**
   1. Retries with backoff
   2. Dead-letter queues for permanent failures
   3. Checkpointing progress
   4. Visibility timeouts and the duplicate-processing risk
4. **Backpressure**
   1. Bounded queues
   2. Rate limiting against downstream services
   3. Why an unbounded queue just moves the failure
5. **Cost estimation**
   1. Tokens per item × items × price
   2. Estimating before running
   3. Budget guards and partial-result reporting
6. **Serving-side batching**
   1. Continuous batching for generation
   2. Why sequences finishing at different lengths breaks static batching

## Required Free Resources

- **Primary:** 'Designing Data-Intensive Applications' (Kleppmann) — chapters 10-11 on batch and stream processing. You may know this material; it applies directly.
- **Primary:** vLLM continuous batching documentation — https://docs.vllm.ai/
- Celery or ARQ documentation — whichever queue library you choose
- KEDA scalers — https://keda.sh/docs/latest/scalers/ — for worker autoscaling

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=59
```

1. **Queue and worker skeleton** (1.5h) — Redis-backed. Producer, queue, pool, sink.
2. **Idempotent processing** (1h) — At-least-once delivery means duplicates. Handle them.
3. **Retries and dead-letter** (1.5h) — Permanent failures go to the DLQ with the error, not silently dropped.
4. **Checkpointing** (1h) — Kill it at 60% and verify it resumes without redoing work.
5. **Backpressure** (1h) — Bounded queue. Verify the producer slows rather than the system falling over.
6. **Progress tracking** (45m) — Items done, failed, remaining, ETA, cost so far.
7. ****Cost estimation**** (1h) — Estimate before running, measure after, compare. Report the error.
8. **Worker autoscaling on queue depth** (1.5h) — KEDA, from Week 58's stretch.
9. **Run it on a real corpus** (1.5h) — Embed or classify 100k documents. Report throughput and cost.

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
w
o
r
k
e
r
s
.
p
y


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
i
n
f
r
a
/
k
8
s
/
w
o
r
k
e
r
s
.
y
a
m
l
```

## Tests To Write

Add: a test that processing is idempotent under duplicate delivery; and a test that a job killed at 60% resumes and processes each item exactly once.

## Portfolio Artifact

`src/workers.py`, deployed to the cluster, with a throughput and cost report for a real corpus.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (35 min).** **Recorded.** *Design batch inference over 100 million documents.* Partitioning, queueing, idempotency, checkpointing, dead-letter, backpressure, autoscaling, cost estimation, and failure recovery. This should be a strong answer.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement priority queues so interactive requests preempt batch work on the same worker pool. This is a real multi-tenancy requirement — you cannot let a 100M-document embedding job starve the interactive RAG endpoint — and the design questions (preemption granularity, starvation avoidance, fairness) are exactly the kind of thing that makes a system design answer specific.
