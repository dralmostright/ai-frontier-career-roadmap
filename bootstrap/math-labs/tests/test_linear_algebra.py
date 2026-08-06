"""Tests for Week 1 linear algebra.

These tests are the specification. Read them before writing any code.

They compare your implementations against NumPy's, which is the point: NumPy is
correct, and matching it to 1e-10 is proof that you understood the operation
rather than something that merely runs.
"""

from __future__ import annotations

import numpy as np
import pytest
from linear_algebra import (
    angle_between,
    batch_cosine_similarity,
    cosine_similarity,
    dot_product,
    euclidean_distance,
    gram_schmidt,
    identity,
    is_orthogonal,
    is_symmetric,
    matmul,
    matrix_vector_product,
    modified_gram_schmidt,
    norm,
    normalize,
    orthogonal_component,
    project,
    rank,
    top_k_similar,
    trace,
    transpose,
)

pytestmark = pytest.mark.week(1)


# ---------------------------------------------------------------------------
# Vector operations
# ---------------------------------------------------------------------------


class TestDotProduct:
    def test_known_value(self):
        assert dot_product(np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0])) == pytest.approx(
            32.0
        )

    def test_orthogonal_vectors_give_zero(self):
        assert dot_product(np.array([1.0, 0.0]), np.array([0.0, 1.0])) == pytest.approx(0.0)

    def test_matches_numpy_on_random_input(self, rng, tol):
        for _ in range(20):
            n = rng.integers(1, 50)
            a, b = rng.normal(size=n), rng.normal(size=n)
            assert dot_product(a, b) == pytest.approx(np.dot(a, b), abs=tol["tight"])

    def test_commutative(self, rng):
        a, b = rng.normal(size=10), rng.normal(size=10)
        assert dot_product(a, b) == pytest.approx(dot_product(b, a))

    def test_self_dot_equals_squared_norm(self, rng):
        v = rng.normal(size=10)
        assert dot_product(v, v) == pytest.approx(norm(v) ** 2)

    def test_rejects_mismatched_shapes(self):
        with pytest.raises(ValueError):
            dot_product(np.array([1.0, 2.0]), np.array([1.0, 2.0, 3.0]))


class TestNorm:
    def test_l2_of_345_triangle(self):
        assert norm(np.array([3.0, 4.0])) == pytest.approx(5.0)

    def test_l1(self):
        assert norm(np.array([1.0, -2.0, 3.0]), p=1) == pytest.approx(6.0)

    def test_linf(self):
        assert norm(np.array([1.0, -7.0, 3.0]), p=float("inf")) == pytest.approx(7.0)

    def test_matches_numpy(self, rng, tol):
        v = rng.normal(size=20)
        for p in (1.0, 2.0, 3.0, float("inf")):
            assert norm(v, p) == pytest.approx(np.linalg.norm(v, p), abs=tol["tight"])

    def test_zero_vector(self):
        assert norm(np.zeros(5)) == pytest.approx(0.0)

    def test_triangle_inequality(self, rng):
        a, b = rng.normal(size=10), rng.normal(size=10)
        assert norm(a + b) <= norm(a) + norm(b) + 1e-10


class TestNormalize:
    def test_result_has_unit_length(self, rng):
        v = rng.normal(size=15)
        assert norm(normalize(v)) == pytest.approx(1.0)

    def test_direction_preserved(self, rng):
        v = rng.normal(size=15)
        assert cosine_similarity(v, normalize(v)) == pytest.approx(1.0)

    def test_zero_vector_raises(self):
        with pytest.raises(ValueError):
            normalize(np.zeros(3))


class TestCosineSimilarity:
    def test_identical_vectors(self, rng):
        v = rng.normal(size=10)
        assert cosine_similarity(v, v) == pytest.approx(1.0)

    def test_opposite_vectors(self, rng):
        v = rng.normal(size=10)
        assert cosine_similarity(v, -v) == pytest.approx(-1.0)

    def test_orthogonal_vectors(self):
        assert cosine_similarity(np.array([1.0, 0.0]), np.array([0.0, 3.0])) == pytest.approx(0.0)

    def test_scale_invariant(self, rng):
        """The whole point: magnitude is discarded, only direction counts."""
        a, b = rng.normal(size=8), rng.normal(size=8)
        assert cosine_similarity(a, b) == pytest.approx(cosine_similarity(100 * a, 0.01 * b))

    def test_always_within_bounds(self, rng):
        for _ in range(50):
            a, b = rng.normal(size=12), rng.normal(size=12)
            assert -1.0 - 1e-12 <= cosine_similarity(a, b) <= 1.0 + 1e-12

    def test_zero_vector_raises(self):
        with pytest.raises(ValueError):
            cosine_similarity(np.zeros(3), np.array([1.0, 2.0, 3.0]))


