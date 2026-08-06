# Week 48: Evaluation and Model Comparison

## Outcome

By Sunday you have a rigorous base-versus-tuned comparison including general-capability regression, and a model card documenting what the model is and is not for.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The evaluation is what makes this a project rather than an experiment.

Three comparisons that must be present: the tuned model against the base model,
the tuned model against a well-prompted base model (the honest baseline most
people skip), and the tuned model against RAG on the same task.

That third comparison is the one that produces the month's best interview
moment. If RAG beats the fine-tune on two of three use cases, saying so
demonstrates judgment in a way that a uniformly positive result cannot.

The DPO material is examined conceptually: DPO replaces RLHF's separate reward
model and RL loop with a direct classification-style objective on preference
pairs, which is simpler, more stable, and usually competitive. Three sentences,
and know why the simplification works.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 6.5 hours
- Project: 5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Preference optimization**
   1. Why SFT alone is insufficient for some behaviors
   2. RLHF: reward model plus PPO, and why it is fiddly
   3. DPO: the direct objective on preference pairs
   4. Why DPO's simplification works
   5. The KL term keeping the policy near the reference — Week 4's divergence, in production
2. **Evaluation design**
   1. Base versus tuned
   2. **Well-prompted base as the honest baseline**
   3. RAG versus fine-tuning on the same task
   4. General capability regression
   5. Out-of-distribution probes
3. **Judging generations**
   1. Week 36's harness, applied
   2. Pairwise with order swapping
   3. Validating the judge, again
   4. Reporting agreement alongside scores
4. **Model cards**
   1. Intended use and out-of-scope use
   2. Training data and its provenance
   3. Metrics by task type
   4. Known failure modes
   5. Ethical considerations

## Required Free Resources

- **Primary:** 'Direct Preference Optimization' — https://arxiv.org/abs/2305.18290 — read sections 1-4
- **Primary:** 'Constitutional AI' — https://arxiv.org/abs/2212.08073 — read for the AI-feedback idea
- TRL documentation — https://huggingface.co/docs/trl/index — DPO implementation
- 'Model Cards for Model Reporting' — https://arxiv.org/abs/1810.03993
- Anthropic's model cards — https://www.anthropic.com/ — read one as a format reference

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=48
```

1. **Build the evaluation set** (1.5h) — Held out by task type, from Week 47's split.
2. **Base versus tuned, pairwise** (2h) — With order swapping. Report the win rate with a CI.
3. ****Well-prompted base as baseline**** (1.5h) — Spend real effort on the prompt. This is the honest comparison.
4. ****RAG versus fine-tuning**** (2h) — Same task, same eval. Month 10's system against Month 12's model.
5. **General capability regression** (1.5h) — A held-out general benchmark, before and after.
6. **Out-of-distribution probes** (1h) — Database questions outside your training distribution. Does it degrade gracefully?
7. **Validate the judge** (1.5h) — Again. 50 hand labels, kappa reported.
8. **Per-task-type breakdown** (1h) — The aggregate hides which task types improved.
9. ****The model card**** (1.5h) — Including the honest conclusion about where RAG wins.

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
e
v
a
l
s
/
f
i
n
e
t
u
n
e
_
e
v
a
l
.
p
y
```

## Tests To Write

Add: a test that the evaluation harness produces identical scores on a repeat run with a cached judge; and a test that the per-task-type breakdown sums correctly to the aggregate.

## Portfolio Artifact

The Month 12 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *Explain DPO versus RLHF in three sentences.* Then: *When would you fine-tune rather than use RAG?* Then: *Your fine-tune improved the target task by 15 points and dropped general capability by 6. Ship it or not?*

**Quarterly (60 min).** **Q4 mock interview.** LLM systems plus applied ML, 45 minutes, recorded. Your LLM systems design score should be at 5 by now.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement DPO on preference pairs you construct from your own domain, and compare against the SFT model. DPO is the current practical standard for preference optimization, implementing it makes the objective concrete, and having done it means you can discuss alignment techniques from experience rather than from reading. Budget four hours and a few dollars of GPU time.
