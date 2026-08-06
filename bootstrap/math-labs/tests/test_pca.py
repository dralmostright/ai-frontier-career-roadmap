"""Tests for Week 2: eigendecomposition, SVD, and PCA."""

from __future__ import annotations

from itertools import pairwise

import numpy as np
import pytest
from pca import (
    PCA,
    compress_image,
    eigen_decomposition,
    explained_variance_ratio,
    low_rank_approximation,
    power_iteration,
    rank_for_variance,
    reconstruction_error,
    svd,
    truncated_svd,
)

pytestmark = pytest.mark.week(2)


@pytest.fixture
def symmetric(rng):
    A = rng.normal(size=(6, 6))
    return A + A.T


@pytest.fixture
def correlated_data(rng):
    """Data with a known dominant direction: y is mostly 2x plus noise."""
    x = rng.normal(size=200)
    y = 2.0 * x + rng.normal(scale=0.1, size=200)
    z = rng.normal(scale=0.05, size=200)
    return np.column_stack([x, y, z])


class TestEigenDecomposition:
    def test_satisfies_the_defining_equation(self, symmetric, tol):
        """A v = lambda v, for every eigenpair. This is the definition."""
        values, vectors = eigen_decomposition(symmetric)
        for i in range(len(values)):
            np.testing.assert_allclose(
                symmetric @ vectors[:, i], values[i] * vectors[:, i], atol=tol["loose"]
            )

    def test_sorted_descending(self, symmetric):
        values, _ = eigen_decomposition(symmetric)
        assert np.all(np.diff(values) <= 1e-12), "NumPy returns ascending; reverse it"

    def test_eigenvectors_are_orthonormal(self, symmetric, tol):
        _, vectors = eigen_decomposition(symmetric)
        np.testing.assert_allclose(vectors.T @ vectors, np.eye(6), atol=tol["loose"])

    def test_trace_equals_sum_of_eigenvalues(self, symmetric):
        values, _ = eigen_decomposition(symmetric)
        assert np.sum(values) == pytest.approx(np.trace(symmetric))

    def test_rejects_nonsymmetric(self, rng):
        with pytest.raises(ValueError):
            eigen_decomposition(rng.normal(size=(4, 4)))

    def test_power_iteration_finds_the_dominant_pair(self, symmetric, tol):
        values, vectors = eigen_decomposition(symmetric)
        lam, vec = power_iteration(symmetric)
        assert abs(lam) == pytest.approx(abs(values[0]), abs=1e-4)
        assert abs(np.dot(vec, vectors[:, 0])) == pytest.approx(1.0, abs=1e-4)


class TestSVD:
    def test_reconstructs_the_original(self, rng, tol):
        A = rng.normal(size=(8, 5))
        U, S, Vt = svd(A)
        np.testing.assert_allclose(U @ np.diag(S) @ Vt, A, atol=tol["loose"])

    def test_singular_values_nonnegative_and_descending(self, rng):
        _, S, _ = svd(rng.normal(size=(8, 5)))
        assert np.all(S >= 0)
        assert np.all(np.diff(S) <= 1e-12)

    def test_factors_are_orthonormal(self, rng, tol):
        U, _, Vt = svd(rng.normal(size=(8, 5)))
        np.testing.assert_allclose(U.T @ U, np.eye(U.shape[1]), atol=tol["loose"])
        np.testing.assert_allclose(Vt @ Vt.T, np.eye(Vt.shape[0]), atol=tol["loose"])

    def test_singular_values_are_sqrt_eigenvalues_of_ata(self, rng):
        """The bridge between the two routes to PCA. Understand this one."""
        A = rng.normal(size=(10, 4))
        _, S, _ = svd(A)
        eigvals, _ = eigen_decomposition(A.T @ A)
        np.testing.assert_allclose(S**2, eigvals, atol=1e-6)

    def test_truncated_shapes(self, rng):
        U, S, Vt = truncated_svd(rng.normal(size=(10, 6)), k=3)
        assert U.shape == (10, 3) and S.shape == (3,) and Vt.shape == (3, 6)

    def test_low_rank_approximation_has_the_requested_rank(self, rng):
        A = rng.normal(size=(10, 6))
        assert np.linalg.matrix_rank(low_rank_approximation(A, 3)) == 3

    def test_error_decreases_monotonically_with_k(self, rng):
        A = rng.normal(size=(12, 8))
        errors = [reconstruction_error(A, low_rank_approximation(A, k)) for k in range(1, 9)]
        assert all(a >= b - 1e-12 for a, b in pairwise(errors))

    def test_full_rank_reconstruction_is_exact(self, rng, tol):
        A = rng.normal(size=(6, 6))
        assert reconstruction_error(A, low_rank_approximation(A, 6)) == pytest.approx(
            0.0, abs=tol["loose"]
        )

    def test_beats_a_random_rank_k_matrix(self, rng):
        """Eckart-Young: truncated SVD is optimal, not merely reasonable."""
        A = rng.normal(size=(10, 6))
        best = reconstruction_error(A, low_rank_approximation(A, 2))
        B = rng.normal(size=(10, 2)) @ rng.normal(size=(2, 6))
        assert best <= reconstruction_error(A, B)


