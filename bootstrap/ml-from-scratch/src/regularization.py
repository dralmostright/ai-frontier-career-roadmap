"""Regularization and generalization — Week 16.

The week's exercise is deliberately backwards: build a model that overfits
badly, then fix it one technique at a time and measure each fix. You end up with
a table of what each intervention bought, which is far more useful than the
knowledge that dropout exists.

The generalization gap — train score minus validation score — is the number to
watch. Every technique here trades a little training performance for a smaller
gap.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


# ---------------------------------------------------------------------------
# Weight penalties
# ---------------------------------------------------------------------------


def l1_penalty(parameters: list[Array], strength: float) -> float:
    """Sum of absolute weights.

    Produces exact zeros because the gradient is a constant ±strength regardless
    of how small the weight is — it keeps pushing until the weight crosses zero
    and stays there. Contrast with L2, whose gradient shrinks with the weight
    and therefore only ever approaches zero asymptotically. That is the real
    answer to "why does L1 give sparsity?" and it is better than the geometric
    diamond-versus-circle picture on its own.
    """
    raise NotImplementedError("Week 16")


def l2_penalty(parameters: list[Array], strength: float) -> float:
    """Sum of squared weights. Shrinks smoothly, never to exactly zero."""
    raise NotImplementedError("Week 16")


def elastic_net_penalty(parameters: list[Array], l1_strength: float, l2_strength: float) -> float:
    """L1 + L2. Sparsity from L1, stability under correlated features from L2."""
    raise NotImplementedError("Week 16")


def add_penalty_gradients(
    parameters: list[Array], gradients: list[Array], l1: float = 0.0, l2: float = 0.0
) -> None:
    """Add penalty gradients in place.

    Never penalize biases or normalization parameters. Penalizing a bias
    constrains the model's ability to shift its output, which has nothing to do
    with the complexity you are trying to control. Every framework excludes them
    by default and it is worth knowing that this is a deliberate choice.
    """
    raise NotImplementedError("Week 16")


# ---------------------------------------------------------------------------
# Early stopping
# ---------------------------------------------------------------------------


@dataclass
class EarlyStopping:
    """Stop when validation stops improving; restore the best weights.

    The cheapest regularizer available and often the most effective. Two details
    people get wrong:

    - **Restore the best weights.** Stopping at epoch 50 having peaked at epoch
      37 means you keep a model that is 13 epochs worse. Snapshot at the peak.
    - **min_delta.** Without it, noise-level fluctuations reset the patience
      counter and training runs forever.
    """

    patience: int = 10
    min_delta: float = 0.0
    mode: str = "min"
    restore_best: bool = True

    best_score_: float = field(init=False, default=float("inf"))
    best_epoch_: int = field(init=False, default=0)
    best_weights_: list[Array] | None = field(init=False, default=None)
    wait_: int = field(init=False, default=0)
    stopped_epoch_: int = field(init=False, default=0)

    def __call__(self, score: float, epoch: int, parameters: list[Array] | None = None) -> bool:
        """Returns True when training should stop."""
        raise NotImplementedError("Week 16")

    def restore(self, parameters: list[Array]) -> None:
        raise NotImplementedError("Week 16")


# ---------------------------------------------------------------------------
# Data augmentation and label smoothing
# ---------------------------------------------------------------------------


def label_smoothing(targets: Array, n_classes: int, smoothing: float = 0.1) -> Array:
    """Replace hard one-hot targets with (1-ε) on the true class and ε/(K-1) elsewhere.

    Stops the model from driving the correct logit to infinity, which is what a
    hard target technically asks for. Improves calibration and, in language
    models, reduces the confident-nonsense failure mode.

    Note the connection back to Week 4: this is the same reasoning as smoothing
    a count distribution to avoid zero probabilities.
    """
    raise NotImplementedError("Week 16")


def mixup(
    X: Array, y: Array, alpha: float = 0.2, rng: np.random.Generator | None = None
) -> tuple[Array, Array]:
    """Train on convex combinations of pairs of examples and their labels.

    Absurd on its face — an image that is 70% cat and 30% dog, labeled 0.7/0.3 —
    and it works remarkably well. The usual explanation is that it enforces
    linear behavior between training examples, which discourages the model from
    being confidently wrong in the gaps between them.
    """
    raise NotImplementedError("Week 16")


def gaussian_noise_augmentation(
    X: Array, sigma: float = 0.1, rng: np.random.Generator | None = None
) -> Array:
    """Add Gaussian noise to inputs.

    For linear models this is provably equivalent to L2 regularization. Worth
    deriving once — it is a satisfying result and it makes "regularization" and
    "augmentation" feel like the same idea seen from two angles.
    """
    raise NotImplementedError("Week 16")


# ---------------------------------------------------------------------------
# Diagnosis — the actual skill
# ---------------------------------------------------------------------------


def diagnose_fit(
    train_scores: list[float], val_scores: list[float], higher_is_better: bool = False
) -> dict[str, object]:
    """Classify a training run and recommend the next action.

    | Symptom | Diagnosis | Action |
    | ------- | --------- | ------ |
    | Both scores poor, converged | Underfitting | Bigger model, better features, train longer |
    | Train good, val much worse | Overfitting | Regularize, augment, get more data |
    | Both good, small gap | Healthy | Ship it |
    | Val better than train | Dropout/BN artifact, or a leaky/too-easy val set | Investigate |
    | Val noisy and jumping | Val set too small, or LR too high | Enlarge val set, lower LR |
    | Loss is NaN | Exploding gradients, bad LR, or a log(0) | Clip, lower LR, check the loss |

    Being able to walk this table out loud, in order, is a common and very
    answerable interview question. Most candidates guess randomly.

    Returns:
        Keys ``diagnosis``, ``gap``, ``recommendations``.
    """
    raise NotImplementedError("Week 16")


def overfit_single_batch(
    model_factory: Callable[[], object], X: Array, y: Array, max_epochs: int = 500
) -> dict[str, object]:
    """Sanity check: can the model memorize 8 examples?

    **Run this before every real training run for the rest of the course.**

    A correct model with a correct training loop drives loss to ~0 on a tiny
    batch within a few hundred steps. If it cannot, the bug is in your code, not
    your hyperparameters, and no amount of learning-rate tuning will save you.
    This one check catches wrong loss reductions, detached gradients, label
    misalignment, and shuffled targets — the four bugs that otherwise cost a day
    each.

    Returns:
        Keys ``converged``, ``final_loss``, ``epochs_needed``, ``diagnosis``.
    """
    raise NotImplementedError("Week 16")


def generalization_gap(train_scores: list[float], val_scores: list[float]) -> dict[str, float]:
    """Track the train/validation gap over training.

    Returns:
        Keys ``final_gap``, ``max_gap``, ``epoch_of_divergence`` — the epoch
        where the gap starts growing monotonically, which is usually the epoch
        early stopping should have fired.
    """
    raise NotImplementedError("Week 16")


def ablation_study(
    base_config: dict,
    variations: dict[str, dict],
    train_fn: Callable[[dict], dict[str, float]],
) -> object:
    """Run one configuration per variation and tabulate the deltas.

    The Week 16 deliverable: a table of what each regularizer bought on the same
    overfitting problem.

    | Config | Train acc | Val acc | Gap |
    | ------ | --------- | ------- | --- |
    | Baseline (overfit) | 1.000 | 0.71 | 0.29 |
    | + L2 | ... | ... | ... |
    | + Dropout | ... | ... | ... |
    | + Early stopping | ... | ... | ... |
    | + All | ... | ... | ... |

    A table like this in a README is worth more than three paragraphs of prose,
    and building the habit now means Month 8's architecture ablations and
    Month 17's research ablations are routine.

    Returns:
        A pandas DataFrame, sorted by validation score.
    """
    raise NotImplementedError("Week 16")
