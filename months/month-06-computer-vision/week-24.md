# Week 24: Vision Transformers and Serving

## Outcome

By Sunday you understand ViTs well enough to say when they beat CNNs and why, and you have a trained model served behind FastAPI with measured p50/p95/p99 latency.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Two threads converge here.

**The ViT thread** is the bridge to Month 8. Patch embedding turns an image into
a sequence of tokens, and from there it is exactly the transformer you are about
to build. Implementing `PatchEmbedding` makes that connection concrete.

The interview answer to "when does a ViT beat a CNN?" is about *data scale*, not
architectural superiority. A CNN's locality and translation-equivariance priors
are free information; a ViT must learn them from data. Below some data threshold
the CNN wins, above it the ViT's flexibility pays off. Being specific about that
tradeoff is what makes the answer good.

**The serving thread** is your first deployed artifact. Warmup, dynamic batching,
and percentile latency are the concepts, and the latency-versus-batch-size curve
is the result.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Vision transformers**
   1. Patch embedding: images become sequences
   2. The CLS token and positional embeddings
   3. Why a ViT is a transformer encoder with a different input pipeline
2. **Inductive bias, quantified**
   1. What the CNN gets for free
   2. What the ViT must learn from data
   3. The data-scale crossover, and why pretraining changes it
3. **Serving**
   1. Model loading and **warmup** — the first inferences are several times slower
   2. Static versus dynamic batching
   3. The latency/throughput tradeoff, measured
4. **Latency measurement**
   1. p50, p95, p99 — never the mean
   2. Discarding warmup iterations
   3. Load testing, and why a single-threaded benchmark misleads
5. **Packaging**
   1. Containerization, image size, and layer caching
   2. Health versus readiness
   3. Model cards

## Required Free Resources

- **Primary:** 'An Image is Worth 16x16 Words' (Dosovitskiy et al.) — https://arxiv.org/abs/2010.11929 — the ViT paper. Read it; you will reference the data-scale finding.
- **Primary:** FastAPI docs — https://fastapi.tiangolo.com/
- Lucas Beyer, 'Vision Transformers' lecture notes — good on the inductive bias argument
- 'Do Vision Transformers See Like Convolutional Neural Networks?' — https://arxiv.org/abs/2108.08810

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=24
```

1. **`PatchEmbedding`** (1h) — Images to token sequences. The bridge to Month 8.
2. **`VisionTransformer`** (2h) — A small one. You will rewrite the attention properly in Week 29.
3. **`cnn_vs_vit_comparison`** (1.5h) — Train both at several dataset sizes. Find the crossover.
4. **`InferenceService` with warmup** (1h) — Twelve dummy batches at startup. Measure the difference warmup makes.
5. **`measure_latency`** (1h) — Percentiles, warmup discarded.
6. **`DynamicBatcher`** (1.5h) — Collect for a few milliseconds, run as one batch.
7. **`latency_vs_batch_size`** (1h) — The capstone figure. Find the throughput knee.
8. **Containerize and measure image size** (1h) — Multi-stage build. Previews Week 57.

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
p
y
t
o
r
c
h
-
l
a
b
s
/
s
r
c
/
v
i
t
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
p
y
t
o
r
c
h
-
l
a
b
s
/
s
r
c
/
s
e
r
v
e
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
p
y
t
o
r
c
h
-
l
a
b
s
/
c
o
n
f
i
g
s
/
v
i
t
_
t
i
n
y
.
y
a
m
l
```

## Tests To Write

Add: a test that the batched service returns the same predictions as single-request inference; and a test that warmup measurably reduces first-request latency.

## Portfolio Artifact

The Month 6 capstone. See `capstone.md`. The latency-versus-batch-size curve is the figure that matters.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *When does a ViT beat a CNN, and when does it not?* The answer is about data scale and inductive bias. Then: *What is the CNN's inductive bias worth, concretely?*

**System design (30 min).** Design an image classification service for 1000 requests/second with a 200ms p99 budget. Batching, autoscaling, model choice, and cost.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Quantize the model to INT8 and produce the full tradeoff table: accuracy, p99 latency, throughput, and model size, for fp32, fp16, and int8. This is a real production decision, the numbers are concrete, and it previews the quantization material in Week 52. Put the table in the capstone README.
