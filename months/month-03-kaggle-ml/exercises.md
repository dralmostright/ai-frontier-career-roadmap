# Month 03 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 9 — Gradient Boosting

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 9.1 | Work one boosting round by hand | 45m | Medium |
| 9.2 | `GradientBoostingRegressor` | 2h | Medium |
| 9.3 | `staged_predict` | 45m | Easy |
| 9.4 | The overfitting demonstration | 1h | Medium |
| 9.5 | Depth ablation | 45m | Easy |
| 9.6 | `GradientBoostingClassifier` | 1.5h | Hard |
| 9.7 | `subsample` and stochastic boosting | 45m | Easy |
| 9.8 | `AdaBoostClassifier` | 1h | Medium |
| 9.9 | Compare against XGBoost/LightGBM | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 9.E1 | Add second-order gradients (Newton boosting, as XGBoost does) | 3h | High — the actual difference between your version and XGBoost |
| 9.E2 | Histogram-based split finding, as LightGBM does | 2.5h | High — the source of most of the speed difference |
| 9.E3 | Implement ordered target statistics (CatBoost's leakage fix) | 2h | High — connects directly to Week 10 |
| 9.E4 | Plot the learning-rate/rounds tradeoff surface | 1.5h | Medium — makes the tradeoff visual |

## Week 10 — Feature Engineering and Data Leakage

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 10.1 | `StandardScaler` with fit/transform separation | 45m | Easy |
| 10.2 | `OneHotEncoder` with unseen-category handling | 1h | Medium |
| 10.3 | `MissingValueImputer` with an indicator column | 45m | Medium |
| 10.4 | `TargetEncoder`, naive version | 1h | Medium |
| 10.5 | `TargetEncoder`, out-of-fold with smoothing | 1.5h | Hard |
| 10.6 | `Pipeline` | 1h | Medium |
| 10.7 | `detect_target_leakage` | 1h | Medium |
| 10.8 | `detect_train_test_contamination` | 1h | Medium |
| 10.9 | `temporal_split_check` | 45m | Easy |
| 10.10 | Datetime and aggregation features | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 10.E1 | Build a leakage scenario quiz: 10 descriptions, some leaky, some not | 2h | Highest — this is direct interview preparation, and writing it teaches you more than answering it |
| 10.E2 | Implement CatBoost-style ordered target statistics | 2.5h | High — a production-grade solution |
| 10.E3 | Adversarial validation: train a classifier to distinguish train from test | 2h | High — the standard Kaggle technique for detecting distribution shift, and directly useful in Week 56 |
| 10.E4 | Automated feature generation with featuretools, then audit it for leakage | 2h | Medium — automated feature generation is a leakage machine |

## Week 11 — Model Evaluation and Calibration

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 11.1 | `k_fold_split`, `stratified_k_fold_split` | 1h | Medium |
| 11.2 | `time_series_split` | 45m | Easy |
| 11.3 | `group_k_fold_split` | 45m | Medium |
| 11.4 | `cross_validate` taking a factory | 1h | Medium |
| 11.5 | `bootstrap_metric_ci` | 1h | Medium |
| 11.6 | `paired_bootstrap_test` | 1.5h | Hard |
| 11.7 | `learning_curve` | 1h | Medium |
| 11.8 | `calibration_curve` and `expected_calibration_error` | 1.5h | Medium |
| 11.9 | `PlattScaling` and `IsotonicCalibration` | 1.5h | Hard |
| 11.10 | `class_weights` and `resample` | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 11.E1 | Nested cross-validation, and measure the optimism of non-nested tuning | 2.5h | Highest — quantifies a bias most people do not know they have |
| 11.E2 | Temperature scaling for multiclass calibration | 1.5h | High — the standard method for neural networks, needed in Week 36 |
| 11.E3 | Compare bootstrap CIs against analytic CIs for AUC (DeLong's method) | 2h | Medium |
| 11.E4 | Build a model-comparison report generator: two models in, a significance-tested comparison out | 2h | High — reusable for the rest of the course |

## Week 12 — Explainability and Error Analysis

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 12.1 | `permutation_importance_report` | 1h | Medium |
| 12.2 | `partial_dependence` | 1h | Medium |
| 12.3 | `individual_conditional_expectation` | 1h | Hard |
| 12.4 | `shapley_values_exact` | 1.5h | Hard |
| 12.5 | `ErrorAnalysis.worst_errors` | 45m | Easy |
| 12.6 | `error_rate_by_slice` | 1h | Medium |
| 12.7 | `confusion_examples` | 45m | Easy |
| 12.8 | `calibration_by_slice` | 45m | Medium |
| 12.9 | `find_label_noise` | 1h | Medium |
| 12.10 | `summary_report` and `model_card` | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 12.E1 | Fix the top error bucket and measure the improvement | 3h | Highest — closes the loop and turns analysis into a result |
| 12.E2 | Audit labels: find the noisiest 1%, correct them, retrain, measure | 3h | High — 'I audited the labels and 3% were wrong' is a great interview story |
| 12.E3 | Build an interactive error-exploration dashboard | 3h | Medium — useful, and a good excuse to learn a dashboard tool before Week 56 |
| 12.E4 | Counterfactual explanations: minimal change that flips the prediction | 2.5h | Medium — powerful for stakeholder communication |

---

## If You Finish Early

In priority order:

1. Week 12's loop-closing exercise — fix the top error bucket and measure it
2. Week 10's leakage quiz — direct interview preparation, and shareable
3. Week 11's nested CV optimism measurement — calibrates your skepticism
4. Week 9's Newton boosting — the real difference between yours and XGBoost

This is the last month of Phase 1. If you have spare hours, the highest-value use
is closing gaps from Months 1-2 rather than extending Month 3. Check the Gate G1
requirements in `SCORECARD.md`.
