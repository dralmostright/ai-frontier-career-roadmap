# Week 71: ML Theory Interviews

## Outcome

By Sunday you can deliver every item in the `INTERVIEW_PREP.md` derivation set cold, on a whiteboard, holding up under three follow-up questions.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Knowing and explaining are different skills, and this week builds the second.

The specific standard: cold, no notes, on a whiteboard, holding up under
follow-ups. Fluency until the first follow-up is the most common failure and it
signals memorization.

The recording discipline matters here more than anywhere. You will discover that
explanations which feel clear in your head are meandering out loud, and the only
way to find that out before an interviewer does is to watch yourself.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 3 hours
- Project: 0 hours
- Interview practice: 13 hours
- Review/write-up: 4 hours

## Theory Lessons

1. **The core derivation set**
   1. All fourteen items from `INTERVIEW_PREP.md`
   2. Cold, whiteboard, under time
2. **The question bank**
   1. Fundamentals, metrics, models, debugging
   2. Why each question is asked
3. **Delivery**
   1. Structure: what it is, why it works, when it fails
   2. Adjusting depth to the audience
   3. Saying 'I don't know' precisely rather than bluffing

## Required Free Resources

- **Primary:** `INTERVIEW_PREP.md` Track 2, the derivation set and question bank
- **Primary:** Your own Months 1-3 notebooks and derivations
- 'Deep Learning Interviews' (Kashani, free) — https://arxiv.org/abs/2201.00650

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=71
```

1. **The fourteen derivations, on paper** (4h) — Cold. Note which are shaky.
2. **Redo the shaky ones** (2h) — Until they are not.
3. ****20 recorded explanations**** (5h) — Three minutes each, no notes. From the question bank.
4. **Watch all 20 back** (2h) — Score each with `coach/interview_rubric.md`. Note every stall and hedge.
5. **Follow-up practice** (2h) — Have someone ask three follow-ups on each of five topics.
6. **One full ML theory mock** (1h) — 45 minutes, recorded, scored.

## Bootstrap Files To Create

```text
c
o
a
c
h
/
i
n
t
e
r
v
i
e
w
s
/
m
l
_
t
h
e
o
r
y
_
l
o
g
.
m
d
```

## Tests To Write

The recordings. Score each; track improvement across the week.

## Portfolio Artifact

Twenty recorded explanations and their scores.

## Interview Drills

**Full mock (45 min).** ML theory, recorded, scored with the rubric.

**Whiteboard set (60 min).** Six derivations back to back, cold, timed.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Explain five of the concepts to someone with no technical background. It is the hardest audience and it exposes fuzzy understanding immediately — you cannot hide behind vocabulary. If you can explain cross-entropy loss to a non-engineer, you can explain it to anyone.
