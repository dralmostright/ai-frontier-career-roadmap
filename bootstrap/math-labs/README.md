# math-labs

**Weeks 1-4 · Month 1 · Capstone: ML Math Toolkit**

The mathematical foundation for everything that follows. Five modules, all
implemented from scratch, all tested against NumPy and SciPy references.

---

## Why This Lab Exists

You can build a RAG chatbot without knowing what an eigenvector is. You cannot
pass a frontier lab's ML depth screen without it, and you cannot debug a model
that is silently training wrong.

Month 1 is the phase most likely to get skipped, because it produces the least
impressive artifact and the payoff is deferred. Skip it and Month 8 becomes
memorization: you will be able to draw a transformer and unable to explain why
attention divides by √d, because you never built the intuition that dot products
of high-dimensional random vectors have variance proportional to d.

Every function here reappears:

| This module | Reappears as |
| ----------- | ------------ |
| `dot_product`, `cosine_similarity` | Vector search (M7, M10), attention scores (M8) |
| `batch_cosine_similarity`, `top_k_similar` | Your retrieval engine (M10) |
| `pca` | Embedding visualization (M7), dimensionality reduction, LoRA's rationale (M12) |
| `autodiff_scalar` | PyTorch's autograd, which stops being magic (M5) |
| `cross_entropy`, `softmax` | Every classifier and every language model you train |
| `kl_divergence` | RLHF/DPO regularization (M12), distribution comparison (M9) |
| `information_gain` | Decision tree splits (Week 7) |
| `bootstrap_confidence_interval` | Every honest result you report from Week 11 on |

---

## Layout

```text
math-labs/
  src/
    linear_algebra.py       Week 1  vectors, matrices, Gram-Schmidt, batched similarity
    pca.py                  Week 2  eigendecomposition, SVD, PCA, image compression
    autodiff_scalar.py      Week 3  reverse-mode autodiff, gradient checking, losses
    probability.py          Week 4  distributions, MLE, Bayes, bootstrap
    information_theory.py   Week 4  entropy, cross entropy, KL, mutual information
  tests/
    test_linear_algebra.py
    test_pca.py
    test_gradients.py
    test_probability.py
  notebooks/
    svd_image_compression.ipynb     Week 2 deliverable
    distribution_simulations.ipynb  Week 4 deliverable
```

---

## Working Method

```bash
cd ../environment
make week W=1
make test              # week 1 tests run and fail — that is the starting state
```

Then, for each function:

1. **Read the test first.** The tests are the specification and they are more
   precise than the docstring.
2. **Derive it on paper.** Especially in Week 3. If you cannot write the
   derivative by hand, implementing it teaches you nothing.
3. **Implement it.** No NumPy shortcut for the thing you are implementing.
4. **Run the test.** Iterate until green.
5. **Explain it out loud.** Thirty seconds, no notes. This is the step that gets
   skipped and it is the one the interview tests.

---

## The Rules

**Do not call the function you are implementing.** `dot_product` may not call
`np.dot`. The tests compare against NumPy, so using NumPy makes them vacuous.

Permitted throughout: `np.array`, indexing, slicing, `+ - * /`, `np.sum`,
`np.sqrt`, `np.exp`, `np.log`, `math.*`, and `np.random.Generator`.

Two deliberate exceptions:

- **Week 2** may use `np.linalg.eigh` and `np.linalg.svd`. Writing a stable
  eigensolver is a numerical-analysis project, not an ML one. Everything around
  those calls — centering, ordering, sign conventions, variance accounting — is
  yours.
- **Tests** may use anything. SciPy is the reference oracle.

---

## Milestones

| Week | You can... | Proof |
| ---- | ---------- | ----- |
| 1 | Explain embeddings geometrically and search a vector space | `test_linear_algebra.py` green |
| 2 | Compress an image with SVD and explain what PCA destroys | `test_pca.py` green + notebook |
| 3 | Derive and verify gradients for any composed expression | `test_gradients.py` green |
| 4 | Explain why cross entropy is the classification loss | `test_probability.py` green |

The Week 3 end-to-end test — fitting `y = 2x + 1` with your own autodiff engine
and nothing else — is the single most important test in the lab. When it passes,
you have built a working, if tiny, deep learning framework.

---

## Common Traps

| Trap | Symptom | Fix |
| ---- | ------- | --- |
| `=` instead of `+=` in backward | Wrong gradients in any graph with a reused node | Gradients accumulate. Always `+=`. |
| Forgetting `zero_grad()` | Loss decreases then explodes | Reset before each backward pass |
| `np.linalg.eigh` ascending order | PCA components in the wrong order | Reverse them |
| Squaring omitted in explained variance | Plausible-looking, wrong scree plot | Variance goes with σ², not σ |
| PCA without centering | PC1 points at the mean | Center. Always. |
| Unclamped `arccos` | NaN for identical vectors | Clamp cosine to [-1, 1] first |
| Softmax without max subtraction | `inf/inf` → NaN on large logits | Subtract the max. It changes nothing mathematically. |
| Unclamped `log` in BCE | NaN with a confident wrong prediction | Clamp probabilities away from 0 and 1 |
| Multiplying probabilities | Underflow to 0.0 | Sum logs |

---

## Interview Drills

One per week, spoken aloud, timed. Record at least one and watch it back.

**Week 1.** Why do embeddings live in vector spaces? What does cosine similarity
measure that Euclidean distance doesn't, and when does that distinction matter?

**Week 2.** Explain PCA to someone who knows linear algebra but not ML. Then
explain what information it loses and when that loss is unacceptable.

**Week 3.** Derive gradient descent for linear regression on a whiteboard. Then
derive the softmax + cross-entropy gradient and explain why it simplifies to
`p - y`.

**Week 4.** Why is cross entropy the loss function for classification? Answer it
three ways: as maximum likelihood, as KL divergence minimization, and as an
information-theoretic coding cost.

---

## Capstone

Turn this lab into a published, installable package. See
`months/month-01-foundations/capstone.md`.

Minimum bar: pip-installable, all tests passing, a README mapping each module to
the ML concept it underpins, and two clean notebooks. It is not an impressive
portfolio piece on its own — it is the artifact that makes the rest of your
portfolio credible.
