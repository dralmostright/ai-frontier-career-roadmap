# Month 12: Fine-Tuning and Preference Optimization

**Weeks 45-48 · Phase 4: LLM Engineering and Applied AI · Lab: `bootstrap/llm-labs/`**

---

## The Month In One Sentence

Fine-tune a model on a dataset you built, and develop the judgment to know when you should not have.

## Why This Month Exists

Fine-tuning is the capability people most want to claim and most often
misapply. The valuable thing this month produces is not a tuned model — it is the
judgment about when tuning is the right tool.

The honest position, which you should be able to argue: fine-tuning teaches
*form*, retrieval supplies *facts*. If the problem is "the model does not know
our internal terminology and output format," fine-tune. If it is "the model does
not know what happened yesterday," retrieve. Most people reach for fine-tuning
when they need RAG.

The LoRA material is directly examined — the parameter arithmetic, the
zero-initialization of B, the mergeability. And the multi-adapter serving pattern
(one base model, many task adapters swapped per request) is a good system design
answer.

Your instruction dataset comes from Month 11's domain work, which means this
month compounds rather than diverging.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 45 | Fine-Tuning Fundamentals | `finetune.py` — a full fine-tune with a regression check |
| 46 | LoRA and QLoRA | `lora.py` — LoRA from scratch plus the rank ablation |
| 47 | Instruction Datasets and Data Quality | A curated DBA instruction dataset with a dataset card |
| 48 | Evaluation and Model Comparison | The Month 12 capstone — a fine-tuned model with an honest evaluation |

**Capstone:** Fine-Tuned DBA Assistant Model — a LoRA fine-tune on a hand-curated domain dataset, with a dataset card, model card, and an honest verdict on whether it was worth it.

## The Through-Lines

**Data quality dominates, again.** Week 34's lesson applies to instruction data
even more sharply: a thousand excellent examples beat a hundred thousand mediocre
ones.

**Measure the regression.** A fine-tune that improves the target task and degrades
general capability is a tradeoff, not a win. Measure both.

**Cards are documentation.** Dataset card and model card. By now this should be
routine.

**Know when not to.** The most valuable conclusion this month can produce is
'RAG was better for two of these three use cases, and here is the evidence.'

## Time and Compute

15-20 hours per week. **A GPU is required.** QLoRA on a 3-7B model needs an A100 or equivalent for a few hours. Colab Pro or a RunPod spot instance. Budget $20-40.

## Files

```text
month-12-finetuning/
  README.md      you are here
  week-45.md     fine-tuning fundamentals
  week-46.md     lora and qlora
  week-47.md     instruction datasets and data quality
  week-48.md     evaluation and model comparison
  capstone.md    fine-tuned dba assistant model
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 47.** The dataset is the deliverable. A great dataset with a mediocre training run beats the reverse.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Fine-tuning when RAG was the answer | Expensive, and the facts still go stale | Form versus facts. Decide first. |
| No general-capability regression check | Tuned model is worse at everything else | Evaluate both the target task and a held-out general benchmark. |
| Training on generated data without review | Model learns the generator's errors | Review every example. Yes, all of them. |
| Randomly initializing LoRA's B matrix | The tuned model starts away from the base | B starts at zero. There is a reason. |
| Evaluating on the training distribution only | Looks great, generalizes poorly | Held-out set, and out-of-distribution probes. |

## Advancement

Before Month 13, you should be able to, without notes:

- [ ] State three criteria for choosing fine-tuning over RAG
- [ ] Derive LoRA's parameter count for a given rank and layer size
- [ ] Explain why LoRA's B matrix is initialized to zero
- [ ] Explain DPO versus RLHF in three sentences
- [ ] Report a fine-tune's target-task gain and its general-capability regression
- [ ] Point at a fine-tuned model with a dataset card, model card, and honest evaluation

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 13 — Distributed AI Systems. Phase 5, and the phase where your operational background dominates.
