"""Probability and statistics from scratch — Week 4.

Distributions, likelihood, and estimation. The through-line for the whole course:
**training a model is maximum likelihood estimation**. Cross-entropy loss is the
negative log likelihood of a categorical distribution. MSE is the negative log
likelihood of a Gaussian with fixed variance. Once you have derived both, loss
functions stop looking like a menu of options and start looking like consequences
of a modeling assumption.

Implement the PDFs and estimators yourself; use `scipy.stats` only in the tests
as the reference.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Descriptive statistics
# ---------------------------------------------------------------------------


def mean(x: Array) -> float:
    """Arithmetic mean."""
    raise NotImplementedError("Week 4")


def variance(x: Array, ddof: int = 0) -> float:
    """Variance. ddof=0 is the population estimate, ddof=1 is Bessel-corrected.

    Know which one you want and why. ddof=1 is unbiased for a sample; ddof=0 is
    what you want when normalizing activations over a batch. NumPy defaults to 0
    and pandas defaults to 1, which causes a specific, recurring, hard-to-spot
    class of bug.
    """
    raise NotImplementedError("Week 4")


def standard_deviation(x: Array, ddof: int = 0) -> float:
    raise NotImplementedError("Week 4")


def covariance_matrix(X: Array, ddof: int = 1) -> Array:
    """Covariance of data shaped (n_samples, n_features).

    Center first, then (X_c.T @ X_c) / (n - ddof). This is the matrix PCA
    eigendecomposes in Week 2 — connect the two explicitly in your write-up.
    """
    raise NotImplementedError("Week 4")


def correlation_matrix(X: Array) -> Array:
    """Covariance normalized to [-1, 1] by the standard deviations."""
    raise NotImplementedError("Week 4")


def standardize(X: Array) -> tuple[Array, Array, Array]:
    """Zero mean, unit variance per feature.

    Returns:
        (standardized, mean, std). Return the statistics so you can apply the
        *training* statistics to validation and test data. Recomputing them on
        the test set is leakage — a Week 10 topic you can start avoiding now.
    """
    raise NotImplementedError("Week 4")


# ---------------------------------------------------------------------------
# Distributions
# ---------------------------------------------------------------------------


@dataclass
class Bernoulli:
    """Single trial with success probability p. The distribution behind every
    binary classifier's output."""

    p: float

    def pmf(self, k: int) -> float:
        raise NotImplementedError("Week 4")

    def log_pmf(self, k: int) -> float:
        """Log probability. Note this is exactly the negative of binary
        cross-entropy — write out both and confirm the identity."""
        raise NotImplementedError("Week 4")

    def sample(self, size: int, rng: np.random.Generator | None = None) -> Array:
        raise NotImplementedError("Week 4")

    @property
    def mean(self) -> float:
        raise NotImplementedError("Week 4")

    @property
    def variance(self) -> float:
        raise NotImplementedError("Week 4")


@dataclass
class Gaussian:
    """Normal distribution. The default assumption almost everywhere, partly
    because of the central limit theorem and partly because it is convenient."""

    mu: float = 0.0
    sigma: float = 1.0

    def pdf(self, x: float | Array) -> float | Array:
        raise NotImplementedError("Week 4")

    def log_pdf(self, x: float | Array) -> float | Array:
        """Compute in log space directly, not as log(pdf(x)).

        For x far from the mean, pdf(x) underflows to 0.0 and log(0) is -inf.
        Working in log space throughout is the general fix, and it is the same
        reason you use log-softmax rather than log(softmax(.)).
        """
        raise NotImplementedError("Week 4")

    def sample(self, size: int, rng: np.random.Generator | None = None) -> Array:
        raise NotImplementedError("Week 4")

    def cdf(self, x: float) -> float:
        """Use `math.erf`. Derive the relationship between erf and the normal CDF."""
        raise NotImplementedError("Week 4")


