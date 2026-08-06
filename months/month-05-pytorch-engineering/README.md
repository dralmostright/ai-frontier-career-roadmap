# Month 05: PyTorch Engineering

**Weeks 17-20 · Phase 2: Deep Learning Mastery · Lab: `bootstrap/pytorch-labs/`**

---

## The Month In One Sentence

Port everything to PyTorch, then wrap it in the production discipline that separates research code from software.

## Why This Month Exists

This is the first month where your background is a visible advantage.

Most people learning PyTorch write a script, get a number, and move on. You are
going to build a *pipeline*: config-driven, seeded, checkpointed, tracked,
tested, and reproducible bit-for-bit. That is not polish — it is the difference
between "I trained a model" and "someone else can reproduce my numbers," and
reviewers who have inherited research code notice within thirty seconds.

The Week 20 reproducibility test — train twice, assert the losses are identical —
is the month's gate and the thing to feature in the capstone README.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 17 | PyTorch Tensors and Autograd | `tensor_labs.py`; the NumPy MLP ported and matched |
| 18 | Modules, Datasets, DataLoaders | `data.py`, `models.py`; a loader-bottleneck diagnosis |
| 19 | Training Loops and Debugging | `train.py`, `evaluate.py` — AMP, clipping, accumulation, checkpointing |
| 20 | Experiment Tracking and Reproducibility | `config.py`, `tracking.py` — and a bit-for-bit reproducibility test |

**Capstone:** MNIST Production Training Pipeline — the same problem as Month 4, done the way a company would do it.

## The Through-Lines

**Month 4 becomes a port.** Every abstraction you meet has a NumPy ancestor you
wrote. That is why this month is fast.

**Reproducibility is operations.** Seeding, environment capture, config diffing,
and checkpoint/resume are all things you already do for stateful production jobs.

**Profile before optimizing.** Week 18's loader-bottleneck diagnosis is the first
instance of a rule that governs Weeks 52 and 59 too.

**Config-driven everything.** From Week 20 onward, no hyperparameter appears in
code. If you are editing Python to change a learning rate, the config system has
failed.

## Time and Compute

15-20 hours per week. CPU is workable; a GPU makes Week 19-20 faster. Kaggle's free tier or Colab is sufficient. Install PyTorch this month — see `bootstrap/pytorch-labs/README.md`.

## Files

```text
month-05-pytorch-engineering/
  README.md      you are here
  week-17.md     pytorch tensors and autograd
  week-18.md     modules, datasets, dataloaders
  week-19.md     training loops and debugging
  week-20.md     experiment tracking and reproducibility
  capstone.md    mnist production training pipeline
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 20.** Reproducibility is the month's differentiator and the capstone gate. Weeks 17-18 can be compressed if you are already comfortable with the API.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Skipping `optimizer.zero_grad()` | Loss decreases then explodes | Gradients accumulate. Same lesson as Week 3. |
| Forgetting `model.eval()` | Validation noisy and slightly low | Dropout and BatchNorm are mode-dependent. |
| `.item()` inside the inner loop | GPU stalls, low utilization | Each call synchronizes. Accumulate on device. |
| Checkpointing weights only | Visible jump in the loss on resume | Save optimizer, scheduler, scaler, and RNG state too. |
| Hyperparameters in code | Cannot reproduce or compare runs | Config files, from Week 20 onward. |
| Unseeded DataLoader workers | Augmentations repeat across workers | `worker_init_fn` and a generator. Silent, and it costs accuracy. |

## Advancement

Before Month 6, you should be able to, without notes:

- [ ] Explain mechanically what `.backward()` does
- [ ] Diagnose a GPU sitting at 30% utilization, in priority order
- [ ] Explain when to use `no_grad` versus `detach`
- [ ] Name every source of nondeterminism in a training run
- [ ] Reproduce a training run bit-for-bit and prove it with a test
- [ ] Point at a config-driven, tested, reproducible training pipeline

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 6 — Computer Vision. The pipeline you built this month is the one you will use for the rest of the course.
