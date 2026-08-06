# Week 01: Vectors, Matrices, Geometry

## Outcome

By Sunday you can implement vector and matrix operations from scratch, explain
geometrically why embeddings live in vector spaces, and articulate what cosine
similarity measures that Euclidean distance does not.

Concretely: `bootstrap/math-labs/tests/test_linear_algebra.py` passes — all 63
tests, including the batched-similarity block that is a preview of Month 10's
retrieval engine.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Every LLM interview question about embeddings, similarity, retrieval, or
attention bottoms out here. When an interviewer asks "why does attention divide
by √d?", the answer requires knowing that the dot product of two d-dimensional
random vectors has variance proportional to d. You cannot reason about that if
"dot product" is a function name rather than a geometric operation.

This is also the week that determines whether Month 8 is understanding or
memorization. Candidates who skip Month 1 can draw a transformer diagram and
cannot explain why any of it is shaped that way.

Direct relevance to your positioning: `batch_cosine_similarity` and
`top_k_similar` are, literally, vector search. In Week 37 you will build the same
thing on pgvector with an ANN index. Having felt the cost of a brute-force scan
makes that index choice a reasoned decision rather than a default.

## Time Budget: 15-20 Hours

- Theory: 4 hours
- Coding: 7 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Vectors as objects with direction and magnitude**
   1. Coordinates versus the geometric object they represent
   2. Vector addition and scalar multiplication, geometrically
   3. Why a 768-dimensional embedding is the same kind of object as a 2-D arrow
2. **The dot product**
   1. Algebraic definition: sum of elementwise products
   2. Geometric definition: |a||b|cos θ
   3. Why these are the same thing — derive it
   4. Orthogonality as zero dot product
   5. The dot product as a similarity measure
3. **Norms**
   1. L1, L2, L∞ and their unit balls
   2. Why the shape of the unit ball predicts L1 sparsity (preview of Week 5)
   3. Normalization and unit vectors
4. **Cosine similarity**
   1. Scale invariance, and when discarding magnitude is right or wrong
   2. Relationship to the dot product for normalized vectors
   3. Why embedding models normalize their outputs
5. **Matrices as linear transformations**
   1. Matrix-vector product as a linear combination of columns
   2. Matrix-vector product as a stack of dot products
   3. Composition as matrix multiplication; why it is not commutative
   4. The identity, the transpose, the trace
6. **Span, basis, and rank**
   1. Linear independence
   2. Column space and what rank measures
   3. Orthogonal and orthonormal bases
7. **Gram-Schmidt orthogonalization**
   1. Projection onto a vector, and the orthogonal residual
   2. The classical algorithm
   3. Why it is numerically unstable, and what modified Gram-Schmidt fixes

## Required Free Resources

Do not attempt all of these. The first two are the week; the rest are reference.

**Primary (watch/read in full, ~4 hours):**
- 3Blue1Brown, Essence of Linear Algebra, chapters 1-9 — https://www.3blue1brown.com/topics/linear-algebra
  The single highest-value resource for this week. Chapters 1-4 and 9 are
  essential; 5-8 are worth it.
- Mathematics for Machine Learning, chapter 2 (sections 2.1-2.4, 3.1-3.3) — https://mml-book.github.io/

**Reference (consult only when stuck):**
- MIT OCW 18.06, lectures 1-4 — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/
- NumPy linear algebra docs — https://numpy.org/doc/stable/reference/routines.linalg.html

**Read after implementing, not before:**
- The Illustrated Word2vec — https://jalammar.github.io/illustrated-word2vec/
  Ties the geometry to embeddings concretely. It will land properly once you
  have written `cosine_similarity` yourself.

## Hands-On Exercises

Work in `bootstrap/math-labs/`. Set `make week W=1` first, then read
`tests/test_linear_algebra.py` before writing any code — the tests are the spec.

1. **Vector operations** (2h) — `dot_product`, `norm`, `normalize`,
   `cosine_similarity`, `euclidean_distance`, `angle_between`. Watch the
   `arccos` clamping trap: floating point produces cosines of 1.0000000000000002
   and `arccos` returns NaN.
