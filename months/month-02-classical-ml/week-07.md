# Week 07: Decision Trees

## Outcome

By Sunday you can implement a CART classifier and regressor from scratch with an efficient split search, and explain precisely why trees overfit and what each hyperparameter does about it.

Concretely: `tests/test_decision_tree.py` passes, including `test_unconstrained_tree_memorizes_the_training_set`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Trees are the base learner for the two models that still win on tabular data,
so Weeks 8 and 9 depend on this one. But the standalone interview value is
narrower than people expect: "why do trees overfit?" and "gini or entropy?" are
the questions, and the second has a boring correct answer that candidates often
over-elaborate.

The genuinely valuable part of this week is the split-search optimization. The
naive implementation is O(n^2 d) per node; sorting once and updating counts
incrementally gets you to O(n d log n). Doing that yourself teaches you more
about algorithmic thinking applied to ML than any amount of theory, and it is the
kind of thing that comes up when an interviewer asks how you would make something
faster.

Connection worth making explicit: `information_gain` is the function you wrote in
Week 4. Decision trees are an information-theoretic algorithm.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Recursive partitioning**
   1. Axis-aligned splits, and what that geometry can and cannot express
   2. The greedy algorithm, and why it is not globally optimal
   3. Stopping criteria and their interactions
2. **Impurity**
   1. Gini impurity: 1 - sum p^2
   2. Entropy: Week 4's function, reused
   3. Information gain as the split criterion
   4. Why they rarely disagree, and why gini is the common default
   5. Variance reduction for regression trees
3. **Finding the best split**
   1. The naive approach and its cost
   2. Sort once, sweep the threshold, update counts incrementally
   3. Handling categorical features
   4. Missing values: surrogate splits versus a separate branch
4. **Why trees overfit**
   1. An unconstrained tree can always reach zero training error
   2. A leaf with three samples is a rule learned from three samples
   3. max_depth, min_samples_split, min_samples_leaf, and what each prevents
   4. Cost-complexity pruning as a principled alternative
5. **What trees cannot do**
   1. No extrapolation — predictions clamp to the training range
   2. Piecewise-constant output, so smooth functions need many splits
   3. High variance: small data changes produce very different trees
   4. Badly calibrated leaf probabilities

## Required Free Resources

- **Primary:** An Introduction to Statistical Learning, ch. 8.1 — https://www.statlearning.com/
- **Primary:** scikit-learn decision tree guide, including the mathematical formulation — https://scikit-learn.org/stable/modules/tree.html
- Elements of Statistical Learning, ch. 9.2 (CART) — https://hastie.su.domains/ElemStatLearn/
- StatQuest, 'Decision Trees' and 'Regression Trees' — good for the split-search intuition
- R2D3, 'A Visual Introduction to Machine Learning' — http://www.r2d3.us/visual-intro-to-machine-learning-part-1/ — the best visual explanation of tree overfitting anywhere

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=7
```

1. **`gini`, `entropy`, `variance_reduction`** (45m) — Reuse the Week 4 implementations. Verify they agree on the same splits most of the time.
2. **Naive `_best_split`** (1.5h) — Get it correct first. Time it on 10,000 rows.
3. **Optimized `_best_split`** (2h) — Sort once per feature, sweep, update counts incrementally. Time it again. The gap is the lesson.
4. **`DecisionTreeClassifier.fit` and `predict`** (1.5h) — Recursive construction with the stopping criteria.
5. **Constraint parameters** (1h) — max_depth, min_samples_split, min_samples_leaf. Verify each is actually respected by walking the tree.
6. **`predict_proba` and observe the overconfidence** (30m) — Deep trees report 1.0 on the strength of two samples. Week 11 fixes this.
7. **`print_tree`** (45m) — Then trace one prediction through it by hand. Interpretability is a real selling point.
8. **`DecisionTreeRegressor`** (1h) — Then demonstrate that it cannot extrapolate — predict at x=1000 after training on x in [0,10].
9. **Compare against sklearn** (45m) — Same data, same hyperparameters. Investigate every disagreement.

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
d
e
c
i
s
i
o
n
_
t
r
e
e
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
t
r
e
e
_
b
o
u
n
d
a
r
i
e
s
.
i
p
y
n
b
```

## Tests To Write

`tests/test_decision_tree.py` is the specification. Add two:

1. A performance test asserting that your optimized split search is at least 10x
   faster than the naive version on 20,000 rows with 20 features. Print both
   times.
2. A test that a tree trained on a rotated version of a linearly-separable
   dataset needs substantially more depth than on the unrotated version — the
   axis-aligned limitation, made concrete.

## Portfolio Artifact

`src/decision_tree.py` and `notebooks/tree_boundaries.ipynb` showing decision boundaries at depths 1, 3, 5, and unlimited on a 2-D problem, with train and test accuracy annotated on each. That four-panel figure explains overfitting better than any paragraph.

## Interview Drills

**Coding (45 min).** Two problems, graphs and BFS/DFS. Tree recursion this week should feel easier than usual — you have been writing it.

**ML theory (20 min).** Recorded: *Why do decision trees overfit, and what are three distinct ways to prevent it?* Then the follow-up: *gini or entropy, and why?* The correct answer to the second is 'they almost always agree, gini avoids a logarithm, that is the whole reason' — resist inventing something deeper.

**System design warm-up (15 min).** You need to serve a tree ensemble at 50k predictions per second. What are your options? (Compilation to code, vectorized traversal, quantized thresholds, and reducing ensemble size are the real answers.)

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement cost-complexity pruning: grow the tree fully, then compute the pruning
path by iteratively removing the subtree with the lowest gain-per-node, and
select alpha by cross-validation.

This is what sklearn's `ccp_alpha` does, and it is a more principled regularizer
than a depth limit because it lets the tree be deep where the data supports it
and shallow where it does not. Plot the alpha path — nodes versus alpha, and
validation accuracy versus alpha — and identify the knee.
