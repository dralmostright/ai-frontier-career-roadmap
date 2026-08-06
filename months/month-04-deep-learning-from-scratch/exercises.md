# Month 04 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 13 — Perceptrons and MLP Foundations

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 13.1 | `Layer` base class and `Linear.forward` | 1h | Easy |
| 13.2 | ReLU, Sigmoid, Tanh forward | 45m | Easy |
| 13.3 | GELU forward | 45m | Medium |
| 13.4 | `Softmax` forward, stably | 30m | Easy |
| 13.5 | `Sequential` | 45m | Easy |
| 13.6 | He and Xavier initialization | 1h | Medium |
| 13.7 | The initialization failure demo | 45m | Medium |
| 13.8 | `iterate_minibatches` | 45m | Easy |
| 13.9 | `MLP` and XOR | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 13.E1 | Implement LeakyReLU and ELU; construct a dead-ReLU case and show they fix it | 1.5h | High |
| 13.E2 | Plot activation distributions layer by layer for three initializations | 1.5h | High — the figure that explains initialization |
| 13.E3 | Implement Swish/SiLU and compare against GELU | 1h | Medium |

## Week 14 — Backpropagation

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 14.1 | Derive on paper: Linear, ReLU, Sigmoid, Tanh gradients | 1.5h | Hard |
| 14.2 | `numerical_gradient` and `relative_error` | 45m | Easy |
| 14.3 | `gradient_check_layer` | 1.5h | Medium |
| 14.4 | `Linear.backward` | 1h | Medium |
| 14.5 | Activation backwards | 1h | Medium |
| 14.6 | `Softmax.backward` | 1h | Hard |
| 14.7 | `CrossEntropyLoss` fused | 1.5h | Hard |
| 14.8 | `Sequential.backward` | 45m | Medium |
| 14.9 | `gradient_norms`, `check_gradient_flow` | 1h | Medium |
| 14.10 | `clip_gradients` by global norm | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 14.E1 | Implement forward-mode autodiff and compare cost for 1 vs 1000 parameters | 2.5h | High — makes the complexity argument concrete |
| 14.E2 | Visualize gradient magnitude by layer over training as a heatmap | 2h | High — great figure, and a real diagnostic |
| 14.E3 | Implement gradient checkpointing: trade compute for activation memory | 3h | High — previews Week 49 |

## Week 15 — Optimization

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 15.1 | `SGD` with momentum and Nesterov | 1.5h | Medium |
| 15.2 | `RMSProp` | 1h | Medium |
| 15.3 | `Adam` without bias correction | 1h | Medium |
| 15.4 | `Adam` with bias correction | 45m | Medium |
| 15.5 | `AdamW` | 1h | Hard |
| 15.6 | `StepLR`, `CosineAnnealingLR` | 1h | Easy |
| 15.7 | `WarmupCosineLR` | 1h | Medium |
| 15.8 | `ReduceLROnPlateau` | 45m | Easy |
| 15.9 | `compare_optimizers` on Rosenbrock | 1.5h | Medium |
| 15.10 | `lr_range_test` | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 15.E1 | Implement Lion or Sophia and compare against AdamW | 2.5h | High — shows you follow the field |
| 15.E2 | Visualize optimizer trajectories on three surfaces: ravine, saddle, plateau | 2h | High — the figure that teaches the whole chain |
| 15.E3 | Implement gradient accumulation and verify it matches a large batch exactly | 1.5h | High — needed in Week 19 |

## Week 16 — Regularization and Generalization

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 16.1 | `l1_penalty`, `l2_penalty`, `add_penalty_gradients` | 45m | Easy |
| 16.2 | `Dropout`, inverted | 1h | Medium |
| 16.3 | `BatchNorm1d` forward, both modes | 1.5h | Medium |
| 16.4 | `BatchNorm1d.backward` | 2h | Hard |
| 16.5 | `LayerNorm` | 1h | Medium |
| 16.6 | `EarlyStopping` with best-weight restoration | 1h | Medium |
| 16.7 | `label_smoothing`, `mixup` | 1h | Medium |
| 16.8 | `overfit_single_batch` | 45m | Medium |
| 16.9 | `diagnose_fit` | 1h | Medium |
| 16.10 | The ablation table | 2h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 16.E1 | Implement GroupNorm and RMSNorm; compare all four normalizations | 2h | High — RMSNorm is what Llama uses (Week 33) |
| 16.E2 | Stochastic depth (randomly skip residual blocks) | 1.5h | Medium |
| 16.E3 | Implement CutMix and compare against Mixup on the vision data you meet in Month 6 | 2h | Medium |

---

## If You Finish Early

Priority: Week 14's gradient checkpointing (previews Week 49), Week 16's RMSNorm (previews Week 33), Week 15's trajectory visualization. Then the capstone's convolution stretch goal, which makes Month 6 a review.
