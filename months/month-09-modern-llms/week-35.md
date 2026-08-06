# Week 35: Training Small Language Models

## Outcome

By Sunday you have trained a language model end to end on your curated data, evaluated it by perplexity, and implemented the full sampling toolkit.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Your first real training run, and the source of the capstone report.

The value is not the model — it is the experience of running a training job and
being able to reason about it. Warmup, loss spikes, gradient norms, throughput,
checkpointing, and what to do when the loss plateaus are all things you can only
learn by doing.

The sampling material is directly examined. "Temperature versus top-k versus
top-p" has a precise answer: temperature rescales logits before the softmax,
top-k truncates to a fixed count, top-p truncates to an adaptive nucleus. Being
able to say why top-p is the modern default — because the nucleus size tracks the
model's confidence — is the depth marker.

MFU is the stretch. Reporting model FLOPs utilization is something almost nobody
outside frontier labs does, and mentioning it signals that you think about
efficiency as a first-class concern.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The training run**
   1. Warmup, and what happens without it
   2. Loss spikes: causes and responses
   3. Gradient norm as the primary diagnostic
   4. Throughput: tokens per second, and MFU
2. **Perplexity**
   1. exp(mean NLL), and its interpretation as effective branching factor
   2. **Tokenizer dependence**, and why cross-model comparison is invalid
   3. Why validation perplexity can improve while generation quality does not
3. **Sampling**
   1. Greedy, and why it degenerates into repetition
   2. Temperature: rescaling logits before the softmax
   3. Top-k: fixed truncation, and its weakness
   4. Top-p: adaptive nucleus, and why it won
   5. Repetition penalty, and what it costs
4. **Scaling behavior**
   1. Loss against parameters, data, and compute
   2. The compute-optimal ratio
   3. What you can and cannot observe at small scale
5. **Reporting**
   1. Training curves, samples, ablations, failures
   2. Reproducibility appendix

## Required Free Resources

- **Primary:** nanoGPT training code and README — https://github.com/karpathy/nanoGPT — the practical reference for a small training run
- **Primary:** 'The Curious Case of Neural Text Degeneration' — https://arxiv.org/abs/1904.09751 — the nucleus sampling paper, and it explains *why* greedy fails
- 'Scaling Laws for Neural Language Models' — https://arxiv.org/abs/2001.08361
- Hugging Face, 'How to generate text' — https://huggingface.co/blog/how-to-generate
- EleutherAI's training logs — reading a real training run's log, including the failures, is unusually instructive

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=35
```

1. **Set up the training run** (1.5h) — Month 5's pipeline, modern architecture, curated data.
2. **Train without warmup, deliberately** (45m) — Watch it diverge. Then add warmup.
3. **The real training run** (3h) — Log everything: loss, LR, gradient norm, throughput. Checkpoint regularly.
4. **`greedy` and observe repetition** (30m) — The motivation for everything else in the file.
5. **`apply_temperature`, `top_k_filter`, `top_p_filter`** (1.5h) — Verify top-p's nucleus size adapts to confidence.
6. **`repetition_penalty` and `min_p_filter`** (1h) — Know the tradeoffs.
7. **`compare_strategies`** (1h) — Same prompt, six settings, tabulated. Goes in the report.
8. **Perplexity evaluation** (1h) — On held-out data. State the tokenizer dependence explicitly.
9. **`estimate_mfu`** (1h) — What fraction of peak compute you achieved. Almost nobody reports this.

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
l
l
m
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
t
r
a
i
n
_
l
m
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
l
l
m
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
a
m
p
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
l
l
m
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
m
i
n
i
_
g
p
t
_
s
m
a
l
l
.
y
a
m
l
```

## Tests To Write

Week-35 blocks in `test_llm_labs.py`. Add: a test that top-p keeps fewer tokens for a peaked distribution than for a flat one — the adaptivity that distinguishes it from top-k.

## Portfolio Artifact

A trained model, the full training curves, the sampling comparison table, and the perplexity evaluation. This feeds directly into the capstone report.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *Temperature, top-k, and top-p — what does each do to the distribution, and why is top-p the default?* Then: *Why do transformers need warmup?* Then: *What is perplexity, and why can't you compare it across tokenizers?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run a four-point scaling study: train models at roughly 1M, 4M, 16M, and 64M parameters on the same data budget, and plot validation loss against parameter count on log-log axes. You should see an approximately linear relationship — a power law, at small scale. This is direct preparation for Month 16 and it is a genuinely interesting result to have produced yourself.
