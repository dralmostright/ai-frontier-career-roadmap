# Month 02 Capstone: Titanic ML Pipeline

## Objective

Build a complete, honest supervised learning pipeline on a beginner
classification dataset. The point is not the score — the point is that every step
is done correctly, your from-scratch implementations match sklearn, and the error
analysis says something a reader did not already know.

## Business Problem

Predict passenger survival from the Titanic manifest. The business framing is
artificial, and pretending otherwise would be the first dishonest thing in your
portfolio.

What the project actually demonstrates: that you can execute the standard
workflow — EDA, feature engineering, baseline, model, evaluation, error analysis
— without cutting the corners that most people cut. Specifically: a real baseline,
metrics chosen for the problem rather than by default, and error analysis that
identifies *which* passengers the model misclassifies and why.

## Technical Requirements

- Load and explore the data, with the missing-value pattern documented
- Feature engineering: title extraction, family size, cabin deck, fare bands
- A trivial baseline (predict the majority class, then predict by sex alone)
- Your from-scratch logistic regression, decision tree, and random forest
- sklearn equivalents, with the results compared and any gap explained
- Stratified cross-validation, not a single split
- Metrics beyond accuracy: precision, recall, F1, ROC-AUC, PR-AUC, confusion matrix
- Threshold selection with a stated cost assumption
- Permutation importance
- Error analysis: who does it get wrong, and is there a pattern?

## Theory Requirements

The README must explain, in your own words:

1. Why you chose the metrics you chose, given the class balance.
2. Why cross-validation rather than a single train/test split, and why stratified.
3. What the bias-variance tradeoff looks like in *this* dataset — show it with a
   learning curve.
4. Why your from-scratch models do or do not match sklearn, with the specific
   cause of any gap.

## System Design Requirements

Light, but establish the shape:

- A `Pipeline` that fits transformers on the training fold only
- Config-driven: model choice and hyperparameters in a YAML file, not in code
- Deterministic: a fixed seed, and the same numbers on a re-run
- The notebook orchestrates; the logic lives in `src/`

## Implementation Plan

**Days 1-2 — EDA and features.** Understand the data before modeling. Document
the missing-value pattern; on this dataset, missingness in `Cabin` is itself
informative and that is worth noticing yourself rather than reading about.

**Day 3 — Baselines.** Majority class, then sex-only. The sex-only baseline gets
about 78% and beating it by less than a few points means your model is not adding
much. Establishing that bar honestly is the point.

**Day 4 — Models.** Your implementations and sklearn's, side by side.

**Day 5 — Evaluation.** Cross-validation, the full metric suite, threshold
selection, calibration inspection.

**Day 6 — Error analysis.** The most valuable day. Look at the misclassified
passengers individually.

**Day 7 — Write-up.** README, notebook cleanup, publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Beats the sex-only baseline | Yes, by a stated margin with a CI |
| From-scratch vs sklearn agreement | Within 2% accuracy; gaps explained |
| Cross-validation | 5-fold stratified, mean and std reported |
| Metrics | Accuracy, precision, recall, F1, ROC-AUC, PR-AUC, all with CIs |
| Error analysis | At least three named failure categories with counts |
| Reproducibility | Same numbers on a re-run from a clean clone |

Report every metric with a bootstrap confidence interval. On a dataset of 891
rows the intervals are wide, and showing that you know it is the honest move.

## Expected Repository Structure

```text
titanic-ml-pipeline/
  README.md
  pyproject.toml
  Makefile
  config/
    logistic.yaml
    forest.yaml
  src/
    data.py          loading, cleaning
    features.py      the transformer pipeline
    models.py        from-scratch and sklearn wrappers
    evaluate.py      metrics, CV, calibration
    analyze.py       error analysis
  notebooks/
    01_eda.ipynb
    02_modeling.ipynb
    03_error_analysis.ipynb
  tests/
    test_features.py
    test_no_leakage.py
    test_models.py
  docs/
    design.md
    evaluation.md
    limitations.md
```

## README Requirements

Above the fold: one-sentence description, the results table, and the
setup commands.

Then: the problem and its honest framing; the baseline and why it matters; the
approach; the results table with confidence intervals; from-scratch versus
sklearn; the error analysis with its three named failure categories; key
technical decisions with rejected alternatives; limitations; interview talking
points.

**The results table must include the baseline row.** A model reported without
its baseline is a number with no meaning, and including it is a discipline worth
establishing now.

## Demo Requirements

A `make demo` that runs the full pipeline end to end in under 60 seconds and
prints the results table plus the top five misclassified passengers with their
features. Someone should be able to clone, run one command, and see the whole
project work.

## Blog Post Requirement

Optional. If you write one, the angle with actual value is the error analysis:
"What the Titanic Dataset's Errors Tell You About Model Evaluation." The
survival-prediction content is written to death; a careful failure analysis is
not.

Post #1 is formally scheduled for Month 5. Defer if the week is tight.

## Interview Story

> "I implemented logistic regression, a decision tree, and a random forest by
> hand and matched scikit-learn to within two percent — which is how I know my
> understanding is real rather than API-deep. The more useful part was the error
> analysis: the model fails on a specific, identifiable group, and I can tell you
> which and why."

45 seconds, no notes.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 2 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 6 | The problem is artificial. Say so; do not oversell. |
| Technical execution | 8 | From-scratch models matching sklearn is the bar. |
| Evaluation rigor | 8 | Baseline, CV, CIs, and a justified metric choice. |
| Code quality | 8 | src/ layout, tests, config-driven. |
| Documentation | 7 | Clear README with the results table above the fold. |
| Reproducibility | 9 | Small data, pure Python. No excuse. |
| Error analysis | 8 | **The differentiator.** Named categories with counts. |
| Portfolio readiness | 5 | Everyone has a Titanic notebook. Keep it, don't feature it. |

**Overall target: 7.5+, with Error Analysis and Evaluation Rigor at 8 or above.**

## Stretch Goals

1. **A learning curve** showing whether more data would help. Ten minutes of
   work, and it answers a question most projects leave open.
2. **Calibration analysis** — plot the reliability curve for each model. Preview
   of Week 11, and it will show your random forest is better calibrated than your
   single tree.
3. **A Kaggle submission**, to make the score real. Note the public leaderboard
   score in the README alongside your CV estimate, and comment on the gap.
4. **Fairness slice analysis** — error rate by sex and by class. On this dataset
   the disparities are large and historically meaningful, and analyzing them is
   good practice for the slice analysis you will do properly in Week 12.

## Limitations To State Honestly

State plainly:

- 891 rows. Confidence intervals are wide and any difference under about three
  points is not distinguishable from noise.
- The dataset is a historical curiosity, not a live prediction problem. There is
  no distribution shift, no deployment, and no cost of being wrong.
- Feature engineering choices were informed by widely-known analyses of this
  dataset, which is a mild form of leakage from the community's collective
  test-set exploration.
- The from-scratch models are slower than sklearn by a large factor and are not
  intended for use.
