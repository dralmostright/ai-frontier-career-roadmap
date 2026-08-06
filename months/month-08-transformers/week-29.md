# Week 29: Attention

## Outcome

By Sunday you can derive and implement scaled dot-product attention with causal and padding masks, and explain the √d scaling from first principles.

Concretely: the week-29 blocks in `test_llm_labs.py` pass, including `test_changing_a_future_token_cannot_change_the_present`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The single most examined topic in LLM interviews.**

The equation is one line. The understanding is in the details: why the scaling,
why the softmax, what the mask does mechanically, and what each of Q, K, V means.

The √d derivation is the one to have cold. The dot product of two d-dimensional
vectors with unit-variance independent components has variance d. Without
scaling, softmax inputs grow with dimension, the softmax saturates toward one-hot,
and its gradient goes to zero. Dividing by √d restores unit variance and keeps
the softmax in its useful range.

Being able to produce that argument — rather than saying "it stabilizes training"
— is the difference between a 6 and a 9 on this question.

## Time Budget: 15-20 Hours

- Theory: 4 hours
- Coding: 8 hours
- Project: 2.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The attention equation**
   1. softmax(QK^T / sqrt(d_k)) V
   2. Reading it as a soft dictionary lookup
   3. What Q, K, and V each represent
   4. Self-attention versus cross-attention
2. **The scaling factor**
   1. Variance of a dot product grows with d
   2. Softmax saturation and the vanishing gradient that follows
   3. Why sqrt(d) and not d
3. **Masking**
   1. Causal masking: -inf above the diagonal, before the softmax
   2. Padding masks, and combining them
   3. Why a large negative number rather than literal -inf
   4. What happens without a causal mask in a language model
4. **Complexity**
   1. O(n^2 d) time and O(n^2) memory in sequence length
   2. Why this is the fundamental constraint on context length
   3. FlashAttention's contribution: same math, better memory access
5. **Attention patterns**
   1. What trained heads actually learn
   2. Attention entropy as a diagnostic
   3. Why a uniform-attention head is doing nothing

## Required Free Resources

- **Primary:** 'Attention Is All You Need' — https://arxiv.org/abs/1706.03762 — read it properly this week. You will read it three more times.
- **Primary:** Jay Alammar, 'The Illustrated Transformer' — https://jalammar.github.io/illustrated-transformer/ — read this *before* the paper
- **Primary:** The Annotated Transformer — https://nlp.seas.harvard.edu/annotated-transformer/ — line-by-line implementation. Read after your own attempt.
- 3Blue1Brown, 'Attention in transformers' — https://www.3blue1brown.com/topics/neural-networks — the best visual treatment
- 'FlashAttention' — https://arxiv.org/abs/2205.14135 — read the introduction for the memory argument

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=29
```

1. **Derive attention on paper** (1h) — Including the variance argument for sqrt(d). Before coding.
2. **`scaled_dot_product_attention`** (1.5h) — Shapes in comments. Return the weights too.
3. **Verify against `F.scaled_dot_product_attention`** (30m) — To 1e-5.
4. **`causal_mask`** (45m) — Register as a buffer, not a parameter.
5. **The causality test** (1h) — Perturb a future token; earlier outputs must not change. The strongest test of correctness.
6. **`padding_mask` and mask combination** (1h) — Logical AND. Handle the fully-masked row without NaN.
7. **Gradient-check attention** (1h) — Using Week 14's tooling. Do this now, not in Week 32.
8. **The saturation demonstration** (1h) — Attention with and without scaling at d=512. Show the softmax saturating.
9. **`attention_entropy`** (45m) — The diagnostic for whether a head is doing anything.

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
a
t
t
e
n
t
i
o
n
.
p
y
```

## Tests To Write

`tests/test_llm_labs.py` week-29 blocks. `test_changing_a_future_token_cannot_change_the_present` is the one that proves causality.

## Portfolio Artifact

`src/attention.py`, gradient-checked, plus a notebook showing the softmax saturation with and without scaling.

## Interview Drills

**Coding (45 min).** Two problems. Keep them easy this week; save the energy.

**ML theory (40 min).** **The big one.** Whiteboard, recorded: *Derive scaled dot-product attention. Why divide by √d? What does the causal mask do, mechanically?* Practice until you can do the full derivation in six minutes without hesitating. This is the highest-value drill in the course.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement chunked attention that never materializes the full n×n matrix — process the sequence in blocks, maintaining running softmax statistics. This is FlashAttention's core idea simplified, and implementing it makes the memory argument something you have felt rather than read. Measure peak memory against the naive version at sequence length 4096.
