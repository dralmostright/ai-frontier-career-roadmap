"""Tests for Week 4: probability, statistics, and information theory."""

from __future__ import annotations

import math

import numpy as np
import pytest
from information_theory import (
    conditional_entropy,
    cross_entropy,
    entropy,
    gini_impurity,
    information_gain,
    js_divergence,
    kl_divergence,
    mutual_information,
    normalize_to_distribution,
    perplexity,
)
from probability import (
    Bernoulli,
    Categorical,
    Gaussian,
    Poisson,
    bayes_rule,
    bootstrap_confidence_interval,
    correlation_matrix,
    covariance_matrix,
    log_likelihood,
    mean,
    mle_bernoulli,
    mle_gaussian,
    standard_deviation,
    standardize,
    variance,
)
from scipy import stats as sp

pytestmark = pytest.mark.week(4)


# ---------------------------------------------------------------------------
# Descriptive statistics
# ---------------------------------------------------------------------------


class TestDescriptive:
    def test_mean_and_variance(self, rng, tol):
        x = rng.normal(size=200)
        assert mean(x) == pytest.approx(np.mean(x), abs=tol["tight"])
        assert variance(x, ddof=0) == pytest.approx(np.var(x), abs=tol["tight"])
        assert variance(x, ddof=1) == pytest.approx(np.var(x, ddof=1), abs=tol["tight"])

    def test_ddof_actually_changes_the_answer(self, rng):
        x = rng.normal(size=10)
        assert variance(x, ddof=1) > variance(x, ddof=0)

    def test_std_is_sqrt_of_variance(self, rng):
        x = rng.normal(size=50)
        assert standard_deviation(x) == pytest.approx(math.sqrt(variance(x)))

    def test_covariance_matches_numpy(self, rng, tol):
        X = rng.normal(size=(100, 4))
        np.testing.assert_allclose(covariance_matrix(X), np.cov(X, rowvar=False), atol=tol["loose"])

    def test_covariance_is_symmetric(self, rng):
        C = covariance_matrix(rng.normal(size=(50, 5)))
        np.testing.assert_allclose(C, C.T)

    def test_correlation_diagonal_is_one(self, rng, tol):
        R = correlation_matrix(rng.normal(size=(80, 4)))
        np.testing.assert_allclose(np.diag(R), np.ones(4), atol=tol["loose"])

    def test_correlation_is_bounded(self, rng):
        R = correlation_matrix(rng.normal(size=(80, 4)))
        assert np.all(np.abs(R) <= 1.0 + 1e-9)

    def test_standardize_returns_training_statistics(self, rng, tol):
        """Return mu and sigma so you can reuse them on val/test. This is the
        Week 10 leakage lesson, arriving six weeks early."""
        X = rng.normal(loc=5.0, scale=3.0, size=(100, 3))
        Z, mu, _ = standardize(X)
        np.testing.assert_allclose(Z.mean(axis=0), np.zeros(3), atol=tol["loose"])
        np.testing.assert_allclose(Z.std(axis=0), np.ones(3), atol=tol["loose"])
        np.testing.assert_allclose(mu, X.mean(axis=0), atol=tol["loose"])


# ---------------------------------------------------------------------------
# Distributions
# ---------------------------------------------------------------------------


class TestBernoulli:
    def test_pmf(self):
        b = Bernoulli(p=0.3)
        assert b.pmf(1) == pytest.approx(0.3)
        assert b.pmf(0) == pytest.approx(0.7)

    def test_moments(self):
        b = Bernoulli(p=0.3)
        assert b.mean == pytest.approx(0.3)
        assert b.variance == pytest.approx(0.21)

    def test_log_pmf_is_negative_bce(self):
        """Confirm the identity in code, then write it out by hand."""
        b = Bernoulli(p=0.3)
        assert b.log_pmf(1) == pytest.approx(math.log(0.3))
        assert b.log_pmf(0) == pytest.approx(math.log(0.7))

    def test_sampling_converges_to_p(self, rng):
        assert np.mean(Bernoulli(p=0.3).sample(50_000, rng)) == pytest.approx(0.3, abs=0.01)


