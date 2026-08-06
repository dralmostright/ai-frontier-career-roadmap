# Week 75: Portfolio Polish

## Outcome

By Sunday every flagship has a README with results above the fold, an architecture diagram, a demo, and honest limitations — and the profile page ties them into one narrative.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Reviewers spend ninety seconds. That ninety seconds decides whether the next
hour happens.

The audit from Week 68 gave you the list. This week executes it: results tables
above the fold, diagrams for anything with three or more components, demo GIFs or
recordings, limitations sections, and setup instructions tested on a clean clone.

The setup instructions are the one people skip and the fastest way to lose a
reviewer. Clone into a fresh directory, follow only the README, and time it.
Whatever breaks is the real quality of your documentation.

The profile README is the landing page and it should lead with the positioning,
not with a list of technologies.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 3 hours
- Project: 11 hours
- Interview practice: 4 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **The 90-second test**
   1. What a reviewer sees first
   2. Results above the fold
   3. Why a diagram beats three paragraphs
2. **README standard**
   1. From `PORTFOLIO_STRATEGY.md`
   2. Problem, results, architecture, decisions, setup, evaluation, limitations, talking points
3. **The profile page**
   1. Positioning statement first
   2. Three flagship cards
   3. Writing
   4. Background framed as advantage

## Required Free Resources

- **Primary:** `PORTFOLIO_STRATEGY.md` — the README standard and the audit questions
- **Primary:** Your Week 68 audit list
- Excalidraw or draw.io for diagrams

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=75
```

1. **Audit all nine against the standard** (1.5h) — Gap list per repository.
2. **Fix the READMEs** (4h) — Results above the fold. Every one.
3. **Architecture diagrams** (2.5h) — For anything with three or more components. Nine diagrams or close to it.
4. ****Three demo recordings**** (2h) — DBA agent, Incident Commander, RAG system. Three minutes each.
5. ****Test setup on a clean clone**** (2h) — All nine. Time each. Fix whatever breaks.
6. **Limitations sections** (1.5h) — Every repository. Honest.
7. **The profile README** (1.5h) — Positioning first. Three cards. Pin the top six.
8. **The 90-second test** (30m) — Private window. Would you interview you?

## Bootstrap Files To Create

```text
A
l
l
 
f
l
a
g
s
h
i
p
 
r
e
p
o
s
i
t
o
r
i
e
s
;
 
G
i
t
H
u
b
 
p
r
o
f
i
l
e
 
R
E
A
D
M
E
```

## Tests To Write

The clean-clone test for all nine. That is the real test.

## Portfolio Artifact

Nine finished repositories and a profile page.

## Interview Drills

**Portfolio walkthrough (30 min).** Four minutes, recorded. Then 90 seconds. Then 20 seconds.

**Coding (45 min).** Two problems. Keep the reps up.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Have three people do the 90-second test on your GitHub and report back what they understood, what impressed them, and what confused them. Your own audit is biased by knowing what everything is. Three outside readings will surface things you cannot see, and they are cheap to get.
