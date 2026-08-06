"""LoRA and QLoRA — Week 46.

Freeze the pretrained weights; learn a low-rank update alongside them.

    h = W0 @ x + (B @ A) @ x * (alpha / r)

where A is (r, d_in), B is (d_out, r), and r is small — typically 8 to 64.

The parameter arithmetic, which you should be able to do in your head:
a 4096x4096 layer has 16.7M parameters. At rank 8, LoRA adds
2 * 8 * 4096 = 65,536 — about 0.4%. That is the entire pitch.

Two details that matter and are often asked:

- **A is initialized random, B is initialized to zero.** So B@A starts at
  zero and the tuned model begins exactly at the base model. Initializing
  both randomly perturbs the model before training and loses the pretrained
  behavior you are trying to preserve.
- **The adapter can be merged into W0 after training**, giving zero inference
  overhead. Unmerged, you pay an extra small matmul per layer. This is why
  LoRA is a *deployment* win, not just a training one.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import Tensor, nn


class LoRALayer:
    """Low-rank adapter wrapping a frozen linear layer."""

    def __init__(
        self,
        base_layer: nn.Module,
        rank: int = 8,
        alpha: float = 16.0,
        dropout: float = 0.0,
    ) -> None:
        raise NotImplementedError("Week 46")

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError("Week 46")

    def merge(self) -> None:
        """Fold B@A into the base weight. Idempotent; guard against double-merge."""
        raise NotImplementedError("Week 46")

    def unmerge(self) -> None:
        raise NotImplementedError("Week 46")


def apply_lora(
    model: nn.Module,
    target_modules: list[str] | None = None,
    rank: int = 8,
    alpha: float = 16.0,
) -> dict[str, Any]:
    """Wrap matching modules with adapters and freeze everything else.

    Which modules to target is a real decision. The original paper adapted
    only the attention query and value projections. Later work found adapting
    all linear layers, including the feed-forward blocks, works better at a
    modest parameter cost. Run both as an ablation and report it — that
    comparison is worth more than picking the popular answer.

    Returns:
        Keys ``trainable_params``, ``total_params``, ``trainable_percent``,
        ``adapted_modules``.
    """
    raise NotImplementedError("Week 46")


def lora_parameter_count(d_in: int, d_out: int, rank: int) -> dict[str, int]:
    """r*(d_in + d_out) versus d_in*d_out.

    The Week 46 interview question, and you should be able to compute it
    without a calculator.
    """
    raise NotImplementedError("Week 46")


def quantize_4bit(weight: Tensor, block_size: int = 64) -> dict[str, Any]:
    """NF4 quantization — the Q in QLoRA.

    Base weights in 4 bits, adapters in bf16. A 7B model drops from ~14GB in
    fp16 to under 4GB, which is what makes fine-tuning viable on a single
    consumer GPU.

    The detail worth knowing: NF4 is *information-theoretically optimal for
    normally-distributed weights* — the quantization levels are placed at
    quantiles of a normal distribution rather than uniformly. Neural network
    weights are approximately normal, so this beats uniform quantization at
    the same bit width.

    Double quantization (quantizing the quantization constants) saves a
    further ~0.4 bits per parameter.
    """
    raise NotImplementedError("Week 46")


def save_adapter(model: nn.Module, path: Path) -> dict[str, Any]:
    """Save only the adapter weights.

    Megabytes instead of gigabytes. This is the operational advantage that
    matters in production: one base model in memory, many task-specific
    adapters swapped in per request. Worth raising in a system design
    interview as a multi-tenant serving strategy.
    """
    raise NotImplementedError("Week 46")


def rank_ablation(
    base_model: Any, dataset: Any, ranks: tuple[int, ...] = (1, 2, 4, 8, 16, 32, 64)
) -> Any:
    """Sweep rank; plot quality against trainable parameters.

    The Week 46 deliverable and a genuinely interesting result: quality
    typically saturates around rank 8-16 for most tasks, so higher ranks buy
    parameters and not performance. Finding your own saturation point is a
    real, reportable finding.
    """
    raise NotImplementedError("Week 46")
