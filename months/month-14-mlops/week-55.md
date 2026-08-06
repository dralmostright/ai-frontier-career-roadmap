# Week 55: CI/CD for ML

## Outcome

By Sunday every pull request runs the test suite and the evaluation suite, and a quality regression beyond threshold fails the build.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The month's most distinctive artifact.**

Conventional CI catches code that does not work. It does not catch a prompt
change that drops faithfulness by four points, or a chunking change that costs
six points of recall, because those still return HTTP 200.

A quality gate — run the eval suite on every PR, compare against the production
baseline, fail on regression — closes that hole. Most teams do not have one, and
having one with a CI log showing it catching a real regression is a concrete,
verifiable artifact.

The design questions are real: which tests gate a deployment, how long the gate
may take, how you handle the eval's inherent noise, and what the threshold should
be. The noise question is the interesting one — you need enough eval samples that
the confidence interval is tighter than your threshold, which is a nice
application of Week 11.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The ML test pyramid**
   1. Unit tests on data transformations and model code
   2. Integration tests on the pipeline
   3. Data validation tests: schema, ranges, distributions
   4. **Quality tests: the eval suite**
   5. Behavioral tests: invariance, directional expectation, minimum functionality
2. **The quality gate**
   1. Baseline comparison
   2. Thresholds, and why they must exceed the noise
   3. Sample size from the confidence interval
   4. Fast subset on every PR, full suite nightly
3. **Pipeline design**
   1. Lint, type, unit, integration, data validation, eval gate
   2. Caching to keep it fast
   3. What runs on PR versus on merge versus nightly
4. **Deployment automation**
   1. Promotion triggered by a passing gate
   2. Manual approval for production
   3. Automated rollback on a post-deploy quality signal
5. **Behavioral testing**
   1. Invariance: paraphrasing the input should not change the answer
   2. Directional: adding evidence should raise confidence
   3. Minimum functionality: the cases that must never fail

## Required Free Resources

- **Primary:** 'Beyond Accuracy: Behavioral Testing of NLP Models with CheckList' — https://arxiv.org/abs/2005.04118 — the behavioral testing taxonomy
- **Primary:** GitHub Actions documentation — https://docs.github.com/en/actions
- 'The ML Test Score' (Breck et al.) — https://research.google/pubs/pub46555/ — a rubric for ML system readiness; score your own project against it
- Great Expectations — https://docs.greatexpectations.io/ — data validation

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=55
```

1. **The base CI workflow** (1h) — Lint, typecheck, unit tests. Cached.
2. **Data validation tests** (1.5h) — Schema, ranges, null rates, distribution shift against a reference.
3. ****The eval gate workflow**** (2.5h) — Run the suite, compare to baseline, fail on regression. The month's artifact.
4. **Threshold selection** (1h) — From Week 11's confidence intervals. How many samples do you need for a 2% threshold?
5. **Fast subset versus full suite** (1h) — PR runs 50 cases; nightly runs 200. Verify the subset is representative.
6. **Behavioral tests** (1.5h) — Invariance, directional, minimum functionality. At least five of each.
7. ****Catch a real regression**** (1.5h) — Deliberately degrade a prompt or chunking parameter. Verify the gate blocks it. Screenshot the CI log.
8. **Automated promotion on pass** (1h) — Merge to main promotes to staging.
9. **Score against the ML Test Score rubric** (1h) — Honest self-assessment. Note the gaps.

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
m
l
o
p
s
-
p
l
a
t
f
o
r
m
/
i
n
f
r
a
/
g
i
t
h
u
b
/
c
i
.
y
m
l


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
m
l
o
p
s
-
p
l
a
t
f
o
r
m
/
i
n
f
r
a
/
g
i
t
h
u
b
/
e
v
a
l
-
g
a
t
e
.
y
m
l
```

## Tests To Write

The workflows are the tests. Add a meta-test: a script that verifies the eval gate would fail given a synthetically degraded model.

## Portfolio Artifact

The workflows, and **a CI log showing the gate catching a real regression**. That screenshot goes in the capstone README.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (30 min).** Recorded: *What tests gate a model deployment?* Walk the pyramid, and be specific about which are ML-specific and why conventional CI misses them. Then: *How do you set the regression threshold?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Build a PR comment bot that posts the evaluation diff — metric by metric, with confidence intervals and a pass/fail verdict — as a comment on every pull request. Making quality visible at the point where the decision is made changes behavior in a way that a nightly report does not, and it is a small amount of code.
