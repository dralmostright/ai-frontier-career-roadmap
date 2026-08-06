# Month 04 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Karpathy, 'A Recipe for Training Neural Networks'** — https://karpathy.github.io/2019/04/25/recipe/
Read it twice, in Week 16 and again in Week 19. It is the best practical guide to
debugging training runs that exists, and the overfit-a-single-batch discipline
comes from here.

**CS231n backpropagation notes** (Week 14) — https://cs231n.github.io/optimization-2/
The clearest written treatment of gradient flow through a computational graph.

**Distill, 'Why Momentum Really Works'** (Week 15) — https://distill.pub/2017/momentum/
Interactive, and it makes the ravine problem visceral in a way no static
explanation does.

---

## Week 13 — Perceptrons and MLP Foundations

- **Primary:** d2l.ai chapters 4-5 (MLPs, numerical stability, initialization) — https://d2l.ai/
- **Primary:** CS231n notes on neural networks — https://cs231n.github.io/neural-networks-1/ and /neural-networks-2/
- 3Blue1Brown, Neural Networks ch. 1-2 — https://www.3blue1brown.com/topics/neural-networks
- 'Delving Deep into Rectifiers' (He et al., 2015) — https://arxiv.org/abs/1502.01852 — the He initialization paper, and short
## Week 14 — Backpropagation

- **Primary:** CS231n, backpropagation notes — https://cs231n.github.io/optimization-2/ — the best written treatment of gradient flow anywhere
- **Primary:** d2l.ai ch. 5.3 (forward and backward propagation) — https://d2l.ai/
- CS231n gradient checking notes — https://cs231n.github.io/neural-networks-3/#gradcheck
- The Matrix Cookbook — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf — keep it open all week
## Week 15 — Optimization

- **Primary:** d2l.ai ch. 12 (optimization algorithms) — https://d2l.ai/
- **Primary:** Distill, 'Why Momentum Really Works' — https://distill.pub/2017/momentum/ — the best explanation of momentum in existence, and interactive
- 'Adam: A Method for Stochastic Optimization' — https://arxiv.org/abs/1412.6980
- 'Decoupled Weight Decay Regularization' (AdamW) — https://arxiv.org/abs/1711.05101 — read section 2; it is the whole argument
- 'Cyclical Learning Rates' (Smith, 2015) — https://arxiv.org/abs/1506.01186 — the LR range test
## Week 16 — Regularization and Generalization

- **Primary:** d2l.ai ch. 5.6 (dropout), 8.5 (batch norm) — https://d2l.ai/
- **Primary:** Karpathy, 'A Recipe for Training Neural Networks' — https://karpathy.github.io/2019/04/25/recipe/ — read this twice. It is the single best practical guide to debugging training, and the overfit-a-single-batch advice comes from here.
- 'Batch Normalization' (Ioffe and Szegedy, 2015) — https://arxiv.org/abs/1502.03167
- 'How Does Batch Normalization Help Optimization?' (Santurkar et al., 2018) — https://arxiv.org/abs/1805.11604 — the paper that displaced the original explanation
- 'Layer Normalization' — https://arxiv.org/abs/1607.06450

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| PyTorch | https://pytorch.org/docs/stable/ | Months 5+ |
| d2l.ai | https://d2l.ai/ | The primary DL textbook for Phase 2-3 |
| Hugging Face | https://huggingface.co/docs | Months 7+ |
| pytest | https://docs.pytest.org/ | The workspace |
| NeetCode 150 | https://neetcode.io/practice | Weekly coding drills |

---

## Deliberately Omitted

- **Convolution.** Deferred to Week 21 where it is the subject rather than a
  distraction.
- **RNNs and LSTMs.** Historically important, largely displaced. Week 25-28 covers
  what you need; know that they exist and why attention replaced them.
- **Second-order optimization (L-BFGS, K-FAC).** Rarely used for deep learning at
  scale, rarely asked.
- **Neural architecture search.** Interesting, not load-bearing.