class TestGaussian:
    def test_pdf_matches_scipy(self):
        g = Gaussian(mu=1.0, sigma=2.0)
        for x in (-3.0, 0.0, 1.0, 4.0):
            assert g.pdf(x) == pytest.approx(sp.norm.pdf(x, 1.0, 2.0))

    def test_pdf_peaks_at_the_mean(self):
        g = Gaussian(mu=1.0, sigma=2.0)
        assert g.pdf(1.0) > g.pdf(1.5) > g.pdf(3.0)

    def test_log_pdf_survives_the_tails(self):
        """log(pdf(x)) underflows to -inf out here. Computing in log space doesn't."""
        assert math.isfinite(Gaussian(0.0, 1.0).log_pdf(50.0))

    def test_cdf_matches_scipy(self):
        g = Gaussian(mu=0.0, sigma=1.0)
        for x in (-2.0, 0.0, 1.5):
            assert g.cdf(x) == pytest.approx(sp.norm.cdf(x), abs=1e-6)

    def test_sampling_recovers_the_parameters(self, rng):
        s = Gaussian(mu=3.0, sigma=2.0).sample(100_000, rng)
        assert np.mean(s) == pytest.approx(3.0, abs=0.05)
        assert np.std(s) == pytest.approx(2.0, abs=0.05)


class TestPoisson:
    def test_pmf_matches_scipy(self):
        p = Poisson(lam=3.0)
        for k in range(8):
            assert p.pmf(k) == pytest.approx(sp.poisson.pmf(k, 3.0))

    def test_pmf_sums_to_one(self):
        assert sum(Poisson(lam=3.0).pmf(k) for k in range(60)) == pytest.approx(1.0, abs=1e-9)

    def test_handles_large_k_without_overflow(self):
        """Use lgamma, not factorial. 200! is not representable as a float64."""
        assert math.isfinite(Poisson(lam=150.0).log_pmf(200))

    def test_mean_equals_lambda(self, rng):
        assert np.mean(Poisson(lam=4.0).sample(50_000, rng)) == pytest.approx(4.0, abs=0.05)


class TestCategorical:
    def test_rejects_unnormalized_probs(self):
        with pytest.raises(ValueError):
            Categorical(probs=np.array([0.5, 0.2]))

    def test_rejects_negative_probs(self):
        with pytest.raises(ValueError):
            Categorical(probs=np.array([1.5, -0.5]))

    def test_sampling_recovers_the_distribution(self, rng):
        probs = np.array([0.1, 0.6, 0.3])
        samples = Categorical(probs=probs).sample(60_000, rng)
        observed = np.bincount(samples, minlength=3) / len(samples)
        np.testing.assert_allclose(observed, probs, atol=0.01)


# ---------------------------------------------------------------------------
# Estimation
# ---------------------------------------------------------------------------


class TestEstimation:
    def test_mle_bernoulli_is_the_sample_mean(self, rng):
        s = Bernoulli(p=0.35).sample(20_000, rng)
        assert mle_bernoulli(s) == pytest.approx(np.mean(s))
        assert mle_bernoulli(s) == pytest.approx(0.35, abs=0.02)

    def test_mle_gaussian(self, rng):
        s = Gaussian(mu=2.0, sigma=1.5).sample(20_000, rng)
        mu, sigma = mle_gaussian(s)
        assert mu == pytest.approx(2.0, abs=0.05)
        assert sigma == pytest.approx(1.5, abs=0.05)

    def test_mle_variance_is_biased_low(self, rng):
        """A small, clean instance of the bias-variance tradeoff."""
        biases = []
        for _ in range(400):
            s = np.random.default_rng(int(rng.integers(1e9))).normal(0.0, 1.0, size=6)
            _, sigma_hat = mle_gaussian(s)
            biases.append(sigma_hat**2 - 1.0)
        assert np.mean(biases) < -0.02

    def test_log_likelihood_sums_logs(self, rng):
        g = Gaussian(mu=0.0, sigma=1.0)
        s = g.sample(500, rng)
        assert log_likelihood(s, g) == pytest.approx(float(np.sum(g.log_pdf(s))), abs=1e-6)

    def test_true_parameters_maximize_likelihood(self, rng):
        s = Gaussian(mu=2.0, sigma=1.0).sample(5_000, rng)
        best = log_likelihood(s, Gaussian(2.0, 1.0))
        assert best > log_likelihood(s, Gaussian(0.0, 1.0))
        assert best > log_likelihood(s, Gaussian(2.0, 3.0))

    def test_bayes_rule_base_rate_problem(self):
        """The interview classic. 99% accurate test, 1-in-10,000 disease."""
        posterior = bayes_rule(prior=1e-4, likelihood=0.99, likelihood_given_not=0.01)
        assert posterior == pytest.approx(0.0098, abs=0.001)

    def test_bayes_rule_with_a_useless_test(self):
        """If P(E|H) == P(E|~H) the evidence carries no information."""
        assert bayes_rule(0.3, 0.5, 0.5) == pytest.approx(0.3)


