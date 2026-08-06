# Month 09 Capstone: Tiny Language Model Training Report

## Objective

Train a small language model end to end and produce a training report a researcher would recognize as competent: data curation decisions with evidence, training curves, evaluation with its caveats, ablations, and what did not work.

## Business Problem

None directly. This is a capability demonstration.

The realistic framing: you are showing that you can be handed compute and a
corpus and produce a model plus an account of what happened. That is the core
Research Engineer competency, and the report is the evidence.

## Technical Requirements

- A curated corpus with the pipeline documented and the duplicate rate reported
- Modern architecture: RoPE, RMSNorm, SwiGLU, GQA
- A training run with warmup, cosine decay, gradient clipping, checkpointing
- Full logging: loss, learning rate, gradient norm, throughput, MFU
- Validation perplexity, with the tokenizer caveat stated
- Generated samples across sampling strategies
- **The data quality ablation**: curated versus raw at equal token count
- **A scaling observation**: at least three model sizes if compute allows
- A reproducibility appendix: configs, seeds, environment, commands

## Theory Requirements

The report must explain:

1. Every curation decision and its measured effect.
2. Why warmup, with your own divergence example.
3. What perplexity does and does not tell you.
4. Each sampling strategy, with your comparison table.
5. What you would do with 10x the compute, and why.

## System Design Requirements

Month 5's pipeline, unchanged. That is the point — the infrastructure investment pays off here.

## Implementation Plan

**Days 1-2** — Curate the corpus. Deduplicate, filter, pack, split. Document the
duplicate rate and what filtering removed.

**Day 3** — The architecture update and a short smoke run.

**Days 4-5** — The main training run, plus the ablation runs.

**Day 6** — Evaluation: perplexity, samples, sampling comparison.

**Day 7** — The report. This is the deliverable.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Training converges | Smooth loss curve, no unexplained spikes |
| Validation perplexity | Reported, with the tokenizer caveat |
| Generation | Coherent for the model size; samples included |
| Data ablation | Curated beats raw at equal tokens, quantified |
| Scaling observation | Three sizes if compute allows |
| MFU | Reported |
| Reproducibility | Configs, seeds, environment, and commands published |

## Expected Repository Structure

```text
tiny-lm-training/
  README.md
  REPORT.md              <- the deliverable
  pyproject.toml
  Makefile
  configs/
    tiny.yaml  small.yaml  medium.yaml
    ablations/*.yaml
  src/
    curate.py  tokenize.py  model.py  train.py  evaluate.py  sample.py
  data/
    README.md            provenance and licensing
  results/
    curves/  samples/  ablations/
  docs/
    curation.md  training_log.md  limitations.md
```

## README Requirements

Short, pointing at `REPORT.md`. Above the fold: one sentence, the headline
perplexity, a generated sample, and the data ablation result.

`REPORT.md` is the real artifact:

1. **Summary** — what was trained, on what, and the headline numbers
2. **Data** — sources, curation pipeline, duplicate rate, what filtering removed
3. **Architecture** — components and why each
4. **Training** — hyperparameters, curves, throughput, MFU, incidents
5. **Evaluation** — perplexity with caveats, samples, sampling comparison
6. **Ablations** — data quality, and scaling if run
7. **What did not work** — the failed runs, honestly
8. **Limitations**
9. **Reproducibility appendix**

Section 7 is the one that makes it credible. A training report where everything
worked first time is a report nobody believes.

## Demo Requirements

`make sample` loads the checkpoint and generates from three prompts across three sampling settings, printed side by side.

## Blog Post Requirement

Optional. The angle with value is the data ablation: 'Deduplicating My Training Data Beat Doubling the Model Size.' A measured claim with a number, which is rare.

## Interview Story

> "Deduplicating the training corpus improved validation perplexity more than
> quadrupling the parameter count did — I ran both, same token budget. That
> changed how I think about where to spend effort on a data-constrained problem."

30 seconds, and it demonstrates a real experimental finding.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 9 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 7 | Capability demonstration, framed honestly. |
| Technical execution | 8 | Modern architecture, clean training run. |
| Evaluation rigor | 8 | Perplexity with caveats, ablations, samples. |
| Code quality | 8 | Month 5's pipeline, reused well. |
| Documentation | 9 | **The report is the artifact.** |
| Reproducibility | 9 | Full appendix; someone else can rerun it. |
| Error analysis | 8 | The 'what did not work' section. |
| Portfolio readiness | 8 | The report, not the model, is what gets read. |

**Overall target: 8.0+, with Documentation and Reproducibility at 9.**

## Stretch Goals

1. **The full scaling study** — four sizes, power-law fit, and a compute-optimal
   estimate. Direct Month 16 preparation.
2. **MFU optimization** — find the bottleneck, fix it, report before and after.
3. **Train on the database corpus** and evaluate on SQL completion. On-brand and
   useful for Month 12.
4. **An instruction-tuning preview** — fine-tune on 500 instruction pairs and
   show the behavior change.

## Limitations To State Honestly

- Model is under 50M parameters trained on a small corpus. It produces locally
  coherent text and nothing resembling reasoning.
- Perplexity is tokenizer-dependent and not comparable to published numbers.
- The scaling observation covers a narrow range; extrapolation is unwarranted.
- Single GPU, limited compute budget. Ablations were run once per configuration
  except where variance is reported.
- No instruction tuning, no alignment, no safety evaluation.