class TestDistanceAndAngle:
    def test_euclidean_matches_numpy(self, rng, tol):
        a, b = rng.normal(size=10), rng.normal(size=10)
        assert euclidean_distance(a, b) == pytest.approx(np.linalg.norm(a - b), abs=tol["tight"])

    def test_distance_to_self_is_zero(self, rng):
        v = rng.normal(size=10)
        assert euclidean_distance(v, v) == pytest.approx(0.0)

    def test_right_angle(self):
        a, b = np.array([1.0, 0.0]), np.array([0.0, 1.0])
        assert angle_between(a, b, degrees=True) == pytest.approx(90.0)

    def test_no_nan_from_floating_point_edge(self, rng):
        """arccos(1.0000000000000002) is NaN. Clamp before calling it."""
        v = rng.normal(size=100)
        assert not np.isnan(angle_between(v, v.copy()))


class TestProjection:
    def test_projection_onto_axis(self):
        v = np.array([3.0, 4.0])
        assert project(v, np.array([1.0, 0.0])) == pytest.approx(np.array([3.0, 0.0]))

    def test_projection_is_parallel_to_target(self, rng):
        v, onto = rng.normal(size=6), rng.normal(size=6)
        p = project(v, onto)
        assert abs(cosine_similarity(p, onto)) == pytest.approx(1.0)

    def test_decomposition_sums_back(self, rng, tol):
        """v = projection + orthogonal component. Always."""
        v, onto = rng.normal(size=6), rng.normal(size=6)
        recovered = project(v, onto) + orthogonal_component(v, onto)
        np.testing.assert_allclose(recovered, v, atol=tol["tight"])

    def test_orthogonal_component_is_orthogonal(self, rng, tol):
        v, onto = rng.normal(size=6), rng.normal(size=6)
        assert dot_product(orthogonal_component(v, onto), onto) == pytest.approx(
            0.0, abs=tol["loose"]
        )

    def test_projection_is_idempotent(self, rng, tol):
        v, onto = rng.normal(size=6), rng.normal(size=6)
        once = project(v, onto)
        np.testing.assert_allclose(project(once, onto), once, atol=tol["loose"])


# ---------------------------------------------------------------------------
# Matrix operations
# ---------------------------------------------------------------------------


class TestMatmul:
    def test_known_2x2(self):
        A = np.array([[1.0, 2.0], [3.0, 4.0]])
        B = np.array([[5.0, 6.0], [7.0, 8.0]])
        np.testing.assert_allclose(matmul(A, B), np.array([[19.0, 22.0], [43.0, 50.0]]))

    def test_matches_numpy_on_random_shapes(self, rng, tol):
        for _ in range(10):
            m, k, n = rng.integers(1, 8, size=3)
            A, B = rng.normal(size=(m, k)), rng.normal(size=(k, n))
            np.testing.assert_allclose(matmul(A, B), A @ B, atol=tol["tight"])

    def test_identity_is_neutral(self, rng, tol):
        A = rng.normal(size=(5, 5))
        np.testing.assert_allclose(matmul(A, identity(5)), A, atol=tol["tight"])

    def test_not_commutative(self):
        """A common interview trip-up. Matrix multiplication has an order."""
        A = np.array([[1.0, 2.0], [3.0, 4.0]])
        B = np.array([[0.0, 1.0], [1.0, 0.0]])
        assert not np.allclose(matmul(A, B), matmul(B, A))

    def test_associative(self, rng, tol):
        A, B, C = rng.normal(size=(3, 4)), rng.normal(size=(4, 2)), rng.normal(size=(2, 5))
        np.testing.assert_allclose(
            matmul(matmul(A, B), C), matmul(A, matmul(B, C)), atol=tol["loose"]
        )

    def test_rejects_bad_inner_dimension(self):
        with pytest.raises(ValueError):
            matmul(np.ones((2, 3)), np.ones((4, 5)))


class TestMatrixBasics:
    def test_transpose(self, rng):
        A = rng.normal(size=(3, 5))
        np.testing.assert_allclose(transpose(A), A.T)

    def test_double_transpose_is_identity(self, rng):
        A = rng.normal(size=(3, 5))
        np.testing.assert_allclose(transpose(transpose(A)), A)

    def test_identity_shape_and_diagonal(self):
        eye = identity(4)
        assert eye.shape == (4, 4)
        np.testing.assert_allclose(eye, np.eye(4))

    def test_trace(self, rng):
        A = rng.normal(size=(6, 6))
        assert trace(A) == pytest.approx(np.trace(A))

    def test_trace_rejects_nonsquare(self):
        with pytest.raises(ValueError):
            trace(np.ones((2, 3)))

    def test_is_symmetric(self, rng):
        A = rng.normal(size=(5, 5))
        assert is_symmetric(A + A.T)
        assert not is_symmetric(A)

    def test_covariance_is_always_symmetric(self, rng):
        """Why PCA works cleanly: covariance matrices are symmetric by construction."""
        X = rng.normal(size=(50, 6))
        assert is_symmetric(np.cov(X, rowvar=False))

    def test_is_orthogonal_for_rotation(self):
        theta = 0.7
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        assert is_orthogonal(R)

    def test_is_orthogonal_rejects_scaling(self):
        assert not is_orthogonal(np.array([[2.0, 0.0], [0.0, 2.0]]))


