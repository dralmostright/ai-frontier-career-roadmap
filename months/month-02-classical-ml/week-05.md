# Week 05: Linear Regression

## Outcome

By Sunday you can implement linear regression two ways — closed form and gradient descent — verify they agree, and demonstrate the bias-variance tradeoff empirically rather than describing it.

Concretely: `tests/test_linear_regression.py` passes, including `test_converges_to_the_closed_form_solution`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Explain the bias-variance tradeoff" is one of the two or three most common
opening ML questions. Most candidates recite the definition. A strong answer
*shows* the decomposition — which is why `bias_variance_decomposition` is in the
exercises rather than just the theory.

The other reason: the normal equation versus gradient descent contrast is the
first appearance of a theme that runs the whole course. Closed-form solutions are
exact and do not scale; iterative ones scale and require tuning. Every later
scaling decision is a version of this tradeoff.

Ridge as numerical stabilization — not just as a generalization trick — is worth
knowing. It is why ridge exists historically, and mentioning it separates you
from candidates who only know the regularization story.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Least squares**
   1. The loss surface, and why it is convex for a linear model
   2. The normal equation, derived by setting the gradient to zero
   3. Why `lstsq` beats forming an explicit inverse
   4. What happens when X^T X is singular
2. **Gradient descent**
   1. The update rule, and the 2/n factor
   2. Why batch size and learning rate are coupled
   3. Convergence, divergence, and reading a loss curve
   4. Feature scaling and why it changes the geometry
3. **Regularization**
   1. Ridge (L2): smooth shrinkage, and the numerical stability argument
   2. Lasso (L1): exact zeros, and why the constant gradient produces them
   3. Why the intercept is never penalized
   4. Ridge as MAP estimation with a Gaussian prior (connects to Week 4)
4. **Bias and variance**
   1. The decomposition of expected error
   2. Model complexity as the knob that trades one for the other
   3. Why more data reduces variance but not bias
   4. Demonstrating it empirically with polynomial features
5. **Regression metrics**
   1. MSE, MAE, RMSE — and what each one's outlier sensitivity buys you
   2. R-squared, and why it can be negative
   3. Reporting in the units of the target

## Required Free Resources

- **Primary:** CS229 lecture notes 1, sections 1-3 — https://cs229.stanford.edu/ — the cleanest derivation of least squares available free
- **Primary:** An Introduction to Statistical Learning, ch. 3 — https://www.statlearning.com/
- Elements of Statistical Learning, ch. 3.4 (shrinkage) — https://hastie.su.domains/ElemStatLearn/
- scikit-learn linear models guide — https://scikit-learn.org/stable/modules/linear_model.html — read after implementing
- StatQuest, 'Ridge and Lasso Regression' — good intuition for why L1 zeroes out

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=5
```

1. **`normal_equation` with optional ridge** (1h) — Use `lstsq`, not `inv`. Then construct a collinear design matrix and show ridge fixes it.
2. **`gradient_descent_step` and the GD path** (1.5h) — Derive dL/dw on paper first. Record the loss history and plot it.
3. **Verify the two methods agree** (30m) — The week's central check. Any discrepancy is a bug or a learning rate problem.
4. **Watch it diverge** (20m) — Set lr=10. Observe. This is the instructive failure.
5. **`mse`, `mae`, `rmse`, `r_squared`** (45m) — Then demonstrate MSE's outlier sensitivity against MAE's.
6. **L1 vs L2 comparison** (1h) — Fit on 10 features where only 1 matters. Show L1 zeroing the rest and L2 not.
7. **`polynomial_features` and the overfitting figure** (1h) — Degrees 1, 3, 9, 15 on 20 noisy points, all four plotted together.
8. **`train_test_split`** (30m) — Shuffle. An unshuffled split on ordered data is a silent disaster.
9. **`bias_variance_decomposition`** (1.5h) — The exercise that turns a recited answer into a demonstrated one.

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
l
i
n
e
a
r
_
r
e
g
r
e
s
s
i
o
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
n
o
t
e
b
o
o
k
s
/
b
i
a
s
_
v
a
r
i
a
n
c
e
.
i
p
y
n
b
```

## Tests To Write

`tests/test_linear_regression.py` is the specification. Add two:

1. A test that ridge regression produces finite weights on a perfectly collinear
   design matrix while OLS does not. This is the numerical-stability argument,
   made executable.
2. A test that the learned weights approach the true generating weights as
   sample size grows — n = 20, 200, 2000, with the error shrinking.

## Portfolio Artifact

`src/linear_regression.py`, tested, plus `notebooks/bias_variance.ipynb` containing the polynomial overfitting figure and the empirical bias-variance decomposition. That decomposition plot is the first genuinely presentable figure of Month 2.

## Interview Drills

**Coding (45 min).** Two problems, sorting and binary search. Timed, spoken aloud, complexity stated unprompted.

**ML theory (25 min).** Out loud, recorded: *Explain bias and variance. Then explain what regularization buys you, and why L1 produces exact zeros while L2 does not.* A 9/10 answer explains L1's sparsity through the constant gradient magnitude, not just the diamond-versus-circle picture.

**Communication (10 min).** Explain to a non-technical stakeholder why a model that fits the training data perfectly might be worse than one that does not.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement gradient descent with three different feature scalings — none,
standardized, and min-max — on the same problem, and plot the loss curves
together.

The curves will differ dramatically, and the reason is geometric: unscaled
features produce an elongated loss surface where gradient descent zigzags. This
is the same phenomenon that motivates momentum in Week 15 and adaptive methods in
Adam, and seeing it in two dimensions makes those later topics concrete rather
than abstract.
