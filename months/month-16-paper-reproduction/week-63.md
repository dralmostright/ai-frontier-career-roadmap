# Week 63: LoRA or DPO Reproduction

## Outcome

By Sunday you have reproduced a parameter-efficient fine-tuning or preference-learning result, including the ablation that isolates the mechanism.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The second reproduction is faster because the harness exists, which lets you
spend the time on the ablation instead — and the ablation is what makes a
reproduction a contribution rather than a re-run.

Good targets: LoRA's rank-quality relationship (you have Month 12's data
already), the claim that adapting all linear layers beats attention-only, DPO
versus SFT on a small preference set, or QLoRA's claim that 4-bit quantization
costs little quality.

The ablation question — "design the experiment that would falsify this claim" —
is directly examined and it is the core of experimental thinking. A claim you
cannot imagine falsifying is not a claim you have understood.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Ablation design**
   1. Change one thing, hold everything else
   2. What the ablation isolates and what it confounds
   3. Falsification: what result would overturn the claim?
2. **Common failure modes in PEFT reproductions**
   1. Learning rate not re-tuned for the reduced parameter count
   2. Different target modules than the paper
   3. Evaluation on the training distribution only
3. **Preference learning**
   1. Preference pair construction
   2. Why DPO's simplification works
   3. The KL term and the reference model
4. **Statistical treatment**
   1. Multiple seeds
   2. Paired comparison across conditions
   3. Multiple-comparison correction when testing many conditions

## Required Free Resources

- **Primary:** 'LoRA' — https://arxiv.org/abs/2106.09685 — reread with reproduction in mind
- **Primary:** 'Direct Preference Optimization' — https://arxiv.org/abs/2305.18290
- 'QLoRA' — https://arxiv.org/abs/2305.14314
- Sebastian Raschka's LoRA experiments — a good model for what careful small-scale ablation looks like
- PEFT and TRL documentation — https://huggingface.co/docs/peft/ and /trl/

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=63
```

1. **Choose and scope the target** (1h) — Write the claim, the reduced version, and the falsification condition.
2. **Pre-register** (45m) — Your prediction, before running.
3. **Reuse the harness** (45m) — Week 62's runner. This is why you built it.
4. **Run the main comparison, 3+ seeds** (3h) — With a properly-tuned baseline.
5. ****The ablation**** (2.5h) — Isolate the mechanism. This is the week's contribution.
6. **Sensitivity analysis** (1.5h) — Does the finding survive a different learning rate? A different dataset size?
7. **Multiple-comparison correction** (45m) — You are testing many conditions. Correct for it.
8. **Compare and diagnose** (1.5h) — Against the paper. Explain the gap.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
r
e
s
e
a
r
c
h
-
r
e
p
r
o
d
u
c
t
i
o
n
/
s
r
c
/
l
o
r
a
_
r
e
p
r
o
.
p
y
```

## Tests To Write

Add: a test that the ablation conditions differ only in the intended variable — a config-diff assertion. Uncontrolled ablations are a common and invisible error.

## Portfolio Artifact

The second reproduction with its ablation and sensitivity analysis.

## Interview Drills

**Coding (45 min).** Two problems.

**Research (25 min).** Recorded: *Design the ablation that would falsify this claim.* Pick a paper and do it cold. Then: *Your result contradicts the paper. What do you do?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Test whether the reproduced finding transfers to your Month 12 domain data. Published results are usually established on general benchmarks, and whether they hold on a narrow domain is a real open question. If LoRA's rank saturation point differs on database instruction data than on general instruction data, that is a small original finding and a natural bridge into Month 17.
