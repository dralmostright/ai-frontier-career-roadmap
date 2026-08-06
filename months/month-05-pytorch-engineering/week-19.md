# Week 19: Training Loops and Debugging

## Outcome

By Sunday you have a training loop with mixed precision, gradient clipping, gradient accumulation, and checkpoint/resume that continues without a visible discontinuity.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Most of this file is not machine learning. It is making a long-running,
stateful, expensive job reliable and resumable — which should feel familiar.

Three features that are not optional by Month 12: mixed precision is roughly a
2x speedup; gradient accumulation is how you train with a batch size your memory
cannot hold; checkpointing is what stops a nine-hour run from being wasted by a
preemption at hour eight.

The two subtleties worth internalizing: gradient accumulation must divide the
loss by the accumulation count, or your effective learning rate is multiplied;
and under AMP you must unscale before clipping, or you clip the wrong quantity
and training silently gets worse.

The memory arithmetic — 16 bytes per parameter for Adam in fp32 — is the Week 49
interview question. Derive it here on a model you can inspect.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The loop, in order**
   1. zero_grad, forward, loss, backward, unscale, clip, step, scheduler
   2. Why the order matters
2. **Mixed precision**
   1. fp16/bf16 forward, fp32 master weights
   2. Why fp16 needs a loss scaler and bf16 does not
   3. Unscaling before clipping
3. **Gradient accumulation**
   1. Simulating a large batch
   2. Dividing the loss by the accumulation count
   3. Why it is not identical to a large batch under BatchNorm
4. **Checkpointing**
   1. Model, optimizer, scheduler, scaler, RNG state, config, git SHA
   2. Why weights-only checkpoints produce a jump on resume
   3. Best-by-validation kept separately
5. **Memory arithmetic**
   1. Parameters + gradients + Adam state = 16 bytes/param in fp32
   2. Activation memory, and why it scales with batch and sequence length
   3. The 7B model calculation

## Required Free Resources

- **Primary:** PyTorch AMP recipe — https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html
- **Primary:** Karpathy, 'A Recipe for Training Neural Networks' — https://karpathy.github.io/2019/04/25/recipe/ — second reading
- PyTorch saving and loading — https://pytorch.org/tutorials/beginner/saving_loading_models.html
- 'Mixed Precision Training' (Micikevicius et al., 2017) — https://arxiv.org/abs/1710.03740

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=19
```

1. **`train_step`** (1h) — Factored out so it is unit-testable. Return the gradient norm.
2. **`Trainer.train_epoch`** (1.5h) — The full order of operations.
3. **Gradient accumulation** (1.5h) — Then verify 4 steps of batch 8 exactly equals 1 step of batch 32.
4. **Mixed precision with a scaler** (1.5h) — Unscale before clipping. There is a test.
5. **`Trainer.validate`** (45m) — `eval()`, `no_grad()`, and restore `train()` on the way out.
6. **`save_checkpoint` / `load_checkpoint`** (1.5h) — Everything, including RNG state. Verify the resumed loss curve is continuous.
7. **`estimate_memory`** (1h) — Derive the 16-bytes-per-parameter rule and verify it against `torch.cuda.memory_allocated`.
8. **`find_lr`** (1h) — The PyTorch version of Week 15's range test. Snapshot and restore state.
9. **`evaluate` and `predict_all`** (1h) — Feed the output into Week 12's error analysis. Same method, new model class.

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
i
n
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
e
v
a
l
u
a
t
e
.
p
y
```

## Tests To Write

`tests/test_pytorch_labs.py` week-19 blocks. The accumulation-equals-large-batch test is the important one.

## Portfolio Artifact

`src/train.py`, `src/evaluate.py`, and a memory-estimate table for models from 1M to 7B parameters.

## Interview Drills

**Coding (45 min).** Two problems, heaps or DP.

**ML theory (30 min).** Recorded: *Training loss drops, validation rises. Next three actions, in order.* Then: *How much memory to train a 7B model with Adam in fp32? Show the arithmetic.*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement EMA of model weights: maintain a shadow copy updated as a running average, and evaluate with it. It typically buys a point or two of accuracy for almost no cost and is used in most production training pipelines. Report the difference on your MNIST run.
