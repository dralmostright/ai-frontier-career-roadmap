# Week 62: Transformer Reproduction

## Outcome

By Sunday you have reproduced a published transformer finding at a scale you can afford, with multiple seeds, a baseline, and a documented account of any discrepancy.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The scoping skill is the deliverable. You cannot reproduce a paper trained on
1,024 GPUs and you are not trying to — you are testing whether the *claim* holds
at a scale you can run.

Good targets: the scaling relationship between loss and parameters, the
attention-versus-recurrence comparison, positional encoding variants and length
generalization, or the pre-norm versus post-norm stability result.

**Expect a discrepancy.** The most common causes, roughly in order: tokenizer
differences, a preprocessing step buried in the appendix, unreported
hyperparameters, a different evaluation protocol, and an off-by-one in the data
split. Finding which one applies is the actual research work, and reporting it is
what makes the report worth reading.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Scoping a reproduction**
   1. Identify the claim's shape, not its magnitude
   2. What scales down cleanly and what does not
   3. Setting a compute budget before starting
2. **Controlled comparison**
   1. Same data, same tokenizer, same budget across conditions
   2. Seeds, and why three is the minimum
   3. A baseline a practitioner would actually use
3. **Discrepancy diagnosis**
   1. Tokenizer differences
   2. Unreported preprocessing
   3. Hyperparameters in an appendix or not at all
   4. Evaluation protocol differences
   5. Data split leakage
4. **Reporting**
   1. Your numbers next to theirs
   2. The discrepancy, and your best explanation
   3. What you could not test at this scale

## Required Free Resources

- **Primary:** 'Attention Is All You Need' — https://arxiv.org/abs/1706.03762 — your fourth reading. It reads differently now.
- **Primary:** 'Scaling Laws for Neural Language Models' — https://arxiv.org/abs/2001.08361 — a good reproduction target at small scale
- The Annotated Transformer — https://nlp.seas.harvard.edu/annotated-transformer/
- 'On Layer Normalization in the Transformer Architecture' — https://arxiv.org/abs/2002.04745 — another good target
- ML Reproducibility Challenge reports — https://reproml.org/ — read two as format references

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=62
```

1. **Scope the experiment** (1.5h) — Write down the claim, your reduced version, and the compute budget. Before running anything.
2. **Pre-register the prediction** (45m) — What do you expect, and what result would surprise you? Write it down first.
3. **Build the experimental harness** (2h) — Week 66's `ExperimentRunner`, brought forward. Resumable, seeded, logged.
4. **Run the baseline** (1.5h) — What a practitioner would do without the paper's contribution.
5. **Run the conditions, 3+ seeds** (3h) — Same data, same budget, varying only the independent variable.
6. **Aggregate with confidence intervals** (1h) — Week 11's tooling. Never a single-seed number.
7. **Compare against the paper** (1h) — Your numbers next to theirs. Note every difference.
8. ****Diagnose the discrepancy**** (2h) — Work the list. This is the real research work.

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
s
r
c
/
t
r
a
n
s
f
o
r
m
e
r
_
r
e
p
r
o
.
p
y
```

## Tests To Write

Add: a test that the experiment runner produces identical results on a repeat run with the same seed — reproducibility of your reproduction.

## Portfolio Artifact

The experiment code, results across seeds, and the discrepancy analysis.

## Interview Drills

**Coding (45 min).** Two problems.

**Research (25 min).** Recorded: *What did the original transformer paper get wrong or leave out?* Then: *Your numbers don't match the paper. Walk me through your diagnosis.*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Email the authors about your discrepancy. Researchers frequently respond to careful, specific questions from someone who has clearly done the work, and the answer is often an unreported detail that explains everything. 'I emailed the authors and it turned out they used a different tokenizer than the one referenced' is both a good story and genuinely useful information.
