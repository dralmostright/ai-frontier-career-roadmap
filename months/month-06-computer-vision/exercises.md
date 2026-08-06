# Month 06 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 21 — CNNs

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 21.1 | `conv2d_naive` with explicit loops | 1.5h | Medium |
| 21.2 | `output_shape` | 30m | Easy |
| 21.3 | `receptive_field` | 1h | Medium |
| 21.4 | `SimpleCNN` | 1.5h | Medium |
| 21.5 | Train on CIFAR-10 | 2h | Medium |
| 21.6 | Augmentation ablation | 1h | Medium |
| 21.7 | Visualize first-layer filters | 45m | Easy |
| 21.8 | Misclassification grid | 45m | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 21.E1 | Implement im2col and show convolution is a matmul | 2h | High — explains how it is actually computed |
| 21.E2 | Depthwise separable convolution; compare parameters and accuracy | 2h | High — the MobileNet idea |
| 21.E3 | Grad-CAM to visualize what the model attends to | 2h | High — great figure, and previews attention |

## Week 22 — ResNet and Modern CNNs

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 22.1 | `ResidualBlock` | 1.5h | Medium |
| 22.2 | Verify gradient flow through the identity path | 45m | Medium |
| 22.3 | `ResNet` from blocks | 1.5h | Medium |
| 22.4 | Plain networks at depth 8, 20, 56 | 2h | Hard |
| 22.5 | Residual networks at the same depths | 1.5h | Medium |
| 22.6 | `compare_depth_with_and_without_residuals` | 1h | Medium |
| 22.7 | Gradient norm by layer, both architectures | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 22.E1 | Implement pre-activation ResNet and compare | 1.5h | High — the pre-norm question again |
| 22.E2 | Stochastic depth: randomly drop residual blocks during training | 2h | Medium |
| 22.E3 | Plot the loss landscape with and without residuals | 3h | High — striking figure, real insight |

## Week 23 — Transfer Learning

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 23.1 | `load_pretrained` with head replacement | 1h | Medium |
| 23.2 | `freeze_layers` and verify | 45m | Easy |
| 23.3 | The BatchNorm trap demo | 1h | Hard |
| 23.4 | `discriminative_learning_rates` | 1h | Medium |
| 23.5 | Fine-tune on a small dataset | 2h | Medium |
| 23.6 | The freeze ablation | 1.5h | Medium |
| 23.7 | Wrong-normalization demo | 45m | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 23.E1 | Gradual unfreezing with a schedule; compare against one-shot | 2h | Medium |
| 23.E2 | Linear probing vs fine-tuning across dataset sizes; find the crossover | 2.5h | High — the empirical decision table |
| 23.E3 | Fine-tune on a genuinely dissimilar domain (medical or satellite imagery) | 2h | High — tests the similarity axis |

## Week 24 — Vision Transformers and Serving

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 24.1 | `PatchEmbedding` | 1h | Medium |
| 24.2 | `VisionTransformer` | 2h | Hard |
| 24.3 | `cnn_vs_vit_comparison` | 1.5h | Hard |
| 24.4 | `InferenceService` with warmup | 1h | Medium |
| 24.5 | `measure_latency` | 1h | Medium |
| 24.6 | `DynamicBatcher` | 1.5h | Hard |
| 24.7 | `latency_vs_batch_size` | 1h | Medium |
| 24.8 | Containerize and measure image size | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 24.E1 | Quantize to INT8 and measure the latency/accuracy tradeoff | 2h | High — previews Week 52 |
| 24.E2 | Export to ONNX and compare runtime performance | 2h | High |
| 24.E3 | Load test with locust and find the saturation point | 2h | High — a real capacity number for the README |

---

## If You Finish Early

Priority: Week 24's INT8 quantization table (previews Week 52), Week 21's Grad-CAM (good figure, previews attention), Week 22's loss landscape (striking, and good Month 16 practice). If you are compressing this month, skip the extensions entirely and move to Month 7.
