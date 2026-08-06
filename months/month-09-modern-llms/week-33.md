# Week 33: Modern Architecture: RoPE, RMSNorm, SwiGLU, GQA

## Outcome

By Sunday your Month 8 transformer has been updated to modern components, and you can explain the motivation for each change.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"What changed between GPT-2 and Llama?" is a question that immediately
separates people who track the field from people who learned transformers once.

Each change has a clean motivation. RoPE encodes relative position through
rotation, which generalizes to longer sequences than learned absolute embeddings.
RMSNorm drops the mean-centering step because it turns out not to matter, saving
compute. SwiGLU gives better quality per parameter than a plain FFN. GQA shrinks
the KV cache, which is the binding constraint on long-context serving.

The GQA answer in particular connects back to Week 32's memory calculation, which
makes it a satisfying question to be asked.

## Time Budget: 15-20 Hours

- Theory: 4 hours
- Coding: 7 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Positional encoding, revisited**
   1. Absolute learned embeddings and their length limit
   2. RoPE: rotating query and key vectors by position
   3. Why rotation encodes *relative* position in the dot product
   4. Length extrapolation, and why RoPE extends further
2. **Normalization**
   1. RMSNorm: drop the mean subtraction
   2. Why it works, and what it saves
   3. Where the norm goes in a modern block
3. **Feed-forward variants**
   1. SwiGLU: a gated linear unit with a Swish activation
   2. The 2/3 width adjustment to keep parameters constant
   3. Why gating helps
4. **Attention variants**
   1. Multi-query attention: one KV head, big cache saving, some quality cost
   2. Grouped-query attention: the compromise that won
   3. Sliding window attention
   4. Mixture of experts, briefly
5. **Putting it together**
   1. A modern block, end to end
   2. What Llama, Mistral, and Qwen each do differently

## Required Free Resources

- **Primary:** 'Llama 2' — https://arxiv.org/abs/2307.09288 — the architecture section
- **Primary:** 'RoFormer' (RoPE) — https://arxiv.org/abs/2104.09864 — read sections 3-4
- 'GQA: Training Generalized Multi-Query Transformer Models' — https://arxiv.org/abs/2305.13245
- 'Root Mean Square Layer Normalization' — https://arxiv.org/abs/1910.07467
- 'GLU Variants Improve Transformer' — https://arxiv.org/abs/2002.05202 — the SwiGLU paper, and refreshingly honest about not knowing why
- Eleuther's blog on RoPE — the clearest explanation of the rotation intuition

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=33
```

1. **Implement RoPE** (2h) — Rotate Q and K by position. Verify the dot product depends only on relative distance.
2. **Test length extrapolation** (1h) — Train at length 128, evaluate at 256. Compare RoPE against learned embeddings.
3. **Implement RMSNorm** (45m) — Then measure the speed difference against LayerNorm.
4. **Implement SwiGLU** (1h) — With the 2/3 width adjustment to hold parameters constant.
5. **Implement GQA** (1.5h) — Verify the KV cache shrinks by the grouping factor.
6. **The modern block** (1h) — RMSNorm + RoPE attention + SwiGLU FFN, pre-norm.
7. **Component ablation** (2h) — Swap one component at a time against the Month 8 baseline. Same seed, same data.

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
o
d
e
r
n
_
b
l
o
c
k
s
.
p
y
```

## Tests To Write

Add: a test that RoPE attention scores depend only on relative position (shift both query and key by k and the score is unchanged); and a test that GQA's KV cache is smaller than MHA's by exactly the grouping factor.

## Portfolio Artifact

`src/modern_blocks.py` and the component ablation table — what each modern component bought over the Month 8 baseline.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *What changed between GPT-2 and Llama, and why each?* Then: *Why did grouped-query attention win over multi-query?* Connect the second answer back to your Week 32 memory calculation.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement RoPE scaling (linear interpolation and NTK-aware) and test context extension: train at 512, evaluate at 2048 with and without scaling. This is a technique actively used to extend production models' context windows, and measuring the quality degradation yourself makes the tradeoff concrete.
