# Month 17: Original Applied Research

**Weeks 65-68 · Phase 6: Research Engineering and Interview Execution · Lab: `bootstrap/research-reproduction/`**

---

## The Month In One Sentence

Produce a piece of original research that only someone with both a database background and AI engineering skills would think to do.

## Why This Month Exists

**The month where the whole course converges.**

Everything before this has been building two things in parallel: AI engineering
capability, and a domain expertise nobody else in the applicant pool has. This
month puts them together into a single artifact.

The recommended question — *can LLM agents reliably diagnose PostgreSQL
performance incidents from telemetry and query plans?* — is one you are uniquely
positioned to answer. There is no established public benchmark. You built one in
Month 11. You can validate the ground truth in a way almost nobody attempting
this could.

**Negative results are fine and often better.** "Agents confidently produce
dangerous recommendations on this specific class of incident" is a more valuable
finding than "agents are pretty good," and far more likely to be read and shared.

This plus Month 11 is the pair that makes you memorable.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 65 | Research Question Selection | `reports/research_proposal.md` — a scoped, falsifiable question |
| 66 | Experiment Design | `reports/experiment_design.md` — baselines, metrics, conditions, ablations |
| 67 | Implementation and Experiments | Results across conditions, seeds, and ablations |
| 68 | Analysis and Writing | The Month 17 capstone — the research report and released benchmark |

**Capstone:** Original AI-for-Databases Research Project — ⭐ original applied research with a released benchmark, answering a question only you would think to ask.

## The Through-Lines

**Pre-registration.** Write your prediction and your falsifier before running
anything. It is the discipline that stops you from retroactively deciding that
whatever happened is what you expected.

**The benchmark is the contribution.** Often more valuable than the finding, and
it outlives any particular model.

**Report the uncomfortable part.** A finding that only flatters your system is a
finding nobody believes.

**Multiple seeds, always.** Agents are stochastic. Variance is a result.

## Time and Compute

15-20 hours per week. Mostly API-bound. Budget $50-100 for the experiment runs — agent evaluations are expensive. Use the Month 13 distributed pipeline and cache aggressively.

## Files

```text
month-17-original-research/
  README.md      you are here
  week-65.md     research question selection
  week-66.md     experiment design
  week-67.md     implementation and experiments
  week-68.md     analysis and writing
  capstone.md    original ai-for-databases research project
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 66.** A well-designed experiment run once beats a badly-designed one run five times. Spend the time on the design.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| A question too broad to answer | Four weeks, no conclusion | Specific, falsifiable, feasible. |
| No pre-registration | Retroactive hypothesis fitting | Write the prediction down first. |
| Single-seed agent evaluation | Noise reported as finding | Five runs minimum. Agents are stochastic. |
| Hiding the negative result | The whole thing becomes unbelievable | Lead with it if it is the finding. |
| No baseline | Cannot say whether the agent added anything | Rule-based heuristics, or a human, or a simpler model. |
| Scope creep | Nothing finishes | One question. Cut ruthlessly in Week 67. |

## Advancement

Before Month 18, you should be able to, without notes:

- [ ] State a research question that is specific, falsifiable, and feasible
- [ ] State in advance what result would change your mind
- [ ] Defend your experimental design against a hostile question
- [ ] Report a negative or uncomfortable result without flinching
- [ ] Present findings in five minutes to a technical audience
- [ ] Point at published original research with a released benchmark

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 18 — Interview War Room. No new learning. Conversion only.
