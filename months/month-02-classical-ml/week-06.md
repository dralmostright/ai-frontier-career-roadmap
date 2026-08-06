# Week 06: Logistic Regression and Classification Metrics

## Outcome

By Sunday you can implement binary and multiclass classifiers from scratch, and — more importantly — evaluate them correctly under class imbalance, choosing thresholds by cost rather than by convention.

Concretely: `tests/test_logistic_regression.py` and `tests/test_metrics.py` pass, including `test_pr_auc_exposes_what_roc_auc_hides`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**This is the most important week of Month 2.** Not because logistic regression
is hard, but because evaluation is where most candidates are visibly weak and
where you can be visibly strong.

The specific questions you will get: "when is PR-AUC better than ROC-AUC?",
"how would you evaluate a fraud model?", "your model is 99% accurate — is that
good?". These are asked constantly because they separate people who have deployed
something from people who have followed a tutorial.

The `p - y` gradient — that sigmoid composed with log loss has all its messy
terms cancel — is a standard derivation request. You derived it in Week 3; this
week you use it.

The threshold-as-cost-minimization framing is your differentiator. You already
think this way about alerting: an alert that pages someone unnecessarily has a
cost, and so does one that stays silent. Most ML candidates default to 0.5 and
have never thought about why.

## Time Budget: 15-20 Hours

- Theory: 3.5 hours
- Coding: 7 hours
- Project: 3 hours
- Interview practice: 2.5 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **From regression to classification**
   1. Why linear regression fails for classification
   2. The sigmoid, and the log-odds interpretation of the logit
   3. Log loss, and why squared error on a sigmoid trains badly
   4. The p - y gradient, and where the terms went
2. **Multiclass**
   1. Softmax as the multiclass sigmoid
   2. Why a two-class softmax is exactly logistic regression
   3. One-vs-rest versus native multinomial
3. **The confusion matrix**
   1. TP, FP, TN, FN, and fixing the layout in your head
   2. Precision: of what you flagged, how much was real
   3. Recall: of what was real, how much you caught
   4. Specificity, and F-beta as the cost-weighted compromise
4. **Threshold-free evaluation**
   1. The ROC curve, and AUC as a ranking probability
   2. The PR curve, and why its baseline is the positive rate
   3. **When ROC-AUC lies:** heavy imbalance, because FPR carries the huge negative count in its denominator
   4. Matthews correlation coefficient, and why it uses all four cells
5. **Choosing a threshold**
   1. 0.5 is a convention, not an optimum
   2. Expected cost minimization with asymmetric costs
   3. Why a calibrated model is required for this to mean anything (Week 11)
6. **Class imbalance**
   1. Why accuracy is meaningless at a 1% positive rate
   2. Class weighting versus resampling
   3. Why resampling breaks calibration

## Required Free Resources

- **Primary:** CS229 lecture notes 1, sections on logistic regression and GLMs — https://cs229.stanford.edu/
- **Primary:** Google ML Crash Course, Classification module — https://developers.google.com/machine-learning/crash-course/classification/video-lecture — unusually good on metrics
- Jason Brownlee, 'ROC Curves and Precision-Recall Curves for Imbalanced Classification' — the clearest treatment of the ROC/PR distinction
- scikit-learn model evaluation guide — https://scikit-learn.org/stable/modules/model_evaluation.html — read after implementing
- 'The Relationship Between Precision-Recall and ROC Curves' (Davis and Goadrich, 2006) — the paper behind the interview answer

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=6
```

1. **`sigmoid`, stably** (30m) — Branch on the sign of z. The naive form warns and returns nan below -745.
2. **`log_loss` with clipping** (30m) — Unclipped, a confident wrong prediction gives inf and then nan everywhere.
3. **`LogisticRegression`** (1.5h) — Full-batch gradient descent using the p-y gradient you derived in Week 3.
4. **`confusion_matrix` and the basic metrics** (1h) — Rows are true, columns predicted. Half of all metric bugs are a transpose.
5. **`roc_curve`, `roc_auc`** (1.5h) — Sort and accumulate — O(n log n). The naive threshold loop is O(n^2) and will not finish.
6. **`precision_recall_curve`, `average_precision`** (1h) — Then verify the PR baseline equals the positive rate.
7. **The imbalance demonstration** (1h) — Build 1%-positive data. Show ROC-AUC above 0.75 while PR-AUC is below 0.4. This is the interview answer, made concrete.
8. **`find_optimal_threshold` with asymmetric costs** (1h) — Show the threshold moving when false negatives cost 50x false positives.
9. **`SoftmaxRegression`** (1.5h) — Then verify the two-class case matches your binary implementation exactly.

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
o
g
i
s
t
i
c
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
s
r
c
/
m
e
t
r
i
c
s
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
m
e
t
r
i
c
s
_
u
n
d
e
r
_
i
m
b
a
l
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

Both test files are the specification. The one to focus on is
`test_pr_auc_exposes_what_roc_auc_hides` — when it passes, you have the interview
answer in executable form.

Add two:

1. A test that your `roc_auc` equals the empirical ranking probability
   P(random positive scored above random negative), computed by brute force.
2. A test that class weighting improves recall on skewed data relative to
   unweighted training, at a fixed threshold.

## Portfolio Artifact

`src/logistic_regression.py`, `src/metrics.py`, and `notebooks/metrics_under_imbalance.ipynb`. The notebook should contain the ROC and PR curves for the same imbalanced model side by side, with the cost curve underneath. That three-panel figure is worth reusing in interviews.

## Interview Drills

**Coding (45 min).** Two problems, trees and recursion. This topic will feel less natural than arrays — front-load it.

**ML theory (30 min).** Recorded, no notes: *When is PR-AUC better than ROC-AUC? Then: how would you evaluate a fraud detection model where fraud is 0.1% of transactions and a missed fraud costs 200x a false alarm?* The second question is where you should shine — cost-weighted thresholds, PR-AUC, and precision at a fixed recall target.

**Communication (15 min).** Your model is 99.9% accurate. Explain to a product manager why you are not shipping it.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Build the full cost analysis for a realistic scenario: a fraud model at 0.1%
positive rate, where a false negative costs $500 and a false positive costs $2 in
review time.

Produce: the expected-cost curve across thresholds, the optimal threshold, the
precision and recall at that threshold, and the annual dollar difference between
your threshold and the default 0.5.

That analysis is a complete interview answer to "how would you evaluate a fraud
model", and having the actual numbers makes it far more convincing than the
qualitative version. Keep the notebook.
