# Month 02: Classical Machine Learning From Scratch

**Weeks 5-8 · Phase 1: Foundations · Lab: `bootstrap/ml-from-scratch/`**

---

## The Month In One Sentence

Implement the classical models by hand until they match sklearn to four decimal places, and learn to evaluate them correctly.

## Why This Month Exists

Two reasons, and the second is the one people underestimate.

The obvious one: gradient boosting and random forests still beat deep learning on
most tabular problems, and tabular problems are most problems. You will be asked
about them.

The less obvious one: **this is where evaluation discipline is built.** Week 6's
metric work — precision, recall, PR-AUC under imbalance, threshold selection as
cost minimization — is the exact reasoning you will apply to RAG faithfulness in
Week 39 and to agent reliability in Week 44. The domain changes; the methodology
does not. Most people who skip Month 2 never develop it, which is why so many
LLM projects have no evaluation at all.

Your background gives you a real head start on the evaluation half. Reasoning
about false positives and false negatives against their operational cost is what
you already do when you decide whether an alert should page someone.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 5 | Linear Regression | `linear_regression.py` + bias-variance decomposition |
| 6 | Logistic Regression and Classification Metrics | `logistic_regression.py`, `metrics.py` — the evaluation toolkit |
| 7 | Decision Trees | `decision_tree.py` with an optimized split search |
| 8 | Ensembles and Random Forests | `random_forest.py` with OOB scoring and permutation importance |

**Capstone:** Titanic ML Pipeline — the standard supervised workflow, executed properly, with from-scratch models matched against sklearn.

## The Through-Lines

**The gradient you derived in Week 3 now fits real models.** Linear regression,
logistic regression, and every gradient-descent loop in this course are the same
three lines you wrote in `autodiff_scalar.py`.

**Information theory becomes an algorithm.** Week 4's `information_gain` is the
decision tree split criterion in Week 7. Trees are an information-theoretic
method, and seeing that makes both topics stick.

**Ensembling is variance reduction.** Week 8's random forest is the bias-variance
decomposition from Week 5, applied. Averaging decorrelated estimators reduces
variance without touching bias — and the *decorrelated* qualifier is the whole
trick.

**Metrics encode cost.** Week 6 is not about memorizing formulas. It is about
choosing a metric that reflects what being wrong actually costs.

## Time and Compute

15-20 hours per week. CPU only. Your laptop is sufficient.

## Files

```text
month-02-classical-ml/
  README.md      you are here
  week-05.md     linear regression
  week-06.md     logistic regression and classification metrics
  week-07.md     decision trees
  week-08.md     ensembles and random forests
  capstone.md    titanic ml pipeline
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 6.** Implementations are recoverable; evaluation habits are not. A
candidate who reaches for accuracy on imbalanced data, or who cannot say why
PR-AUC differs from ROC-AUC, is visibly junior regardless of what else they know.

If the month has to shrink, compress Week 7 (trees are conceptually simple) and
protect Week 6.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Calling sklearn inside your implementation | Tests pass immediately | The tests compare against sklearn. Using it makes them vacuous. |
| Optimizing accuracy on imbalanced data | 94% accuracy, useless model | Week 6 exists to break this habit. Use PR-AUC and cost-weighted thresholds. |
| Skipping the from-scratch tree | Week 7 done in an hour with sklearn | The split-search optimization is the lesson, not the API. |
| Not comparing against sklearn at the end | No validation that you got it right | Match to a few decimal places, then investigate every gap. |
| Treating 0.5 as the threshold | Never tuned | Threshold selection is cost minimization. Week 6 makes this explicit. |

## Advancement

Before Month 3, you should be able to, without notes:

- [ ] Derive gradient descent for logistic regression and explain the p-y result
- [ ] Explain when PR-AUC beats ROC-AUC, with the numbers
- [ ] Explain why trees overfit and name three distinct remedies
- [ ] Explain why bagging reduces variance and boosting reduces bias
- [ ] Implement logistic regression from scratch, unaided, in under 30 minutes
- [ ] Point at a public Titanic pipeline with real error analysis

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 3 — Practical ML, Kaggle, and Model Debugging. You will take these implementations to a real competition and learn to find the leakage.
