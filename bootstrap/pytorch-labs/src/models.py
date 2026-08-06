"""nn.Module patterns — Week 18.

How to structure models so they stay debuggable at depth, and the
initialization and parameter-counting habits worth forming now.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import nn


class MLP:
    """Configurable multi-layer perceptron. The PyTorch port of Week 13.

    Compare the line count against `ml-from-scratch/src/neural_net.py`. The
    framework saves you roughly 400 lines, and you now know exactly which
    400 lines they are.
    """

    def __init__(
        self,
        layer_sizes: list[int],
        activation: str = "relu",
        dropout: float = 0.0,
        batch_norm: bool = False,
    ) -> None:
        raise NotImplementedError("Week 18")

    def forward(self, x: Any) -> Any:
        raise NotImplementedError("Week 18")


def initialize_weights(module: nn.Module, scheme: str = "he") -> None:
    """Apply an initialization scheme recursively.

    Use `module.apply()`. The rules: He for ReLU-family activations, Xavier
    for tanh and sigmoid, zeros for biases, and leave normalization layers at
    their defaults (weight 1, bias 0).

    In Week 30 you will add one more: scale the residual-projection weights
    by 1/sqrt(2*n_layers). Without it, deep transformer residual streams grow
    without bound and training destabilizes.
    """
    raise NotImplementedError("Week 18")


def count_parameters(model: nn.Module, trainable_only: bool = True) -> dict[str, int]:
    """Parameter counts, total and per named submodule.

    Print this for every model you build. Two payoffs: you catch a layer that
    is accidentally 100x larger than intended, and you develop a feel for
    where parameters actually live. In a transformer the answer surprises
    people — the feed-forward blocks hold roughly two thirds, not attention.
    """
    raise NotImplementedError("Week 18")


def model_summary(model: nn.Module, input_shape: tuple[int, ...]) -> str:
    """Layer-by-layer output shapes, parameter counts, and memory.

    Implement with forward hooks. Writing this is the exercise that makes
    hooks click, and you will use hooks again in Week 52 for profiling and
    in Week 62 for activation inspection.
    """
    raise NotImplementedError("Week 18")


def freeze_layers(model: nn.Module, patterns: list[str]) -> int:
    """Set `requires_grad=False` on parameters matching name patterns.

    Two gotchas worth knowing before Week 23:

    - Frozen parameters must still be excluded from the optimizer, or some
      optimizers will apply weight decay to them anyway.
    - Freezing a BatchNorm layer's parameters does not freeze its running
      statistics. You must also call `.eval()` on it, or it keeps adapting
      to your new data distribution.

    Returns:
        Number of parameters frozen.
    """
    raise NotImplementedError("Week 23")
