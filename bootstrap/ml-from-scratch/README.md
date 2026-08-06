# ml-from-scratch

**Weeks 5-16 · Months 2, 3, 4 · Capstones: Titanic Pipeline, Kaggle System, NumPy DL Library**

Twelve weeks and the largest lab in the workspace. Classical machine learning
and a complete deep learning framework, all in NumPy, all tested.

---

## Why This Lab Exists

Two things happen here that do not happen anywhere else.

**Months 2-3 make you dangerous with tabular data.** Gradient boosting still
beats deep learning on most tabular problems, and the evaluation discipline you
build in Weeks 10-12 — leakage tests, calibration, error analysis — is the
discipline you will apply to RAG systems in Week 39 and to an agent benchmark in
Week 68. The methodology transfers completely; only the artifacts change.

**Month 4 removes the magic from PyTorch.** You will write autograd, layers,
losses, optimizers, and a training loop. When Month 5 hands you `nn.Linear` you
will know exactly what it does, and when a training run breaks in Month 8 you
will debug from the computational graph rather than from Stack Overflow.

---

## Layout

```text
ml-from-scratch/
  src/
    linear_regression.py    W5   normal equation, GD, bias-variance
    logistic_regression.py  W6   sigmoid, softmax, the p-y gradient
    metrics.py              W6   confusion matrix through PR-AUC
    decision_tree.py        W7   CART, split search, impurity
    random_forest.py        W8   bagging, feature subsampling, OOB
    boosting.py             W9   gradient boosting, AdaBoost
    features.py             W10  transformers, encoders, leakage detection
    evaluation.py           W11  CV, bootstrap CIs, calibration
    explainability.py       W12  permutation importance, PDP, SHAP, error analysis
    neural_net.py           W13-16  layers, losses, MLP, BatchNorm, LayerNorm
    backprop.py             W14  gradient checking and flow diagnostics
    optimizers.py           W15  SGD through AdamW, LR schedules
    regularization.py       W16  penalties, early stopping, augmentation, diagnosis
  tests/
    test_linear_regression.py  test_logistic_regression.py  test_metrics.py
    test_decision_tree.py      test_random_forest.py        test_boosting.py
    test_no_leakage.py         test_evaluation.py
    test_backprop.py           test_optimizers.py           test_neural_net.py
  notebooks/
    gradient_boosting_lab.ipynb   W9
    error_analysis.ipynb          W12
```

---

## The Rules

Same as `math-labs`, with one addition.

**Do not call the library function you are implementing.** No `sklearn.metrics`
inside `metrics.py`. No `sklearn.tree` inside `decision_tree.py`. The tests
compare against reference behavior, and importing the reference makes them
vacuous.

**Permitted:** NumPy array operations, pandas for `features.py` and
`explainability.py`, scipy for special functions.

**Encouraged, after your implementation passes:** compare against sklearn.
Matching `RandomForestClassifier` to within a couple of points of accuracy is
strong evidence you got it right, and the places you *don't* match are where
sklearn is doing something you should go read about.

---

## Milestones

| Week | Gate | Test that proves it |
| ---- | ---- | ------------------- |
| 5 | Two routes to regression agree | `test_converges_to_the_closed_form_solution` |
| 6 | You understand imbalanced evaluation | `test_pr_auc_exposes_what_roc_auc_hides` |
| 7 | You can build and constrain a tree | `test_unconstrained_tree_memorizes_the_training_set` |
| 8 | You know why forests beat trees | `test_feature_subsampling_decorrelates_the_trees` |
| 9 | You can separate bagging from boosting | `test_too_many_rounds_overfits` |
| 10 | You can prevent leakage structurally | `test_fit_transform_must_differ_from_fit_then_transform` |
| 11 | You report honest numbers | `test_paired_test_detects_a_real_difference` |
| 12 | You can produce a real model report | `ErrorAnalysis.summary_report` |
| 13 | You can build a network | `test_learns_xor` |
| 14 | Your gradients are provably correct | `test_end_to_end_gradient_check` |
| 15 | You understand optimizers as a sequence of fixes | `test_decoupled_decay_differs_from_l2_in_the_gradient` |
| 16 | You can diagnose and fix a training run | `test_trains_mnist_subset_to_high_accuracy` |

