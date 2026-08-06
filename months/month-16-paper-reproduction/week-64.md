# Week 64: Reproducibility Report

## Outcome

By Sunday you have a report a researcher would recognize as competent: claims tested, methods documented, discrepancies explained, failures reported, and everything reproducible.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The report is the artifact. Two weeks of experiments produce data; this week
produces something someone would read.

The sections that make it credible are the ones people omit: the discrepancy
analysis, and "what did not work." A report where every experiment succeeded on
the first attempt is a report nobody believes, and including the failures costs
you nothing while buying substantial trust.

The reproducibility appendix is the other differentiator. Configs, seeds,
environment, and exact commands, such that someone else could rerun it. That is
what distinguishes a report from a blog post.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 5 hours
- Project: 6 hours
- Interview practice: 2 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Report structure**
   1. Claim, scope, setup, results, discrepancies, ablations, failures, conclusion, appendix
   2. Why the discrepancy and failure sections build trust
2. **Writing results**
   1. Tables with confidence intervals
   2. Figures with error bars and captions that state findings
   3. Never a single-seed number
3. **Honest framing**
   1. What you tested and what you did not
   2. Where scale limits the conclusion
   3. Distinguishing 'the claim did not replicate' from 'I could not replicate it'
4. **Reproducibility**
   1. Configs, seeds, environment, commands
   2. A single entry point that reruns everything
   3. Data provenance

## Required Free Resources

- **Primary:** ML Reproducibility Challenge reports — https://reproml.org/ — read three. They are the format you are writing in.
- **Primary:** 'A Checklist for Reproducible Research' — the NeurIPS reproducibility checklist is a good self-audit
- Distill's writing guidelines — for figure and prose quality
- 'Improving Reproducibility in Machine Learning Research' (Pineau et al.) — https://arxiv.org/abs/2003.12206

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=64
```

1. **Draft the structure** (1h) — All nine sections. Outline before writing.
2. **Write the results section** (2h) — Tables with CIs, figures with error bars, captions that state findings.
3. ****Write the discrepancy section**** (2h) — Your numbers versus theirs, and your best explanation for each gap.
4. ****Write 'what did not work'**** (1.5h) — The failed runs, the abandoned approaches, the bugs. Honestly.
5. **The reproducibility appendix** (1.5h) — Configs, seeds, environment, commands. Test it by following it yourself.
6. **Self-audit against the NeurIPS checklist** (1h) — Note every gap. Fix what you can.
7. **Polish the figures** (1.5h) — Error bars, labels, greyscale-readable, findings in the captions.
8. **Have someone else read it** (1h) — Whatever confuses them is unclear.

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
_
r
e
p
o
r
t
.
m
d
```

## Tests To Write

Add: a test that the single entry point reruns every experiment in the report and reproduces the headline numbers within tolerance.

## Portfolio Artifact

The Month 16 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**Research (30 min).** Recorded: *Present your reproduction in five minutes.* Claim, method, result, discrepancy, conclusion. Then: *What would you do with 10x the compute?*

**Quarterly (60 min).** **Q6 mock interview.** Full loop simulation, part one. Coding plus ML depth.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Submit to the ML Reproducibility Challenge if the timing works, or otherwise open an issue on the paper's repository documenting your reproduction and the discrepancy you found. Real engagement with the research community — even a small, careful contribution — is a meaningfully different signal from a repository nobody has read.
