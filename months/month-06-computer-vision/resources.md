# Month 06 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**'Deep Residual Learning'** (Week 22) — https://arxiv.org/abs/1512.03385
Short, clear, foundational. Read it properly — you will cite it when explaining
transformers too.

**CS231n convolutional networks notes** (Week 21) — https://cs231n.github.io/convolutional-networks/
The best written treatment of convolution arithmetic and architecture patterns.

**'An Image is Worth 16x16 Words'** (Week 24) — https://arxiv.org/abs/2010.11929
The ViT paper, and the source of the data-scale finding you will quote.

---

## Week 21 — CNNs

- **Primary:** CS231n convolutional networks notes — https://cs231n.github.io/convolutional-networks/ — the best written treatment
- **Primary:** d2l.ai ch. 7 (CNNs) — https://d2l.ai/
- 'A guide to convolution arithmetic' — https://arxiv.org/abs/1603.07285 — the shape formulas, with figures
- Distill, 'Feature Visualization' — https://distill.pub/2017/feature-visualization/ — what CNN filters actually learn
## Week 22 — ResNet and Modern CNNs

- **Primary:** 'Deep Residual Learning' (He et al., 2015) — https://arxiv.org/abs/1512.03385 — read it properly; it is short, clear, and you will cite it in interviews
- **Primary:** d2l.ai ch. 8.6 (ResNet) — https://d2l.ai/
- 'Identity Mappings in Deep Residual Networks' — https://arxiv.org/abs/1603.05027 — the pre-activation follow-up
- 'Visualizing the Loss Landscape of Neural Nets' — https://arxiv.org/abs/1712.09913 — the figures showing what residuals do to the loss surface are memorable
## Week 23 — Transfer Learning

- **Primary:** PyTorch transfer learning tutorial — https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- **Primary:** CS231n transfer learning notes — https://cs231n.github.io/transfer-learning/ — the decision table originates here
- 'How transferable are features in deep neural networks?' — https://arxiv.org/abs/1411.1792 — the empirical study behind the folklore
- timm documentation — https://huggingface.co/docs/timm — the standard model zoo
## Week 24 — Vision Transformers and Serving

- **Primary:** 'An Image is Worth 16x16 Words' (Dosovitskiy et al.) — https://arxiv.org/abs/2010.11929 — the ViT paper. Read it; you will reference the data-scale finding.
- **Primary:** FastAPI docs — https://fastapi.tiangolo.com/
- Lucas Beyer, 'Vision Transformers' lecture notes — good on the inductive bias argument
- 'Do Vision Transformers See Like Convolutional Neural Networks?' — https://arxiv.org/abs/2108.08810

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| PyTorch | https://pytorch.org/docs/stable/ | Everything |
| d2l.ai | https://d2l.ai/ | The primary textbook |
| Hugging Face | https://huggingface.co/docs | Months 7+ |
| pgvector | https://github.com/pgvector/pgvector | Month 7 capstone |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| timm | https://huggingface.co/docs/timm | Pretrained vision models |
| FastAPI | https://fastapi.tiangolo.com/ | Week 24 serving |
| locust | https://locust.io/ | Load testing |

---

## Deliberately Omitted

- **Object detection and segmentation.** Large subfields, rarely asked outside
  vision-specific roles, and not load-bearing for anything later.
- **GANs and diffusion models.** Fascinating, and a different track. Know the
  one-line summary of each.
- **Video and 3D vision.** Out of scope.
- **Advanced augmentation (AutoAugment, RandAugment).** Use them as tools if you
  like; the theory is not asked.
