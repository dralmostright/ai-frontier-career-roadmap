# Week 65: Research Question Selection

## Outcome

By Sunday you have one research question that is specific, falsifiable, feasible in three weeks, and — as far as you can establish — unanswered.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Question selection determines everything downstream. A vague question produces
four weeks of work and no conclusion.

The criteria: **specific** (not "are agents useful for databases?" but "on which
incident classes do agent diagnoses agree with expert diagnoses, and where do
they systematically fail?"); **falsifiable** (you can state in advance what result
would change your mind); **feasible** (runnable in three weeks on your budget);
and **unanswered** (check thoroughly — if it is answered, cite it and move on).

The literature check matters. Spend real time on it. Finding that your question
is answered is a good outcome discovered in Week 65 and a disaster discovered in
Week 68.

Your advantage: you have a benchmark, ground-truth expertise, and a domain with
no established public evaluation. Very few people can say that.

## Time Budget: 15-20 Hours

- Theory: 5 hours
- Coding: 3 hours
- Project: 5 hours
- Interview practice: 2 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **What makes a good question**
   1. Specific enough to answer
   2. Falsifiable — state the disconfirming result
   3. Feasible within the budget
   4. Unanswered, verified by a literature check
   5. Interesting to someone other than you
2. **Finding the gap**
   1. Reading related work systematically
   2. What existing benchmarks do not cover
   3. Where practitioners disagree
   4. Negative space: what nobody has measured
3. **Pre-registration**
   1. Hypothesis, prediction, falsifier, analysis plan
   2. Why writing it first matters
   3. What you commit to and what stays flexible
4. **Scoping**
   1. One question, not three
   2. The minimum experiment that answers it
   3. What you will cut if you run out of time

## Required Free Resources

- **Primary:** Your Month 11 benchmark and its results — the starting point
- **Primary:** A systematic literature check: arXiv, Semantic Scholar, Google Scholar, and the agent-benchmark landscape (SWE-bench, AgentBench, τ-bench)
- 'The Craft of Research' (Booth et al.) — chapters on question formulation
- OSF pre-registration templates — https://osf.io/prereg/ — a good structure even if you do not register formally
- 'Choosing Problems' — Richard Hamming's 'You and Your Research' talk. Read it once; it is worth the time.

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=65
```

1. **Generate 10 candidate questions** (1.5h) — From your Month 11 results, your Month 16 transfer test, and gaps you noticed.
2. ****Literature check on the top 3**** (3h) — Thorough. If it is answered, you want to know now.
3. **Score against the four criteria** (1h) — Specific, falsifiable, feasible, unanswered. Be honest about feasibility.
4. **Choose one** (45m) — One. Not two.
5. ****Write the falsifier**** (1h) — What result would change your mind? If you cannot say, the question is not falsifiable.
6. **Write the proposal** (2h) — Question, motivation, related work, hypothesis, falsifier, method, timeline, and what you will cut.
7. **Feasibility check** (1h) — Estimate the compute, API cost, and hours. Multiply by 1.5.
8. **Get external feedback** (1h) — Send the proposal to someone. Any technical reader will find the vague parts.

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
r
e
p
o
r
t
s
/
r
e
s
e
a
r
c
h
_
p
r
o
p
o
s
a
l
.
m
d
```

## Tests To Write

None. The test is whether someone else, reading the proposal, can state what result would falsify your hypothesis.

## Portfolio Artifact

The proposal. Publish it — a public pre-registration is a small credibility signal and it holds you to the design.

## Interview Drills

**Coding (45 min).** Two problems. Month 18 starts soon.

**Research (25 min).** Recorded: *Why is this question worth answering?* Sixty seconds, to a technical audience. Then: *What result would change your mind?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Map the agent-benchmark landscape systematically — SWE-bench, AgentBench, τ-bench, WebArena, and any domain-specific ones you find — and position your benchmark within it. What does each measure, what does none of them measure, and where does yours sit? This becomes the related-work section, and doing it properly is what makes the contribution claim defensible.
