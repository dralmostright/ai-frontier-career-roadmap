# Week 08: Ensembles and Random Forests

## Outcome

By Sunday you can build bagging and random forests from scratch, demonstrate empirically that feature subsampling — not bagging alone — is what makes the ensemble work, and use out-of-bag scoring as a free validation set.

Concretely: `tests/test_random_forest.py` passes, including `test_feature_subsampling_decorrelates_the_trees`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The interview question is "bagging versus boosting", and the answer most
candidates give ("bagging is parallel, boosting is sequential") is true and
shallow. The answer that lands is about *what each reduces*: bagging reduces
variance by averaging decorrelated estimators; boosting reduces bias by
sequentially fitting residuals. And the follow-up — "why does a random forest
subsample features?" — separates people who have built one from people who have
called one.

The out-of-bag insight is genuinely elegant and worth being able to derive on the
spot: each bootstrap sample omits about 36.8% of rows, because (1 - 1/n)^n
converges to 1/e. Those rows are a free validation set. Deriving that limit
during an interview is a small, memorable demonstration of comfort with the
material.

Permutation importance matters beyond this week — you will use it in Week 12 for
error analysis and its logic reappears in Week 44 when you ask which evidence the
agent actually relied on.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Bagging**
   1. Bootstrap resampling, and the 1/e out-of-bag fraction
   2. Why averaging reduces variance and leaves bias alone
   3. Why it requires *decorrelated* estimators to help
   4. Out-of-bag error as a free validation estimate
2. **From bagging to random forests**
   1. Feature subsampling at each split
   2. Why decorrelation is the load-bearing idea, not the bootstrap
   3. sqrt(d) for classification, d/3 or d for regression — and why the conventions differ
   4. Why more trees never overfits, unlike boosting
3. **Aggregation**
   1. Majority voting versus probability averaging
   2. Why averaging probabilities is better: voting discards confidence
   3. Why forest probabilities are better calibrated than a single tree's
4. **Feature importance**
   1. Mean decrease in impurity, and its bias toward high-cardinality features
   2. Permutation importance, and why it is more trustworthy
   3. The correlated-features caveat: duplicated features split the credit
5. **Where forests fall short**
   1. Large memory footprint and slow inference relative to a single model
   2. Still cannot extrapolate
   3. Boosting usually wins on accuracy for tabular data
   4. Less interpretable than one tree, more than a neural network

## Required Free Resources

- **Primary:** An Introduction to Statistical Learning, ch. 8.2 — https://www.statlearning.com/
- **Primary:** Breiman, 'Random Forests' (2001) — https://link.springer.com/article/10.1023/A:1010933404324 — genuinely readable, and reading a foundational paper is good practice for Month 16
- scikit-learn ensemble guide — https://scikit-learn.org/stable/modules/ensemble.html#forest
- 'Beware Default Random Forest Importances' — https://explained.ai/rf-importance/ — the case for permutation importance, with evidence
- StatQuest, 'Random Forests Part 1 and 2'

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=8
```

1. **`bootstrap_sample` with OOB indices** (45m) — Then verify empirically that the OOB fraction converges to 1/e over 40 samples.
2. **`RandomForestClassifier.fit`** (1.5h) — Bootstrap, train a constrained tree per sample, store them.
3. **`predict` and `predict_proba`** (1h) — Implement both voting and probability averaging, then compare accuracy.
4. **The decorrelation experiment** (1.5h) — Measure pairwise prediction agreement with max_features='sqrt' versus None. This is the week's key result.
5. **`_compute_oob_score`** (1.5h) — Score each row using only trees that never saw it. Verify it approximates test accuracy within a few points.
6. **`RandomForestRegressor`** (45m) — Note the different max_features default and be able to justify it.
7. **`permutation_importance`** (1.5h) — Verify it ranks the truly relevant features first, and that irrelevant ones score near zero.
8. **The correlated-features caveat** (45m) — Duplicate a feature and show both copies now look unimportant. State this unprompted in interviews.
9. **Compare against sklearn** (30m) — Accuracy within a couple of points is expected. Investigate a larger gap.

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
r
a
n
d
o
m
_
f
o
r
e
s
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
e
n
s
e
m
b
l
e
_
a
n
a
l
y
s
i
s
.
i
p
y
n
b
```

## Tests To Write

`tests/test_random_forest.py` is the specification. The test that matters most
is `test_feature_subsampling_decorrelates_the_trees` — it is the empirical form
of the interview answer.

Add two:

1. A test that a bagged forest with `max_features=None` and `bootstrap=True`
   performs measurably worse than a full random forest on noisy data — isolating
   the contribution of feature subsampling.
2. A test that OOB score tracks held-out test accuracy within 8 points across
   three different datasets.

## Portfolio Artifact

`src/random_forest.py` and `notebooks/ensemble_analysis.ipynb` containing: the OOB-fraction convergence to 1/e, the decorrelation measurement, OOB error versus tree count, and the permutation importance ranking with the correlated-feature caveat demonstrated.

This week also produces the **Month 2 capstone**. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems, heaps or intervals. Timed.

**ML theory (25 min).** Recorded: *Bagging versus boosting — which reduces bias, which reduces variance, and why?* Then: *Why does a random forest subsample features at each split? What would happen without it?* Then: *Derive the out-of-bag fraction.*

**Behavioral (15 min).** Draft story #2: a performance problem you diagnosed. Query plan regression, index issue, anything with a real number attached. Get it to 90 seconds in STAR form.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement isolation forest and use it to detect anomalies in a synthetic time
series of database metrics — connection counts, query latency, lock waits.

Two payoffs. It is a genuinely different use of tree ensembles (isolation rather
than prediction), which broadens your understanding of what the structure is good
for. And it is directly reusable: Month 11's DBA agent needs to decide whether
current telemetry is anomalous, and an isolation forest over historical metrics
is a defensible, cheap way to do that without an LLM call.

Keep the code. You will import it in Week 43.
