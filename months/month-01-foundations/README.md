# Month 01: ML Mathematics Bootcamp

**Weeks 1-4 · Phase 1: Foundations · Lab: `bootstrap/math-labs/`**

---

## The Month In One Sentence

Build the mathematical machinery that everything else in this course is a special
case of — and build it by implementing it, not by reading about it.

## Why This Month Exists

This is the month most likely to get skipped, because it produces the least
impressive artifact and the payoff is deferred by seven months.

Skip it and Month 8 becomes memorization. You will be able to draw a transformer
and unable to say why attention divides by √d, because you never internalized
that the dot product of two d-dimensional random vectors has variance
proportional to d. You will be able to call `loss.backward()` and unable to debug
it when the gradient is wrong.

The engineers who pass frontier lab ML screens are the ones who can derive things
on a whiteboard. Derivation is a skill built by doing derivations, and this is
the month where you do them.

**You have an advantage here that most career-changers do not:** you already
think quantitatively and you already debug systematically. The material is not
conceptually beyond you. The risk is not difficulty; it is impatience.

## What You Build

| Week | Topic | Deliverable |
| ---- | ----- | ----------- |
| 1 | Vectors, matrices, geometry | `linear_algebra.py` — including batched similarity, which is vector search |
| 2 | Eigendecomposition, SVD, PCA | `pca.py` + image compression notebook |
| 3 | Calculus and autodiff | `autodiff_scalar.py` — a working autodiff engine |
| 4 | Probability and information theory | `probability.py`, `information_theory.py` |

**Capstone:** the ML Math Toolkit — all five modules as an installable, tested,
documented package.

## The Through-Lines

Four ideas thread through the month and reappear for the next seventeen.

**Similarity is a dot product.** Week 1's `cosine_similarity` is Week 26's
embedding comparison, Week 29's attention score, and Week 37's vector search. The
same operation, at four levels of abstraction.

**Low-rank structure is everywhere.** Week 2's truncated SVD is why LoRA works
(Week 46) and why embeddings compress (Week 37). Eckart-Young says the truncation
is optimal, not merely convenient.

**Reverse-mode autodiff is the whole of deep learning.** Week 3's `Value` class
is PyTorch's autograd with floats instead of tensors. Week 14 changes the data
type and nothing else conceptually.

**Training is maximum likelihood estimation.** Week 4's derivation — cross
entropy is the NLL of a categorical, MSE is the NLL of a Gaussian — turns loss
functions from a menu into consequences of a modeling assumption.

## Time and Compute

15-20 hours per week. CPU only; nothing this month needs a GPU. Your laptop is
sufficient and will remain so through Week 16.

```bash
cd bootstrap/environment
make setup
make week W=1
make test        # 63 failures. That is the starting line.
```

## Files

```text
month-01-foundations/
  README.md      you are here
  week-01.md     vectors, matrices, geometry
  week-02.md     matrix factorization and SVD
  week-03.md     calculus and gradients        <- the important one
  week-04.md     probability and information theory
  capstone.md    the ML Math Toolkit
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 3.** If the month has to shrink, take hours from Weeks 1 and 2, never from
Week 3. Building an autodiff engine is the single highest-leverage thing you do
in Phase 1, and it is what makes Months 4, 5, and 8 tractable.

The test to treat as the month's real gate is
`test_gradient_descent_fits_a_line` — your engine, your losses, your gradient
descent, fitting an actual model with no framework involved.

## Common Failure Modes

| Failure | Symptom | Fix |
| ------- | ------- | --- |
| Watching without implementing | No commits by Wednesday | Theory capped at 30% of hours. Implement within 72 hours of reading. |
| Transcribing micrograd | Week 3 code identical to Karpathy's | Watch, close the tab, rebuild from memory. |
| Skipping the derivations | Tests pass, whiteboard fails | Derive on paper before coding. Photograph the pages. |
| Using NumPy for the thing you're implementing | Tests pass trivially | `dot_product` may not call `np.dot`. The tests compare against it. |
| Not fixing the PCA sign convention | Tests flake randomly | Pin it deterministically in Week 2. |
| Deferring interview drills | "I'll start those in Month 6" | Two hours a week, from Week 1. Non-negotiable. |

## Advancement

Before Week 5, you should be able to, without notes:

- [ ] Explain why embeddings live in vector spaces, and what cosine similarity
      discards
- [ ] Explain PCA, including what information it destroys
- [ ] Derive gradient descent for linear regression on a whiteboard
- [ ] Derive the softmax + cross-entropy gradient and show the `p - y` cancellation
- [ ] Answer "why is cross entropy the loss for classification?" three ways
- [ ] Point at a public repository containing all of it

If two or more of those are shaky, take a catch-up week. This is the cheapest
point in the course to fix a gap, and the most expensive one to carry forward.

## Next

Month 2 — Classical Machine Learning From Scratch. You will use Week 3's
gradients to fit real models and Week 4's information theory to split decision
trees.
