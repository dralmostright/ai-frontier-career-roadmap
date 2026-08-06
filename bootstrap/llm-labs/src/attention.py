"""Attention — Week 29. The most important file in the course.

Everything reduces to one equation:

    Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

Read it as a soft dictionary lookup. Each query asks "which keys are relevant
to me?", the dot products answer with similarity scores, the softmax turns
scores into weights, and the output is a weighted average of the values.

Three things to be able to derive without notes, because they are asked
constantly:

1. **Why divide by sqrt(d_k)?** The dot product of two d-dimensional vectors
   with unit-variance components has variance d. Without scaling, the softmax
   inputs grow with dimension, the softmax saturates toward one-hot, and its
   gradient goes to zero. Dividing by sqrt(d) restores unit variance.
2. **Why multiple heads?** One head produces one attention pattern. Language
   needs several at once — syntactic dependency, coreference, positional
   locality. Splitting d into h heads of d/h costs nothing extra and buys h
   distinct patterns.
3. **What does the causal mask do?** Sets scores to -inf above the diagonal
   before the softmax, so position i cannot attend to anything after it.
   Without it, a language model reads the answer and the loss collapses to
   near zero while the model learns nothing.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import Tensor


def scaled_dot_product_attention(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    mask: Tensor | None = None,
    dropout_p: float = 0.0,
) -> tuple[Tensor, Tensor]:
    """The core operation.

    Args:
        query: (batch, ..., seq_q, d_k)
        key:   (batch, ..., seq_k, d_k)
        value: (batch, ..., seq_k, d_v)
        mask: Broadcastable boolean; True means "attend here".

    Returns:
        (output, attention_weights) with output (batch, ..., seq_q, d_v) and
        weights (batch, ..., seq_q, seq_k).

    Implementation notes that matter:

    - Use a large negative number, not literal `-inf`, for masked positions.
      A fully-masked row of `-inf` produces NaN after softmax, and fully
      masked rows happen with padding.
    - Return the weights. You will want to visualize them, and the attention
      heatmap is the best figure in your Month 8 README.
    """
    raise NotImplementedError("Week 29")


def causal_mask(seq_len: int, device: Any = None) -> Tensor:
    """Lower-triangular mask of shape (seq_len, seq_len).

    Register it as a buffer, not a parameter — it has no gradient, but it
    must move with the model across devices and be saved in the checkpoint.
    """
    raise NotImplementedError("Week 29")


def padding_mask(lengths: Tensor, max_len: int) -> Tensor:
    """Mask out padding positions from a batch of sequence lengths.

    Combine with the causal mask via logical AND. Forgetting to mask padding
    means the model attends to pad tokens and learns that they carry meaning
    — a bug that degrades quality without ever raising an error.
    """
    raise NotImplementedError("Week 29")


class MultiHeadAttention:
    """Multi-head attention — Week 30.

    The shape choreography, which is the part that takes an hour to get right:

        (B, T, d)  -> project to Q, K, V
        (B, T, d)  -> view as (B, T, h, d/h)
        (B, T, h, d/h) -> transpose to (B, h, T, d/h)
        attention over the last two dims
        (B, h, T, d/h) -> transpose back, reshape to (B, T, d)
        -> output projection

    Two details people get wrong:

    - You need `.contiguous()` before `.view()` after a transpose, or PyTorch
      raises. Understanding *why* — that transpose changes strides without
      moving memory — is a useful piece of mechanical sympathy.
    - The output projection is not decorative. Without it the heads never
      mix, and multi-head attention degenerates into h independent attentions
      glued together.
    """

    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.0, bias: bool = True) -> None:
        raise NotImplementedError("Week 30")

    def forward(
        self, x: Tensor, mask: Tensor | None = None, kv_cache: dict | None = None
    ) -> Tensor:
        raise NotImplementedError("Week 30")


class GroupedQueryAttention:
    """Grouped-query attention — Week 33.

    Multiple query heads share a smaller number of key/value heads. Purely an
    inference-memory optimization: the KV cache shrinks by the grouping factor
    with very little quality loss.

    The reasoning to be able to give: at long context, the KV cache dominates
    inference memory, and it scales with the number of KV heads. Cutting 32 KV
    heads to 8 cuts the cache by 4x. Multi-query attention (one KV head) is
    the extreme case and does cost measurable quality; GQA is the compromise
    that won.
    """

    def __init__(self, d_model: int, n_heads: int, n_kv_heads: int, dropout: float = 0.0) -> None:
        raise NotImplementedError("Week 33")

    def forward(
        self, x: Tensor, mask: Tensor | None = None, kv_cache: dict | None = None
    ) -> Tensor:
        raise NotImplementedError("Week 33")


def kv_cache_memory(
    n_layers: int,
    n_kv_heads: int,
    head_dim: int,
    seq_len: int,
    batch_size: int = 1,
    dtype_bytes: int = 2,
) -> dict[str, float]:
    """Compute KV cache size. A standard interview calculation.

        bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len * batch * dtype_bytes

    The 2 is for K and V. Work a 7B model at 8k context in fp16 and you get
    several gigabytes for a *single* sequence — which is why PagedAttention
    and GQA exist, and why serving long context is expensive.

    Returns:
        Keys ``bytes``, ``mb``, ``gb``, ``per_token_kb``.
    """
    raise NotImplementedError("Week 32")


def attention_entropy(weights: Tensor) -> Tensor:
    """Entropy of each attention distribution.

    A genuinely useful diagnostic. Low entropy means a head is looking at one
    position; high entropy means it is averaging everything and probably
    doing nothing. Heads that collapse to uniform attention are candidates for
    pruning, which is a nice observation to make in your Month 8 write-up.
    """
    raise NotImplementedError("Week 30")


def visualize_attention(weights: Tensor, tokens: list[str], layer: int = 0, head: int = 0) -> Any:
    """Heatmap of one head's attention.

    Put this figure in the Mini-GPT README. Attention maps on a trained model
    show recognizable structure — previous-token heads, delimiter heads — and
    a reader who sees that immediately believes the model works.
    """
    raise NotImplementedError("Week 30")