class TestVarianceAccounting:
    def test_ratios_sum_to_one(self):
        ratios = explained_variance_ratio(np.array([5.0, 3.0, 1.0]))
        assert np.sum(ratios) == pytest.approx(1.0)

    def test_uses_squared_singular_values(self):
        """The most common error in this file."""
        ratios = explained_variance_ratio(np.array([3.0, 4.0]))
        np.testing.assert_allclose(ratios, np.array([9 / 25, 16 / 25]))

    def test_rank_for_variance(self):
        s = np.array([10.0, 1.0, 0.1, 0.01])
        assert rank_for_variance(s, 0.95) == 1
        assert rank_for_variance(s, 0.999) >= 2

    def test_rank_for_full_variance(self):
        assert rank_for_variance(np.array([3.0, 2.0, 1.0]), 1.0) == 3


class TestPCA:
    def test_finds_the_planted_direction(self, correlated_data):
        p = PCA(n_components=1).fit(correlated_data)
        component = p.components_[0]
        expected = np.array([1.0, 2.0, 0.0]) / np.linalg.norm([1.0, 2.0, 0.0])
        assert abs(np.dot(component, expected)) == pytest.approx(1.0, abs=0.05)

    def test_first_component_dominates_correlated_data(self, correlated_data):
        p = PCA().fit(correlated_data)
        assert p.explained_variance_ratio_[0] > 0.95

    def test_transform_shape(self, correlated_data):
        assert PCA(n_components=2).fit_transform(correlated_data).shape == (200, 2)

    def test_components_are_orthonormal(self, correlated_data, tol):
        c = PCA().fit(correlated_data).components_
        np.testing.assert_allclose(c @ c.T, np.eye(len(c)), atol=tol["loose"])

    def test_transformed_data_is_decorrelated(self, correlated_data):
        """The whole point of the rotation."""
        Z = PCA().fit_transform(correlated_data)
        off_diagonal = np.cov(Z, rowvar=False) - np.diag(np.diag(np.cov(Z, rowvar=False)))
        assert np.max(np.abs(off_diagonal)) < 1e-8

    def test_full_rank_roundtrip_is_lossless(self, correlated_data, tol):
        p = PCA()
        np.testing.assert_allclose(
            p.inverse_transform(p.fit_transform(correlated_data)),
            correlated_data,
            atol=tol["loose"],
        )

    def test_truncated_roundtrip_loses_only_the_dropped_variance(self, correlated_data):
        p = PCA(n_components=1)
        recon = p.inverse_transform(p.fit_transform(correlated_data))
        relative = np.linalg.norm(recon - correlated_data) / np.linalg.norm(correlated_data)
        assert 0.0 < relative < 0.1

    def test_pca_two_ways_agree(self, correlated_data):
        """Eigendecomposition of the covariance == SVD of the centered data.

        If you can explain *why*, you understand PCA. If you cannot, go back to
        `test_singular_values_are_sqrt_eigenvalues_of_ata` and work forward.
        """
        by_eigen = PCA(method="eigen").fit(correlated_data)
        by_svd = PCA(method="svd").fit(correlated_data)
        np.testing.assert_allclose(
            by_eigen.explained_variance_ratio_, by_svd.explained_variance_ratio_, atol=1e-8
        )
        for a, b in zip(by_eigen.components_, by_svd.components_, strict=True):
            assert abs(np.dot(a, b)) == pytest.approx(1.0, abs=1e-6)

    def test_centering_is_not_optional(self, rng):
        """Uncentered data far from the origin makes PC1 point at the mean."""
        X = rng.normal(size=(100, 2)) + np.array([500.0, 500.0])
        p = PCA(n_components=1).fit(X)
        mean_direction = p.mean_ / np.linalg.norm(p.mean_)
        assert abs(np.dot(p.components_[0], mean_direction)) < 0.95

    def test_sign_convention_is_deterministic(self, correlated_data):
        """Eigenvectors are defined up to sign. Pin it, or your tests flake."""
        a = PCA(n_components=2).fit(correlated_data).components_
        b = PCA(n_components=2).fit(correlated_data.copy()).components_
        np.testing.assert_allclose(a, b)


class TestImageCompression:
    def test_returns_same_shape(self, rng):
        image = rng.random((64, 64))
        approx, _ = compress_image(image, k=10)
        assert approx.shape == image.shape

    def test_reports_expected_stats(self, rng):
        _, stats = compress_image(rng.random((64, 64)), k=10)
        assert {"compression_ratio", "relative_error", "variance_retained"} <= stats.keys()

    def test_more_components_means_less_error(self, rng):
        image = rng.random((64, 64))
        _, low = compress_image(image, k=5)
        _, high = compress_image(image, k=40)
        assert high["relative_error"] < low["relative_error"]

    def test_structured_images_compress_better_than_noise(self, rng):
        """The lesson: SVD exploits structure. Noise has none."""
        xs = np.linspace(0, 1, 64)
        smooth = np.outer(np.sin(4 * np.pi * xs), np.cos(4 * np.pi * xs))
        noise = rng.random((64, 64))
        _, smooth_stats = compress_image(smooth, k=5)
        _, noise_stats = compress_image(noise, k=5)
        assert smooth_stats["relative_error"] < noise_stats["relative_error"]
