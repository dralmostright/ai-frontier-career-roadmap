# Week 49: GPU and CUDA Basics

## Outcome

By Sunday you can compute training and inference memory for any model size from first principles, reason about arithmetic intensity, and explain what each memory-saving technique buys.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The most directly examined week of Phase 5.**

"How much memory to train a 7B model?" is asked constantly and the answer is
mechanical: parameters at 4 bytes, gradients at 4, Adam's two moments at 8 — 16
bytes per parameter, so 112GB before a single activation. Then activations, which
scale with batch size and sequence length and often dominate.

That calculation is the motivation for everything else: ZeRO shards the 16N,
LoRA shrinks the trainable N, 8-bit optimizers halve the moment storage, gradient
checkpointing trades compute for activation memory.

The other concept worth owning is arithmetic intensity — FLOPs per byte moved.
Inference decode is memory-bandwidth-bound, not compute-bound, which is why
batching helps so much and why the same GPU that trains fast can serve slowly.
That distinction is a good depth marker.

## Time Budget: 15-20 Hours

- Theory: 5 hours
- Coding: 5.5 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **GPU architecture**
   1. SMs, warps, and the execution model at a useful level of abstraction
   2. HBM bandwidth versus compute throughput
   3. Tensor cores and why fp16/bf16 matter
   4. Why GPUs are throughput devices, not latency devices
2. **Training memory**
   1. Parameters, gradients, optimizer state: the 16N rule for Adam fp32
   2. Activation memory, and why it scales with batch × sequence
   3. Fragmentation and the allocator
   4. Worked examples at 125M, 1B, 7B, 70B
3. **Inference memory**
   1. Weights plus KV cache
   2. The KV cache formula from Week 32
   3. Why long context dominates at scale
   4. Batch size and memory
4. **Arithmetic intensity**
   1. FLOPs per byte moved
   2. The roofline model
   3. Prefill: compute-bound. Decode: memory-bandwidth-bound.
   4. Why batching helps decode enormously
5. **Memory-saving techniques**
   1. Mixed precision
   2. Gradient checkpointing: compute for memory
   3. 8-bit optimizers
   4. ZeRO, previewed
   5. What each does to the 16N

## Required Free Resources

- **Primary:** 'Transformer Inference Arithmetic' (Kipply) — https://kipp.ly/transformer-inference-arithmetic/ — the single best resource for this week
- **Primary:** 'Making Deep Learning Go Brrrr From First Principles' (Horace He) — https://horace.io/brrr_intro.html — the compute/memory/overhead framing
- NVIDIA, 'Matrix Multiplication Background User's Guide' — https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/
- 'Mixed Precision Training' — https://arxiv.org/abs/1710.03740
- '8-bit Optimizers via Block-wise Quantization' — https://arxiv.org/abs/2110.02861

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=49
```

1. **Derive the 16N rule** (45m) — On paper. Then verify against `torch.cuda.memory_allocated` on a real model.
2. **Build a memory calculator** (1.5h) — Parameters, gradients, optimizer, activations. Validate against measurements at three model sizes.
3. **Activation memory analysis** (1.5h) — Measure it against batch size and sequence length. Confirm the scaling.
4. **KV cache calculator** (45m) — Week 32's formula, tabulated for 1B/7B/70B at 2k/8k/32k context.
5. **Gradient checkpointing measurement** (1.5h) — Memory saved, compute added. The tradeoff, quantified on your hardware.
6. **Arithmetic intensity** (1.5h) — Compute it for a matmul, an attention layer, and a decode step. Identify which are bandwidth-bound.
7. **Batch size sweep at inference** (1h) — Throughput and latency against batch size. Explain the shape with the roofline model.
8. **The technique comparison table** (1h) — What each memory-saving method costs and buys, on your numbers.

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
n
o
t
e
b
o
o
k
s
/
g
p
u
_
m
e
m
o
r
y
_
m
a
t
h
.
i
p
y
n
b


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
h
a
r
d
w
a
r
e
_
a
r
i
t
h
m
e
t
i
c
.
m
d
```

## Tests To Write

Add: a test that your memory calculator predicts measured allocation within 15% for three model sizes; and a test that the KV cache formula matches an empirical measurement.

## Portfolio Artifact

The memory calculator, validated against measurements, and the technique comparison table. Both are reference material you will use for the rest of the course.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (35 min).** **Recorded, whiteboard.** *How much memory to train a 7B model with Adam in fp32? Show the arithmetic.* Then: *Now with LoRA. Now with ZeRO-3. Now in bf16 with 8-bit optimizers.* Then: *Why is decode memory-bandwidth-bound?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Profile a real training step with `torch.profiler` and attribute the time to compute, memory movement, and Python overhead — Horace He's three-category framing. Most training loops are not compute-bound and finding out which category dominates yours is genuinely useful. Report the breakdown and one optimization you made from it.
