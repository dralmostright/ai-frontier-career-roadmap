"""Linear algebra from scratch — Week 1.

Implement every function using only Python builtins and, where a loop would be
pointlessly slow, plain NumPy array indexing. **Do not call the NumPy function
that already does the job.** `np.dot`, `np.linalg.norm`, and friends are what
the tests compare your work against; using them makes the tests tautological.

The point is not that you will ever ship `dot_product` in production. The point
is that when you later read "attention computes a scaled dot product between
queries and keys," you have a physical intuition for what that means rather than
a memorized phrase.

Interview relevance: every embedding question, every similarity question, and
the entire first half of any transformer explanation reduces to this file.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Vector = NDArray[np.float64]
Matrix = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Vector operations
# ---------------------------------------------------------------------------

def check_1D(a: Vector) -> bool:
    if a.ndim == 1:
        return True
    else:
        return False

def dot_product(a: Vector, b: Vector) -> float:
    """Return the dot product of two vectors.

    The dot product answers "how much does a point in the direction of b?",
    scaled by both magnitudes. It is the single most important operation in
    machine learning: a linear layer is a batch of dot products, and so is
    attention.

    Args:
        a: 1-D array of shape (n,).
        b: 1-D array of shape (n,).

    Returns:
        The scalar sum of elementwise products.

    Raises:
        ValueError: if the shapes differ or the inputs are not 1-D.
    """
    if check_1D(a) or check_1D(b):
        raise ValueError("Not 1D vector")
    if a.size != b.size:
        raise ValueError ("Vectors length not same")
    dot_product=0
    for i in range(a.size):
        dot_product += a[i]*b[i]
    return dot_product    


def norm(v: Vector, p: float = 2.0) -> float:
    """Return the p-norm of a vector.

    p=1 is Manhattan (sum of absolute values), p=2 is Euclidean, p=inf is the
    maximum absolute component. L1 and L2 show up again in Week 5 as the two
    regularization penalties — L1 produces sparsity because its gradient is
    constant, L2 shrinks smoothly because its gradient is proportional to the
    weight. Understand the geometry here and that result stops being a fact you
    memorize.

    Args:
        v: 1-D array.
        p: Order of the norm. Must be >= 1, or float("inf").

    Returns:
        The p-norm as a float.
    """
    raise NotImplementedError("Week 1")


def normalize(v: Vector) -> Vector:
    """Return v scaled to unit L2 length.

    Raises:
        ValueError: if v is the zero vector (no direction to preserve).
    """
    raise NotImplementedError("Week 1")


def cosine_similarity(a: Vector, b: Vector) -> float:
    """Return the cosine of the angle between two vectors.

    This is the similarity metric behind every vector database you will build
    in Month 10. It measures direction only, discarding magnitude — which is
    usually what you want for embeddings, and occasionally exactly wrong.

    Note the relationship to dot product: for unit-length vectors they are
    identical. That is why embedding models normalize their outputs, and why
    pgvector's `<=>` operator is cheap.

    Returns:
        A value in [-1, 1]. 1 means same direction, 0 orthogonal, -1 opposite.

    Raises:
        ValueError: if either vector is the zero vector.
    """
    raise NotImplementedError("Week 1")


def euclidean_distance(a: Vector, b: Vector) -> float:
    """Return the L2 distance between two points."""
    raise NotImplementedError("Week 1")


def project(v: Vector, onto: Vector) -> Vector:
    """Return the vector projection of v onto another vector.

    The component of v that lies along `onto`. This is the operation underneath
    least squares (Week 5): fitting a line is projecting the target vector onto
    the column space of the design matrix.

    Raises:
        ValueError: if `onto` is the zero vector.
    """
    raise NotImplementedError("Week 1")


def orthogonal_component(v: Vector, onto: Vector) -> Vector:
    """Return the part of v orthogonal to `onto`, i.e. v minus its projection.

    This is the residual. In Week 5 you will discover that least squares
    minimizes exactly this quantity.
    """
    raise NotImplementedError("Week 1")


def angle_between(a: Vector, b: Vector, degrees: bool = False) -> float:
    """Return the angle between two vectors.

    Clamp the cosine into [-1, 1] before calling arccos — floating point will
    hand you 1.0000000000000002 and arccos will hand you back a NaN. This is a
    real bug that ships in real similarity-search code.
    """
    raise NotImplementedError("Week 1")


# ---------------------------------------------------------------------------
# Matrix operations
# ---------------------------------------------------------------------------


def matmul(A: Matrix, B: Matrix) -> Matrix:
    """Multiply two matrices.

    Write the triple loop first. Get it right. Then, if you want, write the
    vectorized version and time both — the gap (typically 100-1000x) is a
    lesson about why GPUs matter that is much more convincing when you measure
    it yourself.

    Args:
        A: shape (m, k).
        B: shape (k, n).

    Returns:
        Shape (m, n).

    Raises:
        ValueError: if the inner dimensions do not match.
    """
    raise NotImplementedError("Week 1")


def transpose(A: Matrix) -> Matrix:
    """Return the transpose of A without calling `.T`."""
    raise NotImplementedError("Week 1")


def identity(n: int) -> Matrix:
    """Return the n x n identity matrix."""
    raise NotImplementedError("Week 1")


def trace(A: Matrix) -> float:
    """Return the sum of the diagonal of a square matrix.

    Raises:
        ValueError: if A is not square.
    """
    raise NotImplementedError("Week 1")


def is_orthogonal(A: Matrix, tol: float = 1e-8) -> bool:
    """Return True if A^T A is the identity within tolerance.

    Orthogonal matrices rotate and reflect but never stretch. They preserve
    norms and angles, which is why they are numerically well-behaved and why
    QR and SVD are built out of them.
    """
    raise NotImplementedError("Week 1")


def is_symmetric(A: Matrix, tol: float = 1e-8) -> bool:
    """Return True if A equals its transpose within tolerance.

    Symmetric matrices have real eigenvalues and orthogonal eigenvectors, which
    is why covariance matrices (always symmetric) admit PCA cleanly.
    """
    raise NotImplementedError("Week 1")


def matrix_vector_product(A: Matrix, v: Vector) -> Vector:
    """Multiply a matrix by a vector.

    Two readings of this operation, and you should be fluent in both:

    1. Each output element is a dot product of a row of A with v.
    2. The output is a linear combination of A's *columns*, weighted by v.

    Reading 2 is the one that makes "the column space" and "rank" click, and it
    is the one most people never internalize.
    """
    raise NotImplementedError("Week 1")


# ---------------------------------------------------------------------------
# Orthogonalization
# ---------------------------------------------------------------------------


def gram_schmidt(vectors: list[Vector]) -> list[Vector]:
    """Return an orthonormal basis for the span of the input vectors.

    Classical Gram-Schmidt: for each vector, subtract its projection onto every
    previously accepted basis vector, then normalize. Drop vectors whose
    residual is numerically zero — those are linearly dependent on the ones
    before them.

    Classical Gram-Schmidt is numerically unstable for near-dependent inputs.
    Implement it anyway, then implement `modified_gram_schmidt` and construct a
    case where they disagree. That exercise is worth more than the function.

    Args:
        vectors: List of 1-D arrays of equal length.

    Returns:
        A list of orthonormal vectors spanning the same subspace. May be
        shorter than the input if the input was linearly dependent.
    """
    raise NotImplementedError("Week 1")


def modified_gram_schmidt(vectors: list[Vector]) -> list[Vector]:
    """Numerically stable Gram-Schmidt.

    Same output in exact arithmetic; substantially better in floating point.
    The difference: subtract each projection immediately as you go, rather than
    computing all projections against the original vector.

    Stretch goal: build a nearly-dependent input where the classical version
    produces a basis that fails `is_orthogonal` and this one does not.
    """
    raise NotImplementedError("Week 1")


def rank(A: Matrix, tol: float = 1e-10) -> int:
    """Return the rank of A: the dimension of its column space.

    Implement via Gram-Schmidt on the columns and count what survives. In Week 2
    you will compute it again from the singular values and find that far more
    robust — that comparison is the lesson.
    """
    raise NotImplementedError("Week 1")


# ---------------------------------------------------------------------------
# Batched operations — the bridge to Month 8
# ---------------------------------------------------------------------------


def batch_cosine_similarity(query: Vector, matrix: Matrix) -> Vector:
    """Cosine similarity between one query vector and every row of a matrix.

    This is vector search. Every retrieval system you build in Months 7-11 is
    this function plus an index that avoids computing all of it.

    Implement it as a single matrix-vector product against pre-normalized rows,
    not as a Python loop over rows. Then time both at n=100_000 and write the
    numbers in your week check-in.

    Args:
        query: shape (d,).
        matrix: shape (n, d).

    Returns:
        Shape (n,), similarity to each row.
    """
    raise NotImplementedError("Week 1")


def top_k_similar(query: Vector, matrix: Matrix, k: int = 5) -> tuple[NDArray, Vector]:
    """Return the indices and scores of the k most similar rows.

    Use `np.argpartition` rather than a full sort: you need the top k, not a
    total ordering, and the difference is O(n) versus O(n log n). At n = 10
    million this is the difference between a snappy search and a timeout.

    Returns:
        (indices, scores), both length k, sorted by descending score.
    """
    raise NotImplementedError("Week 1")
