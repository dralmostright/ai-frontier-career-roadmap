# Week 11: Model Evaluation and Calibration

## Outcome

By Sunday you can evaluate a model in a way you would defend under questioning: correct cross-validation for the data structure, confidence intervals on every number, paired tests for model comparison, and calibrated probabilities.

Concretely: `tests/test_evaluation.py` passes, including `test_paired_test_detects_a_real_difference`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

This week separates people who report numbers from people who report results.

Three capabilities, all directly examined:

**Correct cross-validation.** Stratified for imbalance, grouped for
non-independent rows, temporal for time series. Choosing wrong produces an
estimate of a different quantity than the one you care about, and the failure is
silent.

**Honest uncertainty.** "Model A scored 0.84, model B scored 0.86" is not a
finding. On 500 test samples that difference is well inside the noise. The paired
bootstrap tells you whether it is real, and using it is the difference between an
engineer and someone reading a leaderboard.

**Calibration.** When a predicted probability is consumed by a downstream
decision — a threshold, a cost calculation, an agent deciding whether to page
someone — it has to mean what it says. Tree ensembles and SVMs are systematically
miscalibrated, and most people never check.

That last one connects forward: in Week 44 your DBA agent will report confidence
in a diagnosis. If that number is not calibrated, it is decoration.

## Time Budget: 15-20 Hours

- Theory: 3.5 hours
- Coding: 7 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Cross-validation, correctly**
   1. K-fold, and why a single split is a high-variance estimate
   2. Stratified: mandatory under imbalance
   3. Grouped: when rows are not independent
   4. Temporal: expanding windows, never shuffled
   5. Nested CV: the honest way to report a tuned model's score
2. **Uncertainty**
   1. Why a point estimate is incomplete
   2. The bootstrap, from Week 4, applied to metrics
   3. Paired comparison: resample the same rows for both models
   4. Why pairing is far more sensitive than comparing two independent intervals
3. **Learning curves**
   1. Score against training set size
   2. Reading them: underfitting, overfitting, or more data will help
   3. The most useful diagnostic plot in classical ML
4. **Calibration**
   1. What it means for a probability to be calibrated
   2. Reliability curves, and uniform versus quantile binning
   3. Expected calibration error, and the Brier score as a proper scoring rule
   4. Platt scaling and isotonic regression, and when to use which
   5. Why calibration preserves ranking and therefore leaves AUC unchanged
5. **Imbalance, properly**
   1. Class weighting versus resampling
   2. Why resampling breaks calibration and how to correct for it
   3. Why you only ever resample the training fold

## Required Free Resources

- **Primary:** scikit-learn, 'Cross-validation: evaluating estimator performance' — https://scikit-learn.org/stable/modules/cross_validation.html — read the section on grouped and time-series splits carefully
- **Primary:** scikit-learn, 'Probability calibration' — https://scikit-learn.org/stable/modules/calibration.html
- 'On Calibration of Modern Neural Networks' (Guo et al., 2017) — https://arxiv.org/abs/1706.04599 — the paper that showed deep networks are badly miscalibrated. Relevant again in Week 36.
- Efron and Tibshirani on the bootstrap — you need the percentile method, roughly six pages
- 'Statistical Significance Tests for Machine Learning' — for the paired comparison reasoning

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=11
```

1. **`k_fold_split`, `stratified_k_fold_split`** (1h) — Then demonstrate that plain k-fold produces a fold with zero positives on 2%-positive data.
2. **`time_series_split`** (45m) — Expanding windows. Assert every training index precedes every validation index.
3. **`group_k_fold_split`** (45m) — Keep all rows of a group on one side. Necessary whenever rows are not independent.
4. **`cross_validate` taking a factory** (1h) — A factory, not an instance. Reusing a fitted model across folds invalidates everything.
5. **`bootstrap_metric_ci`** (1h) — Then verify the interval narrows with more data.
6. **`paired_bootstrap_test`** (1.5h) — Resample the same rows for both models. This is the function you will use most for the rest of the course.
7. **`learning_curve`** (1h) — Then read three of them and diagnose each: underfitting, overfitting, and would-more-data-help.
8. **`calibration_curve` and `expected_calibration_error`** (1.5h) — Uniform and quantile binning. Show why uniform is useless when predictions cluster.
9. **`PlattScaling` and `IsotonicCalibration`** (1.5h) — Fit on a held-out calibration set. Verify ECE improves and AUC does not change.
10. **`class_weights` and `resample`** (45m) — Then show resampling breaks calibration.

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
e
v
a
l
u
a
t
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
c
a
l
i
b
r
a
t
i
o
n
_
a
n
d
_
u
n
c
e
r
t
a
i
n
t
y
.
i
p
y
n
b
```

## Tests To Write

`tests/test_evaluation.py` is the specification. Add two:

1. A test that non-nested hyperparameter tuning produces an optimistically biased
   score relative to nested CV, on the same data — quantifying the bias.
2. A test that a random forest's probabilities are better calibrated than a
   single deep tree's, measured by ECE, on the same data.

## Portfolio Artifact

`src/evaluation.py` and `notebooks/calibration_and_uncertainty.ipynb`, containing: reliability curves before and after calibration for three model families, a learning curve with its diagnosis, and a paired model comparison with the significance test.

The before/after calibration figure is the one to keep. Most people have never seen it and it makes the concept immediate.

## Interview Drills

**Coding (45 min).** Two problems. Rotate back to trees and graphs.

**ML theory (30 min).** Recorded: *How would you evaluate a fraud detection model?* This is the integrative question for Months 2-3 and your answer should now cover: PR-AUC not accuracy, stratified CV, temporal split if there is a time dimension, calibration because the probability feeds a cost decision, threshold by expected cost, confidence intervals, and slice analysis. Six minutes, structured.

**Communication (15 min).** Explain to a product manager why 'the new model scored 0.86 versus 0.84' might not mean the new model is better.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement nested cross-validation and measure the optimism of the naive
approach: tune hyperparameters with 5-fold CV and report the best fold score,
then do it properly with nested CV, and report the gap.

The gap is typically one to three points, which is exactly the margin that
separates competition ranks and exactly the margin people quietly exploit without
realizing it. Having measured it yourself makes you appropriately skeptical of
reported numbers — including your own — for the rest of the course.
