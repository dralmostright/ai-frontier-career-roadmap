"""Mini-GPT — Week 32. The Month 8 capstone.

A complete decoder-only transformer. Every component implemented, every
architectural choice explainable.

Build order, each step verified before the next:

1. Token embedding + positional encoding
2. N transformer blocks (from `transformer_block.py`)
3. Final layer norm + output projection
4. Weight tying between input embedding and output projection
5. Generation: greedy first, then sampling
6. KV caching, and measure the speedup

Reference: Karpathy's nanoGPT. **Write yours first, then read his.** Reading
it first turns this into transcription, and transcription teaches nothing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import Tensor


@dataclass
class GPTConfig:
    """Model configuration.

    Sensible ratios, worth knowing because they recur across every published
    model: d_ff = 4 * d_model, head_dim = d_model / n_heads (usually 64),
    and vocabulary somewhere between 32k and 100k.
    """

    vocab_size: int = 50257
    block_size: int = 256
    n_layer: int = 6
    n_head: int = 6
    d_model: int = 384
    d_ff: int | None = None
    dropout: float = 0.1
    bias: bool = True
    tie_weights: bool = True

    def __post_init__(self) -> None:
        raise NotImplementedError("Week 32")


class MiniGPT:
    """A decoder-only transformer.

    Design decisions to be able to defend, because your README must and an
    interviewer will ask:

    - **Weight tying.** Sharing the input embedding with the output
      projection saves vocab_size x d_model parameters — often 30% of a small
      model — and usually improves quality. The intuition: the mapping from
      token to vector and from vector to token logit are the same relationship
      in two directions.
    - **Pre-norm.** LayerNorm before the sublayer rather than after. Leaves a
      clean residual path from input to output, which is what makes deep
      transformers trainable without an elaborate warmup schedule.
    - **Final layer norm.** After the last block, before the output
      projection. Skipping it lets the residual stream's scale drift.
    - **Residual projection scaling.** Initialize output projections with std
      scaled by 1/sqrt(2 * n_layer). Without it the residual stream's variance
      grows with depth.
    """

    def __init__(self, config: GPTConfig) -> None:
        raise NotImplementedError("Week 32")

    def forward(self, idx: Tensor, targets: Tensor | None = None) -> tuple[Tensor, Tensor | None]:
        """Forward pass.

        Args:
            idx: Token indices, (batch, seq_len).
            targets: Next-token targets for training loss.

        Returns:
            (logits, loss). Loss is None at inference.

        Sanity check before anything else: an untrained model's loss must be
        approximately ln(vocab_size). About 10.8 for a 50k vocabulary. If your
        first loss is 3.0, your targets are misaligned; if it is 40, your
        initialization is broken. Check this before touching a hyperparameter.
        """
        raise NotImplementedError("Week 32")

    @property
    def num_parameters(self) -> dict[str, int]:
        """Parameter count, broken down by component.

        The breakdown surprises people and is worth being able to quote:
        in a typical transformer the feed-forward blocks hold roughly two
        thirds of the parameters, and attention only about a third. The
        embedding table dominates in small models.
        """
        raise NotImplementedError("Week 32")

    def generate(
        self,
        idx: Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: int | None = None,
        top_p: float | None = None,
        use_cache: bool = True,
    ) -> Tensor:
        """Autoregressive generation.

        Without a cache this is O(n²) in sequence length, because every new
        token re-runs attention over the whole prefix. With a cache it is
        O(n). Implement both, measure the difference, and put the number in
        your README — it is the most concrete demonstration of why KV caching
        exists.

        Remember to crop the context to `block_size`; the model has no
        positional embeddings beyond it and will produce garbage rather than
        an error.
        """
        raise NotImplementedError("Week 32")

    def estimate_mfu(self, tokens_per_second: float, peak_flops: float) -> float:
        """Model FLOPs Utilization: what fraction of peak compute you achieve.

        Roughly 6 x parameters x tokens FLOPs for a training step (2 for the
        forward pass, 4 for the backward). Well-optimized large-scale training
        reaches 40-50% MFU; a naive loop reaches 10-15%.

        Reporting MFU in your Month 9 training report is a strong signal —
        almost nobody outside of frontier labs measures it, and it shows you
        think about efficiency as a first-class concern.
        """
        raise NotImplementedError("Week 35")


def ablation_study(base_config: GPTConfig, dataset: Any, epochs: int = 5) -> Any:
    """**The Month 8 capstone deliverable.**

    Train the same model with one component removed at a time:

    - no positional encoding
    - no residual connections
    - no layer norm
    - post-norm instead of pre-norm
    - single attention head
    - no causal mask
    - no sqrt(d) scaling

    Report validation loss for each. The no-causal-mask row is the most
    instructive: loss drops to near zero because the model reads the answer,
    which makes "why do we mask?" viscerally obvious.

    Returns:
        A DataFrame with the configuration, validation loss, and delta.
    """
    raise NotImplementedError("Week 32")
