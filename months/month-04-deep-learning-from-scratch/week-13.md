# Week 13: Perceptrons and MLP Foundations

## Outcome

By Sunday you can implement forward passes for a full network — Linear, ReLU, Sigmoid, Tanh, GELU, Softmax, Sequential — and train an MLP to solve XOR.

Concretely: the week-13 tests in `test_backprop.py` and `test_neural_net.py` pass.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Why can't a perceptron learn XOR?" is the classic opening question and the
answer — XOR is not linearly separable, and a hidden layer lets the network learn
a representation in which it is — is the entire justification for depth.

The initialization material matters more than it looks. He and Xavier
initialization are not folklore; they keep activation variance roughly constant
across depth, and you will *see* that in the exercises when a badly-initialized
six-layer network collapses to zero activation. That observation is what makes
the Week 30 residual-scaling detail make sense.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The perceptron**
   1. Linear decision boundaries
   2. Why XOR is impossible
   3. How a hidden layer creates a separable representation
2. **Layers as functions**
   1. The forward/backward contract
   2. Why the forward pass caches activations, and what that costs in memory
   3. Composition in `Sequential`
3. **Activations**
   1. ReLU: no positive-side saturation, and the dead-unit failure mode
   2. Sigmoid: the 0.25 gradient ceiling, quantified
   3. Tanh: zero-centered, and why that helps
   4. GELU: smooth, and what every modern transformer uses
4. **Initialization**
   1. Why zeros never break symmetry
   2. He initialization for ReLU: std = sqrt(2/fan_in)
   3. Xavier for tanh: std = sqrt(1/fan_in)
   4. Watching variance collapse or explode across depth
5. **Minibatching**
   1. Why not full batch, why not single example
   2. Shuffling every epoch, not once

## Required Free Resources

- **Primary:** d2l.ai chapters 4-5 (MLPs, numerical stability, initialization) — https://d2l.ai/
- **Primary:** CS231n notes on neural networks — https://cs231n.github.io/neural-networks-1/ and /neural-networks-2/
- 3Blue1Brown, Neural Networks ch. 1-2 — https://www.3blue1brown.com/topics/neural-networks
- 'Delving Deep into Rectifiers' (He et al., 2015) — https://arxiv.org/abs/1502.01852 — the He initialization paper, and short

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=13
```

1. **`Layer` base class and `Linear.forward`** (1h) — Get the shapes right; write them in comments.
2. **ReLU, Sigmoid, Tanh forward** (45m) — Verify sigmoid's derivative peaks at 0.25.
3. **GELU forward** (45m) — Use the tanh approximation. You will meet it again in Week 30.
4. **`Softmax` forward, stably** (30m) — Subtract the max.
5. **`Sequential`** (45m) — Forward in order. Six lines.
6. **He and Xavier initialization** (1h) — Then run signal through six layers and measure activation std at each.
7. **The initialization failure demo** (45m) — Scale weights by 0.1 and watch the signal die. This is the week's key observation.
8. **`iterate_minibatches`** (45m) — Shuffle every epoch. Verify with a test.
9. **`MLP` and XOR** (1.5h) — Four data points, one hidden layer. The classic.

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
m
l
-
f
r
o
m
-
s
c
r
a
t
c
h
/
s
r
c
/
n
e
u
r
a
l
_
n
e
t
.
p
y
```

## Tests To Write

The week-13 blocks in `tests/test_backprop.py` and `tests/test_neural_net.py`. Add one: a test that a network with all-zero initialization produces identical gradients for every hidden unit — the symmetry that never breaks.

## Portfolio Artifact

`src/neural_net.py` forward passes, plus a notebook figure showing activation variance across depth for He, Xavier, and a deliberately bad initialization.

## Interview Drills

**Coding (45 min).** Two problems, arrays and two pointers. New rotation cycle.

**ML theory (20 min).** Recorded: *Why can't a perceptron learn XOR? Draw it.* Then: *Why does initialization matter? What breaks with zeros, and what breaks with values that are too large?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement a `Dense` layer that supports arbitrary batch dimensions — (B, T, d) as well as (B, d). You need this in Week 30 for transformers, and doing it now means the shape handling is already familiar.
