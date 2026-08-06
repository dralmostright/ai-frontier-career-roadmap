# Month 04: Neural Networks From Scratch

**Weeks 13-16 · Phase 2: Deep Learning Mastery · Lab: `bootstrap/ml-from-scratch/`**

---

## The Month In One Sentence

Build a working deep learning framework in NumPy so that PyTorch never has to be magic again.

## Why This Month Exists

Phase 2 opens by removing the mystery. You will write autograd for arrays,
layers, losses, optimizers, and a training loop, and then train MNIST to >95%
with nothing but NumPy.

The payoff is diagnostic ability. When a training run produces NaN at step 400,
or the loss plateaus at exactly ln(C), or the GPU sits at 30% utilization, the
engineers who fix it in ten minutes are the ones who know what the framework is
doing underneath. Two weeks here buys fourteen months of not being stuck.

The interview relevance is direct: "derive backpropagation for a two-layer MLP"
and "why does Adam converge faster and generalize worse than SGD" are standard,
and both become easy once you have implemented them.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 13 | Perceptrons and MLP Foundations | `neural_net.py` layers and activations; XOR solved |
| 14 | Backpropagation | `backprop.py`; every layer gradient-checked |
| 15 | Optimization | `optimizers.py` — SGD through AdamW, plus schedules |
| 16 | Regularization and Generalization | `regularization.py` + the overfit-then-fix ablation table |

**Capstone:** Neural Network Library From Scratch — a miniature deep learning framework in NumPy that trains MNIST to >95%.

## The Through-Lines

**Week 3's scalar autodiff becomes array autodiff.** Conceptually identical; the
difficulty is entirely in shapes and broadcasting.

**Gradient checking is the safety net.** Every layer you write gets checked. This
habit carries to Week 29's attention and Week 67's research code.

**Optimizers are a sequence of fixes.** SGD's ravine problem motivates momentum;
scale variance motivates RMSProp; Adam combines them; AdamW fixes the decay. Learn
it as a chain of problems, not a list.

**Diagnosis before tuning.** Week 16's `overfit_single_batch` becomes the check
you run before every training run for the rest of the course.

## Time and Compute

15-20 hours per week. CPU only. MNIST in NumPy trains in minutes on a laptop.

## Files

```text
month-04-deep-learning-from-scratch/
  README.md      you are here
  week-13.md     perceptrons and mlp foundations
  week-14.md     backpropagation
  week-15.md     optimization
  week-16.md     regularization and generalization
  capstone.md    neural network library from scratch
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 14.** Backpropagation with correct shapes is the load-bearing skill of Phase 2. If a week must shrink, compress Week 13 and protect Week 14.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| `=` instead of `+=` in backward | Wrong gradients in any branching graph | Gradients accumulate. Always `+=`. |
| Not gradient-checking | Model trains slowly to a worse optimum | Check every layer. It takes two minutes. |
| Skipping the initial-loss check | Hours lost to a label bug | Untrained loss must be ln(C). 2.303 for ten classes. |
| Forgetting `.eval()` | Noisy, slightly-low validation metrics | Dropout and BatchNorm are mode-dependent. |
| Tuning before debugging | Endless learning-rate search | Overfit 8 examples first. If it cannot, the bug is in the code. |

## Advancement

Before Month 5, you should be able to, without notes:

- [ ] Derive backpropagation for a two-layer MLP on a whiteboard
- [ ] Explain why sigmoid's 0.25 gradient ceiling causes vanishing gradients
- [ ] Explain why Adam needs bias correction
- [ ] Explain AdamW's decoupled decay and why it differs from L2 in the loss
- [ ] Debug a NaN loss out loud, in priority order
- [ ] Point at a NumPy framework that trains MNIST to >95%

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 5 — PyTorch Engineering. The same concepts, in a framework, with production discipline added.
