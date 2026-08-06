# research-reproduction

**Weeks 61-68 · Months 16, 17 · Capstones: Reproduction Report, Original Research**

Read papers properly, reproduce a published result at small scale, then produce
an original finding of your own.

---

## Why This Lab Exists

Research Engineer roles screen for exactly this and very few applied candidates
have any of it. Even for non-research positions, a candidate who has designed
and run a real experiment reads as fundamentally more serious than one who has
only consumed results.

Month 17 is where the course's two threads finally converge. You will produce a
piece of research that only someone with both a database background and AI
engineering skills would think to do — which is, in one artifact, the entire
thesis of your portfolio.

---

## Layout

```text
research-reproduction/
  papers/                 one summary per paper, using the Week 61 template
  src/
    paper_reading.py      W61  the structured reading method
    transformer_repro.py  W62  small-scale transformer experiment
    lora_repro.py         W63  LoRA rank ablation, or a DPO-style experiment
    experiment.py         W66  experiment runner: configs, seeds, ablations
    analysis.py           W68  statistics, plots, significance
  reports/
    reproduction_report.md   M16 capstone
    research_proposal.md     W65
    experiment_design.md     W66
    final_report.md          M17 capstone
  tests/
```

---

## The Paper Reading Method — Week 61

Three passes. Do not read linearly; almost nobody does and it wastes hours.

**Pass 1 (5 minutes).** Title, abstract, figures, conclusion. Answer: what is
the claim, and do I care? Most papers stop here, and that is correct.

**Pass 2 (30 minutes).** Introduction, method, results. Skip related work and
proofs. Answer: how does it work, what did they measure, is the evidence any
good?

**Pass 3 (2+ hours, rare).** Everything, including the appendix, with the
intent to reimplement. Reserve this for papers you are actually reproducing.

For every paper at pass 2 or beyond, fill in `papers/<slug>.md`:

```markdown
# Title (Authors, Year)

## The Claim
One sentence.

## Why It Matters
What was impossible or unknown before this?

## Method
The core mechanism, in your own words. If you cannot write this without
re-reading, you have not understood it yet.

## Evidence
What experiments? What baselines? What datasets? Is the comparison fair?

## What I'd Question
Weakest claim. Missing ablation. Suspicious baseline. Unreported failure.

## What I'd Reproduce
The smallest experiment that would test the central claim.

## Connections
Related work, and how this changes what I'd build.
```

The "What I'd Question" section is the one that develops research taste. Every
paper has a weak point. Finding it is the skill.

---

## Scoping A Reproduction — Week 62

You cannot reproduce a paper trained on 1,024 GPUs. You are not trying to. You
are reproducing the *claim* at a scale you can run.

The method: identify the claim's *shape*, not its magnitude.

| Paper claims | You reproduce |
| ------------ | ------------- |
| "Transformers beat LSTMs at scale" | The crossover point on a small corpus |
| "LoRA matches full fine-tuning" | The rank/quality curve on a 125M model |
| "Scaling laws are power laws" | The curve across 4 model sizes you can train |
| "DPO matches RLHF" | Preference-learning behavior on a small preference set |

**Expect your numbers not to match.** They rarely do, and tracking down why
teaches you more than matching would have. Common causes, in rough order of
frequency: tokenizer differences, a preprocessing step in the appendix,
unreported hyperparameters, different evaluation protocol, and an off-by-one in
the data split.

Report the discrepancy honestly. "I got 1.4 points below the paper and here is
the tokenizer difference that explains 1.1 of it" is a stronger result than a
number that happens to match.

---

## Month 17: The Original Research

**Recommended question:** *Can LLM agents reliably diagnose PostgreSQL
performance incidents from telemetry and query plans?*

You are uniquely positioned for this. There is no established public benchmark,
you built one in Month 11, and you can validate the ground truth in a way that
almost nobody else attempting this could.

A good research question is:

- **Specific.** Not "are agents useful for databases?" but "on which incident
  classes do agent diagnoses agree with expert diagnoses, and where do they
  systematically fail?"
- **Falsifiable.** You can state in advance what result would change your mind.
- **Feasible.** Runnable in four weeks on your hardware.
- **Unanswered.** Check thoroughly; if it is answered, cite it and move on.

**Negative results are fine and often more interesting.** "Agents confidently
produce dangerous recommendations on this specific class of incident" is a more
valuable finding than "agents are pretty good," and it is far more likely to be
read and shared.

---

## Experimental Hygiene

The standards that separate research from anecdote:

| Requirement | Why |
| ----------- | --- |
| Multiple seeds (≥3, ideally 5) | A single run is noise. Report mean and std. |
| A real baseline | Compare against something a practitioner would actually do |
| Confidence intervals | From Week 11. Always. |
| Pre-registered hypothesis | Write down what you expect *before* running |
| Ablations | Which component causes the effect? |
| Reported failures | The experiments that did not work belong in the report |
| Full reproducibility | Configs, seeds, environment, data. Someone else must be able to run it. |

The pre-registration point matters more than it sounds. Writing your prediction
down first is what stops you from retroactively deciding that whatever happened
is what you expected.

---

## Milestones

| Week | Deliverable |
| ---- | ----------- |
| 61 | Five paper summaries, and a 90-second verbal summary of one |
| 62 | A transformer result reproduced at small scale |
| 63 | A LoRA or DPO result reproduced, with an ablation |
| 64 | A polished reproduction report, discrepancies explained |
| 65 | A scoped, falsifiable research question |
| 66 | An experiment design with baselines, metrics, and ablations |
| 67 | Results collected across multiple seeds |
| 68 | A written report and a published repository |

---

## Interview Drills

| Week | Drill |
| ---- | ----- |
| 61 | Summarize a paper you read this week in 90 seconds. |
| 62 | What did the original transformer paper get wrong or leave out? |
| 63 | Design the ablation that would falsify this claim. |
| 64 | Your numbers don't match the paper. Walk me through your diagnosis. |
| 65 | Why is this question worth answering? |
| 66 | What result would change your mind? |
| 67 | Your result is negative. Is it still worth publishing? |
| 68 | Present your findings in five minutes. |
