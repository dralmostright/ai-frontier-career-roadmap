# Week 09: Gradient Boosting

## Outcome

By Sunday you can implement gradient boosting from scratch for both regression and classification, explain exactly how it differs from bagging, and demonstrate that unlike a random forest it will overfit if you keep going.

Concretely: `tests/test_boosting.py` passes, including `test_too_many_rounds_overfits`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Gradient boosting is still the strongest model for tabular data, which makes
"when would you use gradient boosting over a neural network?" a live question
with a real answer.

The conceptual payoff is bigger than the model though. Boosting is **gradient
descent in function space**: each new tree is fit to the negative gradient of the
loss with respect to the current predictions. Seeing that the same optimization
idea appears at the level of *models* rather than *parameters* is a genuinely
expanding realization, and it makes the algorithm memorable rather than
procedural.

The learning-rate-versus-rounds tradeoff here is the same shape as the one you
will tune for neural networks in Week 15. Meeting it in a simpler setting first
is useful.

## Time Budget: 15-20 Hours

- Theory: 3.5 hours
- Coding: 7 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Boosting as sequential correction**
   1. Fit a weak model, fit the next to what the first got wrong
   2. Why weak learners: a strong first learner leaves no residual
   3. Additive models and the staged prediction
2. **Gradient boosting**
   1. Fitting trees to the negative gradient of the loss
   2. For squared error, the negative gradient *is* the residual
   3. For log loss, it is (y - p)
   4. Gradient descent in function space
3. **Regularization in boosting**
   1. Shrinkage: the learning rate, and the rounds tradeoff
   2. Tree depth: why 2-5 and not 20
   3. Subsampling rows (stochastic gradient boosting) and columns
   4. Early stopping on a validation set
4. **Bagging versus boosting**
   1. Parallel and independent versus sequential and corrective
   2. Variance reduction versus bias reduction
   3. More trees is free versus more rounds eventually overfits
   4. Forgiving to tune versus sensitive to the learning rate
5. **The production implementations**
   1. XGBoost: second-order gradients, regularized objective
   2. LightGBM: histogram binning, leaf-wise growth, native categoricals
   3. CatBoost: ordered boosting, which is out-of-fold target encoding built in
   4. Why they are 100x faster than yours, and what they do differently

## Required Free Resources

- **Primary:** Elements of Statistical Learning, ch. 10 — https://hastie.su.domains/ElemStatLearn/ — the definitive treatment; sections 10.1-10.10
- **Primary:** 'Gradient Boosting explained' by Terence Parr and Jeremy Howard — https://explained.ai/gradient-boosting/ — the clearest walkthrough with worked arithmetic
- XGBoost documentation, 'Introduction to Boosted Trees' — https://xgboost.readthedocs.io/en/stable/tutorials/model.html
- LightGBM features documentation — https://lightgbm.readthedocs.io/en/latest/Features.html — read this for the histogram and leaf-wise ideas
- StatQuest, 'Gradient Boost Parts 1-4' — the arithmetic worked by hand, which is genuinely helpful here

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=9
```

1. **Work one boosting round by hand** (45m) — Four data points, one stump. Do the arithmetic on paper. This is also an interview drill.
2. **`GradientBoostingRegressor`** (2h) — Initialize with the mean, fit each tree to the running residuals.
3. **`staged_predict`** (45m) — Then plot validation error against round index and find the minimum.
4. **The overfitting demonstration** (1h) — 20 rounds versus 800 on noisy data. Show test error rising. The contrast with random forests is the point.
5. **Depth ablation** (45m) — depth 2 versus depth 12 at fixed rounds. Weak learners win, and seeing it is convincing.
6. **`GradientBoostingClassifier`** (1.5h) — Regression trees on log-odds gradients. Verify the base learners really are regressors.
7. **`subsample` and stochastic boosting** (45m) — Show it regularizes.
8. **`AdaBoostClassifier`** (1h) — For contrast. Sample reweighting rather than residual fitting.
9. **Compare against XGBoost/LightGBM** (1h) — Same data. Expect them to win on both speed and accuracy; identify which of their features explains the gap.

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
o
o
s
t
i
n
g
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
g
r
a
d
i
e
n
t
_
b
o
o
s
t
i
n
g
_
l
a
b
.
i
p
y
n
b
```

## Tests To Write

`tests/test_boosting.py` is the specification. Add two:

1. A test that gradient boosting with squared error and depth-1 stumps, run for
   many rounds at a small learning rate, approaches the same fit as a single deep
   tree — demonstrating that boosting builds complexity additively.
2. A test that your implementation's predictions correlate above 0.95 with
   sklearn's `GradientBoostingRegressor` on the same data and hyperparameters.

## Portfolio Artifact

`src/boosting.py` and `notebooks/gradient_boosting_lab.ipynb`. The notebook needs the four figures that make the concepts concrete: staged validation error showing the overfitting point, the depth ablation, the learning-rate/rounds tradeoff, and a direct comparison against your Week 8 random forest on the same data.

## Interview Drills

**Coding (45 min).** Two problems, dynamic programming basics. This will be the least comfortable topic so far — that is expected.

**ML theory (25 min).** Recorded: *Walk me through one iteration of gradient boosting on four data points.* Do the arithmetic out loud. Then: *Bagging versus boosting — when do you pick which?*

**System design warm-up (15 min).** You have a gradient boosting model with 2000 trees and a 10ms latency budget. What are your options?

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement second-order (Newton) boosting: instead of fitting to the negative
gradient alone, use both the gradient and the Hessian to compute optimal leaf
values.

This is the core of what makes XGBoost XGBoost, and the derivation is a nice
application of the second-order Taylor expansion. Compare convergence rate
against your first-order version at the same learning rate — Newton boosting
typically needs meaningfully fewer rounds.
