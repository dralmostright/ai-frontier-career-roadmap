"""Information theory — Week 4.

Four quantities, and the relationships between them, that recur for the next
seventeen months:

- **Entropy** H(p): the average surprise of a distribution. The lower bound on
  bits needed to encode samples from it.
- **Cross entropy** H(p, q): the cost of encoding p using a code built for q.
  This is the loss function for every classifier and every language model you
  will train.
- **KL divergence** D(p || q) = H(p, q) - H(p): the *excess* cost of using the
  wrong distribution. Non-negative, and asymmetric.
- **Mutual information** I(X; Y): how much knowing X reduces uncertainty about Y.

The identity worth internalizing: minimizing cross entropy is minimizing KL
divergence, because H(p) is fixed by the data. That is the answer to "why is
cross entropy the loss for classification?" and it is asked constantly.

KL also appears in Month 12 as the regularizer keeping an RLHF-tuned policy near
its reference model, and in Week 36 as a way to compare model output
distributions. It is not a Month 1 curiosity.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]

EPS = 1e-12
"""Floor for probabilities before taking a log.

0 * log(0) is defined as 0 by convention (the limit is 0), but numpy will hand
you nan. Clamping is the standard fix. Know that it is a convention with a
justification, not a hack.
"""


def entropy(p: Array, base: float = 2.0) -> float:
    """Shannon entropy: -sum p_i log p_i.

    base=2 gives bits, base=e gives nats. ML code almost always uses nats;
    information theory texts almost always use bits. Be explicit about which,
    because a factor of ln(2) ≈ 0.693 in a reported number is exactly the kind
    of discrepancy that costs an afternoon.

    Facts to have at hand:
      - Maximized by the uniform distribution: log(n).
      - Zero for a point mass — no uncertainty, no information.
      - Never negative for a discrete distribution.

    Raises:
        ValueError: if p has negative entries or does not sum to 1.
    """
    raise NotImplementedError("Week 4")


def cross_entropy(p: Array, q: Array, base: float = 2.0) -> float:
    """H(p, q) = -sum p_i log q_i.

    The cost of using a code optimized for q to encode data from p. In training,
    p is the one-hot label and q is your model's prediction — which collapses
    the sum to a single term, ``-log q[correct_class]``. That is why the
    classification loss you write in Week 6 looks nothing like this formula
    despite being exactly this formula.

    Note the asymmetry: H(p, q) != H(q, p).
    """
    raise NotImplementedError("Week 4")


def kl_divergence(p: Array, q: Array, base: float = 2.0) -> float:
    """D(p || q) = sum p_i log(p_i / q_i).

    Properties to be able to state and justify:
      - Non-negative, zero iff p == q (Gibbs' inequality).
      - Asymmetric, so it is not a distance metric.
      - Infinite if q_i == 0 anywhere p_i > 0. This is the practical reason
        smoothing exists.

    The forward/reverse distinction is worth knowing: minimizing D(p || q) over
    q makes q cover p's support (mode-covering); minimizing D(q || p) makes q
    concentrate on one mode (mode-seeking). Variational inference uses the
    second, which is why VAEs produce blurry samples.
    """
    raise NotImplementedError("Week 4")


def js_divergence(p: Array, q: Array, base: float = 2.0) -> float:
    """Jensen-Shannon divergence: the symmetrized, bounded cousin of KL.

    JS(p, q) = 0.5 * D(p || m) + 0.5 * D(q || m), where m = (p + q) / 2.

    Symmetric, always finite, and bounded by log(2) in bits. Its square root is
    a true metric. Use it when you need to compare two distributions neither of
    which is privileged — for instance, comparing token distributions from two
    model checkpoints in Week 48.
    """
    raise NotImplementedError("Week 4")


def perplexity(log_probs: Array, base: float = np.e) -> float:
    """Perplexity: exp(mean negative log likelihood).

    The standard language model metric, and one you must be able to interpret
    rather than merely report. A perplexity of 20 means the model is, on
    average, as uncertain as if choosing uniformly among 20 tokens.

    Crucially, perplexity is tokenizer-dependent. Two models with different
    vocabularies are not comparable on perplexity, and this catches people out.
    In Week 35 you will compute this on your own trained model; in Week 62 the
    comparability problem becomes a real obstacle to reproducing a paper.

    Args:
        log_probs: Per-token log probabilities of the *observed* tokens.
    """
    raise NotImplementedError("Week 4")


def mutual_information(joint: Array, base: float = 2.0) -> float:
    """I(X; Y) = sum p(x,y) log( p(x,y) / (p(x) p(y)) ).

    Equivalently H(X) + H(Y) - H(X, Y), and equivalently the KL divergence
    between the joint and the product of marginals. Zero exactly when X and Y
    are independent.

    Practical use: feature selection that catches non-linear dependence, where
    correlation would report zero.

    Args:
        joint: Joint probability table of shape (|X|, |Y|), summing to 1.
    """
    raise NotImplementedError("Week 4")


def conditional_entropy(joint: Array, base: float = 2.0) -> float:
    """H(Y|X): the uncertainty remaining in Y once X is known.

    Verify H(Y|X) = H(X, Y) - H(X) numerically. That identity is the backbone of
    information gain, which is how decision trees choose splits in Week 7 —
    information gain is literally H(Y) - H(Y|split).
    """
    raise NotImplementedError("Week 4")


def information_gain(parent_labels: Array, child_label_sets: list[Array]) -> float:
    """Entropy reduction from a split. Week 7 uses this directly.

    IG = H(parent) - sum_i (|child_i| / |parent|) * H(child_i)

    Writing it in Week 4 and using it in Week 7 is deliberate: decision trees
    are an information-theoretic algorithm, and seeing that connection makes
    both topics stick.

    Args:
        parent_labels: Class labels before the split.
        child_label_sets: Class labels in each partition after the split.
    """
    raise NotImplementedError("Week 4")


def gini_impurity(labels: Array) -> float:
    """1 - sum p_i^2. The other standard split criterion.

    Gini and entropy almost always choose the same split. Gini is marginally
    cheaper (no logarithm), which is why CART defaults to it. "They rarely
    disagree, and Gini avoids a log" is the correct interview answer to "why
    would you pick one over the other?" — resist the temptation to invent a
    deeper reason.
    """
    raise NotImplementedError("Week 4")


def normalize_to_distribution(counts: Array, smoothing: float = 0.0) -> Array:
    """Turn counts into a probability distribution, with optional add-k smoothing.

    Smoothing exists because a zero probability is infinitely costly under a log
    loss and makes KL divergence infinite. This is the same reason n-gram
    language models needed smoothing, and the intuition transfers directly to
    why label smoothing helps neural classifiers (Week 16).
    """
    raise NotImplementedError("Week 4")
