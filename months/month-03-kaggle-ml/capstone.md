# Month 03 Capstone: End-to-End Kaggle Tabular System

## Objective

Enter a real Kaggle tabular competition and build the entry the way you would
build a production model: config-driven, leak-proof, cross-validated,
calibrated, explained, and documented.

**The report is the artifact, not the leaderboard rank.** A top-10% finish with a
sloppy notebook is worth less to your portfolio than a top-40% finish with an
error analysis that teaches the reader something.

## Business Problem

Pick a competition with a real problem behind it. Good choices: Home Credit
Default Risk (credit scoring), Porto Seguro (insurance claims), IEEE-CIS Fraud
Detection, or any active tabular competition.

Prefer one with class imbalance and a time dimension — those exercise the Week 10
and Week 11 material properly. Avoid the purely synthetic playground series
competitions; there is no domain to reason about and therefore no error analysis
worth writing.

State the business problem in the README as if you were briefing a stakeholder:
who uses this prediction, what decision it drives, and what being wrong costs in
each direction.

## Technical Requirements

- A `Pipeline` with all learned transformations fit inside the CV fold
- Feature engineering with a documented rationale per feature group
- A leakage test suite that runs in CI
- A trivial baseline, then a strong single model, then an ensemble
- Cross-validation matched to the data structure (stratified, grouped, or temporal)
- Gradient boosting (your own for understanding, XGBoost or LightGBM for the entry)
- Calibrated probabilities where the competition metric is probabilistic
- Bootstrap confidence intervals on every reported number
- Permutation importance and SHAP
- Error analysis with named failure buckets
- A submission, with the public leaderboard score compared against your CV estimate

## Theory Requirements

The README must explain:

1. Why you chose this CV strategy for this data structure.
2. Why the competition metric is or is not the right metric for the underlying
   business problem — and if it is not, what you would use instead.
3. What your leakage tests check, and what they caught.
4. The gap between your CV estimate and the public leaderboard score, and your
   explanation for it.

That fourth point is the interesting one. A large gap means overfitting to the CV
folds, a distribution difference, or a leak. Diagnosing it honestly is more
impressive than a small gap.

## System Design Requirements

- Config-driven: every hyperparameter in YAML
- `make train`, `make evaluate`, `make submit`
- Seeded and reproducible; the same submission from a clean clone
- Experiment log: every run recorded with its config and its CV score
- Feature engineering separated from modeling so features can be reused across models

## Implementation Plan

**Days 1-2 — Understand the data.** EDA, missing-value patterns, target
distribution, the time structure if there is one, and duplicate detection. Decide
the CV strategy *before* building anything and write down why.

**Day 3 — Baseline and infrastructure.** The trivial baseline, the pipeline, the
leakage tests, the config system, the experiment log. Do this before feature
engineering; retrofitting it is painful.

**Days 4-5 — Features and models.** Iterate. Log every experiment. Resist the
urge to skip the log.

**Day 6 — Calibration and uncertainty.** Reliability curves, CIs on everything,
paired tests for the model comparisons you report.

**Day 7 — Error analysis.** Read the worst predictions. Bucket them. This is the
day that produces the artifact.

**Day 8 — Write-up and submit.**

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Beats the trivial baseline | Yes, with a stated margin and CI |
| CV strategy matches the data structure | Documented and justified |
| Leakage tests | Present, passing, and at least one caught something |
| CV vs leaderboard gap | Under 5% relative, or explained |
| Calibration | ECE reported; calibrated if the metric is probabilistic |
| Confidence intervals | On every reported number |
| Error analysis | 3+ named buckets with counts and recoverable-score estimates |
| Reproducibility | Same submission from a clean clone |

## Expected Repository Structure

```text
kaggle-tabular-system/
  README.md
  pyproject.toml
  Makefile
  config/
    base.yaml
    lgbm.yaml
    ensemble.yaml
  src/
    data.py
    features.py
    models.py
    validation.py
    calibrate.py
    analyze.py
    submit.py
  notebooks/
    01_eda.ipynb
    02_feature_development.ipynb
    03_error_analysis.ipynb
  tests/
    test_features.py
    test_no_leakage.py
    test_validation.py
  experiments/
    log.jsonl
  docs/
    design.md
    evaluation.md
    error_analysis.md
    limitations.md
```

## README Requirements

Above the fold: one-sentence description, the results table including the
baseline, and the three setup commands.

Then: the business problem framed for a stakeholder; the CV strategy and why;
the results with confidence intervals; the CV-versus-leaderboard gap and its
explanation; feature importance; **the error analysis with named buckets**; key
technical decisions with rejected alternatives; limitations; interview talking
points.

The error analysis section is the reason someone would read this repository
rather than the thousand other Kaggle notebooks on the same competition. Give it
real space.

## Demo Requirements

`make demo` runs the pipeline on a data subset in under two minutes and prints
the results table, the top ten features by permutation importance, and the error
bucket summary.

## Blog Post Requirement

Recommended this month, and the angle that has value is the error analysis or
the leakage work — not the modeling.

Working titles: "The Leak I Found in My Own Kaggle Pipeline" or "What 200
Misclassified Rows Told Me That AUC Did Not."

Both say something specific that most Kaggle write-ups do not. Publish on
dev.to or your own site and cross-post to LinkedIn.

## Interview Story

> "I can turn raw data into a measurable, production-minded model — and I can
> tell you exactly where it breaks. On this one, error analysis found that a
> third of the false positives came from a single data-entry pattern. Handling
> it moved PR-AUC seven points, which was more than any model change I tried."

45 seconds. The specific number is what makes it work.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 3 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 8 | Real problem, stated with its costs. |
| Technical execution | 8 | Pipeline, config, leakage tests, ensemble. |
| Evaluation rigor | 9 | **The point of the month.** CV, CIs, calibration, paired tests. |
| Code quality | 8 | src/ layout, tests in CI. |
| Documentation | 8 | The report is the artifact. |
| Reproducibility | 8 | Same submission from a clean clone. |
| Error analysis | 9 | **The differentiator.** Buckets, counts, and a fix that moved the number. |
| Portfolio readiness | 7 | Medium weight. The report is what makes it worth showing. |

**Overall target: 8.0+, with Evaluation Rigor and Error Analysis at 9.**

## Stretch Goals

1. **Close the error-analysis loop.** Fix the top bucket, re-measure, report the
   before and after. Highest value by a wide margin.
2. **Adversarial validation.** Train a classifier to distinguish train from test.
   If it succeeds, there is distribution shift and your CV is optimistic. This is
   the standard Kaggle technique and it is directly useful in Week 56.
3. **A pseudo-labeling experiment**, reported honestly whether or not it helps.
4. **Cost-sensitive threshold analysis** with a stated business cost ratio, and
   the dollar difference from the default threshold.

## Limitations To State Honestly

State plainly:

- Kaggle data is cleaner than production data and the test distribution is fixed.
  There is no drift, no upstream schema change, and no late-arriving label.
- Public leaderboard score is itself a form of test-set feedback, and using it to
  select models is a mild leak. Note how many submissions you made.
- The ensemble is more complex than the accuracy gain justifies for most
  production settings. Say what you would actually deploy.
- Feature engineering was informed by public discussion of the competition, which
  is community-level test-set exploration.
