# Month 02 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 5 — Linear Regression

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 5.1 | `normal_equation` with optional ridge | 1h | Medium |
| 5.2 | `gradient_descent_step` and the GD path | 1.5h | Medium |
| 5.3 | Verify the two methods agree | 30m | Easy |
| 5.4 | Watch it diverge | 20m | Easy |
| 5.5 | `mse`, `mae`, `rmse`, `r_squared` | 45m | Easy |
| 5.6 | L1 vs L2 comparison | 1h | Medium |
| 5.7 | `polynomial_features` and the overfitting figure | 1h | Medium |
| 5.8 | `train_test_split` | 30m | Easy |
| 5.9 | `bias_variance_decomposition` | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 5.E1 | Implement Huber loss and show it is robust where MSE is not | 1.5h | High — a good 'what if the data has outliers' answer |
| 5.E2 | Derive and verify that ridge = MAP with a Gaussian prior | 2h | High — connects Weeks 4 and 5 |
| 5.E3 | Locally weighted linear regression (CS229 notes) | 2h | Medium — a nice non-parametric contrast |
| 5.E4 | Elastic net, and find where it beats both L1 and L2 | 1.5h | Medium |

## Week 6 — Logistic Regression and Classification Metrics

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 6.1 | `sigmoid`, stably | 30m | Easy |
| 6.2 | `log_loss` with clipping | 30m | Easy |
| 6.3 | `LogisticRegression` | 1.5h | Medium |
| 6.4 | `confusion_matrix` and the basic metrics | 1h | Easy |
| 6.5 | `roc_curve`, `roc_auc` | 1.5h | Medium |
| 6.6 | `precision_recall_curve`, `average_precision` | 1h | Medium |
| 6.7 | The imbalance demonstration | 1h | Medium |
| 6.8 | `find_optimal_threshold` with asymmetric costs | 1h | Medium |
| 6.9 | `SoftmaxRegression` | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 6.E1 | Implement Newton's method / IRLS for logistic regression; compare convergence to GD | 2h | High — shows second-order optimization concretely |
| 6.E2 | Build a cost-curve plot: expected cost vs threshold, for three cost ratios | 1.5h | High — the figure that makes the interview answer visual |
| 6.E3 | Implement MCC and compare its behavior to F1 across imbalance levels | 1h | Medium |
| 6.E4 | Multi-label classification with per-label thresholds | 2h | Medium |

## Week 7 — Decision Trees

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 7.1 | `gini`, `entropy`, `variance_reduction` | 45m | Easy |
| 7.2 | Naive `_best_split` | 1.5h | Medium |
| 7.3 | Optimized `_best_split` | 2h | Hard |
| 7.4 | `DecisionTreeClassifier.fit` and `predict` | 1.5h | Medium |
| 7.5 | Constraint parameters | 1h | Medium |
| 7.6 | `predict_proba` and observe the overconfidence | 30m | Easy |
| 7.7 | `print_tree` | 45m | Easy |
| 7.8 | `DecisionTreeRegressor` | 1h | Medium |
| 7.9 | Compare against sklearn | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 7.E1 | Cost-complexity pruning, and the alpha path | 2.5h | High — the principled alternative to depth limits, and sklearn's actual method |
| 7.E2 | Surrogate splits for missing values | 2h | Medium — how CART actually handles nulls |
| 7.E3 | Visualize the decision boundary in 2-D at increasing depths | 1.5h | High — the clearest possible picture of overfitting |
| 7.E4 | Categorical split handling without one-hot encoding | 2h | Medium — why LightGBM handles categoricals natively |

## Week 8 — Ensembles and Random Forests

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 8.1 | `bootstrap_sample` with OOB indices | 45m | Easy |
| 8.2 | `RandomForestClassifier.fit` | 1.5h | Medium |
| 8.3 | `predict` and `predict_proba` | 1h | Medium |
| 8.4 | The decorrelation experiment | 1.5h | Hard |
| 8.5 | `_compute_oob_score` | 1.5h | Hard |
| 8.6 | `RandomForestRegressor` | 45m | Easy |
| 8.7 | `permutation_importance` | 1.5h | Medium |
| 8.8 | The correlated-features caveat | 45m | Medium |
| 8.9 | Compare against sklearn | 30m | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 8.E1 | Extremely Randomized Trees (random thresholds too); compare bias/variance | 2h | High — isolates the decorrelation effect even further |
| 8.E2 | Plot OOB error against number of trees; find where it plateaus | 1h | High — the empirical answer to 'how many trees?' |
| 8.E3 | Implement isolation forest for anomaly detection | 2.5h | High — directly useful for Month 11's telemetry anomaly detection |
| 8.E4 | Parallelize training with multiprocessing; measure the speedup | 1.5h | Medium |

---

## If You Finish Early

In priority order:

1. Week 6's cost-curve stretch goal — it produces a complete interview answer
2. Week 8's isolation forest — you will import it in Week 43
3. Week 7's cost-complexity pruning — the principled regularizer
4. An extra hour of coding drills, focused on trees and graphs

Not more theory. The binding constraint is implementation and articulation.
