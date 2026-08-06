# Week 21: CNNs

## Outcome

By Sunday you can implement convolution by hand, compute receptive fields, and train a CNN to over 80% on CIFAR-10.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The receptive field calculation is a standard interview question with a
mechanical answer, and the inductive-bias framing — locality and translation
equivariance as *priors built into the architecture* — is the setup for the
Week 24 ViT comparison.

Writing convolution as explicit loops before calling `nn.Conv2d` is the same
discipline as Month 4: it makes the layer legible, and it makes `im2col` and the
"convolution is a matrix multiply" observation land.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Convolution**
   1. Kernels, stride, padding, dilation
   2. The output-shape formula, memorized
   3. Why parameter sharing beats a fully-connected layer on images
   4. Convolution as a matrix multiply (im2col)
2. **Inductive bias**
   1. Locality: nearby pixels relate
   2. Translation equivariance: a cat is a cat anywhere
   3. Why these priors let CNNs win with far fewer parameters
3. **Pooling and downsampling**
   1. Max versus average
   2. Stride as an alternative to pooling
   3. Why classification networks downsample aggressively
4. **Receptive fields**
   1. The backward recurrence
   2. Linear growth with depth, exponential with stride
   3. Why the final layer must see the whole image
5. **Architecture patterns**
   1. Conv-BN-ReLU order, and why BN before the activation
   2. `bias=False` when BN follows
   3. Channel progression

## Required Free Resources

- **Primary:** CS231n convolutional networks notes — https://cs231n.github.io/convolutional-networks/ — the best written treatment
- **Primary:** d2l.ai ch. 7 (CNNs) — https://d2l.ai/
- 'A guide to convolution arithmetic' — https://arxiv.org/abs/1603.07285 — the shape formulas, with figures
- Distill, 'Feature Visualization' — https://distill.pub/2017/feature-visualization/ — what CNN filters actually learn

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=21
```

1. **`conv2d_naive` with explicit loops** (1.5h) — Verify against `F.conv2d`. Slow and clarifying.
2. **`output_shape`** (30m) — Memorize the formula. It resolves every shape error.
3. **`receptive_field`** (1h) — The backward recurrence. Verify: three 3x3 convs see 7x7.
4. **`SimpleCNN`** (1.5h) — Conv-BN-ReLU blocks. `bias=False` before BN.
5. **Train on CIFAR-10** (2h) — Target >80%. Use the Month 5 pipeline unchanged.
6. **Augmentation ablation** (1h) — No augmentation, flip only, flip+crop. Report the table.
7. **Visualize first-layer filters** (45m) — They learn edge detectors. Seeing it is worth the time.
8. **Misclassification grid** (45m) — Look at what it got wrong. Week 12's method, new domain.

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
c
n
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
c
o
n
f
i
g
s
/
c
i
f
a
r
1
0
.
y
a
m
l
```

## Tests To Write

`tests/test_pytorch_labs.py` week-21 blocks. Add one: `conv2d_naive` matches `F.conv2d` to 1e-5 across five random shape/stride/padding combinations.

## Portfolio Artifact

`src/cnn.py`, a CIFAR-10 run above 80%, the augmentation ablation table, and the filter visualization.

## Interview Drills

**Coding (45 min).** Two problems, matrix traversal — thematically apt.

**ML theory (20 min).** Recorded: *Compute the receptive field of a 3-layer CNN with 3x3 kernels and one stride-2 layer.* Then: *Why do CNNs beat MLPs on images with fewer parameters?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement Grad-CAM and produce a figure showing where the model looks for correct and incorrect predictions. It is a genuinely useful debugging tool, it makes a striking README figure, and it is conceptually a precursor to attention visualization in Week 30.
