# Month 12 Capstone: Fine-Tuned DBA Assistant Model

## Objective

Fine-tune a small open model on database diagnostic tasks using a dataset you built, evaluate it rigorously against three baselines, and state honestly where fine-tuning was and was not the right choice.

## Business Problem

The Month 11 agent uses a general-purpose model. It works, and it is verbose,
inconsistently formatted, and occasionally uses terminology a DBA would not.

A fine-tuned model could produce consistent structured diagnoses in domain
vocabulary at lower cost per call. Whether it *should* is the question this
project answers, and the answer may be no for some task types — which is a
legitimate and valuable finding.

Frame it that way in the README: this is an evaluation of whether fine-tuning
helps here, not an assertion that it does.

## Technical Requirements

- The curated instruction dataset from Week 47, with a dataset card
- LoRA or QLoRA fine-tune of a 1-7B open model
- The rank ablation showing where quality saturates
- **Four-way evaluation**: base, well-prompted base, fine-tuned, and RAG
- General capability regression measurement
- Per-task-type breakdown
- Validated judge with kappa reported
- A model card
- Adapter weights published (megabytes, not gigabytes)
- Integration back into the Month 11 agent, with a before/after comparison

## Theory Requirements

The README must explain:

1. Your three criteria for choosing fine-tuning over RAG, and how this task
   scored against them.
2. LoRA's parameter count for your configuration, derived.
3. Why B is initialized to zero.
4. What the regression measurement showed and how you weighed it.
5. **Where RAG won**, if it did.

## System Design Requirements

- Adapter-based deployment: one base model, adapters swapped per task
- The training pipeline reproducible from config
- Evaluation harness reusable across model versions
- The tuned model swappable into the Month 11 agent behind an interface

## Implementation Plan

**Day 1** — Dataset finalization and formatting.

**Day 2** — LoRA training, plus the rank ablation.

**Day 3** — Target-task evaluation and the regression check.

**Day 4** — The RAG comparison. This is the interesting day.

**Day 5** — Integrate into the Month 11 agent; measure the difference on the
benchmark.

**Day 6** — Cards, README, publish.

## Evaluation Plan

| Comparison | What it answers |
| ---------- | --------------- |
| Tuned vs base | Did fine-tuning do anything? |
| Tuned vs well-prompted base | Did it beat the cheap alternative? |
| Tuned vs RAG | Was fine-tuning the right tool? |
| Tuned vs base on general benchmark | What did it cost? |
| Agent accuracy with tuned vs base model | Did it help the flagship? |

Targets: win rate above 0.65 against the base on target tasks, general capability
regression under 5 points, and an honest statement of the RAG comparison whichever
way it fell.

## Expected Repository Structure

```text
dba-assistant-finetune/
  README.md
  MODEL_CARD.md
  DATASET_CARD.md
  pyproject.toml
  Makefile
  configs/
    lora_r8.yaml  lora_r16.yaml  qlora.yaml
  data/
    train.jsonl  heldout.jsonl  README.md
  src/
    prepare.py  train.py  evaluate.py  compare.py  merge.py
  evals/
    tasks/  judge_validation.jsonl  results/
  adapters/
    dba-lora-r8/
  docs/
    ablations.md  rag_comparison.md  limitations.md
```

## README Requirements

Above the fold: one sentence, the four-way comparison table, and the honest
one-line verdict.

Then: the problem and the decision framework; the dataset with a link to its
card; the LoRA configuration with the parameter arithmetic; the rank ablation
curve; **the four-way comparison**; the regression measurement; the per-task
breakdown; the agent integration result; **where RAG won**; limitations.

**The verdict line is the most important sentence in the README.** Something
like: "Fine-tuning clearly won for plan explanation and output formatting. For
factual questions about specific PostgreSQL versions, RAG was better and I would
not fine-tune for that." That sentence is what makes a reviewer trust everything
above it.

## Demo Requirements

`make demo` runs five prompts through the base model, the well-prompted base, the fine-tuned model, and the RAG system, printing all four outputs side by side.

## Blog Post Requirement

Optional this month — post #4 was Month 11's and it is the bigger one.

If you write one, the angle is the honest comparison: "I Fine-Tuned a Model for
My Domain. RAG Was Better for Half of It." Counter-narrative, specific, and
useful.

## Interview Story

> "The fine-tune beat the base model by 18 points on plan explanation and output
> formatting, and it regressed general reasoning by 4. But for factual questions
> about specific PostgreSQL behavior, RAG beat it outright — the facts go stale
> and retrieval just handles that better. So I use the adapter for form and
> retrieval for facts, and I can show you the table that led to that."

60 seconds, and the judgment is the point.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 12 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 8 | Framed as an evaluation, not an assertion. |
| Technical execution | 8 | LoRA from scratch, rank ablation, adapter deployment. |
| Evaluation rigor | 9 | **Four-way comparison with regression measurement.** |
| Code quality | 8 | Reproducible training, reusable eval harness. |
| Documentation | 9 | Dataset card and model card both present and real. |
| Reproducibility | 8 | Config-driven; adapters published. |
| Error analysis | 8 | Per-task breakdown and failure modes. |
| Portfolio readiness | 9 | **Flagship #6.** The honest verdict is what sells it. |

**Overall target: 8.5+. Flagship. The four-way comparison is what earns it.**

## Stretch Goals

1. **DPO on your own preference pairs**, compared against SFT.
2. **Fine-tuning plus RAG combined** — usually the right production answer and
   rarely measured.
3. **Multi-adapter serving** with a task router.
4. **Quantize the merged model** and measure the quality/size/latency tradeoff.

## Limitations To State Honestly

- The dataset is roughly 1000 examples curated by one person from one
  perspective. It encodes my diagnostic style, which is not the only valid one.
- The base model is small (1-7B). Findings may not transfer to larger models,
  where fine-tuning behaves differently.
- General capability regression is measured on one benchmark, which is a narrow
  probe.
- The judge was validated at kappa 0.7 on 50 examples; disagreements above that
  rate are unexplained.
- The RAG comparison uses my Month 10 system, which is tuned for this corpus.
  A less-tuned RAG system would compare differently.
- Evaluated on PostgreSQL tasks only.
