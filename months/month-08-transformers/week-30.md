# Week 30: Transformer Blocks

## Outcome

By Sunday you can implement multi-head attention and a complete transformer block, and justify pre-norm over post-norm.

Concretely: the week-30 blocks pass, and every component is gradient-checked.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Multi-head attention's shape choreography is where an hour disappears, and
getting it right is the practical skill. The conceptual content is why heads
exist at all: one head produces one attention pattern, and language needs
several simultaneously — syntactic dependency, coreference, positional locality.

The pre-norm versus post-norm question is a good discriminator. The original
paper used post-norm and needed careful warmup; pre-norm leaves a clean residual
path from input to output and is what made very deep transformers trainable
without elaborate schedules. Everything modern uses pre-norm.

The other detail worth knowing: the FFN holds roughly two thirds of a
transformer's parameters, not attention. That surprises people and it is a good
sign you have counted.

## Time Budget: 15-20 Hours

- Theory: 3.5 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Multi-head attention**
   1. Splitting d into h heads of d/h
   2. The reshape and transpose choreography
   3. Why the output projection is required, not decorative
   4. Why h heads of d/h costs the same as one head of d
2. **The feed-forward block**
   1. Two linear layers with an activation, expansion factor 4
   2. Why it holds most of the parameters
   3. GELU, and later SwiGLU
3. **Residuals and normalization**
   1. The residual stream as the model's working memory
   2. Pre-norm versus post-norm, and why pre-norm won
   3. LayerNorm over BatchNorm for sequences
   4. Residual projection scaling by 1/sqrt(2*n_layers)
4. **Positional information**
   1. Attention is permutation-invariant without it
   2. Learned versus sinusoidal embeddings
   3. Why RoPE replaced both (Week 33)
5. **Encoder versus decoder blocks**
   1. Bidirectional versus causal attention
   2. Cross-attention in encoder-decoder models

## Required Free Resources

- **Primary:** The Annotated Transformer — https://nlp.seas.harvard.edu/annotated-transformer/
- **Primary:** 'On Layer Normalization in the Transformer Architecture' — https://arxiv.org/abs/2002.04745 — the pre-norm paper, and the source of your interview answer
- d2l.ai ch. 11 (attention and transformers) — https://d2l.ai/
- Anthropic, 'A Mathematical Framework for Transformer Circuits' — https://transformer-circuits.pub/2021/framework/index.html — read the residual stream section; it is the best framing available

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=30
```

1. **`MultiHeadAttention` shape choreography** (2h) — Write every shape in a comment. This is where the hour goes.
2. **Gradient-check MHA** (45m) — Immediately.
3. **Verify heads learn different patterns** (1h) — Compare per-head attention weights. If they are identical, something is wrong.
4. **The feed-forward block** (45m) — Expansion 4, GELU.
5. **Count parameters by component** (45m) — Confirm the FFN holds about two thirds.
6. **The full block, pre-norm** (1.5h) — Residual, norm, attention, residual, norm, FFN.
7. **Post-norm variant** (1h) — Then train both at depth 12 and compare stability.
8. **Positional embeddings** (1h) — Learned and sinusoidal. Then remove them and show the model becomes permutation-invariant.
9. **Residual scaling initialization** (45m) — 1/sqrt(2*n_layers). Measure residual stream variance with and without.
10. **`visualize_attention`** (1h) — The heatmap. It goes in the capstone README.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
l
l
m
-
l
a
b
s
/
s
r
c
/
t
r
a
n
s
f
o
r
m
e
r
_
b
l
o
c
k
.
p
y
```

## Tests To Write

Week-30 blocks. Add: a test that removing the output projection makes the heads' contributions non-interacting, detectable by comparing against a concatenation-only baseline.

## Portfolio Artifact

`src/transformer_block.py`, gradient-checked, plus the attention heatmap and the pre-norm/post-norm stability comparison.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *Why multi-head instead of one wide head?* Then: *Why pre-norm rather than post-norm?* Then: *Where do a transformer's parameters actually live?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Measure residual stream norm growth across depth for pre-norm and post-norm variants at 6, 12, and 24 layers. The post-norm variant's activations grow without bound; pre-norm's do not. That plot is the mechanism behind your interview answer, and producing it yourself makes the answer specific rather than received.