class TestBootstrap:
    def test_interval_contains_the_true_mean(self, rng):
        s = rng.normal(loc=5.0, scale=2.0, size=500)
        lo, hi = bootstrap_confidence_interval(s, n_resamples=2000, rng=rng)
        assert lo < 5.0 < hi

    def test_interval_narrows_with_more_data(self, rng):
        small = rng.normal(0.0, 1.0, size=30)
        large = rng.normal(0.0, 1.0, size=3000)
        lo_s, hi_s = bootstrap_confidence_interval(small, n_resamples=2000, rng=rng)
        lo_l, hi_l = bootstrap_confidence_interval(large, n_resamples=2000, rng=rng)
        assert (hi_l - lo_l) < (hi_s - lo_s)

    def test_works_for_the_median(self, rng):
        """No analytic formula needed. That's the appeal."""
        s = rng.normal(loc=5.0, scale=2.0, size=500)
        lo, hi = bootstrap_confidence_interval(s, statistic=np.median, n_resamples=2000, rng=rng)
        assert lo < 5.0 < hi


# ---------------------------------------------------------------------------
# Information theory
# ---------------------------------------------------------------------------


class TestEntropy:
    def test_fair_coin_is_one_bit(self):
        assert entropy(np.array([0.5, 0.5])) == pytest.approx(1.0)

    def test_uniform_over_n_is_log_n(self):
        assert entropy(np.ones(8) / 8) == pytest.approx(3.0)

    def test_point_mass_is_zero(self):
        assert entropy(np.array([1.0, 0.0, 0.0])) == pytest.approx(0.0)

    def test_uniform_is_the_maximum(self, rng):
        skewed = normalize_to_distribution(rng.random(5))
        assert entropy(np.ones(5) / 5) >= entropy(skewed)

    def test_base_e_gives_nats(self):
        assert entropy(np.array([0.5, 0.5]), base=math.e) == pytest.approx(math.log(2))

    def test_rejects_invalid_distribution(self):
        with pytest.raises(ValueError):
            entropy(np.array([0.5, 0.2]))


class TestCrossEntropyAndKL:
    def test_cross_entropy_equals_entropy_when_p_is_q(self):
        p = np.array([0.2, 0.3, 0.5])
        assert cross_entropy(p, p) == pytest.approx(entropy(p))

    def test_cross_entropy_is_asymmetric(self):
        p, q = np.array([0.9, 0.1]), np.array([0.5, 0.5])
        assert cross_entropy(p, q) != pytest.approx(cross_entropy(q, p))

    def test_kl_is_zero_iff_identical(self):
        p = np.array([0.2, 0.3, 0.5])
        assert kl_divergence(p, p) == pytest.approx(0.0, abs=1e-12)

    def test_kl_is_nonnegative(self, rng):
        for _ in range(50):
            p = normalize_to_distribution(rng.random(6))
            q = normalize_to_distribution(rng.random(6))
            assert kl_divergence(p, q) >= -1e-12

    def test_the_identity(self):
        """H(p, q) = H(p) + D(p || q). This is why minimizing cross entropy
        minimizes KL: H(p) doesn't depend on your model."""
        p, q = np.array([0.7, 0.2, 0.1]), np.array([0.4, 0.4, 0.2])
        assert cross_entropy(p, q) == pytest.approx(entropy(p) + kl_divergence(p, q))

    def test_kl_is_asymmetric(self):
        p, q = np.array([0.9, 0.1]), np.array([0.5, 0.5])
        assert kl_divergence(p, q) != pytest.approx(kl_divergence(q, p))

    def test_js_is_symmetric(self):
        p, q = np.array([0.9, 0.1]), np.array([0.4, 0.6])
        assert js_divergence(p, q) == pytest.approx(js_divergence(q, p))

    def test_js_is_bounded_by_one_bit(self):
        assert js_divergence(np.array([1.0, 0.0]), np.array([0.0, 1.0])) == pytest.approx(1.0)


