# Week 67: Implementation and Experiments

## Outcome

By Sunday the experiments have run, the data is collected with full provenance, and you have looked at it honestly — including the parts that do not support your hypothesis.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Execution week. The discipline is resisting the urge to change the design
mid-flight.

You will be tempted, especially if early results are unflattering. Adjusting the
metric, adding a condition, or dropping a scenario after seeing the data is
p-hacking even when it feels like refinement. If you must change something, note
it explicitly in the report as a deviation from the pre-registration.

The other discipline: record failures. A crashed run, a scenario the agent could
not parse, a condition that errored — those are data. Silently dropping them
biases your results toward the configurations that happen to be stable.

Budget guarding matters here. Agent evaluations are expensive; use the Week 51
cost budget and the Month 13 pipeline.

## Time Budget: 15-20 Hours

- Theory: 2 hours
- Coding: 9 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Execution discipline**
   1. Do not change the design mid-flight
   2. If you must, document it as a deviation
   3. Why post-hoc adjustment is p-hacking even when it feels reasonable
2. **Recording failures**
   1. Crashed runs, unparseable outputs, errored conditions
   2. Why silently dropping them biases results
   3. Reporting the failure rate as part of the result
3. **Provenance**
   1. Every result tagged with config, seed, commit, and cost
   2. Resumability, because something will fail
4. **Looking at the data**
   1. Aggregate first, then per-condition, then individual failures
   2. Reading twenty individual failures
   3. Distinguishing a real pattern from a noticed coincidence

## Required Free Resources

- **Primary:** Your Month 13 distributed pipeline — this is what it was for
- **Primary:** Your Month 11 benchmark and Month 14 tracking
- 'The Garden of Forking Paths' (Gelman and Loken) — on post-hoc analysis. Short and uncomfortable.

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=67
```

1. **Final pilot and budget estimate** (1h) — Estimate total cost before committing. Set the budget guard.
2. **Run the main experiment** (4h) — All conditions, all seeds. Use the distributed pipeline.
3. **Run the baselines** (2h) — Including the human baseline you timed in Week 66.
4. **Run the ablations** (3h) — As planned. No new ones invented after seeing results.
5. **Record failures** (1h) — Every crashed run, every unparseable output. With counts.
6. **Verify provenance** (45m) — Can you trace every number back to a config and a commit?
7. **First look at the data** (1.5h) — Aggregate, then per-condition. Resist interpreting yet.
8. ****Read twenty individual failures**** (1.5h) — The qualitative half. This is where the interesting findings come from.

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
 
 
a
n
d
 
 
r
e
s
u
l
t
s
/
```

## Tests To Write

Add: a test that every result row has a config hash, seed, and commit; and a test that the failure count plus the success count equals the attempted count — no silent drops.

## Portfolio Artifact

The complete results with provenance, and the failure log.

## Interview Drills

**Coding (45 min).** Two problems.

**Research (25 min).** Recorded: *Your result is negative. Is it still worth publishing?* Then: *What surprised you in the data?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run an inter-rater check: have someone else — ideally another engineer — score twenty agent outputs against your rubric, and measure agreement. If agreement is low, your scoring is subjective and the headline number is softer than it appears. Reporting that is uncomfortable and it is exactly the kind of honesty that makes the rest of the report credible.
