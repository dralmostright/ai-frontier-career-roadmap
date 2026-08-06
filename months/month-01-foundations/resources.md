# Month 01 Resources

Everything, organized by week. **Do not attempt all of it.** Each week names one
or two primary resources; the rest is reference material to consult when stuck.

Theory is capped at 30% of your hours. If you are over that, you are watching
instead of building.

---

## The Three Worth Doing In Full

Almost everything in this index should be consulted selectively. These three are
worth watching or reading end to end:

1. **3Blue1Brown, Essence of Linear Algebra** (Weeks 1-2, ~3.5 hours) —
   https://www.3blue1brown.com/topics/linear-algebra
   The best intuition-building resource in existence for this material. Chapters
   1-9 for Week 1, 13-14 for Week 2.

2. **Karpathy, "building micrograd"** (Week 3, ~2.5 hours) —
   https://karpathy.ai/zero-to-hero.html
   Watch it, then close the tab and rebuild from memory. This video is the single
   highest-leverage 2.5 hours in Phase 1.

3. **Chris Olah, "Visual Information Theory"** (Week 4, ~1 hour) —
   https://colah.github.io/posts/2015-09-Visual-Information/
   The clearest treatment of entropy, cross entropy, and KL anywhere.

---

## Week 1 — Vectors, Matrices, Geometry

**Primary**
- 3Blue1Brown, Essence of Linear Algebra ch. 1-9 — https://www.3blue1brown.com/topics/linear-algebra
- Mathematics for Machine Learning, ch. 2.1-2.4, 3.1-3.3 — https://mml-book.github.io/

**Reference**
- MIT OCW 18.06, lectures 1-4 — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/
- NumPy linear algebra reference — https://numpy.org/doc/stable/reference/routines.linalg.html
- Gram-Schmidt and numerical stability (MIT 18.06 lecture 17)

**Read after implementing**
- The Illustrated Word2vec — https://jalammar.github.io/illustrated-word2vec/
  Connects the geometry to embeddings. Lands properly once you have written
  `cosine_similarity` yourself.

**Skip unless curious**
- Strang's full 18.06 course. It is excellent and it is 35 lectures. You do not
  have time and you do not need it.

---

## Week 2 — Matrix Factorization and SVD

**Primary**
- 3Blue1Brown, Essence of Linear Algebra ch. 13-14 — https://www.3blue1brown.com/topics/linear-algebra
- Mathematics for Machine Learning, ch. 4.1-4.5 and ch. 10 — https://mml-book.github.io/

**Reference**
- MIT OCW 18.06, lectures 21-22 (eigenvalues), 29-30 (SVD)
- scikit-learn PCA guide — https://scikit-learn.org/stable/modules/decomposition.html#pca
  Read after implementing. Compare their sign convention to yours.
- "A Singularly Valuable Decomposition" (Kalman, 1996) — a readable classic

**For the stretch goal**
- Halko, Martinsson, Tropp, "Finding Structure with Randomness" —
  https://arxiv.org/abs/0909.4061
  The randomized SVD paper. Sections 1 and 4 are the readable parts.

---

## Week 3 — Calculus and Gradients

**Primary**
- Karpathy, "building micrograd" — https://karpathy.ai/zero-to-hero.html
- 3Blue1Brown, Essence of Calculus ch. 1-4 — https://www.3blue1brown.com/topics/calculus
- 3Blue1Brown, Neural Networks ch. 3-4 — https://www.3blue1brown.com/topics/neural-networks

**Reference**
- micrograd source (~150 lines) — https://github.com/karpathy/micrograd
  **After** yours works. Then diff the designs.
- CS231n, backpropagation notes — https://cs231n.github.io/optimization-2/
  The best written treatment of gradient flow. Worth reading in full.
- CS231n, gradient checking notes — https://cs231n.github.io/neural-networks-3/#gradcheck
- The Matrix Cookbook — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
  Not needed this week (scalars only). Bookmark it for Week 14.

**For the derivations**
- CS229 lecture notes 1, sections on linear and logistic regression —
  https://cs229.stanford.edu/
  The cleanest written derivations of the two gradients you must know cold.

---

## Week 4 — Probability, Statistics, Information Theory

**Primary**
- Mathematics for Machine Learning, ch. 6 — https://mml-book.github.io/
- Chris Olah, "Visual Information Theory" — https://colah.github.io/posts/2015-09-Visual-Information/
- Seeing Theory, ch. 1-4 (interactive) — https://seeing-theory.brown.edu/

**Reference**
- MIT OCW 18.05 — https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/
- SciPy stats reference — https://docs.scipy.org/doc/scipy/reference/stats.html
  Your test oracle.
- 3Blue1Brown, "Bayes theorem" and "The medical test paradox" —
  https://www.3blue1brown.com/topics/probability

**On the bootstrap**
- Efron and Tibshirani, "An Introduction to the Bootstrap" — the standard
  reference. You need roughly six pages of it; find the percentile method.

**Optional**
- MacKay, "Information Theory, Inference, and Learning Algorithms" (free PDF) —
  https://www.inference.org.uk/mackay/itila/
  Chapters 1-2 and 4. Excellent and long; dip in rather than reading through.

---

## Tools and Documentation

| Tool | Link | Used for |
| ---- | ---- | -------- |
| NumPy | https://numpy.org/doc/stable/ | Everything |
| SciPy stats | https://docs.scipy.org/doc/scipy/reference/stats.html | Week 4 test oracle |
| Matplotlib | https://matplotlib.org/stable/ | Every notebook |
| pytest | https://docs.pytest.org/ | The whole workspace |
| Hypothesis | https://hypothesis.readthedocs.io/ | Property tests |
| ruff | https://docs.astral.sh/ruff/ | Linting |

---

## Interview Preparation

**Coding, from Week 1**
- NeetCode 150 — https://neetcode.io/practice
  Arrays and two pointers (Week 1), hash maps (Week 2), strings and sliding
  window (Week 3), your choice (Week 4). Two to three problems weekly, timed.

**ML theory**
- Deep Learning Interviews (Kashani, free) — https://arxiv.org/abs/2201.00650
  Chapters on calculus, probability, and information theory map directly to this
  month.

---

## What This Month Deliberately Omits

Named here so you know it is a choice rather than an oversight:

- **Full 18.06 or 18.05.** Both excellent, both far more than you need. You are
  building the specific machinery ML uses, not taking a mathematics course.
- **Measure-theoretic probability.** Never needed in this course.
- **Convex optimization theory.** Week 15 covers the optimizers empirically,
  which is what interviews test.
- **Matrix calculus in full generality.** Week 14 introduces what you need, with
  the Matrix Cookbook as reference. Deriving matrix derivatives from first
  principles is a rabbit hole.

If you finish a week early, the correct move is not more theory. It is the
stretch goal, or an extra hour of interview drills.
