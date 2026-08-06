# Month 08 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 29 — Attention

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 29.1 | Derive attention on paper | 1h | Hard |
| 29.2 | `scaled_dot_product_attention` | 1.5h | Medium |
| 29.3 | Verify against `F.scaled_dot_product_attention` | 30m | Easy |
| 29.4 | `causal_mask` | 45m | Medium |
| 29.5 | The causality test | 1h | Hard |
| 29.6 | `padding_mask` and mask combination | 1h | Medium |
| 29.7 | Gradient-check attention | 1h | Medium |
| 29.8 | The saturation demonstration | 1h | Medium |
| 29.9 | `attention_entropy` | 45m | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 29.E1 | Implement a memory-efficient chunked attention (FlashAttention's idea, simplified) | 3h | High — makes the memory argument concrete |
| 29.E2 | Measure actual attention memory against sequence length; plot the quadratic | 1.5h | High — the constraint, quantified |
| 29.E3 | Implement relative position bias (T5-style) and compare | 2h | Medium |

## Week 30 — Transformer Blocks

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 30.1 | `MultiHeadAttention` shape choreography | 2h | Hard |
| 30.2 | Gradient-check MHA | 45m | Medium |
| 30.3 | Verify heads learn different patterns | 1h | Medium |
| 30.4 | The feed-forward block | 45m | Easy |
| 30.5 | Count parameters by component | 45m | Easy |
| 30.6 | The full block, pre-norm | 1.5h | Medium |
| 30.7 | Post-norm variant | 1h | Hard |
| 30.8 | Positional embeddings | 1h | Medium |
| 30.9 | Residual scaling initialization | 45m | Medium |
| 30.10 | `visualize_attention` | 1h | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 30.E1 | Implement cross-attention and a minimal encoder-decoder | 2.5h | Medium — useful context, rarely asked directly |
| 30.E2 | Measure residual stream norm growth across depth for pre- and post-norm | 1.5h | High — the mechanism behind the pre-norm answer |
| 30.E3 | Implement attention head pruning based on entropy; measure quality loss | 2.5h | High — interesting result, good README content |

## Week 31 — Encoder Models: BERT Concepts

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 31.1 | Implement the MLM masking scheme | 1h | Medium |
| 31.2 | Train a tiny encoder with MLM | 2h | Hard |
| 31.3 | Compare MLM and next-token loss curves | 1h | Medium |
| 31.4 | Fine-tune a small pretrained BERT | 1.5h | Medium |
| 31.5 | Pooling comparison | 1h | Medium |
| 31.6 | Cross-encoder versus bi-encoder | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 31.E1 | Implement ELECTRA's replaced-token-detection objective | 3h | Medium — a more sample-efficient alternative |
| 31.E2 | Probe what BERT layers encode (syntactic vs semantic) | 2.5h | High — good interpretability practice for Month 16 |
| 31.E3 | Distill a small encoder from a larger one | 3h | High — previews Month 12 |

## Week 32 — Decoder Models: Mini-GPT

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 32.1 | `GPTConfig` and the model skeleton | 1h | Easy |
| 32.2 | Assemble the full model | 2h | Medium |
| 32.3 | Verify the initial loss is ln(V) | 30m | Easy |
| 32.4 | Train on a small corpus | 2h | Medium |
| 32.5 | Greedy generation | 1h | Easy |
| 32.6 | KV caching | 2h | Hard |
| 32.7 | `kv_cache_memory` | 45m | Medium |
| 32.8 | `num_parameters` breakdown | 45m | Easy |
| 32.9 | **The ablation study** | 3h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 32.E1 | Implement speculative decoding with a smaller draft model | 3h | High — a real inference optimization, and a good interview topic |
| 32.E2 | Scaling study: train at 4 model sizes and plot loss vs parameters | 3h | High — previews Month 9 and Month 16 |
| 32.E3 | Visualize attention patterns across layers on trained weights | 2h | High — the figures show recognizable structure and make a great README |

---

## If You Finish Early

Priority: Week 32's scaling study (previews Months 9 and 16), Week 30's residual-norm measurement (the mechanism behind your pre-norm answer), Week 29's chunked attention (makes the memory argument physical). This is the month where extra hours pay the highest return in the whole course.