The Month 4 capstone gate is the last one. When your NumPy framework trains
digits to >93% (and full MNIST to >95%), you have built a deep learning library.

---

## The Five Habits This Lab Installs

Carry all five into every remaining month.

**1. Overfit a single batch first.** `overfit_single_batch` in
`regularization.py`. Before any real training run, confirm the model can
memorize eight examples. This catches wrong loss reductions, detached gradients,
misaligned labels, and shuffled targets — four bugs that otherwise cost a day
each. Ten seconds to run.

**2. Check the initial loss.** An untrained classifier over C classes must
report ln(C). 2.303 for ten classes, 6.91 for a thousand, ~10.4 for a 32k
vocabulary in Week 35. Wrong initial loss means something is broken before
training starts.

**3. Gradient-check every new gradient.** Every layer in Week 14, attention in
Week 29, whatever you write in Week 67. A wrong gradient does not crash; it
quietly trains to a worse optimum.

**4. Plot the loss curve, every time.** It answers "is the LR wrong", "am I
overfitting", and "has it converged" in one glance. Each of those costs an hour
to answer without it.

**5. Report an interval, not a number.** `bootstrap_metric_ci`. "0.84
[0.81, 0.87]" is a result; "0.84" is a number. This habit is what makes your
Month 17 research credible.

---

## Common Traps

| Trap | Symptom | Fix |
| ---- | ------- | --- |
| Naive sigmoid | Overflow warnings, nan | Branch on the sign of z |
| Unclipped log loss | inf, then nan everywhere | Clip probabilities to [eps, 1-eps] |
| Transposed confusion matrix | Precision and recall swapped | Rows = true, columns = predicted |
| Reusing one model across CV folds | Suspiciously good, unstable scores | Pass a factory, not an instance |
| Fitting the scaler before splitting | Validation score is fiction | Fit on train, transform the rest |
| Naive target encoding | Near-perfect validation, useless model | Out-of-fold encoding + smoothing |
| Random split on time series | Great offline, bad in production | `time_series_split` |
| `=` instead of `+=` in backward | Wrong gradients in branching graphs | Gradients accumulate |
| Forgetting `.eval()` | Noisy, slightly-low validation metrics | Dropout and BatchNorm are mode-dependent |
| Skipping Adam's bias correction | First few hundred steps barely move | Divide by (1 - β^t) |
| No warmup on a deep network | Divergence in the first 100 steps | `WarmupCosineLR` |
| Per-parameter gradient clipping | Training subtly worse | Clip by *global* norm |

---

## Interview Drills

| Week | Drill |
| ---- | ----- |
| 5 | Derive gradient descent for linear regression. Then explain what regularization buys and why L1 gives sparsity. |
| 6 | When is PR-AUC better than ROC-AUC? Give the numbers, not the vibe. |
| 7 | Why do trees overfit, and what are three different ways to stop it? |
| 8 | Bagging vs boosting: which reduces bias, which reduces variance, and why? |
| 9 | Walk through one boosting iteration by hand on four data points. |
| 10 | Here is a scenario. Find the leakage. (Use `detect_target_leakage`'s test cases.) |
| 11 | How would you evaluate a fraud model at a 0.1% positive rate? |
| 12 | Your model is 94% accurate and the business says it's useless. Explain how. |
| 13 | Why can't a perceptron learn XOR? Draw it. |
| 14 | Derive backpropagation for a two-layer MLP on a whiteboard. |
| 15 | Why does Adam converge faster and sometimes generalize worse than SGD? |
| 16 | Loss is NaN at step 400. Debug it out loud, in priority order. |

---

## Capstones

- **Month 2** — Titanic ML Pipeline. From-scratch models matched against sklearn.
- **Month 3** — End-to-End Kaggle Tabular System. The Week 12 error analysis
  report is the artifact, not the leaderboard rank.
- **Month 4** — Neural Network Library From Scratch. Trains MNIST to >95% with
  nothing but NumPy.

Full specifications in `months/month-0{2,3,4}-*/capstone.md`.
