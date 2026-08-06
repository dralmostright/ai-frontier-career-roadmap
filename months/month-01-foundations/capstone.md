# Month 01 Capstone: ML Math Toolkit

## Objective

Package the four weeks of implementation into a single installable, tested,
documented Python library, published publicly, with a README that maps every
module to the machine learning concept it underpins.

The deliverable is not the code — you already wrote that. The deliverable is
turning working code into an artifact a stranger can install, run, and understand
in ten minutes.

## Business Problem

There is no business problem. This is a conditioning capstone, and pretending
otherwise would be dishonest.

What it *is* for: every later project in this portfolio claims mathematical
depth. This repository is the evidence for that claim. When a reviewer reads
"implemented multi-head attention from scratch" in Month 8, the presence of a
from-scratch autodiff engine from Month 1 makes it credible rather than
aspirational.

It also establishes the engineering standard you will hold for seventeen more
months. Get the packaging, testing, and documentation habits right here, while
the code is simple, and they become automatic by the time the projects are hard.

## Technical Requirements

An installable package, `ml-math-toolkit`, containing:

| Module | Contents | Week |
| ------ | -------- | ---- |
| `linalg` | Vector ops, matrix ops, Gram-Schmidt, batched similarity | 1 |
| `decomposition` | Eigendecomposition, power iteration, SVD, PCA | 2 |
| `autodiff` | Reverse-mode scalar autodiff, gradient checking, losses | 3 |
| `probability` | Distributions, MLE, Bayes, bootstrap | 4 |
| `information` | Entropy, cross entropy, KL, JS, MI, information gain | 4 |

Requirements:

- Every function implemented from scratch. No calling the library function you
  are reimplementing. (Permitted exceptions: `np.linalg.eigh` and
  `np.linalg.svd`, documented in the README with the reason.)
- Type hints throughout.
- Docstrings that state what the function does and why it matters for ML.
- `pip install -e .` works from a clean clone.
- Zero lint errors under `ruff`.

## Theory Requirements

The README must contain a section, written in your own words, covering:

1. Why the dot product is the fundamental operation in machine learning, tracing
   it from vector similarity through attention.
2. What PCA does geometrically, and precisely what it discards.
3. Why reverse-mode autodiff is the right algorithm for ML, with the complexity
   argument against forward mode.
4. Why cross entropy is the loss for classification, answered from maximum
   likelihood *and* from information theory.

Two to three paragraphs each. Written without looking at a reference — if you
cannot write it unaided, you have not finished learning it.

## System Design Requirements

Light for this capstone, but establish the pattern:

- `src/` layout, not a flat package
- Separation between the numerical core and the plotting/notebook helpers
- A single public API surface per module, with private helpers marked
- No circular imports; `information` may depend on `probability`, not vice versa

## Implementation Plan

**Days 1-2 — Packaging.** Restructure `bootstrap/math-labs/src/` into a proper
package with `pyproject.toml`. Verify `pip install -e .` and that all tests pass
against the installed package rather than a `sys.path` hack.

**Day 3 — Test hardening.** Get to 90%+ coverage on the numerical core. Add the
property-based tests suggested in each week file. Verify every test would fail
if you broke the implementation — mutate one function deliberately and confirm
a test catches it.

**Day 4 — Notebooks.** Clean up the four notebooks. Every cell executes top to
bottom in a fresh kernel. Every figure has axis labels and a caption. Remove all
scratch cells.

**Day 5 — README.** The theory sections, the module map, the install
instructions, the examples.

**Day 6 — Review and publish.** Score with the rubric. Fix whatever scores below
7. Push to a public repository.

## Evaluation Plan

There is no model to evaluate, so evaluate correctness instead:

| Check | Target |
| ----- | ------ |
| Test suite | 100% passing |
| Coverage on numerical core | ≥ 90% |
| Agreement with NumPy/SciPy reference | Within 1e-10 for closed-form, 1e-6 for iterative |
| Gradient check on every autodiff operation | Relative error < 1e-6 |
| `pip install -e . && pytest` from a clean clone | Works, first try |
| Lint | Zero `ruff` errors |

Include a `benchmarks.md` with the timing comparisons from Weeks 1 and 2: naive
versus vectorized matmul, looped versus batched cosine similarity. Numbers, on
your hardware, with the hardware stated.

## Expected Repository Structure