2. **Projection** (1h) — `project` and `orthogonal_component`. Verify the
   decomposition sums back to the original. This is least squares in disguise
   and you will meet it again in Week 5.
3. **Matrix operations** (2h) — `matmul` (write the triple loop first, then
   vectorize and time both), `transpose`, `identity`, `trace`, `is_symmetric`,
   `is_orthogonal`, `matrix_vector_product`.
4. **Gram-Schmidt** (1.5h) — classical and modified. Then construct a
   nearly-dependent input where the classical version fails `is_orthogonal` and
   the modified version does not. This is the week's most instructive exercise.
5. **Rank** (0.5h) — via Gram-Schmidt on the columns.
6. **Batched similarity** (1.5h) — `batch_cosine_similarity` and `top_k_similar`.
   Use `argpartition`, not a full sort. Time the batched version against a Python
   loop at n=100,000 and write both numbers in your check-in.

## Bootstrap Files To Create

Implement (all currently `raise NotImplementedError`):

```text
bootstrap/math-labs/src/linear_algebra.py
```

Create:

```text
bootstrap/math-labs/notebooks/vector_geometry.ipynb
```

The notebook should contain: a 2-D visualization of projection and its
orthogonal residual, a plot of the L1/L2/L∞ unit balls, a demonstration that
cosine similarity is scale-invariant while Euclidean distance is not, and the
timing comparison from exercise 6.

## Tests To Write

`tests/test_linear_algebra.py` already exists and is the specification. Beyond
making it pass, add three of your own:

1. A property test using Hypothesis: `cosine_similarity(a, b)` is always in
   [-1, 1] for any non-zero float vectors.
2. A test that `matmul` raises on mismatched inner dimensions with a message
   naming both shapes.
3. A regression test for the `arccos` clamping bug: `angle_between(v, v.copy())`
   must return 0.0, not NaN, for a 1000-dimensional random vector.

```bash
cd bootstrap/environment
make week W=1
make test          # 63 failures — the starting line
# ... implement ...
make check         # lint + typecheck + test, all green
```

## Portfolio Artifact

Commit to the public course repository:

- `src/linear_algebra.py` — clean, typed, documented
- `tests/test_linear_algebra.py` — passing, plus your three additions
- `notebooks/vector_geometry.ipynb` — executed, with outputs

Not a portfolio showpiece on its own. It is the foundation that makes Month 8
credible, and the commit history starts here.

## Interview Drills

**Coding (45 min, timed).** Two problems, spoken aloud, from the arrays and
two-pointers set on NeetCode. State complexity unprompted. Write a test case
before declaring done.

**ML theory (20 min).** Answer out loud, no notes, then record one:

> Why do embeddings live in vector spaces? What does cosine similarity measure
> that Euclidean distance does not, and when does that distinction matter?

A strong answer covers: semantic relationships as geometric ones; cosine
measuring direction only; why magnitude in an embedding often encodes frequency
or length rather than meaning; and a case where Euclidean is the right choice
(when magnitude is meaningful — say, count vectors).

**Communication (10 min).** Explain the dot product to someone who has not done
linear algebra since school. Two minutes, no jargon, one concrete example.

## Evaluation Rubric

| Score | Standard |
| ----- | -------- |
| 3 | Some functions implemented. Tests failing. Copied from references. |
| 5 | Most tests pass. Cannot explain why Gram-Schmidt orthogonalizes. |
| 7 | All tests pass. Clean code. Can explain every function's geometry. Notebook done. |
| 9 | Above, plus the modified-Gram-Schmidt instability demonstrated, the timing comparison measured, and the interview drill answered cold in under 3 minutes. |
| 10 | Above, plus your three extra tests caught a real bug, and you can explain the connection from dot product to attention scaling unprompted. |

Score yourself in `coach/weekly_checkin_template.md` on all six axes.

## Stretch Goal

Implement `matmul` three ways — triple loop, NumPy broadcasting, and blocked/tiled
— and benchmark all three at n = 128, 512, and 1024. Plot the results.

Then explain the gap. The blocked version is faster than naive looping for the
same reason GPU kernels are structured the way they are: memory locality, not
arithmetic. This is the intuition that makes Week 49's GPU material land, and
almost nobody arrives at Month 13 with it.
