# Week 53: Experiment Tracking

## Outcome

By Sunday every training and evaluation run is recorded with enough context that you could reproduce or explain it six months later.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Week 20 built local tracking. This week makes it a system, and the interview
question is "what belongs in an experiment record?"

The answer is longer than people expect: exact config including unoverridden
defaults, git SHA and dirty flag, environment snapshot, metrics over time not
just final, artifact paths, wall-clock and cost, and — the field everyone omits —
a one-line human note on why this run exists.

That last field is the one you will thank yourself for. Forty runs in, "run 31:
testing whether the chunking change helps on the long-document category" is the
difference between an experiment log and an archive.

Lineage is the other half. Being able to answer "why does this model behave this
way?" three months later requires tracing back to data, code, and config.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 7.5 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **What an experiment record contains**
   1. Config, including defaults
   2. Git SHA and dirty flag
   3. Environment snapshot
   4. Metrics over time
   5. Artifacts
   6. Cost and wall clock
   7. **The why note**
2. **Lineage**
   1. Data version to code version to model version
   2. Why weights-only provenance is insufficient
   3. Tracing a production prediction back to its training run
3. **Tracking systems**
   1. MLflow: open source, self-hostable, adequate
   2. Weights & Biases: better UI, hosted
   3. Building your own: what Week 20 taught you about the requirements
4. **Comparison**
   1. Only the columns that varied
   2. Paired comparison across runs
   3. Why a leaderboard without confidence intervals misleads
5. **Data versioning**
   1. DVC and the content-addressed approach
   2. Why dataset hashes belong in the run record

## Required Free Resources

- **Primary:** MLflow tracking documentation — https://mlflow.org/docs/latest/tracking.html
- **Primary:** 'Hidden Technical Debt in Machine Learning Systems' — https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html — the paper that named the problem. Short and worth reading.
- DVC documentation — https://dvc.org/doc — for data versioning
- Chip Huyen, 'Designing Machine Learning Systems' — chapter 6

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=53
```

1. **Design the record schema** (1h) — Write down every field and why. Then compare against MLflow's.
2. **`ExperimentTracker` with full capture** (1.5h) — Config, git, environment, metrics, artifacts, cost, note.
3. **Stand up MLflow** (1h) — `make services-up`. Backed by the lab Postgres.
4. **Log 10 real runs** (1.5h) — From Month 12's rank ablation. Retrofit the tracking.
5. **`compare_runs`** (1h) — Only varying columns. Sorted by the metric.
6. **Dataset hashing and lineage** (1.5h) — Content-address your Week 47 dataset. Record the hash in every run.
7. **`lineage` traversal** (1h) — From a model version back to data, code, and config.
8. **The six-months-later test** (45m) — Pick an old run. Can you explain it from the record alone?

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
s
r
c
/
t
r
a
c
k
i
n
g
.
p
y
```

## Tests To Write

Add: a test that a run record contains every required field; and a test that lineage traversal from a model version reaches the dataset hash.

## Portfolio Artifact

`src/tracking.py`, MLflow running, and ten real runs logged and comparable.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (25 min).** Recorded: *What belongs in an experiment record, and why each field?* Then: *Six months from now, how do you explain why a production model behaves the way it does?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Retrofit tracking into your Month 13 distributed evaluation so every evaluation run — not just training — is recorded with its cost, config, and results. Evaluation runs are experiments too, and being able to compare eval runs across code versions is what makes the Week 55 quality gate meaningful.
