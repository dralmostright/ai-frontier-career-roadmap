# Week 46: LoRA and QLoRA

## Outcome

By Sunday you have implemented LoRA from scratch, applied it to a real model, and produced the rank-versus-quality curve showing where it saturates.

## Why This Matters For OpenAI/Anthropic-Level Interviews

LoRA is directly examined and the questions are specific: derive the parameter
count, explain why B is initialized to zero, explain why the adapter can be
merged.

The parameter arithmetic you should do in your head: a 4096×4096 layer has 16.7M
parameters; rank-8 LoRA adds 2 × 8 × 4096 = 65,536, about 0.4%. That is the whole
pitch.

The zero-initialization detail matters: B starts at zero so B@A is zero and the
tuned model begins exactly at the base model. Initializing both randomly perturbs
the model before training and discards the pretrained behavior you are trying to
preserve.

The mergeability point is the deployment argument, and it leads to the good
system design answer: one base model in memory, many task adapters swapped per
request. That is a real multi-tenant serving pattern.

The rank ablation is the week's finding. Quality typically saturates around rank
8-16, which means higher ranks buy parameters and not performance — and knowing
your own saturation point is better than quoting someone else's.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The low-rank hypothesis**
   1. Fine-tuning updates have low intrinsic rank
   2. The connection to Week 2's truncated SVD
   3. Why this is a defensible parameterization rather than an arbitrary one
2. **LoRA mechanics**
   1. h = W0x + (BA)x · (alpha/r)
   2. Parameter count: r(d_in + d_out) versus d_in·d_out
   3. **B initialized to zero**, A initialized random
   4. alpha as a scaling factor, and the alpha/r convention
3. **Which modules to adapt**
   1. The original paper: query and value projections only
   2. Later work: all linear layers, including the FFN
   3. Running the ablation rather than picking the popular answer
4. **Merging**
   1. Folding BA into W0 for zero inference overhead
   2. Unmerged: an extra matmul per layer
   3. Multi-adapter serving: one base, many adapters
5. **QLoRA**
   1. 4-bit NF4 quantization of the base weights
   2. Why NF4 is information-theoretically optimal for normal weights
   3. Double quantization
   4. Paged optimizers
   5. What it makes possible on one consumer GPU

## Required Free Resources

- **Primary:** 'LoRA' — https://arxiv.org/abs/2106.09685 — read it fully; it is short and directly examined
- **Primary:** 'QLoRA' — https://arxiv.org/abs/2305.14314 — read the NF4 section carefully
- PEFT documentation — https://huggingface.co/docs/peft/index — use after implementing yours
- Sebastian Raschka, 'Practical Tips for Finetuning LLMs Using LoRA' — the empirical guidance, with experiments
- Unsloth — https://github.com/unslothai/unsloth — makes QLoRA practical on modest hardware

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=46
```

1. **Derive the parameter count** (30m) — On paper. For rank 4, 8, 16, 64 on a 4096×4096 layer.
2. **`LoRALayer` from scratch** (2h) — B initialized to zero. Verify the initial output equals the base model exactly.
3. **`apply_lora` to a real model** (1.5h) — Report trainable parameter percentage.
4. **`merge` and `unmerge`** (1h) — Verify merged output equals unmerged, and measure the inference speed difference.
5. **Train with your LoRA** (2h) — Compare quality and time against Week 45's full fine-tune.
6. ****`rank_ablation`**** (2.5h) — Ranks 1, 2, 4, 8, 16, 32, 64. Plot quality against trainable parameters. Find your saturation point.
7. **Target-module ablation** (1.5h) — Attention only versus all linear. Parameters and quality.
8. **`save_adapter`** (45m) — Megabytes, not gigabytes. This is the deployment argument.
9. **QLoRA with bitsandbytes** (1.5h) — 4-bit base, bf16 adapters. Measure the memory saving.

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
l
o
r
a
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
l
o
r
a
_
d
b
a
.
y
a
m
l
```

## Tests To Write

Add: a test that a freshly-initialized LoRA layer produces output identical to the base layer (because B is zero); and a test that merged and unmerged adapters produce identical outputs.

## Portfolio Artifact

`src/lora.py` and the rank-versus-quality curve. That curve is the week's finding.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *Derive LoRA's parameter count for rank 8 on a 4096×4096 layer.* Then: *Why is B initialized to zero?* Then: *How would you serve fifty different fine-tuned variants of one model?* The third question is where the multi-adapter answer shines.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Build multi-adapter serving: one base model loaded once, three task-specific adapters, and a router that swaps adapters per request. Measure the memory saving against loading three full models and the switching latency. This is a real production pattern for multi-tenant fine-tuned deployments and it is a memorable, specific system design answer.
