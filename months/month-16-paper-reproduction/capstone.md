# Month 16 Capstone: Published Reproduction Report

## Objective

Produce a reproduction report that a researcher would recognize as competent work: scoped claims, controlled experiments, multiple seeds, honest discrepancy analysis, and full reproducibility.

## Business Problem

None. This is a research-engineering capability demonstration, and the audience
is anyone deciding whether you can be trusted with an experiment.

What it proves: you can read a claim, design a test of it within a budget,
execute the test carefully, and report what you found — including the parts that
are inconvenient.

## Technical Requirements

- Two reproductions: one architectural (Week 62), one PEFT or preference-based (Week 63)
- Each scoped to under 8 GPU-hours
- Three or more seeds per condition
- A baseline a practitioner would actually use
- At least one ablation isolating the mechanism
- A sensitivity analysis
- Confidence intervals on every number
- Multiple-comparison correction where applicable
- A reproducibility appendix with a single rerun entry point

## Theory Requirements

The report must explain:

1. Each paper's claim, and how you scoped it down while preserving its shape.
2. What you predicted before running, and whether you were right.
3. Every discrepancy and your best explanation.
4. What the scale reduction means for the conclusion's validity.

## System Design Requirements

- The experiment runner: resumable, seeded, logged, cost-tracked
- Configs as data; every condition reproducible from one file
- Results persisted with full provenance
- One command reruns everything

## Implementation Plan

Weeks 61-63 produce the material. Week 64 is the report:

**Day 1** — Structure and results tables.
**Day 2** — Discrepancy analysis. The hardest section.
**Day 3** — Ablations and sensitivity.
**Day 4** — Failures, limitations, appendix.
**Day 5** — Figures and polish.
**Day 6** — External read, revise, publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Both reproductions completed | Yes, within budget |
| Seeds per condition | ≥ 3, with mean and std reported |
| Baseline present and fairly tuned | Yes |
| Discrepancies explained | Every one, with a stated best explanation |
| Failures reported | Yes — a clean report is not credible |
| Rerun entry point | `make reproduce` regenerates the headline numbers |
| Self-audit | NeurIPS checklist completed, gaps noted |

## Expected Repository Structure

```text
reproduction-study/
  README.md
  REPORT.md              <- the deliverable
  Makefile
  pyproject.toml
  configs/
    experiment_a/  experiment_b/  ablations/
  src/
    runner.py  analysis.py
    transformer_repro.py  lora_repro.py
  papers/
    summaries for the five papers read in Week 61
  results/
    raw/  figures/  tables/
  docs/
    discrepancies.md  failures.md  reproducibility.md
```

## README Requirements

Short, pointing at `REPORT.md`. Above the fold: the two claims tested, the
headline verdict for each, and `make reproduce`.

`REPORT.md` carries the nine sections. The two that matter most are the
discrepancy analysis and the failures section — they are what a reviewer reads to
decide whether to believe the rest.

## Demo Requirements

`make reproduce` reruns both experiments at reduced scale (one seed, fewer steps) and regenerates the headline table, in under 20 minutes.

## Blog Post Requirement

Optional. If written, the angle is a specific discrepancy: 'My Numbers Were 1.4
Points Off. It Was the Tokenizer.' Specific diagnostic stories get read; general
reproduction summaries do not.

## Interview Story

> "My numbers came in 1.4 points below the paper's. Tracking that down taught me
> more than matching would have — 1.1 points of it was a tokenizer difference the
> paper mentions in an appendix footnote, and the rest I still can't account for,
> which I say in the report."

45 seconds. The honesty is the point.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 16 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 8 | Claims scoped clearly, with the shape preserved. |
| Technical execution | 8 | Controlled experiments, multiple seeds, real baselines. |
| Evaluation rigor | 9 | **CIs, correction, sensitivity analysis.** |
| Code quality | 8 | Resumable runner, config-driven. |
| Documentation | 10 | **The report is the artifact. Target 10.** |
| Reproducibility | 10 | **One command reruns it. Target 10.** |
| Error analysis | 9 | Discrepancy analysis and the failures section. |
| Portfolio readiness | 8 | Research Engineer roles screen for exactly this. |

**Overall target: 8.5+, with Documentation and Reproducibility at 10.**

## Stretch Goals

1. **Submit to the ML Reproducibility Challenge.** A real venue and real review.
2. **A third reproduction** of a claim you suspect is wrong.
3. **Contact the authors** about your discrepancy and include their response.
4. **Test transfer** of both findings to your domain data — the bridge to Month 17.

## Limitations To State Honestly

- Both experiments run at roughly 1/100th the scale of the originals. Findings
  that depend on scale would not appear.
- Three seeds per condition. Enough to see the variance, not enough for a tight
  interval on small effects.
- Single hardware configuration; no cross-platform verification.
- One discrepancy remains unexplained and is reported as such.
- Compute budget capped at 8 GPU-hours per experiment, which constrained the
  hyperparameter search for both the method and the baseline.
