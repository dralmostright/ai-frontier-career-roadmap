# Week 02: Matrix Factorization and SVD

## Outcome

By Sunday you can use SVD for dimensionality reduction and image compression,
implement PCA two different ways and explain why they agree, and answer
precisely what information PCA destroys.

Concretely: `bootstrap/math-labs/tests/test_pca.py` passes, and
`notebooks/svd_image_compression.ipynb` produces a compression curve you can
explain.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Explain PCA" is one of the most common opening ML questions, and most candidates
give the memorized answer ("it reduces dimensions while preserving variance")
and collapse on the follow-up. The follow-ups are: what exactly does it lose, why
does centering matter, and what is the relationship between the eigendecomposition
and SVD routes.

Beyond the direct question, low-rank structure recurs throughout the course.
LoRA (Week 46) is a low-rank update, and the reason it works at all is the same
reason truncated SVD works: the useful information in a large matrix often lives
in a small number of directions. Eckart-Young — that truncated SVD is *optimal*,
not merely reasonable — is what makes that a principled claim rather than a hope.

For your positioning: embedding visualization in Month 7 uses PCA, and the
"how many dimensions do I actually need?" question in Month 10 is answered with
`rank_for_variance`. Being able to say "we retained 95% of variance in 40 of 768
dimensions and cut index size by 94%" is a much better line than "we used PCA."

## Time Budget: 15-20 Hours

- Theory: 4.5 hours
- Coding: 6 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Eigenvalues and eigenvectors**
   1. The defining equation Av = λv, read geometrically: directions the
      transformation only stretches
   2. Why symmetric matrices have real eigenvalues and orthogonal eigenvectors
   3. Eigendecomposition A = QΛQ^T for symmetric A
   4. Power iteration, and why repeated multiplication converges to the dominant
      eigenvector
2. **Singular value decomposition**
   1. A = UΣV^T for *any* matrix — no squareness, no symmetry required
   2. The geometric reading: every linear map is rotate, scale, rotate
   3. Singular values as the scaling factors
   4. The relationship to eigendecomposition: σ² are the eigenvalues of A^T A
3. **Low-rank approximation**
   1. Truncating to the top k triplets
   2. The Eckart-Young theorem: this is optimal in Frobenius norm
   3. When compression helps, and the k(m + n + 1) versus mn arithmetic
4. **Principal component analysis**
   1. The covariance matrix and why it is always symmetric
   2. PCA as eigendecomposition of the covariance
   3. PCA as SVD of the centered data — and why SVD is numerically preferable
   4. Explained variance, and why it uses σ² not σ
   5. Choosing k: the elbow, and the better answer of a variance threshold
5. **What PCA destroys**
   1. Interpretability: components are linear combinations of features
   2. The variance you chose to drop — precisely, and be able to quantify it
   3. Why maximum variance is not the same as maximum useful signal
   4. Why it fails on nonlinear structure

## Required Free Resources

**Primary:**
- 3Blue1Brown, Essence of Linear Algebra, chapters 13-14 (change of basis,
  eigenvectors) — https://www.3blue1brown.com/topics/linear-algebra
- Mathematics for Machine Learning, chapter 4 (4.1-4.5) and chapter 10 (PCA) —
  https://mml-book.github.io/

**Reference:**
- MIT OCW 18.06, lectures 21-22 (eigenvalues), 29-30 (SVD) —
  https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/
- scikit-learn PCA user guide — https://scikit-learn.org/stable/modules/decomposition.html#pca
  Read it *after* implementing yours, then compare their sign convention to yours.

