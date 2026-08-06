# Month 04 Capstone: Neural Network Library From Scratch

## Objective

Package Weeks 13-16 into a coherent, documented, tested deep learning framework with a PyTorch-shaped API, and demonstrate it by training MNIST to over 95% test accuracy using nothing but NumPy.

## Business Problem

None, and say so. This is a comprehension artifact.

What it demonstrates: that the abstractions you use for the next fourteen months
are ones you could rebuild. That claim is checkable, which is what makes it
worth making.

## Technical Requirements

- Layers: Linear, ReLU, Sigmoid, Tanh, GELU, Softmax, Dropout, BatchNorm1d, LayerNorm, Sequential
- Losses: MSE, CrossEntropy (fused), BCE (fused)
- Optimizers: SGD (+momentum, +Nesterov), RMSProp, Adam, AdamW
- Schedules: Step, Cosine, WarmupCosine, ReduceLROnPlateau
- Training loop with minibatching, validation, early stopping, and history
- Every gradient verified by `gradient_check` with relative error < 1e-6
- Trains MNIST to >95% test accuracy
- A PyTorch-comparison notebook: same architecture, same hyperparameters, both frameworks, matching curves

## Theory Requirements

The README must explain, in your own words:

1. What backpropagation is, mechanically, in terms of the computational graph.
2. Why reverse mode beats forward mode for machine learning.
3. The optimizer chain: what each one fixes about the previous one.
4. Why LayerNorm rather than BatchNorm for sequence models.

## System Design Requirements

PyTorch-shaped API — `Layer`, `Loss`, `Optimizer` base classes; `parameters()` and `gradients()`; `train()`/`eval()` modes. The point is that porting to PyTorch in Month 5 should be mechanical.

## Implementation Plan

**Days 1-2** — Consolidate Weeks 13-16 into a clean package. Gradient-check
everything again after refactoring.

**Day 3** — MNIST data loading and the training run. Target >95%.

**Day 4** — The PyTorch comparison notebook. Same architecture, same seed, same
hyperparameters. The loss curves should track closely; investigate if they do not.

**Day 5** — Documentation, README, theory sections.

**Day 6** — Review, score, publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| MNIST test accuracy | > 95% |
| Every gradient checked | Relative error < 1e-6 |
| PyTorch comparison | Loss curves within 5% at every epoch |
| Initial loss | ln(10) = 2.303, verified by a test |
| `overfit_single_batch` | Converges in < 500 steps |
| Reproducibility | Same accuracy from a clean clone |

## Expected Repository Structure

```text
numpy-deep-learning/
  README.md
  pyproject.toml
  Makefile
  src/npdl/
    __init__.py
    layers.py
    losses.py
    optimizers.py
    schedulers.py
    regularization.py
    training.py
    gradcheck.py
  tests/
  notebooks/
    01_mnist_training.ipynb
    02_pytorch_comparison.ipynb
    03_optimizer_comparison.ipynb
    04_regularization_ablation.ipynb
  docs/
    design.md
    gradients.md      the derivations, written out
    limitations.md
```

## README Requirements

Above the fold: one sentence, the MNIST accuracy number, and the setup commands.

Then: what it is and why; the API with a ten-line training example; the four
theory sections; the MNIST result with its training curve; the PyTorch comparison
figure; the optimizer and regularization ablation tables; how gradients are
verified; limitations.

`docs/gradients.md` — the derivations written out properly — is the part that
makes this repository more than a toy. Nobody else's from-scratch framework has
it.

## Demo Requirements

`make demo` trains a small MNIST model for 60 seconds and prints the accuracy, plus a gradient-check report showing every layer passing.

## Blog Post Requirement

**Post #1 is due next month, but this is the better subject.** Working title:
"What a DBA Learns Building a Neural Network From Scratch."

The angle nobody else has: computational graphs as dependency graphs, gradient
accumulation as a concurrency concern, numerical stability as the same class of
problem as integer overflow, and the ln(C) check as an assertion. Write it from
your perspective, not as a generic backprop tutorial.

## Interview Story

> "I wrote the framework, so when someone asks why the loss is NaN I start from
> the computational graph rather than from Stack Overflow. It trains MNIST to
> 96%, every gradient is numerically verified, and the loss curves match PyTorch
> to within a few percent on the same architecture."

45 seconds.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 4 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 6 | Comprehension artifact. Frame it honestly. |
| Technical execution | 9 | **The point.** Every gradient correct, MNIST >95%. |
| Evaluation rigor | 8 | Gradient checks, PyTorch comparison, ablations. |
| Code quality | 8 | PyTorch-shaped API, clean separation. |
| Documentation | 9 | The derivations document is the differentiator. |
| Reproducibility | 9 | Pure NumPy. No excuse. |
| Error analysis | 6 | Limited scope; the ablation tables are the closest analogue. |
| Portfolio readiness | 8 | **Engineers are impressed by this one**, and engineers run the screens. |

**Overall target: 8.0+, with Technical Execution and Documentation at 9.**

## Stretch Goals

1. **A convolution layer** with a correct backward pass. Hard, and it makes
   Month 6 a review.
2. **Publish to PyPI.** `pip install npdl` working is a small finishing signal.
3. **An interactive gradient-flow visualizer** — norms by layer over training.
4. **Train on CIFAR-10** with an MLP and report how badly it does, then explain
   why convolution is necessary. A good negative result.

## Limitations To State Honestly

- No GPU support. Roughly 50-100x slower than PyTorch on the same model.
- No convolution, no recurrence, no attention.
- Scalar learning rate only; no per-parameter groups.
- Memory-inefficient: every activation is retained with no checkpointing.
- It is a learning artifact. Use PyTorch.
