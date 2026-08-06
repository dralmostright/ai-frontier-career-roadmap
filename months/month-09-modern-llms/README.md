# Month 09: Modern LLMs

**Weeks 33-36 · Phase 3: NLP and Transformers · Lab: `bootstrap/llm-labs/`**

---

## The Month In One Sentence

Update the Month 8 architecture to what actually ships in 2026, curate a dataset properly, and run a real training job you can report on.

## Why This Month Exists

Month 8 built a 2017 transformer. This month brings it to the present and,
more importantly, teaches you to *run and reason about a training job*.

The architecture updates — RoPE, RMSNorm, SwiGLU, grouped-query attention — are
each a small change with a clear motivation, and "what changed between GPT-2 and
Llama, and why?" is a question that separates people tracking the field from
people who learned transformers once.

The data curation week is the underrated one. Deduplication and quality filtering
routinely beat parameter scaling, and being able to show that with your own
ablation is a stronger claim than citing someone else's.

Week 36's evaluation material is where Phase 3 hands off to Phase 4. Evaluating
generations with no ground truth is the central difficulty of applied LLM work,
and everything in Months 10-17 depends on doing it honestly.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 33 | Modern Architecture: RoPE, RMSNorm, SwiGLU, GQA | `modern_blocks.py` — the Llama-era components |
| 34 | Tokenization and Data Curation | `data_curation.py` + the quality-versus-scale ablation |
| 35 | Training Small Language Models | A trained LM with full training curves, plus `sampling.py` |
| 36 | LLM Evaluation Basics | `eval_harness.py` — and a validated judge |

**Capstone:** Tiny Language Model Training Report — a small LM trained on curated data, with a report covering curation, training, evaluation, and honest failures.

## The Through-Lines

**Every architectural change has a reason.** RoPE for length generalization,
RMSNorm for cost, SwiGLU for quality per parameter, GQA for KV cache size. Learn
the motivation, not the formula.

**Data quality beats scale.** Week 34's ablation is the evidence.

**Perplexity is tokenizer-dependent.** This bites in Week 62 when you cannot
match a paper's number.

**Judges need validation.** Week 36's LLM-as-judge is only trustworthy if you
measured its agreement with human labels. That discipline carries to Weeks 39
and 44.

## Time and Compute

15-20 hours per week. A GPU is required for Week 35. Colab Pro is the practical choice. Keep the model under 50M parameters; a clean small experiment beats a sloppy large one.

## Files

```text
month-09-modern-llms/
  README.md      you are here
  week-33.md     modern architecture: rope, rmsnorm, swiglu, gqa
  week-34.md     tokenization and data curation
  week-35.md     training small language models
  week-36.md     llm evaluation basics
  capstone.md    tiny language model training report
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 35.** Your first real training run, and the source of the capstone report. Week 33 can be compressed to reading if time is short.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| No warmup | Divergence in the first 100 steps | WarmupCosine. This will happen if you skip it. |
| Not deduplicating | Memorization, and inflated validation scores | Near-duplicate detection across train and val. |
| Comparing perplexity across tokenizers | Meaningless numbers | Perplexity is tokenizer-dependent. Say so. |
| Unvalidated LLM judge | Confident, meaningless scores | Hand-label 50 examples and measure agreement. |
| Losing the training curves | Cannot report anything | Log from step zero. Month 5's tracking, reused. |

## Advancement

Before Month 10, you should be able to, without notes:

- [ ] Explain what changed between GPT-2 and Llama, and why each change was made
- [ ] Explain why grouped-query attention won
- [ ] Show, from your own ablation, that data quality beats parameter count
- [ ] Explain temperature, top-k, and top-p precisely
- [ ] Design an evaluation for a model with no ground truth
- [ ] Point at a trained language model with a full training report

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 10 — Retrieval-Augmented Generation. Phase 4 begins, and the work becomes directly employable.