**Optional, worth it if you have time:**
- "A Singularly Valuable Decomposition" (Kalman, 1996) — a readable classic on
  why SVD deserves more attention than it gets in most curricula.

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=2
```

1. **Eigendecomposition** (1h) — `eigen_decomposition`. The trap: NumPy's `eigh`
   returns *ascending* eigenvalues and every ML convention assumes descending.
   Reverse them. Verify Av = λv for every pair.
2. **Power iteration** (1h) — `power_iteration`. Watch it converge from a random
   start. Then construct a matrix where the top two eigenvalues are nearly equal
   and observe convergence slow to a crawl. That ratio *is* the convergence rate.
3. **SVD** (1h) — `svd`, `truncated_svd`, `low_rank_approximation`,
   `reconstruction_error`. Verify that σ² equals the eigenvalues of A^T A. This
   is the identity that makes the two PCA routes equivalent; do not move on until
   you see why.
4. **Variance accounting** (0.5h) — `explained_variance_ratio`,
   `rank_for_variance`. The common bug is forgetting to square.
5. **PCA** (2h) — the full class, both methods. Two details that will bite:
   centering is mandatory (skip it and PC1 points at the mean), and you must fix
   a sign convention or your results change between runs and your tests flake.
6. **Image compression** (1.5h) — `compress_image` and the notebook. Compress a
   grayscale photo at k = 1, 5, 20, 50, 100. Show the images, the compression
   ratio, and the variance retained. Then do the same on pure noise and observe
   that it does not compress. That contrast is the lesson: SVD exploits
   structure, and noise has none.

## Bootstrap Files To Create

Implement:

```text
bootstrap/math-labs/src/pca.py
```

Create:

```text
bootstrap/math-labs/notebooks/svd_image_compression.ipynb
```

## Tests To Write

`tests/test_pca.py` is the specification. The test to pay attention to is
`test_pca_two_ways_agree` — when it passes and you can explain *why*, you
understand PCA at interview depth.

Add two of your own:

1. A test that PCA on data with one dominant direction recovers that direction
   to within 0.01 radians, using a planted signal you construct.
2. A test that reconstruction error from `low_rank_approximation(A, k)` is less
   than or equal to the error from any random rank-k factorization — an empirical
   check of Eckart-Young over 20 random trials.

## Portfolio Artifact

- `src/pca.py`, tested and clean
- `notebooks/svd_image_compression.ipynb` with the compression grid, the
  variance curve, and the noise comparison

The image compression notebook is the first genuinely presentable thing you
produce in this course. Make the figures good: a grid of reconstructions at
increasing k, with the compression ratio and variance retained in each caption.

## Interview Drills

**Coding (45 min).** Two problems, hash maps and counting. Timed.

**ML theory (25 min).** Two questions, out loud, recorded:

> 1. Explain PCA to someone who knows linear algebra but not ML.
> 2. What information does PCA destroy? When is that unacceptable?

A 9/10 answer to the second names three things: interpretability, the discarded
variance (quantified), and the fact that maximum variance is not the same as
maximum *discriminative* signal — you can construct a dataset where the
class-separating direction has the smallest variance and PCA throws it away
first. Be able to describe that construction.

**System design warm-up (15 min).** You have 10 million 768-dimensional
embeddings. Storage and search are too expensive. Walk through your options,
including PCA, product quantization, and simply using a smaller embedding model.
State the tradeoff each one makes. You will build this for real in Week 37.

## Evaluation Rubric

| Score | Standard |
| ----- | -------- |
| 3 | SVD called via NumPy; PCA not working. |
| 5 | Tests pass. Cannot explain the eigen/SVD equivalence. |
| 7 | All tests pass, both PCA methods agree, notebook complete, can explain the geometry. |
| 9 | Above, plus can derive why σ² are the eigenvalues of A^T A, and can quantify exactly what a given PCA truncation lost. |
| 10 | Above, plus can construct the counterexample where PCA discards the discriminative direction, and connects low-rank structure forward to LoRA unprompted. |

## Stretch Goal

Implement randomized SVD (Halko, Martinsson, Tropp) and compare it against the
exact version on a 5000×5000 matrix: accuracy of the top 50 singular values, and
wall-clock time.

Randomized SVD is how large-scale systems actually compute this, and the core
trick — project onto a random low-dimensional subspace, then decompose the small
result — is the same idea behind several approximate methods you will meet later.
Understanding *why* a random projection preserves the dominant structure
(Johnson-Lindenstrauss) is genuinely useful for reasoning about embedding
dimensionality in Month 10.
