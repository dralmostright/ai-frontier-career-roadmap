# Week 03: Calculus and Gradients

## Outcome

By Sunday you have built a working reverse-mode automatic differentiation engine
and used it to train a model by gradient descent. You can derive and implement
gradients for the losses used throughout the rest of the course, and verify any
gradient numerically.

Concretely: `bootstrap/math-labs/tests/test_gradients.py` passes, including
`test_gradient_descent_fits_a_line` — your engine, and nothing else, fitting
y = 2x + 1.

**This is the most important week of Month 1.** When it is done, PyTorch's
`.backward()` is no longer magic.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Derive gradient descent for linear regression" and "derive the softmax +
cross-entropy gradient" are asked in essentially every ML screen. They are asked
because they are cheap to pose and they cleanly separate people who have done the
derivation from people who have read about it.

The deeper payoff is debugging. When a training run produces NaN at step 400, or
a loss that plateaus at exactly ln(C), the engineers who diagnose it in ten
minutes are the ones who know what the framework is computing. You will hit
exactly this in Weeks 19, 32, and 35, and this week is what makes those hours
instead of days.

The `p - y` cancellation — that softmax composed with cross-entropy has the
gradient `predicted minus actual`, with everything else cancelling — is one of
the most elegant results in the field and one of the most frequently asked. Derive
it by hand this week and you will never forget it.

## Time Budget: 15-20 Hours

- Theory: 4 hours
- Coding: 8 hours
- Project: 2 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Derivatives, reconsidered**
   1. The derivative as a local linear approximation
   2. Partial derivatives and the gradient vector
   3. The gradient as the direction of steepest ascent — and why gradient
      *descent* therefore steps against it
2. **The chain rule**
   1. Single variable, then multivariable
   2. Composition of functions as composition of derivatives
   3. The multivariable case: when a variable feeds several consumers, its
      gradients **sum**. This is why autodiff accumulates with `+=`.
3. **Computational graphs**
   1. Any expression as a DAG of operations
   2. Forward mode versus reverse mode
   3. Why reverse mode wins for machine learning: one backward pass yields all n
      partial derivatives, where forward mode needs n passes. With 7 billion
      parameters that difference is the entire field.
4. **Reverse-mode automatic differentiation**
   1. Topological ordering, and why it guarantees correctness
   2. Local derivatives at each node
   3. Seeding the output gradient at 1.0
   4. Gradient accumulation
5. **Numerical differentiation and gradient checking**
   1. Forward difference, O(h) error
   2. Central difference, O(h²) error for the same cost
   3. Choosing h: truncation error versus floating-point cancellation
   4. Relative versus absolute error, and why relative is the only sane choice
6. **The gradients you must know cold**
   1. MSE with respect to the prediction, then to the weights
   2. Sigmoid, and why its derivative caps at 0.25
   3. Binary cross-entropy composed with sigmoid → `p - y`
   4. Softmax composed with cross-entropy → `p - onehot(y)`
   5. Why the fused form is both faster and numerically stabler
7. **Numerical stability**
   1. The log-sum-exp trick, and why softmax subtracts the max
   2. Clamping inside logarithms
   3. Why you sum log-probabilities instead of multiplying probabilities

## Required Free Resources

**Primary — watch this first, in full (~2.5 hours):**
- Karpathy, "The spelled-out intro to neural networks and backpropagation:
  building micrograd" — https://karpathy.ai/zero-to-hero.html

  Then **close it and write your own from memory.** Transcribing it teaches you
  nothing; rebuilding it teaches you everything. Consult it only when genuinely
  stuck, and then close it again.

- 3Blue1Brown, Essence of Calculus, chapters 1-4 —
  https://www.3blue1brown.com/topics/calculus
- 3Blue1Brown, Neural Networks chapters 3-4 (backpropagation) —
  https://www.3blue1brown.com/topics/neural-networks

**Reference:**
- micrograd source, ~150 lines — https://github.com/karpathy/micrograd
  Read this *after* yours works, and diff the designs.
- CS231n backpropagation notes — https://cs231n.github.io/optimization-2/
  The best written treatment of gradient flow through a graph.
