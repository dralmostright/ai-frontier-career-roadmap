# Week 66: Experiment Design

## Outcome

By Sunday you have an experimental design you could defend against a hostile question: baselines chosen, metrics justified, conditions controlled, ablations planned, and the analysis specified in advance.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The week that determines whether Month 17 produces a finding or a mess.** A
well-designed experiment run once beats a badly-designed one run five times.

The baseline choice is the most consequential decision. For an agent study, the
candidates are: a rule-based heuristic system, a single LLM call with the same
telemetry and no agent loop, a human expert (time yourself), and random or
majority-class. You want at least two. If the single-call baseline matches the
agent, the agent loop is not earning its cost — and that is a finding worth
reporting.

Specifying the analysis in advance is the other discipline. Deciding how you will
analyze the data after seeing it is how honest people produce dishonest research.

## Time Budget: 15-20 Hours

- Theory: 4 hours
- Coding: 5 hours
- Project: 5.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Baselines**
   1. What a practitioner would actually do
   2. The trivial baseline: majority class, random
   3. The simpler-method baseline: one LLM call, no loop
   4. The human baseline, timed
   5. Why a weak baseline invalidates the result
2. **Metrics**
   1. Choosing metrics that reflect the question
   2. Primary versus secondary
   3. Pre-committing, so you do not pick the flattering one afterward
3. **Conditions and controls**
   1. The independent variable
   2. What must be held constant
   3. Confounds, and how you will detect them
4. **Ablations**
   1. Which component causes the effect
   2. Planning them before running the main experiment
5. **Analysis plan**
   1. Specified before data collection
   2. Statistical tests, correction, and the threshold
   3. How you will handle a null result
6. **Sample size**
   1. How many scenarios and how many seeds
   2. Power: can you detect the effect you care about?

## Required Free Resources

- **Primary:** Week 11's evaluation module and Week 68's analysis module — your own tooling
- **Primary:** 'Statistical Significance Tests for Machine Learning' — for the comparison design
- 'Experimental Design' chapters in any research methods text — the concepts are domain-general
- SWE-bench and τ-bench papers — read their methodology sections as design references

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=66
```

1. **Choose the baselines** (1.5h) — At least two. Include the simpler-method baseline; it is the honest one.
2. ****Time the human baseline**** (1.5h) — Diagnose five of your own scenarios yourself, timed, without looking at the answer. This is a real data point.
3. **Define the metrics** (1h) — Primary and secondary. Justify each against the question.
4. **Specify the conditions** (1h) — Independent variable, controls, and the confounds you will check for.
5. **Plan the ablations** (1h) — Before running anything.
6. **Write the analysis plan** (1.5h) — Tests, correction, thresholds, and how you handle a null result.
7. **Power and sample size** (1h) — How many scenarios and seeds to detect the effect you care about?
8. **Build the harness** (2h) — `ExperimentRunner`, wired to the Month 13 distributed pipeline.
9. **Pilot run** (1h) — Two scenarios, one seed. Shake out the plumbing before committing the budget.

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
e
x
p
e
r
i
m
e
n
t
_
d
e
s
i
g
n
.
m
d


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
e
x
p
e
r
i
m
e
n
t
.
p
y
```

## Tests To Write

Add: a test that the experiment runner produces identical results on a reseeded rerun; and a config-diff test asserting conditions differ only in the intended variable.

## Portfolio Artifact

The design document and the harness. The design document is what you defend in an interview.

## Interview Drills

**Coding (45 min).** Two problems.

**Research (30 min).** Recorded: *Defend your experimental design.* Have someone ask hostile questions: why that baseline, why that metric, what confounds you have not controlled. Then: *What would a null result mean here?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run a simulation study: generate synthetic results under a known effect size, run your planned analysis, and verify it detects the effect. Then generate results under the null and verify it does not falsely detect one. This validates your analysis pipeline before you spend real money on real runs, and it is the kind of methodological care that distinguishes careful work.
