# Month 01 Exercises

Every exercise for the month in one place, with time estimates and difficulty.
The **core** set is required — it is what the tests check. The **extension** set
is optional and ordered by value.

Total core time: roughly 26 hours across four weeks.

---

## Week 1 — Vectors, Matrices, Geometry

### Core (8.5h)

| # | Exercise | Time | Difficulty |
| - | -------- | ---- | ---------- |
| 1.1 | `dot_product`, `norm`, `normalize` | 45m | Easy |
| 1.2 | `cosine_similarity`, `euclidean_distance` | 30m | Easy |
| 1.3 | `angle_between` — clamp the cosine before `arccos` | 20m | Easy, one trap |
| 1.4 | `project`, `orthogonal_component` | 45m | Medium |
| 1.5 | `matmul` — triple loop first, then vectorized, then time both | 1h | Medium |
| 1.6 | `transpose`, `identity`, `trace`, `is_symmetric`, `is_orthogonal` | 45m | Easy |
| 1.7 | `matrix_vector_product` — implement both readings | 30m | Medium |
| 1.8 | `gram_schmidt` | 1h | Medium |
| 1.9 | `modified_gram_schmidt`, and construct a case where classical fails | 1h | Hard |
| 1.10 | `rank` via Gram-Schmidt | 30m | Medium |
| 1.11 | `batch_cosine_similarity` — one matmul, not a loop | 45m | Medium |
| 1.12 | `top_k_similar` — `argpartition`, not `argsort` | 30m | Medium |
| 1.13 | Notebook: projection, unit balls, scale invariance, timings | 1h | Easy |

**1.9 is the week's most instructive exercise.** Constructing an input where
classical Gram-Schmidt visibly loses orthogonality teaches more about numerical
computing than any amount of reading about it.

### Extensions

| # | Exercise | Time | Value |
| - | -------- | ---- | ----- |
| 1.E1 | Blocked/tiled matmul; benchmark against naive and NumPy at n=128/512/1024 | 2h | **High** — the memory-locality intuition that makes Week 49 land |
| 1.E2 | Householder QR, compared against Gram-Schmidt for stability | 2h | Medium |
| 1.E3 | Hypothesis property tests for all vector operations | 1h | Medium |
| 1.E4 | Visualize a 2-D linear transformation as an animation | 1.5h | Low, fun |

---

## Week 2 — Matrix Factorization and SVD

### Core (7.5h)

| # | Exercise | Time | Difficulty |
| - | -------- | ---- | ---------- |
| 2.1 | `eigen_decomposition` — remember to reverse `eigh`'s ordering | 45m | Easy, one trap |
| 2.2 | `power_iteration`, then observe slow convergence when λ₁ ≈ λ₂ | 1h | Medium |
| 2.3 | `svd`, `truncated_svd` | 45m | Easy |
| 2.4 | Verify σ² equals the eigenvalues of AᵀA | 30m | Medium, **essential** |
| 2.5 | `low_rank_approximation`, `reconstruction_error` | 45m | Medium |
| 2.6 | `explained_variance_ratio`, `rank_for_variance` — square the σ | 30m | Easy, one trap |
| 2.7 | `PCA` via eigendecomposition | 1h | Medium |
| 2.8 | `PCA` via SVD, and verify the two agree | 45m | Medium, **essential** |
| 2.9 | Fix a deterministic sign convention | 20m | Easy, prevents flaky tests |
| 2.10 | `compress_image` and the notebook grid | 1.5h | Medium |

**2.4 and 2.8 are the exercises that matter.** They are the same fact seen twice,
and understanding it is the difference between reciting PCA and knowing it.

### Extensions

| # | Exercise | Time | Value |
| - | -------- | ---- | ----- |
| 2.E1 | Randomized SVD; compare accuracy and speed at n=5000 | 3h | **High** — how it is done at scale |
| 2.E2 | PCA on a real embedding set (download GloVe vectors), plot 2-D | 1.5h | **High** — previews Month 7 |
| 2.E3 | Construct data where PCA discards the discriminative direction | 1h | **High** — the 10/10 interview answer |
| 2.E4 | Compare PCA against t-SNE and UMAP on the same data | 2h | Medium |

**2.E3 is worth doing.** Being able to say "here is a dataset where PCA throws
away exactly the direction you need, and here is why" moves your answer to "what
does PCA lose?" from a 7 to a 10.

---

## Week 3 — Calculus and Gradients

### Core (10h)

| # | Exercise | Time | Difficulty |
| - | -------- | ---- | ---------- |
| 3.1 | **Derive on paper:** MSE, sigmoid, sigmoid+BCE, softmax+CE | 1.5h | Hard, **do this first** |
| 3.2 | `Value.__add__`, `__mul__`, `__pow__`, and their backward closures | 1.5h | Medium |
| 3.3 | `__neg__`, `__sub__`, `__truediv__` | 30m | Easy |
| 3.4 | `exp`, `log`, `tanh`, `relu`, `sigmoid` | 1h | Medium |
| 3.5 | `topological_sort` | 45m | Medium |
| 3.6 | `backward`, `zero_grad` | 45m | Medium |
| 3.7 | `numerical_gradient` — central difference, copy the input | 30m | Easy |
| 3.8 | `gradient_check` — relative error | 1h | Medium, **most valuable function in the workspace** |
| 3.9 | `mse_loss`, `binary_cross_entropy` with clamping | 45m | Medium |
| 3.10 | `softmax` with max subtraction, `cross_entropy` fused | 1h | Hard |
| 3.11 | Make `test_gradient_descent_fits_a_line` pass | 45m | Medium, **the week's gate** |

