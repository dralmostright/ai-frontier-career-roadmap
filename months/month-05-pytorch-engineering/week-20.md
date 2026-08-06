# Week 20: Experiment Tracking and Reproducibility

## Outcome

By Sunday your training runs are config-driven, tracked, and reproducible bit-for-bit — verified by a test that trains twice and asserts the losses are identical.

Concretely: `test_two_short_runs_produce_identical_losses` passes.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The month's differentiator.** Reproducibility is unglamorous, rarely taught,
and immediately recognizable to anyone who has inherited someone else's research
code.

"How do you make a training run reproducible?" is a question where you should
enumerate rather than gesture: seed Python, NumPy, torch, and CUDA; set
`use_deterministic_algorithms`; seed DataLoader workers; pin the environment;
record the git SHA and whether the tree was dirty; accept that some fast kernels
are nondeterministic and say which tradeoff you chose.

That last clause is what makes the answer senior. Full determinism costs
throughput. The professional position is to use it while developing, disable it
for long production runs, and *state which you did* in the write-up.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 7 hours
- Project: 4.5 hours
- Interview practice: 2 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Configuration**
   1. Typed, validated config with Pydantic
   2. YAML plus dotted CLI overrides
   3. Config diffing: what changed between run 12 and run 31
2. **Sources of nondeterminism**
   1. Python hash seed, `random`, NumPy, torch, CUDA
   2. cuDNN algorithm selection
   3. Atomic operations and floating-point reduction order
   4. DataLoader worker seeding
   5. Set and dict iteration order
3. **Environment capture**
   1. Versions, hardware, git SHA, dirty flag, pip freeze
   2. Why the dirty flag matters: uncommitted code is not reproducible
4. **Experiment records**
   1. What belongs in one, and why each field
   2. The one-line 'why does this run exist' note that everybody omits
   3. Comparing runs: only the columns that varied

## Required Free Resources

- **Primary:** PyTorch reproducibility notes — https://pytorch.org/docs/stable/notes/randomness.html — the authoritative list
- **Primary:** MLflow tracking docs — https://mlflow.org/docs/latest/tracking.html
- Pydantic settings — https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- 'Reproducibility in Machine Learning' — read one of the several good posts on this; the common thread is that seeds are necessary and insufficient

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=20
```

1. **`TrainConfig` with Pydantic** (1.5h) — Validation at load time, not at minute forty.
2. **`load_config` with dotted overrides** (1h) — `--optimizer.lr 0.01` without writing a file per run.
3. **`diff_configs`** (1h) — What changed between two runs.
4. **`set_seed`** (1h) — Everything. Then read the PyTorch randomness notes and check you covered it all.
5. **`capture_environment`** (1h) — Including the git dirty flag.
6. **`verify_reproducibility`** (1.5h) — **The month's gate.** Train twice, assert identical losses.
7. **Hunt down the first divergence** (1.5h) — If the runs differ, walk the checklist. This debugging is the real exercise.
8. **`ExperimentTracker`** (1.5h) — Local JSONL first. Add MLflow after.
9. **`compare_runs` and `plot_training_curves`** (1h) — Only the columns that varied.

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
p
y
t
o
r
c
h
-
l
a
b
s
/
s
r
c
/
c
o
n
f
i
g
.
p
y


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
p
y
t
o
r
c
h
-
l
a
b
s
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
p
y
t
o
r
c
h
-
l
a
b
s
/
s
r
c
/
r
e
p
r
o
d
u
c
i
b
i
l
i
t
y
.
p
y


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
p
y
t
o
r
c
h
-
l
a
b
s
/
c
o
n
f
i
g
s
/
m
n
i
s
t
.
y
a
m
l
```

## Tests To Write

`tests/test_pytorch_labs.py` week-20 blocks. `test_two_short_runs_produce_identical_losses` is the gate.

## Portfolio Artifact

The Month 5 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *How do you make a training run reproducible? Name every source of nondeterminism.* Then the follow-up: *What does full determinism cost, and when would you turn it off?*

**Quarterly (60 min).** **Q2 mock interview.** Coding plus deep learning fundamentals, 45 minutes, recorded. Score with `coach/interview_rubric.md`. Compare against your Month 3 mock.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Containerize the training run and verify that it produces identical losses on two different machines. This is the strongest form of the reproducibility claim and it is what the capstone README should be able to assert. If the numbers differ across hardware, find out why — it is usually a nondeterministic kernel or a different BLAS.
