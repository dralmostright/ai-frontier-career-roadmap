# Month 08: Transformers From First Principles

**Weeks 29-32 · Phase 3: NLP and Transformers · Lab: `bootstrap/llm-labs/`**

---

## The Month In One Sentence

Build a transformer component by component, then ablate each component to see what it was doing.

## Why This Month Exists

**The most important month in the course for interview outcomes.**

"Derive attention" and "explain what breaks without layer norm" are asked in
essentially every frontier lab loop. They are asked because they cleanly separate
people who have implemented a transformer from people who have read about one,
and that distinction is very hard to fake under follow-up questions.

You are going to implement one piece at a time, gradient-check each piece, and
then run an ablation study that measures what each component contributes. That
ablation table is worth more than the model — it turns "I know transformers have
residual connections" into "removing residual connections raised validation loss
from 3.1 to 5.8 and the model stopped improving after epoch 2."

Budget extra hours this month. If any month deserves 20 hours a week rather than
15, it is this one.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 29 | Attention | `attention.py` — scaled dot-product attention, gradient-checked |
| 30 | Transformer Blocks | `transformer_block.py` — MHA, FFN, residuals, norm |
| 31 | Encoder Models: BERT Concepts | `bert_finetune.py` — a fine-tuned encoder classifier |
| 32 | Decoder Models: Mini-GPT | `mini_gpt.py` — a working GPT with KV caching, plus the ablation study |

**Capstone:** Mini-GPT — a decoder-only transformer built from scratch, trained, and ablated component by component.

## The Through-Lines

**Attention is a similarity computation.** Week 1's dot product, scaled and
softmaxed. The √d factor exists because dot products of d-dimensional vectors
have variance proportional to d.

**Residual connections, again.** The Week 22 gradient argument applies unchanged.

**Layer norm over batch norm.** The Week 16 reasoning — batch statistics are
unusable for variable-length sequences and batch size 1 — is why.

**Gradient checking is the safety net.** Finding an attention bug in Week 29
takes ten minutes. Finding it in Week 32 takes three days.

## Time and Compute

15-20 hours per week. A GPU is strongly recommended from Week 32. Colab Pro is the cheapest path. Keep models under 20M parameters; the goal is understanding and clean ablations, not scale.

## Files

```text
month-08-transformers/
  README.md      you are here
  week-29.md     attention
  week-30.md     transformer blocks
  week-31.md     encoder models: bert concepts
  week-32.md     decoder models: mini-gpt
  capstone.md    mini-gpt
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Weeks 29 and 30.** Do not compress either. Week 31 (encoders) is the compressible one if you must.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Using `-inf` for the mask | NaN when a row is fully masked | Use a large negative number. Padding creates fully-masked rows. |
| Forgetting `.contiguous()` after transpose | Runtime error in the reshape | Understand why: transpose changes strides without moving memory. |
| Skipping the output projection | Heads never mix | Multi-head degenerates into h independent attentions. |
| Not checking the initial loss | Hours lost | Untrained loss must be ln(vocab_size). ~10.8 for 50k. |
| Copying nanoGPT | You learn nothing | Build yours first, then read his and diff. |
| No causal mask | Loss collapses to near zero | The model reads the answer. It is a good ablation and a terrible bug. |

## Advancement

Before Month 9, you should be able to, without notes:

- [ ] Derive scaled dot-product attention cold, including the √d justification
- [ ] Implement multi-head attention from memory
- [ ] Explain why pre-norm beat post-norm
- [ ] Explain KV caching and compute its memory for a given model
- [ ] Explain what breaks without each component, from your own ablations
- [ ] Point at a working Mini-GPT with an ablation table in the README

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 9 — Modern LLMs. Architecture updates, data curation, and your first real training run.
