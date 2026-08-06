# Week 32: Decoder Models: Mini-GPT

## Outcome

By Sunday you have a complete decoder-only transformer that trains, generates coherent text, and caches keys and values — and an ablation table measuring what each component contributes.

Concretely: week-32 tests pass, including `test_initial_loss_is_ln_vocab_size` and `test_kv_cache_produces_identical_output`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

This is the artifact that gets you past ML depth screens.

The KV caching material is directly examined: "explain KV caching and compute its
memory for a 7B model at 8k context" is a standard question, and the answer —
several gigabytes for a single sequence — is what motivates PagedAttention,
grouped-query attention, and most of modern inference infrastructure.

The ablation study is the differentiator. Anyone can say "transformers have
residual connections." Very few can say "I removed them and validation loss went
from 3.1 to 5.8, and here is the plot." That table is the thing that makes your
Month 8 README worth opening.

The no-causal-mask ablation is the most instructive: loss collapses to near zero
because the model reads the answer, which makes "why do we mask?" viscerally
obvious in a way no explanation achieves.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 9 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Assembling the model**
   1. Token embedding, positional encoding, N blocks, final norm, output projection
   2. Weight tying, and the parameter saving
   3. Initialization, including residual scaling
2. **Training a language model**
   1. Next-token prediction and the shifted targets
   2. The ln(vocab_size) initial loss check
   3. Why the loss is per-token, not per-sequence
3. **Generation**
   1. Autoregressive decoding
   2. Cropping to block_size
   3. Why naive generation is O(n^2)
4. **KV caching**
   1. What is cached and why it is valid
   2. The memory formula: 2 * layers * kv_heads * head_dim * seq * batch * dtype
   3. Prefill versus decode: compute-bound versus memory-bound
   4. Why long context is expensive
5. **Ablation methodology**
   1. Change one thing, hold everything else fixed
   2. Same seed, same data, same steps
   3. Reporting honestly, including surprises

## Required Free Resources

- **Primary:** Karpathy, 'Let's build GPT: from scratch, in code, spelled out' — https://www.youtube.com/watch?v=kCc8FmEb1nY — **watch after your own attempt**
- **Primary:** nanoGPT — https://github.com/karpathy/nanoGPT — read after yours works, then diff the designs
- 'Language Models are Unsupervised Multitask Learners' (GPT-2) — https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- 'Efficient Memory Management for LLM Serving' (vLLM/PagedAttention) — https://arxiv.org/abs/2309.06180 — read the motivation section

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=32
```

1. **`GPTConfig` and the model skeleton** (1h) — Sensible ratios: d_ff = 4*d_model, head_dim = 64.
2. **Assemble the full model** (2h) — Embeddings, blocks, final norm, output projection, weight tying.
3. **Verify the initial loss is ln(V)** (30m) — **Before training anything.** If it is wrong, stop and debug.
4. **Train on a small corpus** (2h) — Tiny Shakespeare or your own text. Watch it learn.
5. **Greedy generation** (1h) — Then observe the repetition. This motivates Week 35.
6. **KV caching** (2h) — Verify identical output with and without, then measure the speedup.
7. **`kv_cache_memory`** (45m) — Compute for a 7B model at 8k context. Memorize the order of magnitude.
8. **`num_parameters` breakdown** (45m) — By component. The FFN dominance surprises people.
9. ****The ablation study**** (3h) — Seven configurations, same seed, same steps. The month's deliverable.

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
m
i
n
i
_
g
p
t
.
p
y


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
c
o
n
f
i
g
s
/
m
i
n
i
_
g
p
t
_
t
i
n
y
.
y
a
m
l
```

## Tests To Write

Week-32 blocks. `test_initial_loss_is_ln_vocab_size` and `test_kv_cache_produces_identical_output` are the two that matter most.

## Portfolio Artifact

The Month 8 capstone. See `capstone.md`. The ablation table and the attention visualizations are the artifacts.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (40 min).** Recorded: *Explain KV caching. Compute its memory for a 7B model at 8k context.* Then: *Walk me through your ablation results — what breaks without each component?* The second question is one you can now answer with data, which almost nobody can.

**Behavioral (15 min).** Draft story #8: learning something hard, fast. Month 8 is the material.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement speculative decoding: use a small fast model to draft several tokens, then verify them in one forward pass of the large model. Accepted drafts are free; rejected ones cost nothing extra. It is a genuinely clever technique, it is deployed in production systems, and being able to explain the acceptance criterion is a strong signal that you follow inference research.
