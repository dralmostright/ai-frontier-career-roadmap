# Week 22: ResNet and Modern CNNs

## Outcome

By Sunday you can implement a residual block, train a small ResNet, and demonstrate empirically that plain networks get worse past a certain depth while residual ones keep improving.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The highest-transfer week of Month 6.** "Why do residual connections work?" is
asked about CNNs and about transformers, and the answer is the same: the
derivative of (x + F(x)) with respect to x is 1 + F'(x), and that identity term
means gradient reaches early layers undiminished no matter how small F' becomes.

Without residuals, gradient is a product of many terms and vanishes
geometrically with depth. With them, there is always a path of derivative 1.

You will reimplement this in Week 30. Producing the depth-comparison plot
yourself — plain networks degrading, residual ones not — makes the argument
something you have seen rather than read.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7.5 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The degradation problem**
   1. Deeper plain networks perform *worse* on training data, not just test
   2. Why this is not overfitting
   3. What the original ResNet paper actually demonstrated
2. **Residual connections**
   1. out = F(x) + x
   2. The gradient argument: 1 + F'(x)
   3. Identity versus projection shortcuts, and when you need the 1x1 conv
3. **ResNet architecture**
   1. Basic block versus bottleneck
   2. Stage structure and downsampling
   3. Why BN goes inside the residual branch
4. **Pre-activation and after**
   1. Pre-activation ResNet (BN-ReLU-Conv)
   2. Why pre-norm won, in CNNs and later in transformers
   3. DenseNet, and concatenation versus addition
5. **Residual scaling**
   1. Why deep residual streams need initialization scaling
   2. The 1/sqrt(2*n_layers) factor you will need in Week 30

## Required Free Resources

- **Primary:** 'Deep Residual Learning' (He et al., 2015) — https://arxiv.org/abs/1512.03385 — read it properly; it is short, clear, and you will cite it in interviews
- **Primary:** d2l.ai ch. 8.6 (ResNet) — https://d2l.ai/
- 'Identity Mappings in Deep Residual Networks' — https://arxiv.org/abs/1603.05027 — the pre-activation follow-up
- 'Visualizing the Loss Landscape of Neural Nets' — https://arxiv.org/abs/1712.09913 — the figures showing what residuals do to the loss surface are memorable

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=22
```

1. **`ResidualBlock`** (1.5h) — Including the 1x1 projection when shape changes.
2. **Verify gradient flow through the identity path** (45m) — Confirm the early-layer gradient is not vanishing.
3. **`ResNet` from blocks** (1.5h) — Stage structure with downsampling.
4. **Plain networks at depth 8, 20, 56** (2h) — Train all three. Watch the deepest get worse.
5. **Residual networks at the same depths** (1.5h) — Watch them not.
6. **`compare_depth_with_and_without_residuals`** (1h) — The week's deliverable figure.
7. **Gradient norm by layer, both architectures** (1h) — The mechanism, made visible.

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
r
e
s
n
e
t
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
r
e
s
n
e
t
1
8
.
y
a
m
l
```

## Tests To Write

`tests/test_pytorch_labs.py` week-22 blocks. Add one: a 30-layer plain network's first-layer gradient norm is at least 100x smaller than a 30-layer residual network's, on the same data.

## Portfolio Artifact

`src/resnet.py` and the depth-comparison figure — accuracy against depth for plain and residual networks, on the same axes. That single plot is the whole argument.

## Interview Drills

**Coding (45 min).** Two problems, recursion.

**ML theory (25 min).** Recorded: *Why do residual connections make deep networks trainable?* Answer with the gradient argument, not intuition. Then: *What is the degradation problem, and why is it not overfitting?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Reproduce the loss-landscape visualization from Li et al. for a plain and a residual network. It requires filter-normalized random directions and a 2-D loss grid, and the resulting figures — a chaotic landscape versus a smooth bowl — are the most convincing explanation of residual connections that exists. Good practice for Month 16 too.
