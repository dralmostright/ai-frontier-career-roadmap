"""Transfer learning and vision transformers — Weeks 23-24."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import nn


def load_pretrained(
    name: str = "resnet18", num_classes: int = 10, freeze_backbone: bool = True
) -> nn.Module:
    """Load a pretrained backbone and replace the classifier head.

    Two things to get right, both of which silently degrade accuracy:

    - **Normalization must match pretraining.** ImageNet models expect
      ImageNet mean and std. Feeding them differently-normalized inputs works
      — it just performs worse than it should, with no error to tell you.
    - **Frozen BatchNorm needs `.eval()`.** Freezing parameters does not stop
      the running statistics from updating, and on a small new dataset those
      statistics drift badly.
    """
    raise NotImplementedError("Week 23")


def discriminative_learning_rates(
    model: nn.Module, base_lr: float, decay: float = 0.3
) -> list[dict]:
    """Lower learning rates for earlier layers.

    Early layers learn edges and textures that transfer across almost any
    vision task; late layers learn task-specific structure. Training them at
    the same rate either destroys useful early features or under-trains the
    head.

    Returns:
        Parameter groups for the optimizer.
    """
    raise NotImplementedError("Week 23")


def feature_extraction_vs_finetuning(dataset_size: int, similarity: str) -> dict[str, Any]:
    """The decision table. Week 23's interview answer, made concrete.

    | Data | Similar to pretraining | Strategy |
    | ---- | ---------------------- | -------- |
    | Small | Yes | Freeze everything, train the head only |
    | Small | No | Freeze early layers, fine-tune the last block |
    | Large | Yes | Fine-tune everything at a low LR |
    | Large | No | Fine-tune everything, or train from scratch |

    The reasoning underneath: fine-tuning has more capacity to overfit, so
    the amount you unfreeze should scale with the data you have.
    """
    raise NotImplementedError("Week 23")


class PatchEmbedding:
    """Split an image into patches and linearly project each one — Week 24.

    This is the whole trick of a ViT. A 224x224 image with 16x16 patches
    becomes a sequence of 196 tokens, and from there it is *exactly* the
    transformer you will build in Month 8. Implementing this makes the
    connection concrete: images become sequences, and everything else is
    shared.
    """

    def __init__(self, image_size: int = 224, patch_size: int = 16, embed_dim: int = 768) -> None:
        raise NotImplementedError("Week 24")

    def forward(self, x: Any) -> Any:
        raise NotImplementedError("Week 24")


class VisionTransformer:
    """A small ViT. Compare it against your CNN on the same data.

    The result you should observe, and be ready to explain: on a small
    dataset the CNN wins, sometimes decisively. The ViT has almost no
    inductive bias about images — no locality, no translation equivariance —
    so it must learn from data what the CNN gets for free. Given enough data
    that flexibility becomes an advantage; below that threshold it is a
    liability.

    "When does a ViT beat a CNN?" is a Week 24 interview question and the
    correct answer is about data scale, not architecture superiority.
    """

    def __init__(
        self,
        image_size: int = 32,
        patch_size: int = 4,
        embed_dim: int = 192,
        depth: int = 6,
        num_heads: int = 3,
        num_classes: int = 10,
    ) -> None:
        raise NotImplementedError("Week 24")

    def forward(self, x: Any) -> Any:
        raise NotImplementedError("Week 24")


def cnn_vs_vit_comparison(dataset_sizes: list[int]) -> Any:
    """Train both at several dataset sizes; plot accuracy against data volume.

    The crossover point is the Week 24 artifact and the reason your answer to
    the interview question will be specific rather than hand-wavy.
    """
    raise NotImplementedError("Week 24")
