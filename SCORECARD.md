# Scorecard

How you are graded, when you may advance, and what to do when you fall short.

Self-assessment only works if it is honest. The failure mode is generosity: you
score yourself 8/10 because you feel like you understood it. The test is not
feeling. The test is performance under conditions — can you do it again, unaided,
under time pressure, while explaining it out loud?

---

## Weekly Scorecard

At the end of every week, score yourself on six axes.

```text
Theory understanding:    /10
Implementation quality:  /10
Testing quality:         /10
Write-up quality:        /10
Interview explanation:   /10
Consistency:             /10
------------------------------
Average:                 /10
```

### What each score means

**Theory understanding**
| Score | Standard |
| ----- | -------- |
| 3 | Watched the lecture. Could not re-derive anything. |
| 5 | Can restate the idea. Cannot derive it. |
| 7 | Can derive it with a hint or a reference. Understands why it works. |
| 9 | Can derive it cold on a whiteboard and explain the failure modes. |
| 10 | Can derive it, explain alternatives, and say why this one won. |

**Implementation quality**
| Score | Standard |
| ----- | -------- |
| 3 | Copied from a tutorial. Runs. |
| 5 | Wrote it yourself with heavy reference. Works on the happy path. |
| 7 | Clean, typed, modular, handles edge cases. Someone else could read it. |
| 9 | Production quality. Configurable, logged, documented, no dead code. |
| 10 | You would merge this into a codebase you were responsible for. |

**Testing quality**
| Score | Standard |
| ----- | -------- |
| 3 | No tests. |
| 5 | A couple of smoke tests. |
| 7 | Meaningful unit tests covering the logic and at least one edge case. |
| 9 | Unit tests plus property or numerical-correctness tests (gradient checks, reference comparisons). |
| 10 | Above, plus the tests actually caught a bug this week. |

**Write-up quality**
| Score | Standard |
| ----- | -------- |
| 3 | No README. |
| 5 | README exists and says what the code does. |
| 7 | README explains problem, approach, results, and how to run it. |
| 9 | A stranger can reproduce your results from the README alone. |
| 10 | Above, plus limitations stated honestly and a diagram where useful. |

**Interview explanation**
| Score | Standard |
| ----- | -------- |
| 3 | Cannot explain it without reading notes. |
| 5 | Can explain it, slowly, with gaps. |
| 7 | Can explain it clearly in 3 minutes without notes. |
| 9 | Can explain it, handle three follow-up questions, and draw it. |
| 10 | Can explain it to a non-expert and to a specialist, adjusting depth. |

**Consistency**
| Score | Standard |
| ----- | -------- |
| 3 | Fewer than 6 hours this week. |
| 5 | 10-12 hours, bunched into a weekend. |
| 7 | 15+ hours spread across at least 4 days. |
| 9 | 15-20 hours, at least 5 days, no zero days. |
| 10 | Above, and you hit every planned session without renegotiating with yourself. |

### Pass condition

**Average ≥ 7/10.** Advance to next week.

**Average < 7/10.** Write a remediation plan before starting the next week. Use
the block in `coach/weekly_checkin_template.md`. The plan must be specific:

