# Week 52: Performance Profiling

## Outcome

By Sunday you can profile training and inference systematically, attribute time to its real cause, and demonstrate one optimization with before-and-after numbers.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Inference p99 is 4 seconds and p50 is 200ms — diagnose it" is a question where
your background should produce a visibly better answer than most ML candidates.
The systematic approach — measure the distribution, find what is different about
the slow requests, check queueing versus execution, check for a cold path — is
ordinary performance work.

The AI-specific content is knowing where time actually goes in these systems:
prefill versus decode, tokenization overhead, data loading, Python overhead
between kernels, and cold-start costs.

Quantization is the other topic, and it is a real production lever. INT8 typically
halves memory and improves throughput with modest quality loss; INT4 goes further
with more loss. Having measured the tradeoff yourself makes the recommendation
credible.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Profiling method**
   1. Measure before hypothesizing
   2. The three buckets: compute, memory movement, overhead
   3. Percentiles, not means
   4. Distinguishing queueing from execution
2. **Training bottlenecks**
   1. Data loading, and Week 18's diagnosis
   2. Small kernels and Python overhead between them
   3. Synchronization points: `.item()`, `.cpu()`, printing
   4. Memory fragmentation
3. **Inference bottlenecks**
   1. Prefill versus decode, and their different profiles
   2. Tokenization cost, which is larger than people expect
   3. Batch composition and padding waste
   4. Cold start
4. **Optimization levers**
   1. Batching, and continuous batching for generation
   2. Quantization: INT8, INT4, and what each costs
   3. Kernel fusion and `torch.compile`
   4. KV cache management and PagedAttention
   5. Caching at the application layer
5. **Serving systems**
   1. vLLM and what it does differently
   2. Continuous batching versus static batching
   3. Speculative decoding

## Required Free Resources

- **Primary:** PyTorch profiler recipe — https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html
- **Primary:** 'Efficient Memory Management for LLM Serving' (vLLM) — https://arxiv.org/abs/2309.06180
- Horace He, 'Making Deep Learning Go Brrrr' — https://horace.io/brrr_intro.html — reread with profiling in mind
- vLLM documentation — https://docs.vllm.ai/
- 'LLM.int8()' — https://arxiv.org/abs/2208.07339 — the quantization paper

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=52
```

1. **Profile a training step** (1.5h) — Attribute time to the three buckets. Identify the top cost.
2. **Find and fix a synchronization stall** (1h) — Add a `.item()` in the inner loop, measure the damage, remove it.
3. **Profile inference: prefill vs decode** (1.5h) — Separate the two. Their profiles are completely different.
4. **Measure tokenization overhead** (45m) — Often a surprising fraction of short-request latency.
5. **The p99 investigation** (1.5h) — Deliberately create a p99/p50 gap — cold cache, one large input — then diagnose it as if you did not know.
6. **INT8 quantization** (1.5h) — Quality, memory, latency, throughput. The full table.
7. **`torch.compile`** (1h) — Measure the speedup and the compile cost.
8. **Try vLLM** (1.5h) — Compare throughput against your own serving code. Explain the gap.
9. ****The optimization**** (1.5h) — Pick the top bottleneck, fix it, measure. Before and after.

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
p
r
o
f
i
l
i
n
g
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
d
o
c
s
/
p
r
o
f
i
l
i
n
g
_
r
e
p
o
r
t
.
m
d
```

## Tests To Write

Add: a test that the quantized model's outputs stay within a tolerance of the fp32 model on a fixed input set.

## Portfolio Artifact

The profiling report with a measured optimization. 'I found X, changed Y, and throughput went from A to B' is the shape.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (35 min).** **Recorded.** *Inference p99 is 4 seconds, p50 is 200ms. Diagnose it.* Then: *Design an inference serving platform for three models with different latency SLOs.* The first question is where your background shows.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement continuous batching: instead of waiting for a whole batch to finish generating, evict completed sequences and admit new ones each step. This is the central idea in vLLM and modern LLM serving, and the throughput improvement over static batching is large because sequences finish at very different lengths. Measure it against your Week 24 static batcher.
