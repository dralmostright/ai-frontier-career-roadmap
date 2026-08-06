# Week 14: Backpropagation

## Outcome

By Sunday every layer has a correct backward pass, verified numerically, and you can derive backpropagation for a two-layer MLP on a whiteboard.

Concretely: `test_end_to_end_gradient_check` passes with relative error below 1e-6.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The load-bearing week of Phase 2.** "Derive backpropagation" is asked in
essentially every deep learning screen, and the answer requires having done it.

The calculus is Week 3's chain rule. The difficulty is entirely shapes: dL/dW has
the shape of W, dL/dx has the shape of x, and once you write the shapes down the
transposes place themselves. That trick — derive by shape, not by memory — is
worth internalizing because it works for attention too.

Gradient checking is the other deliverable, and it is the more valuable one
long-term. A wrong gradient does not crash. It trains slowly to a worse optimum
while you blame the learning rate for four days.

## Time Budget: 15-20 Hours

- Theory: 3.5 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Backprop as reverse-mode autodiff**
   1. Reverse topological order
   2. Why `Sequential.backward` runs in reverse — that reversal *is* the algorithm
   3. Local gradients times the incoming gradient
2. **Layer gradients**
   1. Linear: dL/dW = x^T g, dL/db = sum(g), dL/dx = g W^T
   2. Deriving each by shape rather than by memory
   3. Activation gradients, and reusing the cached forward output
3. **Losses, fused**
   1. MSE
   2. Cross entropy fused with softmax: the p-y result
   3. Why frameworks warn against applying softmax before CrossEntropyLoss
   4. The ln(C) initial-loss check
4. **Gradient checking**
   1. Central differences
   2. Relative error, and the interpretation thresholds
   3. Why float64 is required
5. **Diagnostics**
   1. Gradient norms per layer, and what their shape tells you
   2. Vanishing: norms shrinking geometrically with depth
   3. Exploding: norms in the thousands
   4. Global-norm clipping, and why not per-parameter

## Required Free Resources

- **Primary:** CS231n, backpropagation notes — https://cs231n.github.io/optimization-2/ — the best written treatment of gradient flow anywhere
- **Primary:** d2l.ai ch. 5.3 (forward and backward propagation) — https://d2l.ai/
- CS231n gradient checking notes — https://cs231n.github.io/neural-networks-3/#gradcheck
- The Matrix Cookbook — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf — keep it open all week

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=14
```

1. **Derive on paper: Linear, ReLU, Sigmoid, Tanh gradients** (1.5h) — Shapes first. Photograph the pages.
2. **`numerical_gradient` and `relative_error`** (45m) — Central difference; operate on a copy.
3. **`gradient_check_layer`** (1.5h) — The most valuable function in the workspace.
4. **`Linear.backward`** (1h) — Check it immediately.
5. **Activation backwards** (1h) — All five. Check each.
6. **`Softmax.backward`** (1h) — The dense Jacobian. Then note why fusing with CE avoids it.
7. **`CrossEntropyLoss` fused** (1.5h) — Verify the initial loss is ln(C) and the gradient is (p-y)/n.
8. **`Sequential.backward`** (45m) — Reverse order. Verify with a tracer that it really runs backwards.
9. **`gradient_norms`, `check_gradient_flow`** (1h) — Then build a 12-layer sigmoid network and watch gradients vanish.
10. **`clip_gradients` by global norm** (45m) — Verify it preserves direction.

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
b
a
c
k
p
r
o
p
.
p
y
```

## Tests To Write

`tests/test_backprop.py` week-14 blocks. Add one: a test that a 12-layer sigmoid network's first-layer gradient norm is at least 1000x smaller than its last-layer norm — vanishing gradients, quantified.

## Portfolio Artifact

`src/backprop.py` with every layer gradient-checked, plus the vanishing-gradient figure.

## Interview Drills

**Coding (45 min).** Two problems, hash maps.

**ML theory (30 min).** Whiteboard, recorded: *Derive backpropagation for a two-layer MLP.* Then: *Explain vanishing gradients. Give three causes and three fixes.* Practice until the derivation takes under five minutes.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement gradient checkpointing: discard intermediate activations during the forward pass and recompute them during backward. Measure the memory saving and the compute cost. This is the technique that makes large-model training fit in memory (Week 49), and implementing it small makes the tradeoff concrete.
