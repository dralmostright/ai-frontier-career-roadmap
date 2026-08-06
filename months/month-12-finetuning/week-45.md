# Week 45: Fine-Tuning Fundamentals

## Outcome

By Sunday you have full-fine-tuned a small model, measured both the target-task gain and the general-capability regression, and can argue when fine-tuning is the wrong choice.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The decision framework is the deliverable, not the model.

"When is fine-tuning the wrong answer?" is a question that separates people who
have shipped from people who have followed a tutorial. Three criteria worth
having ready: fine-tune when you need to change *form* (output structure, tone,
terminology) rather than supply *facts*; when the behavior is stable rather than
changing daily; and when you have enough high-quality examples that the model can
generalize rather than memorize.

Catastrophic forgetting is the phenomenon to measure. A model tuned hard on a
narrow task gets worse at everything else, and most fine-tuning writeups do not
check. Measuring it and reporting it honestly is the senior move.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7.5 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The fine-tuning landscape**
   1. Continued pretraining, supervised fine-tuning, preference optimization
   2. What each stage changes
   3. Where in the pipeline your problem sits
2. **Form versus facts**
   1. Fine-tuning teaches structure, style, and terminology
   2. Retrieval supplies knowledge
   3. Why fine-tuning facts goes stale and costs more
   4. The three criteria for choosing
3. **Full fine-tuning mechanics**
   1. Learning rates: one to two orders of magnitude below pretraining
   2. Why more epochs overfits fast on small datasets
   3. Loss masking: train on completions, not prompts
4. **Catastrophic forgetting**
   1. What it is and why it happens
   2. Measuring it with a held-out general benchmark
   3. Mitigations: lower LR, fewer epochs, mixing in general data
5. **Evaluation design**
   1. Target task, held out
   2. General capability, held out
   3. Out-of-distribution probes
   4. Comparing against a well-prompted base model as the baseline

## Required Free Resources

- **Primary:** Hugging Face fine-tuning guide — https://huggingface.co/docs/transformers/training
- **Primary:** 'Training language models to follow instructions' (InstructGPT) — https://arxiv.org/abs/2203.02155 — the SFT sections
- Sebastian Raschka's fine-tuning articles — consistently the clearest practical writing on this
- 'LIMA: Less Is More for Alignment' — https://arxiv.org/abs/2305.11206 — the data-quality argument, with evidence
- Anthropic, 'Prompt engineering vs fine-tuning' guidance in the Claude docs — https://docs.claude.com/

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=45
```

1. **Build the decision framework** (1h) — Write down your three criteria. Test them against five real scenarios.
2. **Set up a small model and dataset** (1.5h) — A 0.5-1.5B model. Small enough to iterate.
3. **Loss masking on completions** (1h) — Train on the answer, not the question. Verify the mask is right.
4. **The full fine-tune** (2h) — Low LR, few epochs, checkpoint often.
5. **Target-task evaluation** (1h) — Held out. Against a well-prompted base model as the baseline.
6. ****Regression check**** (1.5h) — A general benchmark, before and after. Report the delta whichever way it goes.
7. **Overfitting demonstration** (1h) — Train for ten epochs on 200 examples. Watch it memorize.
8. **LR sensitivity** (1h) — Three learning rates. Fine-tuning is more sensitive than pretraining.

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
l
l
m
-
l
a
b
s
/
s
r
c
/
f
i
n
e
t
u
n
e
.
p
y
```

## Tests To Write

Add: a test that loss masking excludes prompt tokens from the loss computation; and a test that the fine-tuned model's output format matches the training format on held-out inputs.

## Portfolio Artifact

`src/finetune.py`, the target-task and regression numbers, and your written decision framework.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *When is fine-tuning the wrong answer?* Give three criteria with an example each. Then: *What is catastrophic forgetting and how do you measure it?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Compare fine-tuning against careful few-shot prompting on the same task, at the same evaluation. Few-shot with a strong model is frequently competitive with fine-tuning a weak one, at a fraction of the effort. Report the comparison honestly — if prompting wins, that is the more useful finding and reporting it demonstrates judgment.
