"""Evaluation loop — Week 19."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import nn
    from torch.utils.data import DataLoader


def evaluate(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    device: str = "cpu",
    metrics: dict[str, Any] | None = None,
) -> dict[str, float]:
    """Run a full evaluation pass.

    `model.eval()` and `torch.no_grad()`, then restore `model.train()` on the
    way out. Accumulate metrics on the device and move to CPU once at the
    end — calling `.item()` per batch synchronizes and stalls the pipeline.
    """
    raise NotImplementedError("Week 19")


def predict_all(model: nn.Module, loader: DataLoader, device: str = "cpu") -> tuple:
    """Collect predictions, probabilities, and labels for the whole set.

    Feed the result straight into `ml-from-scratch/src/explainability.py`.
    The error-analysis discipline from Week 12 applies unchanged to deep
    models; only the model class differs.
    """
    raise NotImplementedError("Week 19")


def confusion_analysis(y_true: Any, y_pred: Any, class_names: list[str]) -> Any:
    """Confusion matrix plus the most-confused class pairs.

    For vision, also save a grid of the worst misclassifications as an image.
    Looking at what the model got wrong is worth more than any aggregate
    number, and images make it immediate.
    """
    raise NotImplementedError("Week 19")


def test_time_augmentation(
    model: nn.Module, loader: DataLoader, augmentations: list, device: str = "cpu"
) -> Any:
    """Average predictions over several augmented views.

    A reliable point or two of accuracy for a proportional increase in
    inference cost. Worth knowing as a technique and worth naming the cost
    when you propose it.
    """
    raise NotImplementedError("Week 19")
