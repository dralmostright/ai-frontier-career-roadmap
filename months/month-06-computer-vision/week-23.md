# Week 23: Transfer Learning

## Outcome

By Sunday you can fine-tune a pretrained vision model correctly, set discriminative learning rates, and justify what to freeze based on dataset size and domain similarity.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Transfer learning is how nearly all applied deep learning actually works, and
the freeze decision is the same structural decision you will make in Week 46
about full fine-tuning versus LoRA.

Two traps that silently cost accuracy and produce no error: using the wrong
normalization statistics for a pretrained backbone, and freezing BatchNorm
parameters without also calling `.eval()` on those layers so the running
statistics stop drifting. Both are worth knowing because both are common.

The decision table — small/similar means freeze everything, large/dissimilar
means fine-tune everything or train from scratch — is a clean, memorable
interview answer.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 7 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Why transfer works**
   1. Early layers learn general features: edges, textures, colors
   2. Late layers learn task-specific structure
   3. Why the boundary moves with domain similarity
2. **Strategies**
   1. Feature extraction: freeze the backbone, train the head
   2. Fine-tuning: unfreeze some or all, at a low learning rate
   3. The decision table by dataset size and domain similarity
3. **Discriminative learning rates**
   1. Lower rates for earlier layers
   2. Parameter groups in the optimizer
   3. Gradual unfreezing
4. **The traps**
   1. Normalization must match pretraining
   2. Frozen BatchNorm needs `.eval()`, not just `requires_grad=False`
   3. Frozen parameters should be excluded from the optimizer, or weight decay still applies

## Required Free Resources

- **Primary:** PyTorch transfer learning tutorial — https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- **Primary:** CS231n transfer learning notes — https://cs231n.github.io/transfer-learning/ — the decision table originates here
- 'How transferable are features in deep neural networks?' — https://arxiv.org/abs/1411.1792 — the empirical study behind the folklore
- timm documentation — https://huggingface.co/docs/timm — the standard model zoo

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=23
```

1. **`load_pretrained` with head replacement** (1h) — Get the normalization right.
2. **`freeze_layers` and verify** (45m) — Check `requires_grad` and the optimizer's parameter list.
3. **The BatchNorm trap demo** (1h) — Freeze parameters only, then also `.eval()`. Show the accuracy difference.
4. **`discriminative_learning_rates`** (1h) — Parameter groups with a decay factor.
5. **Fine-tune on a small dataset** (2h) — 100 images per class. Compare against training from scratch.
6. **The freeze ablation** (1.5h) — Freeze all / last block / nothing. Table of accuracy and training time.
7. **Wrong-normalization demo** (45m) — Use CIFAR statistics on an ImageNet model. Measure the loss.

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
t
r
a
n
s
f
e
r
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
f
i
n
e
t
u
n
e
.
y
a
m
l
```

## Tests To Write

Add: a test that `freeze_layers` sets `requires_grad=False` on matched parameters and leaves others trainable; and a test that a frozen BatchNorm layer in `eval()` mode does not update its running statistics.

## Portfolio Artifact

`src/transfer.py`, the freeze ablation table, and the linear-probe-versus-fine-tune crossover plot if you do the extension.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (20 min).** Recorded: *Which layers do you freeze when fine-tuning, and why does the answer depend on dataset size?* Give the four-cell decision table.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run the linear-probe versus full-fine-tune comparison across dataset sizes — 50, 200, 1000, 5000 images per class — and find the crossover point where fine-tuning starts winning. This is the empirical version of the decision table, and it is the same experiment shape you will run in Week 46 for LoRA rank.
