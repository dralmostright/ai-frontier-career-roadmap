# Week 74: AI Infrastructure System Design

## Outcome

By Sunday you can design training, evaluation, and inference infrastructure with the fluency of someone who has operated systems — because you have.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**Your strongest interview territory.** Multi-tenant GPU scheduling, capacity
planning, on-call design, incident response, cost attribution — these are
database and platform problems with different nouns.

The specific advantage: you can talk about failure and cost concretely. Most ML
candidates describe a happy path. You can describe what pages at 3am, what the
error budget is, how long the rollback takes, and what it costs per month.

Bring your artifacts. The Month 15 postmortem, the Month 14 quality gate, and the
Month 13 cost report are all things you can point at during a design discussion,
and pointing at a real artifact is worth more than describing a hypothetical.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 2 hours
- Project: 0 hours
- Interview practice: 14 hours
- Review/write-up: 4 hours

## Theory Lessons

1. **The six designs**
   1. Multi-tenant GPU cluster with fair scheduling
   2. Distributed training platform with fault tolerance
   3. Model registry and deployment pipeline
   4. Observability platform for ML systems
   5. Batch inference over 100M documents
   6. On-call and incident response for an AI platform
2. **Where you are strong**
   1. Failure modes and blast radius
   2. Capacity planning
   3. Cost attribution
   4. On-call design and runbooks
   5. Rollback and recovery
3. **Bringing your artifacts**
   1. The postmortem, the quality gate, the cost report
   2. Pointing at real work during a design discussion

## Required Free Resources

- **Primary:** `INTERVIEW_PREP.md` Track 4, infrastructure designs
- **Primary:** Your Months 13, 14, 15 work — you have built most of this
- Google SRE Book and Workbook — https://sre.google/

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=74
```

1. **Write all six designs** (6h) — One hour each.
2. ****Present six, recorded**** (4.5h) — 45 minutes each.
3. **Cost model drills** (1.5h) — Monthly cost for each design at a stated scale. Rough, confident numbers.
4. **On-call design** (1.5h) — Rotation, escalation, runbook coverage, alert budget. This should be easy for you.
5. **Artifact integration** (1h) — Practice referencing your postmortem and quality gate naturally within a design.

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
s
y
s
t
e
m
_
d
e
s
i
g
n
s
/
```

## Tests To Write

The recordings, scored.

## Portfolio Artifact

Twelve designs total across Weeks 73-74, written and recorded.

## Interview Drills

**Full design mock (45 min).** Multi-tenant GPU cluster. Recorded, scored.

**Hostile questioning (30 min).** Have someone challenge every assumption in one design.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Design a system you have *not* built — a feature store, a real-time recommendation platform, or a multi-region inference service — and get feedback. It tests whether your framework generalizes beyond your own projects, which is what an interviewer is actually assessing.
