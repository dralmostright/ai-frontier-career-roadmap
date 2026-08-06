"""Convolutional networks — Weeks 21-22.

Implement convolution by hand before calling `nn.Conv2d`, for the same reason
you built autodiff before using it: the layer stops being opaque.

Convolution embodies two inductive biases: locality (nearby pixels relate)
and translation equivariance (a cat is a cat anywhere in the frame). Those
priors are why CNNs beat MLPs on images with far fewer parameters, and why
ViTs need much more data to compete — they have to learn the priors instead
of being born with them. That contrast is the Week 24 interview answer.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass


def conv2d_naive(x: Any, kernel: Any, stride: int = 1, padding: int = 0) -> Any:
    """Convolution with explicit loops. Slow and clarifying.

    Write the four nested loops. Verify against `F.conv2d`. Then never do it
    this way again — but you will now know what `im2col` is optimizing and
    why convolution is a matrix multiply in disguise.
    """
    raise NotImplementedError("Week 21")


def output_shape(input_size: int, kernel: int, stride: int, padding: int, dilation: int = 1) -> int:
    """floor((input + 2*padding - dilation*(kernel-1) - 1) / stride) + 1.

    Memorize this. Shape mismatches are the most common CNN error and this
    formula resolves every one of them.
    """
    raise NotImplementedError("Week 21")


def receptive_field(layers: list[dict[str, int]]) -> dict[str, int]:
    """Compute the receptive field of a stack of conv/pool layers.

    A standard interview question with a mechanical answer. Working backward:

        rf = 1
        for layer in reversed(layers):
            rf = (rf - 1) * stride + kernel

    The insight worth stating: receptive field grows linearly with depth for
    stride-1 convolutions and exponentially when you add stride or pooling.
    That is why classification networks downsample aggressively — you need
    the final layer to see the whole image.

    Returns:
        Keys ``receptive_field``, ``effective_stride``, ``per_layer``.
    """
    raise NotImplementedError("Week 21")


class SimpleCNN:
    """Conv-BN-ReLU-Pool blocks into a classifier head. CIFAR-10 target: >80%.

    Order matters: Conv -> BN -> ReLU. Putting BN after the activation
    normalizes a non-negative distribution, which wastes half of its range.
    Also set `bias=False` on a conv immediately followed by BN — BN's shift
    parameter makes the bias redundant, and it is free parameters otherwise.
    """

    def __init__(self, num_classes: int = 10, channels: tuple[int, ...] = (32, 64, 128)) -> None:
        raise NotImplementedError("Week 21")

    def forward(self, x: Any) -> Any:
        raise NotImplementedError("Week 21")


class ResidualBlock:
    """The idea that made 50-layer networks trainable.

    out = ReLU(x + F(x))

    The gradient explanation, which is the one to give in an interview: the
    derivative of (x + F(x)) with respect to x is 1 + F'(x). The 1 is an
    identity path, so gradient reaches earlier layers undiminished no matter
    how small F' becomes. Without it, gradient is a product of many terms and
    vanishes geometrically with depth.

    Implementation detail people miss: when the block changes shape, the skip
    connection needs a 1x1 convolution to match. Otherwise the addition
    cannot happen.
    """

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1) -> None:
        raise NotImplementedError("Week 22")

    def forward(self, x: Any) -> Any:
        raise NotImplementedError("Week 22")


class ResNet:
    """Small ResNet from residual blocks. Compare depth 8 vs 20 vs 56.

    The Week 22 deliverable is the plot: plain networks get *worse* past a
    certain depth while residual networks keep improving. Reproducing that
    figure yourself is far more convincing than reading it.
    """

    def __init__(self, block_counts: tuple[int, ...] = (2, 2, 2), num_classes: int = 10) -> None:
        raise NotImplementedError("Week 22")

    def forward(self, x: Any) -> Any:
        raise NotImplementedError("Week 22")


def compare_depth_with_and_without_residuals(depths: list[int], epochs: int = 20) -> Any:
    """Train plain and residual networks at several depths; return the table.

    The Week 22 artifact. One table, and the residual-connection question is
    answered with evidence rather than assertion.
    """
    raise NotImplementedError("Week 22")
