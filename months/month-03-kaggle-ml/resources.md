# Month 03 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Christoph Molnar, 'Interpretable Machine Learning'** (Week 12, free) — https://christophm.github.io/interpretable-ml-book/
The standard reference for everything in Week 12. Read the chapters on
permutation importance, PDP, ICE, LIME, and SHAP.

**Andrew Ng, 'Machine Learning Yearning'** (Week 12, free)
The error analysis chapters are short and they are the clearest statement of the
method anywhere. Forty minutes, high return.

**scikit-learn, 'Common pitfalls and recommended practices'** (Week 10) — https://scikit-learn.org/stable/common_pitfalls.html
Read the data leakage section in full. It is the most practically useful page in
the entire sklearn documentation.

---

## Week 9 — Gradient Boosting

- **Primary:** Elements of Statistical Learning, ch. 10 — https://hastie.su.domains/ElemStatLearn/ — the definitive treatment; sections 10.1-10.10
- **Primary:** 'Gradient Boosting explained' by Terence Parr and Jeremy Howard — https://explained.ai/gradient-boosting/ — the clearest walkthrough with worked arithmetic
- XGBoost documentation, 'Introduction to Boosted Trees' — https://xgboost.readthedocs.io/en/stable/tutorials/model.html
- LightGBM features documentation — https://lightgbm.readthedocs.io/en/latest/Features.html — read this for the histogram and leaf-wise ideas
- StatQuest, 'Gradient Boost Parts 1-4' — the arithmetic worked by hand, which is genuinely helpful here
## Week 10 — Feature Engineering and Data Leakage

- **Primary:** Kaggle Learn, Feature Engineering — https://www.kaggle.com/learn/feature-engineering — short and practical
- **Primary:** Kaggle Learn, Intermediate ML, 'Data Leakage' lesson — https://www.kaggle.com/code/alexisbcook/data-leakage
- 'Leakage in Data Mining' (Kaufman et al., 2011) — the paper that named and categorized this properly. Worth reading; it is clearer than most treatments.
- scikit-learn, 'Common pitfalls and recommended practices' — https://scikit-learn.org/stable/common_pitfalls.html — read the data leakage section in full
- CatBoost's ordered target statistics documentation — https://catboost.ai/en/docs/concepts/algorithm-main-stages_cat-to-numberic — a production solution to the target encoding problem
## Week 11 — Model Evaluation and Calibration

- **Primary:** scikit-learn, 'Cross-validation: evaluating estimator performance' — https://scikit-learn.org/stable/modules/cross_validation.html — read the section on grouped and time-series splits carefully
- **Primary:** scikit-learn, 'Probability calibration' — https://scikit-learn.org/stable/modules/calibration.html
- 'On Calibration of Modern Neural Networks' (Guo et al., 2017) — https://arxiv.org/abs/1706.04599 — the paper that showed deep networks are badly miscalibrated. Relevant again in Week 36.
- Efron and Tibshirani on the bootstrap — you need the percentile method, roughly six pages
- 'Statistical Significance Tests for Machine Learning' — for the paired comparison reasoning
## Week 12 — Explainability and Error Analysis

- **Primary:** Christoph Molnar, 'Interpretable Machine Learning' (free) — https://christophm.github.io/interpretable-ml-book/ — chapters on PDP, ICE, permutation importance, LIME, and SHAP. The standard reference.
- **Primary:** Andrew Ng, 'Machine Learning Yearning' (free) — the chapters on error analysis are the clearest statement of the method
- 'A Unified Approach to Interpreting Model Predictions' (Lundberg and Lee, 2017) — https://arxiv.org/abs/1705.07874 — the SHAP paper
- 'Model Cards for Model Reporting' (Mitchell et al., 2019) — https://arxiv.org/abs/1810.03993
- SHAP documentation — https://shap.readthedocs.io/ — use it after implementing exact Shapley values yourself

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| NumPy | https://numpy.org/doc/stable/ | Everything |
| pandas | https://pandas.pydata.org/docs/ | Tabular data |
| scikit-learn | https://scikit-learn.org/stable/user_guide.html | Reference implementations to compare against |
| matplotlib | https://matplotlib.org/stable/ | Every notebook |
| pytest | https://docs.pytest.org/ | The workspace |
| NeetCode 150 | https://neetcode.io/practice | Weekly coding drills |
| XGBoost | https://xgboost.readthedocs.io/ | Week 9 and the capstone |
| LightGBM | https://lightgbm.readthedocs.io/ | Week 9 and the capstone |
| SHAP | https://shap.readthedocs.io/ | Week 12, after implementing exact Shapley yourself |
| Kaggle | https://www.kaggle.com/competitions | The capstone |

---

## Deliberately Omitted

- **AutoML.** Useful in practice, teaches nothing here. You are building the
  judgment that AutoML automates.
- **Deep learning for tabular data.** Occasionally competitive, usually not, and
  Phase 2 covers deep learning properly. Know that TabNet and FT-Transformer
  exist and that gradient boosting still usually wins.
- **Hyperparameter optimization theory (Bayesian optimization, Hyperband).** Use
  Optuna as a tool if you like; the theory is not asked and not load-bearing.
- **Full SHAP theory.** Implement exact Shapley values on a small problem to
  understand the definition, then use the library. The approximation algorithms
  are a research area of their own.