```text
ml-math-toolkit/
  README.md
  pyproject.toml
  LICENSE
  Makefile
  src/
    ml_math_toolkit/
      __init__.py
      linalg.py
      decomposition.py
      autodiff.py
      probability.py
      information.py
  tests/
    test_linalg.py
    test_decomposition.py
    test_autodiff.py
    test_probability.py
    test_information.py
  notebooks/
    01_vector_geometry.ipynb
    02_svd_image_compression.ipynb
    03_autodiff_walkthrough.ipynb
    04_distribution_simulations.ipynb
  docs/
    design.md
    benchmarks.md
    limitations.md
```

## README Requirements

Above the fold — visible without scrolling:

- One-sentence description
- The compression grid figure from Week 2 (it is the most visually striking
  thing you have)
- Install and test commands

Then:

- **What this is** — a from-scratch implementation of the mathematics underneath
  machine learning, built to understand rather than to use in production
- **Why it exists** — honest framing, including that NumPy does all of this
  faster
- **Module map** — the table above, with a one-line "where this shows up in ML"
  per module
- **The four theory sections**
- **Examples** — five to ten lines each, runnable
- **Verification** — how it is tested against references
- **Limitations** — see below
- **Interview talking points** — three things you would want to be asked about

## Demo Requirements

A `demo.py` or `demo.ipynb` that, in under 60 seconds, shows:

1. Cosine similarity finding the nearest neighbor among 10,000 random vectors
2. SVD compressing an image, side by side, with the compression ratio
3. The autodiff engine fitting y = 2x + 1 and printing the recovered parameters
4. A bootstrap confidence interval on a sample mean

Four cells, four visible results. Someone should be able to run it and
immediately see that all four modules work.

## Blog Post Requirement

Optional this month. If you write one, the angle with the most value is:

> "What a DBA Learns Building Autodiff From Scratch"

The interesting content is not the math — plenty of people have written that. It
is the perspective: computational graphs as dependency graphs, gradient
accumulation as a concurrency problem, and numerical stability as the same class
of concern as integer overflow in a production system. That framing is yours and
nobody else is writing it.

Defer it if the week is tight. Post #1 is formally scheduled for Month 5.

## Interview Story

> "Before I touched PyTorch I built the math underneath it — linear algebra,
> a reverse-mode autodiff engine, the probability and information theory that
> loss functions come from. It means when a gradient is wrong I start from the
> computational graph instead of from Stack Overflow. It also means I can derive
> attention rather than recite it."

Deliverable: 45 seconds, no notes.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 1 targets:

| Dimension | Target | Note |
| --------- | ------ | ---- |
| Problem framing | 6 | Deliberately low. This is conditioning, not a product. Do not oversell it. |
| Technical execution | 8 | The code should be genuinely correct and clean. |
| Evaluation rigor | 7 | Correctness against references, plus the benchmarks. |
| Code quality | 8 | Establish the standard here while the code is simple. |
| Documentation | 8 | The theory sections are the differentiator. |
| Reproducibility | 9 | There is no excuse for anything less on a pure-Python package. |
| Error analysis | 5 | Limited scope here. Numerical accuracy analysis is the closest analogue. |
| Portfolio readiness | 6 | Supporting evidence, not a showpiece. |

**Overall target: 7.0+.** Do not chase 9 on this one — the marginal hour is
better spent on Month 2. Reproducibility and Code Quality are where to insist on
high marks, because those habits compound.

## Stretch Goals

Ranked by value.

1. **Publish to PyPI.** `pip install ml-math-toolkit` working from anywhere is a
   small thing that signals you finish work. An hour, mostly packaging metadata.
2. **Property-based testing with Hypothesis** across the numerical core.
   Invariants like "cosine similarity is always in [-1, 1]" and "PCA
   reconstruction error never increases with more components" catch edge cases
   that example-based tests miss.
3. **Array-valued autodiff.** Extend `Value` to NumPy arrays with
   broadcasting-aware backward passes. This is the hard part of Week 14, so doing
   it now converts Month 4 into a review.
4. **A `docs/` site** via MkDocs, with the theory sections rendered and the
   notebooks embedded. Cheap, and it makes the repository look considered.

## Limitations To State Honestly

Your `docs/limitations.md` should say, plainly:

- This is 10-1000x slower than NumPy, because NumPy calls BLAS and this calls
  Python.
- The autodiff engine is scalar-valued and does not scale beyond toy models.
- The eigensolver is NumPy's; implementing a numerically stable one is a
  different discipline.
- Numerical stability has been addressed at the known trouble spots (log-sum-exp,
  clamping) but has not been systematically analyzed.
- It is a learning artifact. Use NumPy and PyTorch for real work.

Stating this clearly is not weakness. It is the first instance of a habit that
runs through the whole portfolio, and reviewers notice its absence far more than
its presence.
