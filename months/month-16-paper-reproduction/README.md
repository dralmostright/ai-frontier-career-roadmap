# Month 16: Paper Reproduction

**Weeks 61-64 · Phase 6: Research Engineering and Interview Execution · Lab: `bootstrap/research-reproduction/`**

---

## The Month In One Sentence

Read papers properly, reproduce a published result at a scale you can afford, and explain honestly why your numbers differ.

## Why This Month Exists

Research Engineer roles screen for exactly this and very few applied candidates
have any of it. Even for non-research positions, a candidate who has designed and
run a real experiment reads as fundamentally more serious.

The skill being built is not "implement a paper." It is scoping: identifying the
*shape* of a claim and testing it at a scale you can run. "Transformers beat
LSTMs at scale" becomes "find the crossover point on a small corpus." "LoRA
matches full fine-tuning" becomes "the rank-quality curve on a 125M model."

**Expect your numbers not to match.** They rarely do. Tracking down why — usually
a tokenizer difference, an unreported preprocessing step, or a different
evaluation protocol — teaches you more than matching would have, and reporting
the discrepancy honestly is what makes the report credible.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 61 | Paper Reading Method | Five paper summaries using the structured template |
| 62 | Transformer Reproduction | A reproduced transformer result at small scale |
| 63 | LoRA or DPO Reproduction | A second reproduction, with an ablation |
| 64 | Reproducibility Report | The Month 16 capstone — a polished reproduction report |

**Capstone:** Published Reproduction Report — two reproductions with ablations, honest discrepancies, and a reproducibility appendix.

## The Through-Lines

**Read in three passes.** Most papers stop at pass one, and that is correct.

**Every paper has a weak point.** Finding it is the skill Week 61 builds, and it
is what research taste consists of.

**Scope the claim, not the scale.** You are testing the shape of a finding.

**Discrepancies are the interesting part.** A report where everything matched
first time is a report nobody believes.

## Time and Compute

15-20 hours per week. Colab Pro or a spot instance for Weeks 62-63. Keep every experiment under 8 GPU-hours; if it needs more, redesign it smaller.

## Files

```text
month-16-paper-reproduction/
  README.md      you are here
  week-61.md     paper reading method
  week-62.md     transformer reproduction
  week-63.md     lora or dpo reproduction
  week-64.md     reproducibility report
  capstone.md    published reproduction report
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 64.** The report is the artifact. Weeks 62 and 63 produce the data; Week 64 turns it into something someone would read.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| Reading linearly | Hours spent on related work you did not need | Three passes. Most papers stop at pass one. |
| Choosing a reproduction that needs a cluster | Nothing finishes | Scope the claim's shape, not its magnitude. |
| Hiding the discrepancy | The report is not credible | Report the gap and your best explanation. |
| Single seed | Noise reported as signal | Three seeds minimum. Report mean and std. |
| No baseline | The number means nothing | Compare against what a practitioner would actually do. |

## Advancement

Before Month 17, you should be able to, without notes:

- [ ] Summarize a paper in 90 seconds: claim, method, evidence, weakness
- [ ] Identify the weakest claim in a paper you read this week
- [ ] Scope a reproduction to fit your compute budget
- [ ] Explain a discrepancy between your numbers and a paper's
- [ ] Design the ablation that would falsify a given claim
- [ ] Point at a published reproduction report with honest discrepancies

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 17 — Original Applied Research. The project only you would build.
