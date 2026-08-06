# Week 10: Feature Engineering and Data Leakage

## Outcome

By Sunday you have a transformer pipeline that makes leakage structurally difficult, a test suite that catches it when it happens anyway, and the ability to spot it in a described scenario within a minute.

Concretely: `tests/test_no_leakage.py` passes, including `test_fit_transform_must_differ_from_fit_then_transform`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The most valuable week in Phase 1**, and the one that maps most directly onto
what you already do.

Leakage is the reason machine learning projects fail silently. The model scores
0.95 offline and 0.61 in production, and the postmortem finds that a feature
encoded information unavailable at prediction time. This is a data-lineage bug,
and you have spent years reasoning about which data was written when, by whom,
and what depends on it.

"Find the leakage in this scenario" is a standard interview question and one you
should answer faster than almost anyone. The variants: a feature computed after
the outcome; an identifier correlated with collection order; a scaler fit on the
full dataset; target encoding without out-of-fold computation; a random split on
time-series data; duplicate rows across train and test.

The test suite you write this week is a template you carry to every subsequent
project, including the Month 10 RAG eval set and the Month 17 benchmark.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **What leakage is**
   1. Information in training that will not be available at prediction time
   2. Why it produces optimistic offline scores and production failures
   3. Target leakage versus train/test contamination versus temporal leakage
2. **The fit/transform discipline**
   1. Any transformation that learns must learn from the training fold only
   2. Why this includes scalers, encoders, imputers, and feature selectors
   3. Why pipelines exist: to make the discipline structural rather than remembered
3. **Categorical encoding**
   1. One-hot: unseen categories and cardinality explosion
   2. Ordinal: when the ordering is real and when you are inventing one
   3. Target encoding: powerful and the most dangerous transformation in common use
   4. Out-of-fold encoding and smoothing, and why both are required
4. **Missing values**
   1. Imputation with training statistics
   2. Why the missingness indicator is often more informative than the imputed value
   3. MCAR, MAR, MNAR — and why the third breaks naive imputation
5. **Temporal data**
   1. Why a random split lets the model learn from the future
   2. Expanding-window and rolling-window splits
   3. Feature computation windows, and the lag you must respect
6. **Detection**
   1. A single feature with 0.99 AUC is almost never a great feature
   2. Duplicate detection across splits
   3. The sanity check: does the offline score survive a temporal split?

## Required Free Resources

- **Primary:** Kaggle Learn, Feature Engineering — https://www.kaggle.com/learn/feature-engineering — short and practical
- **Primary:** Kaggle Learn, Intermediate ML, 'Data Leakage' lesson — https://www.kaggle.com/code/alexisbcook/data-leakage
- 'Leakage in Data Mining' (Kaufman et al., 2011) — the paper that named and categorized this properly. Worth reading; it is clearer than most treatments.
- scikit-learn, 'Common pitfalls and recommended practices' — https://scikit-learn.org/stable/common_pitfalls.html — read the data leakage section in full
- CatBoost's ordered target statistics documentation — https://catboost.ai/en/docs/concepts/algorithm-main-stages_cat-to-numberic — a production solution to the target encoding problem

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=10
```

1. **`StandardScaler` with fit/transform separation** (45m) — Then verify that transformed test data is *not* exactly zero-mean. If it is, you refit.
2. **`OneHotEncoder` with unseen-category handling** (1h) — Decide the policy explicitly. The silent default is a crash at 2am.
3. **`MissingValueImputer` with an indicator column** (45m) — Then show a case where the indicator carries more signal than the imputed value.
4. **`TargetEncoder`, naive version** (1h) — Build it wrong first. Measure the validation score. It will be spectacular and fake.
5. **`TargetEncoder`, out-of-fold with smoothing** (1.5h) — Then measure again. The drop is the lesson.
6. **`Pipeline`** (1h) — Chain transformers so cross-validation refits everything inside each fold.
7. **`detect_target_leakage`** (1h) — Single-feature AUC screening. Test it by planting the target as a feature.
8. **`detect_train_test_contamination`** (1h) — Exact and near-duplicate detection across splits.
9. **`temporal_split_check`** (45m) — Assert every training timestamp precedes every test timestamp.
10. **Datetime and aggregation features** (1h) — Cyclical encoding for hour and day. Hour 23 and hour 0 are adjacent in reality.

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
f
e
a
t
u
r
e
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
t
e
s
t
s
/
t
e
s
t
_
n
o
_
l
e
a
k
a
g
e
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
l
e
a
k
a
g
e
_
d
e
m
o
n
s
t
r
a
t
i
o
n
s
.
i
p
y
n
b
```

## Tests To Write

`tests/test_no_leakage.py` is both the specification and the week's deliverable.
Treat it as a template to carry into every later project.

Add two:

1. A test that fitting a scaler on the full dataset before splitting produces a
   measurably higher cross-validation score than fitting inside the pipeline —
   quantifying how much the leak is worth.
2. A test that an ID-like column (one unique value per row) is flagged by
   `detect_target_leakage` when it correlates with the target through collection
   order.

## Portfolio Artifact

`src/features.py`, `tests/test_no_leakage.py`, and `notebooks/leakage_demonstrations.ipynb`.

The notebook is the portfolio piece: five leakage scenarios, each showing the inflated score, the corrected score, and the size of the gap. That gap table — 'this leak was worth 11 points of AUC' — is a compelling artifact and directly reusable as an interview answer.

## Interview Drills

**Coding (45 min).** Two problems. Return to arrays and hash maps for a confidence week.

**ML theory (30 min).** The leakage quiz, out loud, timed. Five scenarios, 60 seconds each: *A hospital readmission model includes 'discharge_disposition'. A churn model includes 'days_since_last_login'. A fraud model is validated with a random split on six months of transactions. A house price model's neighborhood feature is target-encoded on the full dataset. A click model includes 'time_on_page'.* For each: is there leakage, where, and how do you fix it?

**Behavioral (15 min).** Draft story #5: a mistake you made. A real one, with the fix and the systemic prevention. Leakage stories work well here if you have one.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Build the leakage scenario quiz as a reusable artifact: ten realistic scenarios
in a notebook, each with the data, the leaky feature, the inflated score, the
corrected score, and an explanation.

This is the highest-value stretch goal in Month 3 for three reasons. Writing the
scenarios forces you to understand each leakage mechanism precisely. The artifact
is genuinely useful to other people, which makes it shareable. And it is direct
preparation for a question you will certainly be asked.

Publish it separately from the capstone. A focused, useful notebook gets more
attention than a section inside a larger project.
