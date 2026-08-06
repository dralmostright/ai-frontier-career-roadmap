# Week 69: Coding Sprint 1

## Outcome

By Sunday you solve mediums in these categories in 20-25 minutes with narration, complexity analysis, and a test — consistently.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Coding speed decays. You have been doing two or three problems a week for
sixteen months, which maintains familiarity but not speed.

This week rebuilds throughput on the categories that appear most often. Arrays,
strings, and hash maps are roughly half of all interview problems and they are
the ones you should be fastest on.

The standard is not just correctness. It is: restate the problem, state the
approach and complexity before typing, narrate while coding, write a test
unprompted, and finish in 25 minutes. Practising all five together is different
from practising correctness alone.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 13 hours
- Project: 0 hours
- Interview practice: 5 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Pattern recognition**
   1. Two pointers: sorted arrays, pair-finding, in-place partitioning
   2. Sliding window: contiguous subarray or substring with a constraint
   3. Hash map: counting, seen-before, complement lookup
   4. Prefix sums: range queries
2. **The interview protocol**
   1. Restate and confirm constraints
   2. State the approach and complexity before typing
   3. Narrate while coding
   4. Test unprompted
   5. Discuss improvements
3. **Time management**
   1. Five minutes clarifying, five designing, twelve coding, three testing
   2. When to abandon an approach

## Required Free Resources

- **Primary:** NeetCode 150, arrays and hashing, two pointers, sliding window — https://neetcode.io/practice
- **Primary:** Your own Weeks 1-68 problem log — revisit the ones you struggled with
- LeetCode top interview 150 for volume

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=69
```

1. **Arrays and hashing: 15 problems** (4h) — Timed. Log time, approach, and whether you needed a hint.
2. **Two pointers: 10 problems** (2.5h) — Timed.
3. **Sliding window: 10 problems** (3h) — The pattern most people find hardest to recognize.
4. **Strings: 5 problems** (1.5h) — Timed.
5. ****Five recorded solves**** (2h) — Full protocol, narrated, on video. Watch them back.
6. **Review the log** (1h) — Which categories are slow? Those get Week 70's spare time.

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
c
o
d
i
n
g
_
l
o
g
.
m
d
```

## Tests To Write

The log is the record. Track: problem, category, time, hints needed, and whether you tested unprompted.

## Portfolio Artifact

The coding log. It is also your diagnostic for Week 70.

## Interview Drills

**Timed set (2h).** Four problems back to back under timed conditions, no breaks. Simulates the fatigue of a real screen.

**Recorded solve (30 min).** One medium, full protocol, on video. Score with `coach/interview_rubric.md`.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Do two Pramp sessions. Solo practice does not reproduce the specific pressure of someone watching, and the gap between your solo time and your observed time is the number that matters. Book them early; slots fill.
