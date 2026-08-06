# Month 17 Capstone: Original AI-for-Databases Research Project

## Objective

Answer one original, falsifiable question about LLM agents in the database
domain, with a purpose-built benchmark, real baselines, multiple seeds, and an
honest report — then release the benchmark publicly.

## Business Problem

The recommended question: **can LLM agents reliably diagnose PostgreSQL
performance incidents from telemetry and query plans, and where do they
systematically fail?**

It matters because agents are being deployed into operational roles on the
assumption that they are reliable enough, and nobody has measured it in this
domain. There is no public benchmark. The people who could build one — database
experts — mostly are not building agent evaluations, and the people building
agent evaluations mostly cannot judge a query plan.

You can do both. That is the entire opportunity.

Alternative questions if you prefer: does evidence-citation requirement reduce
agent hallucination in diagnostic tasks? Does retrieval over historical
postmortems improve diagnostic accuracy, and by how much? How does agent
reliability degrade as telemetry becomes incomplete?

## Technical Requirements

- A pre-registered proposal with a stated falsifier
- A benchmark of 40+ scenarios with documented ground truth
- At least two baselines, including a simpler-method baseline and a timed human baseline
- Five or more seeds per condition
- Planned ablations
- Confidence intervals, paired tests, effect sizes, and multiple-comparison correction
- A failure log with counts
- An inter-rater check on the scoring
- **The benchmark released publicly** with data, docs, runner, and licence
- A report with an honest limitations section

## Theory Requirements

The report must explain:

1. Why the question is worth answering and why it is unanswered.
2. Why the ground truth is trustworthy — this is the crux of the contribution.
3. Why these baselines, and what a weak baseline would have concealed.
4. What the result means, and what it does not.
5. What would change your mind.

## System Design Requirements

- Benchmark scenarios as versioned data, not code
- Reproducible setup and teardown from seed
- The runner separable from the benchmark so others can evaluate their own agents
- Results with full provenance

## Implementation Plan

Weeks 65-67 produce the material. Week 68 is analysis and writing:

**Day 1** — Analysis: aggregation, tests, effect sizes.
**Day 2** — Figures.
**Day 3-4** — The report.
**Day 5** — Benchmark release: docs, runner, licence, card.
**Day 6** — External read, revise, publish, and the five-minute presentation.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Pre-registered before running | Yes, published |
| Scenarios | 40+, with documented ground truth |
| Baselines | ≥2, including a simpler method and a timed human |
| Seeds per condition | ≥5 |
| Statistical treatment | CIs, paired tests, effect sizes, correction |
| Failures reported | Counts, not silently dropped |
| Inter-rater agreement | Measured and reported |
| Benchmark released | Data, docs, runner, licence |
| Finding stated in one sentence | Yes |

## Expected Repository Structure

```text
dba-agent-reliability-study/
  README.md
  REPORT.md                <- the finding
  PROPOSAL.md              <- pre-registration
  Makefile
  benchmark/
    scenarios/             40+ YAML scenarios
    README.md              construction, ground truth, usage
    runner.py
    LICENSE
  src/
    experiment.py  analysis.py  baselines.py
  results/
    raw/  figures/  tables/  failures.log
  docs/
    experiment_design.md  limitations.md  related_work.md
```

## README Requirements

Above the fold: **the finding, in one sentence**, the headline figure, and a
link to the benchmark.

Then: the question and why it matters; related work and the gap; the benchmark
and why the ground truth is trustworthy; the method; the results with CIs; the
ablations; **the failure taxonomy**; limitations; how to use the benchmark; the
pre-registration link.

**Lead with the finding, including if it is negative.** "LLM agents diagnose
routine database incidents at 82% accuracy but produce confidently wrong and
occasionally dangerous recommendations on ambiguous multi-cause incidents, at a
rate of 14%" is a far more compelling opening than a positive summary.

## Demo Requirements

`make reproduce` runs a subset of the benchmark against a baseline agent and regenerates the headline figure in under 30 minutes.

## Blog Post Requirement

**Post #6 is due this month and it is the capstone of your writing.**

Working title: "Can LLM Agents Diagnose Database Incidents? A Benchmark and a
Warning."

Lead with the finding and the warning. Publish the benchmark alongside it. This
is the post most likely to reach the people who hire for these roles, because it
says something specific that nobody else is positioned to say.

## Interview Story

> "There was no benchmark for this, so I built one — forty incident scenarios
> with ground truth I can actually verify, because I've been diagnosing these for
> fifteen years. The finding is that agents handle routine incidents well and
> fail badly on ambiguous ones, and worse, they fail *confidently* — 14% of the
> time on multi-cause incidents they produce a recommendation that would make
> things worse. I've released the benchmark so others can measure their own
> agents."

90 seconds. This is the story that separates you from every other applied
candidate.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 17 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 10 | **A genuinely original, well-motivated question. Target 10.** |
| Technical execution | 9 | Benchmark, baselines, seeds, ablations. |
| Evaluation rigor | 10 | **The statistical treatment. Target 10.** |
| Code quality | 8 | Reusable runner, versioned scenarios. |
| Documentation | 10 | **Report plus benchmark documentation. Target 10.** |
| Reproducibility | 9 | Pre-registration, provenance, one-command rerun. |
| Error analysis | 10 | **The failure taxonomy is the finding. Target 10.** |
| Portfolio readiness | 10 | **Flagship #9. The pair with Month 11.** |

**Overall target: 9.0+. This and Month 11 are the two that must be excellent.**

## Stretch Goals

1. **Submit to a workshop.** Several venues cover agents and evaluation.
2. **A public leaderboard** so others can submit against your benchmark.
3. **A second research question** if the first resolves early.
4. **Extend the benchmark** to a second database engine.

## Limitations To State Honestly

State these prominently:

- Scenarios are synthetic. Real incidents involve multiple simultaneous causes,
  incomplete telemetry, and time pressure that the benchmark does not model.
- Ground truth is established by the scenario generator, so the agent is graded
  against causes I chose to inject.
- 40 scenarios is small. Confidence intervals are wide and per-category numbers
  are wider.
- The human baseline is one expert — me — which is both a strength (accurate
  ground truth) and a limitation (my diagnostic style is not the only valid one).
- Inter-rater agreement on the scoring rubric was measured on 20 items with one
  other rater.
- Tested against PostgreSQL and one model family. Generalization to other engines
  and models is untested.
- The finding is about diagnosis, not remediation. The agent never executes.