- The Matrix Cookbook — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
  Keep it open from Week 14 onward.

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=3
```

1. **Derive on paper first** (1.5h). Before writing any code, derive by hand:
   the MSE gradient, the sigmoid derivative, sigmoid+BCE, and softmax+cross-
   entropy. Photograph the pages and put them in the notebook. If you cannot
   derive it, implementing it teaches you nothing.
2. **The `Value` class** (2h) — arithmetic operations with their backward
   closures. The critical detail: `+=`, never `=`. A graph where any node feeds
   two consumers will give silently wrong gradients otherwise, and
   `test_diamond_graph` exists to catch exactly that.
3. **Activations** (1h) — `exp`, `log`, `tanh`, `relu`, `sigmoid`. Note that
   tanh's and sigmoid's derivatives are expressible in terms of their *outputs* —
   cache the forward result and reuse it. That trick is why frameworks store
   activations, and why activation memory dominates training memory in Week 49.
4. **The backward pass** (1.5h) — `topological_sort`, `backward`, `zero_grad`.
   Seed the output gradient at 1.0 and walk the sort in reverse.
5. **Gradient checking** (1.5h) — `numerical_gradient`, `gradient_check`. Use
   central differences and relative error. **This is the most valuable function
   in the entire bootstrap workspace.** You will use it in Weeks 14, 29, 30, and
   67.
6. **Losses** (1.5h) — `mse_loss`, `binary_cross_entropy`, `softmax`,
   `cross_entropy`. Implement the softmax max-subtraction and the BCE clamping;
   there are tests that specifically check you did.
7. **Train something** (1h) — make `test_gradient_descent_fits_a_line` pass.
   Your engine, your losses, your gradient descent, fitting an actual model. This
   is the moment the week pays off.

## Bootstrap Files To Create

Implement:

```text
bootstrap/math-labs/src/autodiff_scalar.py
```

Create:

```text
bootstrap/math-labs/notebooks/autodiff_walkthrough.ipynb
```

The notebook should include: your handwritten derivations (photographed), a
visualization of a small computational graph with gradients annotated on each
edge, and the loss curve from the line-fitting exercise.

## Tests To Write

`tests/test_gradients.py` is the specification. Add three:

1. Gradient-check a deeply nested expression — at least eight composed
   operations — and confirm relative error below 1e-6.
2. A test that `zero_grad` resets the *entire* ancestry, not just the node it was
   called on.
3. A test demonstrating that BCE without clamping produces `inf`, and that yours
   does not. Write it as a regression test with a comment explaining the bug.

## Portfolio Artifact

- `src/autodiff_scalar.py` — a working autodiff engine
- `notebooks/autodiff_walkthrough.ipynb` — derivations, graph visualization,
  training curve

This one is worth featuring modestly. "I wrote my own autodiff engine before
touching PyTorch" is a credible, checkable claim and it makes everything you say
about deep learning later carry more weight.

## Interview Drills

**Coding (45 min).** Two problems, strings and sliding window. Timed.

**ML theory — the big one (30 min).** Whiteboard, out loud, recorded:

> 1. Derive gradient descent for linear regression. Start from the loss.
> 2. Derive the gradient of softmax composed with cross-entropy. Show the
>    cancellation.

For question 2, a 9/10 answer writes out the softmax Jacobian, applies the chain
rule, splits the i = j and i ≠ j cases, and shows the terms collapsing to
`p - y`. Practice until you can do it in four minutes without hesitating.

**Debugging drill (15 min).** Answer out loud:

> Your loss is NaN at step 400. Walk me through your diagnosis, in priority
> order.

The ordered checklist: check for `log(0)` or division by zero in the loss;
check the learning rate; check for exploding gradients and whether clipping is
on; check the data for NaNs or infinities; check for numerical overflow in an
exponential. Being *ordered* is the point — anyone can list causes, and the
signal is knowing which to check first.

## Evaluation Rubric

| Score | Standard |
| ----- | -------- |
| 3 | Followed the video, code is a transcription, gradients not checked. |
| 5 | Engine works for simple expressions. Diamond-graph test fails. |
| 7 | All tests pass. Gradient checking works. Can derive MSE and sigmoid+BCE. |
| 9 | Above, plus the line-fitting test passes, and you can derive softmax+cross-entropy on a whiteboard in under 5 minutes without notes. |
| 10 | Above, plus you can explain why reverse mode beats forward mode for ML with the complexity argument, and your gradient checker caught a real bug this week. |

**Do not score above 7 if you cannot derive at least two of the four gradients
unaided.** This is the week where inflated self-assessment costs the most later.

## Stretch Goal

Extend `Value` to support arrays instead of scalars — a minimal tensor autodiff.
You need broadcasting-aware backward passes, which is genuinely harder: the
gradient of a broadcast operation must be summed back down to the original shape.

Getting this right is the core difficulty of Week 14, so doing it now converts
Month 4 from a struggle into a review. It is also the exercise that makes you
understand why shape errors are the most common bug in deep learning code.