class TestPerplexity:
    def test_uniform_over_v_gives_perplexity_v(self):
        """A model with no information has perplexity equal to vocab size."""
        log_probs = np.full(100, math.log(1 / 50))
        assert perplexity(log_probs) == pytest.approx(50.0)

    def test_perfect_model_has_perplexity_one(self):
        assert perplexity(np.zeros(20)) == pytest.approx(1.0)

    def test_better_model_has_lower_perplexity(self):
        good = np.full(50, math.log(0.5))
        bad = np.full(50, math.log(0.1))
        assert perplexity(good) < perplexity(bad)


class TestMutualInformation:
    def test_independent_variables_share_no_information(self):
        joint = np.outer(np.array([0.6, 0.4]), np.array([0.3, 0.7]))
        assert mutual_information(joint) == pytest.approx(0.0, abs=1e-12)

    def test_perfectly_dependent_variables(self):
        joint = np.array([[0.5, 0.0], [0.0, 0.5]])
        assert mutual_information(joint) == pytest.approx(1.0)

    def test_nonnegative(self, rng):
        joint = normalize_to_distribution(rng.random((3, 4)).ravel()).reshape(3, 4)
        assert mutual_information(joint) >= -1e-12

    def test_conditional_entropy_identity(self, rng):
        """H(Y|X) = H(X,Y) - H(X). Verify numerically, then use it in Week 7."""
        joint = normalize_to_distribution(rng.random((3, 4)).ravel()).reshape(3, 4)
        px = joint.sum(axis=1)
        assert conditional_entropy(joint) == pytest.approx(
            entropy(joint.ravel()) - entropy(px), abs=1e-9
        )


class TestSplitCriteria:
    def test_pure_node_has_zero_impurity(self):
        pure = np.array([1, 1, 1, 1])
        assert entropy(normalize_to_distribution(np.bincount(pure))) == pytest.approx(0.0)
        assert gini_impurity(pure) == pytest.approx(0.0)

    def test_balanced_binary_node(self):
        assert gini_impurity(np.array([0, 0, 1, 1])) == pytest.approx(0.5)

    def test_perfect_split_has_maximum_gain(self):
        parent = np.array([0, 0, 1, 1])
        gain = information_gain(parent, [np.array([0, 0]), np.array([1, 1])])
        assert gain == pytest.approx(1.0)

    def test_useless_split_has_no_gain(self):
        parent = np.array([0, 0, 1, 1])
        gain = information_gain(parent, [np.array([0, 1]), np.array([0, 1])])
        assert gain == pytest.approx(0.0, abs=1e-12)

    def test_gain_is_never_negative(self, rng):
        parent = rng.integers(0, 3, size=40)
        split = rng.integers(0, 2, size=40).astype(bool)
        assert information_gain(parent, [parent[split], parent[~split]]) >= -1e-12


class TestSmoothing:
    def test_normalizes_counts(self):
        d = normalize_to_distribution(np.array([2.0, 3.0, 5.0]))
        np.testing.assert_allclose(d, np.array([0.2, 0.3, 0.5]))

    def test_smoothing_removes_zeros(self):
        """A zero makes KL infinite and log loss undefined. That's why smoothing exists."""
        d = normalize_to_distribution(np.array([5.0, 0.0, 5.0]), smoothing=1.0)
        assert np.all(d > 0)
        assert np.sum(d) == pytest.approx(1.0)