@dataclass
class Poisson:
    """Counts per interval. Directly useful to you: query arrivals, lock waits,
    error events per minute. Week 44's anomaly detection uses it."""

    lam: float

    def pmf(self, k: int) -> float:
        """Use `math.lgamma` for the factorial. 170! overflows a float64;
        lgamma does not."""
        raise NotImplementedError("Week 4")

    def log_pmf(self, k: int) -> float:
        raise NotImplementedError("Week 4")

    def sample(self, size: int, rng: np.random.Generator | None = None) -> Array:
        raise NotImplementedError("Week 4")


@dataclass
class Categorical:
    """Distribution over k outcomes. This is what a language model outputs at
    every position, over a vocabulary of 50,000+ outcomes."""

    probs: Array

    def __post_init__(self) -> None:
        """Validate: non-negative and summing to 1 within tolerance."""
        raise NotImplementedError("Week 4")

    def pmf(self, k: int) -> float:
        raise NotImplementedError("Week 4")

    def sample(self, size: int, rng: np.random.Generator | None = None) -> NDArray[np.int64]:
        """Inverse-CDF sampling. In Week 35 you will do exactly this to sample
        tokens, with temperature and top-k applied to `probs` first."""
        raise NotImplementedError("Week 4")


# ---------------------------------------------------------------------------
# Estimation
# ---------------------------------------------------------------------------


def mle_bernoulli(samples: Array) -> float:
    """MLE for p. The answer is the sample mean — derive why.

    Write the likelihood, take the log, differentiate with respect to p, set to
    zero. Three lines. Do it on paper before implementing; this is the simplest
    possible instance of the pattern that underlies all supervised training.
    """
    raise NotImplementedError("Week 4")


def mle_gaussian(samples: Array) -> tuple[float, float]:
    """MLE for (mu, sigma).

    The MLE for variance uses ddof=0 and is *biased* — it underestimates. Know
    that this is a real phenomenon with a name, and know that the correction
    (ddof=1) trades bias for variance. It is a clean, small example of the
    bias-variance tradeoff you will discuss in Week 5.
    """
    raise NotImplementedError("Week 4")


def log_likelihood(samples: Array, distribution: object) -> float:
    """Sum of log probabilities under a distribution.

    Sum logs; never multiply probabilities. A thousand probabilities of 0.5
    multiply to 1e-301 and then to 0.0. This is why every objective in deep
    learning is a log likelihood.
    """
    raise NotImplementedError("Week 4")


def bayes_rule(prior: float, likelihood: float, likelihood_given_not: float) -> float:
    """Posterior P(H|E) from prior, P(E|H), and P(E|~H).

    The base-rate question, and a genuinely common interview question:

        A test is 99% sensitive and 99% specific. The disease affects 1 in
        10,000. You test positive. What is P(disease)?

    The answer is about 1%, and the reason is that the base rate dominates.
    Be able to produce that number and explain it in under 60 seconds. It is
    the same reasoning as "your fraud model has 99% accuracy on a 0.1% fraud
    rate," which is Week 11.
    """
    raise NotImplementedError("Week 4")


def bootstrap_confidence_interval(
    samples: Array,
    statistic: object = None,
    n_resamples: int = 10_000,
    confidence: float = 0.95,
    rng: np.random.Generator | None = None,
) -> tuple[float, float]:
    """Percentile bootstrap CI for any statistic.

    Resample with replacement, recompute the statistic, take the empirical
    percentiles. It requires no distributional assumption, which is why it
    works for medians, AUCs, and BLEU scores where the analytic formula either
    does not exist or is not worth deriving.

    You will use this constantly from Week 11 onward. "Model A scored 0.84 and
    model B scored 0.86" is not a result; "0.84 [0.81, 0.87] versus 0.86
    [0.83, 0.89]" is an honest one, and reporting the second is a seniority
    signal that costs you ten lines of code.

    Args:
        statistic: Callable mapping an array to a float. Defaults to the mean.
    """
    raise NotImplementedError("Week 4")
