# Week 68: Analysis and Writing

## Outcome

By Sunday you have a technical report with a clear finding, honest limitations, and a publicly released benchmark.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The finding is whatever the data says. Your job is to report it clearly and
resist the pull toward a more flattering framing.

If the finding is negative — agents are unreliable on a specific incident class,
or the simple baseline matches the agent — **lead with it**. Negative results
from a domain expert with a purpose-built benchmark are more interesting than
positive ones, more likely to be read, and considerably more credible.

The benchmark release is the other contribution, and possibly the more durable
one. Models get replaced every few months; a well-constructed benchmark with
documented ground truth stays useful. Release it properly: data, documentation,
a runner, and a leaderboard format.

The five-minute presentation is the interview drill. Practice it until it is
automatic.

## Time Budget: 15-20 Hours

- Theory: 2 hours
- Coding: 4 hours
- Project: 7 hours
- Interview practice: 2 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Analysis**
   1. Aggregate across seeds with confidence intervals
   2. Paired tests where the design supports them
   3. Effect size alongside significance
   4. Multiple-comparison correction
   5. Distinguishing pre-registered from exploratory analysis
2. **Writing the finding**
   1. State it in one sentence
   2. Lead with the uncomfortable part if that is the finding
   3. Distinguishing 'X does not work' from 'I could not make X work'
3. **Figures**
   1. Error bars always
   2. Captions that state the finding
   3. Greyscale-readable
4. **Limitations**
   1. Scale, scope, generalization, and construct validity
   2. Why an honest limitations section increases credibility
5. **Release**
   1. Benchmark data, documentation, runner, and licence
   2. Making it easy for someone else to use

## Required Free Resources

- **Primary:** Your Week 68 `analysis.py` module
- **Primary:** Three well-written applied research reports as format references — the SWE-bench paper is a good one
- 'Ten Simple Rules for Structuring Papers' — https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619
- Hugging Face dataset cards — https://huggingface.co/docs/hub/datasets-cards — for the benchmark release

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=68
```

1. **Aggregate and test** (1.5h) — CIs, paired tests, correction, effect sizes.
2. **Produce the figures** (2h) — Error bars, findings in captions, greyscale-safe.
3. ****State the finding in one sentence**** (1h) — If you cannot, you have not finished analyzing.
4. **Write the report** (3h) — Question, related work, method, results, discussion, limitations, appendix.
5. **Write the limitations honestly** (1.5h) — Scale, scope, generalization, construct validity, and your inter-rater result.
6. ****Release the benchmark**** (2h) — Data, docs, runner, licence, dataset card.
7. **External read** (1h) — Someone technical who is not you. Whatever confuses them is unclear.
8. **The five-minute presentation** (1.5h) — Recorded. Slides optional; clarity is not.

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
f
i
n
a
l
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

Add: a test that the released benchmark runner reproduces the headline numbers from the report.

## Portfolio Artifact

The Month 17 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**Research (30 min).** **Recorded.** *Present your findings in five minutes.* Question, method, finding, limitation, what next. Then take hostile questions on the design.

**Portfolio (30 min).** Full portfolio audit before Month 18. All nine flagships. Whatever is not finished, list it — Week 75 is when you fix it.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Set up a public leaderboard for your benchmark — a simple repository where others can submit results, with a documented submission format and evaluation script. This turns a benchmark into infrastructure that other people use, and 'I built the benchmark the field uses for X' is a considerably stronger claim than 'I built a benchmark.' Even modest adoption is a real signal.