**3.1 before 3.2.** Implementing a derivative you have not derived teaches you
where the parentheses go, not what the mathematics means.

### Extensions

| # | Exercise | Time | Value |
| - | -------- | ---- | ----- |
| 3.E1 | Array-valued `Value` with broadcasting-aware backward | 4h | **Highest** — this is the hard part of Week 14 |
| 3.E2 | Visualize the computational graph with graphviz | 1.5h | **High** — great notebook figure |
| 3.E3 | Add `sin`, `cos`, `sqrt`, `abs`, and gradient-check each | 1h | Medium |
| 3.E4 | Implement forward-mode autodiff; compare cost for 1 vs 1000 inputs | 2h | **High** — makes the complexity argument concrete |
| 3.E5 | Train a 2-layer MLP on XOR using only `Value` | 2h | Medium — previews Week 13 |

**3.E1 is the highest-value extension in the entire month.** Broadcasting-aware
backward passes are the main difficulty of Week 14, and doing it now turns
Month 4 from a struggle into a review.

---

## Week 4 — Probability and Information Theory

### Core (7h)

| # | Exercise | Time | Difficulty |
| - | -------- | ---- | ---------- |
| 4.1 | `mean`, `variance`, `standard_deviation` with ddof | 30m | Easy |
| 4.2 | `covariance_matrix`, `correlation_matrix` | 45m | Medium |
| 4.3 | `standardize` returning the training statistics | 20m | Easy, previews Week 10 |
| 4.4 | `Bernoulli`, `Gaussian` — including stable `log_pdf` | 1h | Medium |
| 4.5 | `Poisson` — use `lgamma`, not `factorial` | 45m | Medium, one trap |
| 4.6 | `Categorical` with inverse-CDF sampling | 45m | Medium, previews Week 35 |
| 4.7 | `mle_bernoulli`, `mle_gaussian`, `log_likelihood` | 45m | Medium |
| 4.8 | Verify the MLE variance bias empirically | 30m | Medium |
| 4.9 | `bayes_rule`, and work the base-rate problem | 30m | Easy, **memorize the answer** |
| 4.10 | `bootstrap_confidence_interval` | 45m | Medium |
| 4.11 | `entropy`, `cross_entropy`, `kl_divergence`, `js_divergence` | 1h | Medium |
| 4.12 | Verify H(p,q) = H(p) + D(p‖q) numerically | 20m | Easy, **essential** |
| 4.13 | `perplexity`, `mutual_information`, `conditional_entropy` | 45m | Medium |
| 4.14 | `information_gain`, `gini_impurity` | 30m | Easy, used in Week 7 |
| 4.15 | Notebook: distributions, CLT, likelihood surface, base rate, entropy curve | 1.5h | Easy |

### Extensions

| # | Exercise | Time | Value |
| - | -------- | ---- | ----- |
| 4.E1 | Bayesian linear regression with a predictive distribution | 3h | **High** — connects to Week 5's ridge as MAP |
| 4.E2 | Derive and verify: cross entropy = NLL of a categorical; MSE = NLL of a Gaussian | 1.5h | **Highest** — this is the month's central idea |
| 4.E3 | Implement a Metropolis-Hastings sampler for a 2-D distribution | 2h | Medium |
| 4.E4 | Compute mutual information between features and target on a real dataset; compare to correlation | 1.5h | **High** — previews Week 10 |

**4.E2 is not really optional.** If you can derive both, "why this loss function?"
becomes a question you answer from first principles for the rest of the course.

---

## Cross-Week Integration

Do these at the end of Week 4, before the capstone. They connect the modules and
frequently surface misunderstandings that the per-week tests miss.

| # | Exercise | Time | Value |
| - | -------- | ---- | ----- |
| X.1 | Verify `information_theory.cross_entropy` matches `autodiff_scalar.cross_entropy` | 45m | **High** — reconciles two implementations |
| X.2 | Use Week 3 autodiff to fit a logistic regression, evaluate with Week 4 metrics | 1.5h | **High** — previews Week 6 |
| X.3 | PCA (Week 2) a dataset, then fit on the reduced data. Plot accuracy vs components | 1.5h | Medium |
| X.4 | Compute the entropy (Week 4) of a distribution PCA (Week 2) was applied to; relate variance retained to information retained | 1h | Medium, conceptually interesting |

**X.1 is the one to prioritize.** Two implementations of the same quantity,
written from different angles, and any discrepancy is a misunderstanding you
would otherwise carry into Month 2.

---

## If You Finish Early

In priority order:

1. Extension 3.E1 (array autodiff) — converts Month 4 into a review
2. Extension 4.E2 (loss functions as MLE) — the month's central idea
3. Extension 2.E3 (PCA counterexample) — the 10/10 interview answer
4. Integration exercise X.1 — catches real misunderstandings
5. An extra hour of interview drills

Do **not** spend it on more theory reading. The binding constraint in this course
is implementation and articulation, never input.
