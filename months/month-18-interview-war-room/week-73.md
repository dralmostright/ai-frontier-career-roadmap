# Week 73: LLM System Design

## Outcome

By Sunday you can deliver any of the six core LLM system designs in 45 minutes, with requirements, metrics, deep dive, scaling, failure modes, tradeoffs, and cost.

## Why This Matters For OpenAI/Anthropic-Level Interviews

System design is where you can be strongest, and the reason is structural: most
ML candidates skip requirements, failure modes, and cost, and those are the
sections you will do naturally.

The framework matters as much as the content. Interviewers grade structure, and
following the same seven-step arc every time — requirements, success metrics,
high-level design, deep dive, scaling, failure modes, tradeoffs — makes you
legible.

Two things to do unprompted: ask about the cost budget in the requirements phase,
and cover failure modes without being asked. Both are unusual and both signal
production experience.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 2 hours
- Project: 0 hours
- Interview practice: 14 hours
- Review/write-up: 4 hours

## Theory Lessons

1. **The framework**
   1. Requirements (5), metrics (2), high-level (10), deep dive (15), scaling (5), failure modes (5), tradeoffs (3)
   2. Why steps 2, 6, and 7 are where you win
2. **The six designs**
   1. ChatGPT-like conversational system
   2. Enterprise RAG over 10M documents
   3. LLM evaluation platform
   4. Inference serving platform
   5. Training platform
   6. **Database reliability assistant** — your signature
3. **Questions to ask back**
   1. Read/write ratio, p99 target, cost budget, error tolerance, staleness tolerance, compliance boundary

## Required Free Resources

- **Primary:** `INTERVIEW_PREP.md` Track 4
- **Primary:** Your own Months 10, 13, 14, 15 designs — you have built four of the six
- Chip Huyen, 'Machine Learning Systems Design' — https://huyenchip.com/machine-learning-systems-design/toc.html
- System Design Primer — https://github.com/donnemartin/system-design-primer

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=73
```

1. **Write all six designs** (6h) — One hour each. Full seven-step structure.
2. ****Present six, recorded**** (4.5h) — 45 minutes each, whiteboard visible. Watch them back.
3. **Practice the questions-back list** (1h) — Until asking about cost budget is automatic.
4. **Failure mode drills** (1.5h) — For each design, name five failure modes, their detection, and their recovery.
5. **Cost estimation drills** (1h) — Cost per request for each design. Rough numbers, stated confidently.

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

The recordings, scored against the Track 4 rubric.

## Portfolio Artifact

Six written designs and six recordings.

## Interview Drills

**Full design mock (45 min).** Enterprise RAG. Recorded, scored.

**Rapid-fire (30 min).** Six designs, five minutes each. Just the structure. Builds fluency in the arc.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Present the database reliability assistant design to someone instructed to ask hostile questions — why not just use monitoring, what happens when it is wrong, why would anyone trust it, what is the actual ROI. This is your signature design and it will attract the most scrutiny; rehearsing the defense is worth more than rehearsing the pitch.