- Which axis failed and why (be concrete: "I didn't test because I ran out of
  time on Saturday" not "I need to test more").
- What specific work closes the gap.
- Where those hours come from next week — which planned item gets cut.

Remediate inside the following week. Do not stack remediation debt. Two
consecutive weeks below 7 means you take a **reset week**: no new material, only
closing gaps.

### Elite condition

- Average ≥ 9/10.
- Public artifact is recruiter-readable without explanation.
- You can explain every design choice you made, without notes, to a skeptic.

Aim for elite in roughly one week in four. Elite in every week means you are
either superhuman or grading yourself dishonestly. Assume the latter and
recalibrate.

---

## Monthly Scorecard

At the end of each month, in addition to the four weekly scores:

```text
Capstone quality:            /10   (use coach/capstone_review_rubric.md)
Portfolio contribution:      /10
Interview readiness delta:   /10
Theory retention:            /10   (re-test yourself on Month N-1 material)
DBA differentiation:         /10   (did this month strengthen the moat?)
------------------------------------
Monthly average:             /10
```

**Theory retention** is the one people skip and it is the one that matters most.
At the start of each month, spend 30 minutes re-deriving something from two
months ago, cold. If you cannot, your earlier scores were inflated.

**Pass condition:** monthly average ≥ 7 AND capstone ≥ 7.
A capstone below 7 must be fixed before the next month's capstone starts. You may
proceed with the next month's *weeks* while fixing it.

---

## Quarterly Review

Every third month, run a full assessment. This is the honest one.

```text
Q1 (Months 1-3)    Foundations
Q2 (Months 4-6)    Deep Learning
Q3 (Months 7-9)    Transformers
Q4 (Months 10-12)  Applied LLM
Q5 (Months 13-15)  Systems
Q6 (Months 16-18)  Research and Interviews
```

Each quarterly review requires:

1. **A recorded mock interview** in the quarter's domain. Watch it back.
2. **A cold-start test.** Pick a capstone from the quarter. Without looking at the
   code, explain the architecture and re-derive the core algorithm on paper.
3. **A portfolio audit.** Open your GitHub as a stranger. Would you interview you?
4. **A calibration check.** Compare your weekly self-scores against the mock
   interview result. If you have been scoring 8s and the mock went badly, your
   scoring is broken. Adjust downward by the gap and re-score the quarter.

---

## Advancement Gates

Hard gates. Do not pass without meeting the bar.

| Gate | After Week | Requirement |
| ---- | ---------- | ----------- |
| **G1** | 12 | Kaggle system published. Can implement logistic regression and a decision tree from scratch, unaided, in under 45 minutes. |
| **G2** | 24 | Model trained and served behind a tested API. Can debug a non-converging training run out loud. |
| **G3** | 36 | Mini-GPT trains and generates. Can derive multi-head attention on a whiteboard, cold, including the √d scaling and the causal mask. |
| **G4** | 48 | DBA agent shipped with a real eval suite. Can quote its accuracy, failure modes, and safety design. |
| **G5** | 60 | Full stack deployed on Kubernetes with runbooks. Can whiteboard an LLM serving platform in 45 minutes. |
| **G6** | 68 | Reproduction and original research published. Can defend the experimental design against a hostile question. |
| **G7** | 78 | Passing mock loops. Nine flagships public. Applications submitted. |

**If you fail a gate:** do not advance on schedule. Take two to four weeks,
close the specific gap, and re-test. The course is 78 productive weeks, not 78
calendar weeks. Advancing through a failed gate guarantees you fail the same
material later, in an interview, with a recruiter watching.

---

## Interview Readiness Score

Track this monthly from Month 6 onward. Score 1-5 per row.

| Dimension | 1 | 3 | 5 |
| --------- | - | - | - |
| Python coding under time | Struggles with easy problems | Solves mediums in 25 min | Solves mediums in 15 min, clean, tested |
| ML theory depth | Recites definitions | Derives with prompting | Derives cold, discusses alternatives |
| DL / transformer depth | Knows the diagram | Can implement it | Can implement and optimize it |
| LLM systems design | Names components | Designs a working system | Designs with tradeoffs, costs, and failure modes |
| Infrastructure design | Generic answers | Solid, specific design | Design informed by real operational experience |
| Project storytelling | Rambles | Clear STAR narrative | Compelling, quantified, adapted to the audience |
| Portfolio strength | Scattered repos | Several strong projects | Coherent, differentiated body of work |

**Target trajectory:**

| Month | Target total (of 35) |
| ----- | -------------------- |
| 6  | 12 |
| 9  | 17 |
| 12 | 22 |
| 15 | 27 |
| 18 | 31+ |

Below 25 at Month 18 means you extend rather than apply. Applying underprepared
burns the referral and the company for 6-12 months.

---

## The Honesty Protocol

Three checks against self-deception:

1. **The recording test.** Once a month, record yourself explaining something.
   Watch it. Your self-score for "interview explanation" is whatever you would
   give that recording if a stranger sent it to you.

2. **The cold-start test.** Once a month, reimplement something from a month ago
   from memory. What you cannot rebuild, you do not know.

3. **The stranger test.** Once a quarter, send a capstone README to someone who
   was not involved and ask them to run it. Whatever they get stuck on is the
   real score for write-up quality.

Inflated scores do not cost you anything today. They cost you the offer in
Month 20.
