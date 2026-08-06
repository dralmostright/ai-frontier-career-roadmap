# Week 12: Explainability and Error Analysis

## Outcome

By Sunday you can produce a model report an engineering manager could act on: what the model is good at, where it fails, why, and what to do about it.

Concretely: `tests` pass and the Month 3 capstone report is written.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Error analysis is root-cause analysis. This is the week where your background
gives you the clearest advantage in Phase 1, and where the skill transfers most
directly to the rest of the course.

The workflow — rank failures by loss, read the worst twenty individually, bucket
them into named categories, count each bucket, estimate the recoverable score,
fix the biggest one, re-measure — is a postmortem. You have run these. Most ML
engineers have not, and it shows: they report aggregate metrics and stop.

The interview question this prepares you for is "your model is 94% accurate and
the business says it is useless — explain how that happens." The answer is slice
analysis: the aggregate hides that performance on the segment that matters is
55%. Being able to walk through finding that is a strong signal.

Everything here transfers. Week 39's RAG error analysis, Week 44's agent failure
taxonomy, and Week 68's research analysis are the same method applied to
different outputs.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Global explanations**
   1. Permutation importance, and why it beats impurity-based importance
   2. Partial dependence plots, and their correlated-feature failure mode
   3. Individual conditional expectation, and the heterogeneity PDPs hide
2. **Local explanations**
   1. Shapley values: average marginal contribution across all orderings
   2. Why exact computation is O(2^d) and what SHAP approximates
   3. LIME: locally faithful, globally meaningless — and why that is fine
3. **Error analysis as a method**
   1. Rank by loss, read the worst individually
   2. Bucket into named categories with counts
   3. Estimate the score recoverable per bucket
   4. Fix the largest, re-measure, repeat
4. **Slice analysis**
   1. Performance by feature value, by segment, by cohort
   2. Why the aggregate always hides the interesting failure
   3. Fairness slices, and when a disparity is a problem
   4. Calibration by slice: models are often calibrated overall and not by subgroup
5. **Label noise**
   1. Some fraction of labels in any real dataset are wrong
   2. Finding them: confidently predicted as the other class
   3. Why fixing labels often beats changing models
6. **Model cards**
   1. Intended use and out-of-scope use
   2. Metrics overall and by slice
   3. Limitations and ethical considerations
   4. Why writing these becomes routine by Month 12

## Required Free Resources

- **Primary:** Christoph Molnar, 'Interpretable Machine Learning' (free) — https://christophm.github.io/interpretable-ml-book/ — chapters on PDP, ICE, permutation importance, LIME, and SHAP. The standard reference.
- **Primary:** Andrew Ng, 'Machine Learning Yearning' (free) — the chapters on error analysis are the clearest statement of the method
- 'A Unified Approach to Interpreting Model Predictions' (Lundberg and Lee, 2017) — https://arxiv.org/abs/1705.07874 — the SHAP paper
- 'Model Cards for Model Reporting' (Mitchell et al., 2019) — https://arxiv.org/abs/1810.03993
- SHAP documentation — https://shap.readthedocs.io/ — use it after implementing exact Shapley values yourself

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=12
```

1. **`permutation_importance_report`** (1h) — Ranked, with mean and std. State the correlated-features caveat in the docstring.
2. **`partial_dependence`** (1h) — Then construct a case with correlated features where the PDP misleads.
3. **`individual_conditional_expectation`** (1h) — Find a case where the PDP is flat and the ICE curves are half up, half down.
4. **`shapley_values_exact`** (1.5h) — Enumerate coalitions on a 6-feature problem. Then use the SHAP library and compare.
5. **`ErrorAnalysis.worst_errors`** (45m) — Then actually read twenty of them. This is the highest-value hour of the week.
6. **`error_rate_by_slice`** (1h) — Find a slice where performance is dramatically worse than aggregate.
7. **`confusion_examples`** (45m) — Sample from one confusion-matrix cell and look for a pattern.
8. **`calibration_by_slice`** (45m) — Models calibrated overall are often badly calibrated per subgroup.
9. **`find_label_noise`** (1h) — Flag confidently-misclassified examples and inspect them by hand.
10. **`summary_report` and `model_card`** (1.5h) — The deliverable. Write it so an engineering manager knows what to do next.

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
x
p
l
a
i
n
a
b
i
l
i
t
y
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
r
r
o
r
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

Add tests for the numerical parts:

1. Exact Shapley values sum to the difference between the prediction and the
   baseline — the efficiency axiom, which is a strong correctness check.
2. Permutation importance for a feature the model provably ignores is
   approximately zero.
3. `find_label_noise` recovers planted label flips: flip 5% of labels
   deliberately and verify the function surfaces them in its top ranks.

That third test is a nice one — it validates the method against known ground
truth, which is exactly the pattern you will use for the Month 11 benchmark.

## Portfolio Artifact

`src/explainability.py` and `notebooks/error_analysis.ipynb`.

This week produces the **Month 3 capstone report**. The error analysis section is the artifact that makes the whole capstone worth showing — see `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems. Timed. This is the end of the first 12-week topic rotation; note which topics still feel weak.

**ML theory (30 min).** Recorded: *Your model is 94% accurate and the business says it is useless. Walk me through how you would find out why.* Then: *Explain SHAP to someone who has not heard of it.*

**Portfolio (20 min).** First quarterly portfolio audit. Open your GitHub in a private window, spend 90 seconds as a stranger, and answer the four questions in `PORTFOLIO_STRATEGY.md`.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Close the loop: use the error analysis to identify the largest failure bucket,
make one targeted change to address it, and measure the result.

This is what separates analysis from theater. Most error analysis produces a
document; this produces a before-and-after number. The README line — "error
analysis identified that 34% of false positives came from a single data-entry
pattern; handling it improved PR-AUC from 0.71 to 0.78" — is worth more than
every other sentence in the project.

If the change does not help, report that too. A negative result honestly reported
is still a result, and it is preparation for Month 17.
