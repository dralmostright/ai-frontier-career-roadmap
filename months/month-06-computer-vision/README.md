# Month 06: Computer Vision

**Weeks 21-24 · Phase 2: Deep Learning Mastery · Lab: `bootstrap/pytorch-labs/`**

---

## The Month In One Sentence

Use vision as the cheapest domain in which to practise full training pipelines, then ship a model behind an API and measure its latency.

## Why This Month Exists

Vision is not your destination, and this month is scoped accordingly. It is
here for three reasons.

Vision datasets are small, fast, and **visually debuggable** — when a model is
wrong you can look at what it got wrong. That feedback loop does not exist for
language models, so you learn the pipeline here and apply it there.

CNNs are still asked about. Receptive fields, residual connections, and the
CNN-versus-ViT inductive bias question come up, and the residual-connection
answer transfers directly to Week 30.

Month 6 produces your first *deployed* artifact. Training a model and serving one
are different skills, and the latency-versus-batch-size curve you measure this
month is your first real systems result.

**This is the compressible month.** If you are certain you are targeting LLM-only
roles and you need time, cut Weeks 23-24 to one week. Do it knowingly, accepting
the loss of CNN interview coverage — not by drift.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 21 | CNNs | `cnn.py`; CIFAR-10 above 80% |
| 22 | ResNet and Modern CNNs | `resnet.py` + the depth-with-and-without-residuals plot |
| 23 | Transfer Learning | `transfer.py`; a fine-tuned model with a freeze ablation |
| 24 | Vision Transformers and Serving | `vit.py`, `serve.py`; the Month 6 capstone |

**Capstone:** Image Classification Service — a trained classifier behind a containerized API, with measured latency and a model card.

## The Through-Lines

**Residual connections.** The gradient argument you learn in Week 22 is the same
one that makes deep transformers trainable in Week 30.

**Transfer learning.** The freeze/fine-tune decision in Week 23 is the same
decision as full-tune versus LoRA in Week 46.

**Patches are tokens.** Week 24's ViT turns an image into a sequence, at which
point it is exactly the transformer you build in Month 8.

**Serving is measurement.** Week 24's latency percentiles and batching curve are
the first instance of the systems thinking that dominates Phase 5.

## Time and Compute

15-20 hours per week. A GPU helps significantly. Kaggle's free weekly GPU hours or Colab are sufficient; CIFAR-10 trains in minutes on a T4.

## Files

```text
month-06-computer-vision/
  README.md      you are here
  week-21.md     cnns
  week-22.md     resnet and modern cnns
  week-23.md     transfer learning
  week-24.md     vision transformers and serving
  capstone.md    image classification service
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 22.** Residual connections are the concept with the highest transfer value to Month 8. Weeks 23-24 are the compressible ones.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Wrong normalization for a pretrained model | Accuracy quietly lower, no error | ImageNet models expect ImageNet mean and std. |
| Freezing BatchNorm parameters but not calling `.eval()` | Running stats drift on the new data | Freeze both. |
| Reporting mean latency | Hides the p99 that users feel | Percentiles. Always. |
| Serving without warmup | First users get the worst latency | Run a dozen dummy batches at startup. |
| Same transforms for train and eval | Augmentation applied at inference | Separate pipelines. |

## Advancement

Before Month 7, you should be able to, without notes:

- [ ] Compute the receptive field of a given CNN stack
- [ ] Explain why residual connections make deep networks trainable, via gradient flow
- [ ] Decide what to freeze when fine-tuning, and justify it by dataset size
- [ ] Say when a ViT beats a CNN, with the data-scale reasoning
- [ ] Report p50/p95/p99 for a served model and explain the batching tradeoff
- [ ] Point at a containerized inference service with a measured latency curve

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 7 — NLP Foundations. Phase 3 begins, and your first AI+database fusion project.
