# Month 03: Practical ML, Kaggle, and Model Debugging

**Weeks 9-12 · Phase 1: Foundations · Lab: `bootstrap/ml-from-scratch/`**

---

## The Month In One Sentence

Learn the things that separate a model that scores well offline from a model that works: leakage prevention, calibration, honest uncertainty, and error analysis.

## Why This Month Exists

Month 2 taught you to build models. Month 3 teaches you to trust them, which
is the harder and rarer skill.

Three specific capabilities, all of which are asked about directly:

**Leakage prevention.** The most common way a machine learning project fails is
that it worked beautifully offline and terribly in production, because the
offline evaluation was measuring something else. Leakage is a data-lineage bug,
and lineage reasoning is something you already do professionally.

**Honest uncertainty.** Reporting "AUC 0.84" is a number. Reporting "AUC 0.84
[0.81, 0.87]" is a result. This distinction is what makes your Month 17 research
credible, and building the habit here means it costs nothing later.

**Error analysis.** The Week 12 workflow — rank failures by loss, read the worst
twenty individually, bucket them, fix the biggest bucket — is a postmortem in
different clothing. This is the week your incident-response background pays the
most obvious dividend in Phase 1.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 9 | Gradient Boosting | `boosting.py` + the bagging/boosting comparison |
| 10 | Feature Engineering and Data Leakage | `features.py`, `tests/test_no_leakage.py` — a reusable leakage test suite |
| 11 | Model Evaluation and Calibration | `evaluation.py` — cross-validation, bootstrap CIs, calibration |
| 12 | Explainability and Error Analysis | `explainability.py` + a professional model report |

**Capstone:** End-to-End Kaggle Tabular System — a real competition entry built like production software, with the report as the deliverable.

## The Through-Lines

**Leakage is a lineage problem.** Every transformation that learns from data must
learn from the training fold only. Weeks 10 and 11 make this structural rather
than a matter of discipline.

**Every number gets an interval.** From Week 11 onward, no metric is reported
without a confidence interval. This is the habit that makes Weeks 39, 44, and 68
defensible.

**Calibration matters when a number is consumed.** A predicted probability that
feeds a downstream decision must mean what it says. Week 11 makes this precise,
and Week 44's agent confidence scores depend on it.

**Aggregate metrics hide everything interesting.** Week 12's slice analysis is
the same instinct as looking at p99 rather than the mean.

## Time and Compute

15-20 hours per week. CPU only, though gradient boosting on a larger Kaggle dataset may take a few minutes per fit. Kaggle's free notebooks are an option if your laptop struggles.

## Files

```text
month-03-kaggle-ml/
  README.md      you are here
  week-09.md     gradient boosting
  week-10.md     feature engineering and data leakage
  week-11.md     model evaluation and calibration
  week-12.md     explainability and error analysis
  capstone.md    end-to-end kaggle tabular system
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 10.** Leakage is the failure mode that invalidates everything downstream,
and it is invisible — it looks like a great score.

If the month has to shrink, compress Week 9 (boosting is conceptually
straightforward after Week 8) and protect Weeks 10 and 12.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Fitting the scaler before splitting | Validation score is fiction | Fit on train, transform the rest. Week 10's tests enforce this. |
| Naive target encoding | Near-perfect validation, useless model | Out-of-fold encoding plus smoothing. There is a test for exactly this. |
| Reporting a single number | No sense of whether a difference is real | Bootstrap CI on everything, from Week 11. |
| Chasing leaderboard position | Weeks spent on 0.001 improvements | The report is the artifact. Rank is not. |
| Skipping the individual error review | Only aggregate metrics | Read the worst twenty predictions. Actually read them. |
| Tuning on the test set | Optimistic by several points | Nested CV, or a genuinely held-out set touched once. |

## Advancement

Before Month 4, you should be able to, without notes:

- [ ] Identify the leakage in a described scenario within 60 seconds
- [ ] Explain out-of-fold target encoding and why naive encoding fails
- [ ] Explain calibration, and when a miscalibrated model is unacceptable
- [ ] Produce a bootstrap confidence interval and interpret it correctly
- [ ] Explain why a 94%-accurate model can be worthless
- [ ] Point at a public Kaggle project with a professional error-analysis report

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 4 — Neural Networks From Scratch. Phase 2 begins, and the evaluation discipline from this month applies unchanged.