class TestMatrixVectorProduct:
    def test_matches_numpy(self, rng, tol):
        A, v = rng.normal(size=(4, 6)), rng.normal(size=6)
        np.testing.assert_allclose(matrix_vector_product(A, v), A @ v, atol=tol["tight"])

    def test_is_linear_combination_of_columns(self, rng, tol):
        """The reading of matmul that most people never internalize."""
        A, v = rng.normal(size=(4, 3)), rng.normal(size=3)
        by_columns = sum(v[j] * A[:, j] for j in range(3))
        np.testing.assert_allclose(matrix_vector_product(A, v), by_columns, atol=tol["tight"])


# ---------------------------------------------------------------------------
# Orthogonalization
# ---------------------------------------------------------------------------


class TestGramSchmidt:
    @pytest.mark.parametrize("impl", [gram_schmidt, modified_gram_schmidt])
    def test_output_is_orthonormal(self, impl, rng, tol):
        vectors = [rng.normal(size=5) for _ in range(4)]
        basis = impl(vectors)
        for v in basis:
            assert norm(v) == pytest.approx(1.0, abs=tol["loose"])
        for i, u in enumerate(basis):
            for w in basis[i + 1 :]:
                assert dot_product(u, w) == pytest.approx(0.0, abs=tol["loose"])

    @pytest.mark.parametrize("impl", [gram_schmidt, modified_gram_schmidt])
    def test_spans_the_same_subspace(self, impl, rng, tol):
        """Each original vector must be reconstructible from the basis."""
        vectors = [rng.normal(size=5) for _ in range(3)]
        basis = impl(vectors)
        for v in vectors:
            reconstruction = sum(dot_product(v, b) * b for b in basis)
            np.testing.assert_allclose(reconstruction, v, atol=tol["loose"])

    @pytest.mark.parametrize("impl", [gram_schmidt, modified_gram_schmidt])
    def test_drops_dependent_vectors(self, impl):
        a = np.array([1.0, 0.0, 0.0])
        b = np.array([2.0, 0.0, 0.0])  # dependent on a
        c = np.array([0.0, 1.0, 0.0])
        assert len(impl([a, b, c])) == 2

    def test_already_orthonormal_input_is_preserved(self, rng, tol):
        basis = gram_schmidt([np.array([1.0, 0.0]), np.array([0.0, 1.0])])
        np.testing.assert_allclose(np.abs(basis[0]), np.array([1.0, 0.0]), atol=tol["loose"])


class TestRank:
    def test_full_rank(self, rng):
        assert rank(rng.normal(size=(5, 3))) == 3

    def test_rank_deficient(self):
        A = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])  # column 2 = 2 * column 1
        assert rank(A) == 1

    def test_zero_matrix(self):
        assert rank(np.zeros((4, 4))) == 0

    def test_matches_numpy(self, rng):
        for _ in range(10):
            A = rng.normal(size=(6, 4))
            assert rank(A) == np.linalg.matrix_rank(A)


# ---------------------------------------------------------------------------
# Batched operations — the retrieval preview
# ---------------------------------------------------------------------------


class TestBatchedSimilarity:
    def test_matches_the_scalar_version(self, rng, tol):
        query = rng.normal(size=8)
        matrix = rng.normal(size=(20, 8))
        batched = batch_cosine_similarity(query, matrix)
        expected = np.array([cosine_similarity(query, row) for row in matrix])
        np.testing.assert_allclose(batched, expected, atol=tol["loose"])

    def test_output_shape(self, rng):
        assert batch_cosine_similarity(rng.normal(size=8), rng.normal(size=(20, 8))).shape == (20,)

    def test_top_k_finds_the_planted_match(self, rng):
        matrix = rng.normal(size=(100, 16))
        query = matrix[42] * 3.0  # same direction, different magnitude
        indices, scores = top_k_similar(query, matrix, k=5)
        assert indices[0] == 42
        assert scores[0] == pytest.approx(1.0, abs=1e-6)

    def test_top_k_is_sorted_descending(self, rng):
        indices, scores = top_k_similar(rng.normal(size=16), rng.normal(size=(100, 16)), k=10)
        assert len(indices) == len(scores) == 10
        assert np.all(np.diff(scores) <= 1e-12)


@pytest.mark.slow
class TestPerformance:
    """Not correctness — a reality check.

    Write the numbers into your Week 1 check-in. When you get to Month 10 and
    have to choose an index type, having felt the cost of a brute-force scan
    makes that decision concrete instead of theoretical.
    """

    def test_batched_beats_looping(self, rng):
        import time

        matrix = rng.normal(size=(20_000, 128))
        query = rng.normal(size=128)

        start = time.perf_counter()
        batch_cosine_similarity(query, matrix)
        batched = time.perf_counter() - start

        start = time.perf_counter()
        [cosine_similarity(query, row) for row in matrix[:2000]]
        looped = (time.perf_counter() - start) * 10  # extrapolate to 20k

        print(f"\nbatched: {batched * 1000:.1f}ms   looped (est): {looped * 1000:.1f}ms")
        assert batched < looped
