# Month 02 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**CS229 lecture notes 1** (Weeks 5-6) — https://cs229.stanford.edu/
The cleanest free derivations of linear and logistic regression. Read sections
1-3 and the GLM section properly; they are the source for two derivations you
must know cold.

**An Introduction to Statistical Learning, chapters 3, 4, 8** — https://www.statlearning.com/
Free PDF. The best-pitched treatment of classical ML: rigorous enough to be
useful, accessible enough to read in a week.

**R2D3, 'A Visual Introduction to Machine Learning'** (Week 7) — http://www.r2d3.us/visual-intro-to-machine-learning-part-1/
Fifteen minutes, and the best visual explanation of tree overfitting in existence.

---

## Week 5 — Linear Regression

- **Primary:** CS229 lecture notes 1, sections 1-3 — https://cs229.stanford.edu/ — the cleanest derivation of least squares available free
- **Primary:** An Introduction to Statistical Learning, ch. 3 — https://www.statlearning.com/
- Elements of Statistical Learning, ch. 3.4 (shrinkage) — https://hastie.su.domains/ElemStatLearn/
- scikit-learn linear models guide — https://scikit-learn.org/stable/modules/linear_model.html — read after implementing
- StatQuest, 'Ridge and Lasso Regression' — good intuition for why L1 zeroes out
## Week 6 — Logistic Regression and Classification Metrics

- **Primary:** CS229 lecture notes 1, sections on logistic regression and GLMs — https://cs229.stanford.edu/
- **Primary:** Google ML Crash Course, Classification module — https://developers.google.com/machine-learning/crash-course/classification/video-lecture — unusually good on metrics
- Jason Brownlee, 'ROC Curves and Precision-Recall Curves for Imbalanced Classification' — the clearest treatment of the ROC/PR distinction
- scikit-learn model evaluation guide — https://scikit-learn.org/stable/modules/model_evaluation.html — read after implementing
- 'The Relationship Between Precision-Recall and ROC Curves' (Davis and Goadrich, 2006) — the paper behind the interview answer
## Week 7 — Decision Trees

- **Primary:** An Introduction to Statistical Learning, ch. 8.1 — https://www.statlearning.com/
- **Primary:** scikit-learn decision tree guide, including the mathematical formulation — https://scikit-learn.org/stable/modules/tree.html
- Elements of Statistical Learning, ch. 9.2 (CART) — https://hastie.su.domains/ElemStatLearn/
- StatQuest, 'Decision Trees' and 'Regression Trees' — good for the split-search intuition
- R2D3, 'A Visual Introduction to Machine Learning' — http://www.r2d3.us/visual-intro-to-machine-learning-part-1/ — the best visual explanation of tree overfitting anywhere
## Week 8 — Ensembles and Random Forests

- **Primary:** An Introduction to Statistical Learning, ch. 8.2 — https://www.statlearning.com/
- **Primary:** Breiman, 'Random Forests' (2001) — https://link.springer.com/article/10.1023/A:1010933404324 — genuinely readable, and reading a foundational paper is good practice for Month 16
- scikit-learn ensemble guide — https://scikit-learn.org/stable/modules/ensemble.html#forest
- 'Beware Default Random Forest Importances' — https://explained.ai/rf-importance/ — the case for permutation importance, with evidence
- StatQuest, 'Random Forests Part 1 and 2'

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

---

## Deliberately Omitted

- **SVMs and the kernel trick.** Worth knowing they exist; rarely asked at
  frontier labs and not used in the rest of this course. If an interviewer raises
  them, "maximum-margin classifier, kernels let it fit non-linear boundaries in
  a lifted space" is sufficient.
- **Naive Bayes.** Ten minutes of reading. It appears in Week 28 as a text
  classification baseline, which is the only place it matters here.
- **k-means and clustering.** Deferred to Week 26 where it is applied to
  embeddings, which is the context you will actually use it in.
- **Formal statistical learning theory (VC dimension, PAC bounds).** Intellectually
  interesting, essentially never asked, and not load-bearing for anything later.
