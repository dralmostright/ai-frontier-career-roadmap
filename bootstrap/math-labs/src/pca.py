"""Eigendecomposition, SVD, and PCA — Week 2.

You may use `np.linalg.eigh` and `np.linalg.svd` here. Implementing a numerically
stable eigensolver is a numerical-analysis course, not an ML course. What you are
implementing is everything *around* those calls: centering, ordering, sign
conventions, variance accounting, reconstruction, and the equivalence between the
covariance-eigendecomposition and SVD routes to the same answer.

The single most valuable thing in this file is `test_pca_two_ways_agree`. When
you can explain *why* the eigenvectors of X^T X are the right singular vectors of
X, you understand PCA at the level an interviewer is probing for.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Matrix = NDArray[np.float64]
Vector = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Eigendecomposition
# ---------------------------------------------------------------------------


def eigen_decomposition(A: Matrix) -> tuple[Vector, Matrix]:
    """Eigendecomposition of a symmetric matrix, sorted by descending eigenvalue.

    NumPy's `eigh` returns eigenvalues in *ascending* order. Every downstream
    convention in ML assumes descending. Reversing it is a one-liner and
    forgetting it is a bug you will make exactly once.

    Args:
        A: Symmetric matrix of shape (n, n).

    Returns:
        (eigenvalues, eigenvectors) where eigenvalues has shape (n,) sorted
        descending, and eigenvectors has shape (n, n) with eigenvector i as
        *column* i.

    Raises:
        ValueError: if A is not square or not symmetric.
    """
    raise NotImplementedError("Week 2")


def power_iteration(A: Matrix, num_iters: int = 1000, tol: float = 1e-10) -> tuple[float, Vector]:
    """Find the dominant eigenvalue/eigenvector by repeated multiplication.

    Start from a random unit vector, multiply by A, normalize, repeat. It
    converges to the eigenvector with the largest absolute eigenvalue, at a rate
    governed by the ratio of the top two eigenvalues.

    Worth implementing for two reasons: it makes eigenvectors feel like an
    attractor rather than an algebraic definition, and it is the conceptual
    ancestor of PageRank and of the power method inside randomized SVD.

    Returns:
        (eigenvalue, eigenvector) with the eigenvector normalized to unit length.
    """
    raise NotImplementedError("Week 2")


# ---------------------------------------------------------------------------
# SVD
# ---------------------------------------------------------------------------


def svd(A: Matrix, full_matrices: bool = False) -> tuple[Matrix, Vector, Matrix]:
    """Singular value decomposition: A = U @ diag(S) @ Vt.

    Wrap `np.linalg.svd` and guarantee the conventions the rest of this module
    relies on: singular values non-negative and sorted descending.

    Geometric reading, which is the one to have in an interview: *every* linear
    map is a rotation (Vt), then an axis-aligned scaling (S), then another
    rotation (U). There is nothing else a matrix can do.

    Returns:
        (U, S, Vt) with S of shape (min(m, n),).
    """
    raise NotImplementedError("Week 2")


def truncated_svd(A: Matrix, k: int) -> tuple[Matrix, Vector, Matrix]:
    """Keep only the top k singular triplets.

    Args:
        A: shape (m, n).
        k: Number of components. Must satisfy 1 <= k <= min(m, n).

    Returns:
        (U_k, S_k, Vt_k) with shapes (m, k), (k,), (k, n).
    """
    raise NotImplementedError("Week 2")


def low_rank_approximation(A: Matrix, k: int) -> Matrix:
    """Best rank-k approximation of A in the Frobenius norm.

    The Eckart-Young theorem says truncated SVD is *optimal* — no rank-k matrix
    is closer. That is a strong statement and it is why SVD underpins
    compression, denoising, and (loosely) why LoRA's low-rank update is a
    defensible parameterization rather than an arbitrary one.

    Returns:
        Shape (m, n), rank at most k.
    """
    raise NotImplementedError("Week 2")


def reconstruction_error(A: Matrix, A_approx: Matrix, relative: bool = True) -> float:
    """Frobenius norm of the difference, optionally relative to ||A||_F."""
    raise NotImplementedError("Week 2")


def explained_variance_ratio(singular_values: Vector) -> Vector:
    """Fraction of total variance captured by each component.

    Variance goes with the *square* of the singular value. Forgetting to square
    is the most common error in this file and it produces a plot that looks
    plausible and is wrong.

    Returns:
        Shape (k,), summing to 1.0.
    """
    raise NotImplementedError("Week 2")


def rank_for_variance(singular_values: Vector, threshold: float = 0.95) -> int:
    """Smallest number of components retaining at least `threshold` of variance.

    This is how you pick k in practice, and "I looked at the elbow" is a weaker
    interview answer than "I retained 95% of variance in 40 of 768 dimensions."
    """
    raise NotImplementedError("Week 2")


# ---------------------------------------------------------------------------
# PCA
# ---------------------------------------------------------------------------


@dataclass
class PCA:
    """Principal component analysis, fit two ways.

    Rotate the data so the axes point along directions of maximum variance, then
    optionally discard the low-variance directions. It is lossy, and what it
    loses is exactly the variance you chose to drop — be able to say that
    precisely when asked "what information does PCA destroy?"

    Attributes:
        n_components: How many components to keep. None keeps all.
        method: "eigen" (eigendecomposition of the covariance matrix) or "svd"
            (SVD of the centered data). They give the same answer up to sign;
            SVD is numerically better because it never forms X^T X, which
            squares the condition number.
    """

    n_components: int | None = None
    method: str = "svd"

    mean_: Vector = field(init=False, repr=False)
    components_: Matrix = field(init=False, repr=False)
    explained_variance_: Vector = field(init=False, repr=False)
    explained_variance_ratio_: Vector = field(init=False, repr=False)
    singular_values_: Vector = field(init=False, repr=False)

    def fit(self, X: Matrix) -> PCA:
        """Fit on data of shape (n_samples, n_features).

        Centering is not optional. Skipping it makes the first component point
        at the mean rather than at the direction of maximum variance, and the
        result silently becomes meaningless.

        Sign convention: eigenvectors are only defined up to sign, so fix one
        deterministically (e.g. force the largest-magnitude element of each
        component to be positive). Without this your results change between
        runs and your tests become flaky for reasons that look like a real bug.
        """
        raise NotImplementedError("Week 2")

    def transform(self, X: Matrix) -> Matrix:
        """Project data into component space. Shape (n_samples, n_components)."""
        raise NotImplementedError("Week 2")

    def fit_transform(self, X: Matrix) -> Matrix:
        raise NotImplementedError("Week 2")

    def inverse_transform(self, Z: Matrix) -> Matrix:
        """Map back to the original space. Lossy unless all components kept."""
        raise NotImplementedError("Week 2")


# ---------------------------------------------------------------------------
# Application: image compression
# ---------------------------------------------------------------------------


def compress_image(image: Matrix, k: int) -> tuple[Matrix, dict[str, float]]:
    """Rank-k approximation of a grayscale image, with a compression report.

    The demo for `notebooks/svd_image_compression.ipynb`. Storing U_k, S_k, and
    Vt_k costs k*(m + n + 1) floats instead of m*n, so compression only helps
    when k is well below m*n/(m + n).

    Returns:
        (approximation, stats) where stats has keys ``compression_ratio``,
        ``relative_error``, ``variance_retained``, and ``bytes_saved``.
    """
    raise NotImplementedError("Week 2")
