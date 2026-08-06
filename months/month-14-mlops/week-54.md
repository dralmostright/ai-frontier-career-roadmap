# Week 54: Model Registry and Versioning

## Outcome

By Sunday you have a registry with staged promotion, eval-gated production deploys, and a rollback you have timed and documented in a runbook.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The rollback is the deliverable. "A model is misbehaving at 2am — walk me
through it" is a question most ML engineers answer badly, and you should answer it
with a procedure, a time, and a runbook.

The requirement that makes it work: a model version is weights *plus* the code
that produced them *plus* the data *plus* the config *plus* the eval results.
Rolling back weights alone can produce a model that no longer matches its serving
code, which is a worse outage than the one you were fixing.

Two rules worth enforcing in code rather than in a wiki: promotion to production
requires a passing eval run, with no exceptions; and the previous production
version stays immediately re-promotable.

Then test it. An untested rollback is an untested code path.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **What a version is**
   1. Weights, code, data, config, eval results
   2. Why partial versioning breaks rollback
   3. Content addressing and immutability
2. **Staged promotion**
   1. none → staging → production → archived
   2. Gates at each transition
   3. Exactly one production version
   4. Audit trail: who, when, why
3. **Rollback**
   1. Keeping the previous version hot
   2. Time to rollback as a measured SLO
   3. Testing it on a schedule
   4. The runbook: executable by someone who did not build it
4. **Deployment strategies**
   1. Blue-green, canary, shadow
   2. Shadow mode for ML specifically: serve old, log new, compare
   3. Why canary needs a quality signal, not just an error rate
5. **Lineage in production**
   1. Tagging predictions with the model version
   2. Reconstructing which model produced a given output

## Required Free Resources

- **Primary:** MLflow Model Registry — https://mlflow.org/docs/latest/model-registry.html
- **Primary:** Google SRE Book, release engineering — https://sre.google/sre-book/release-engineering/
- Chip Huyen, 'Designing Machine Learning Systems' — chapter 7, deployment patterns
- 'Continuous Delivery for Machine Learning' (Sato, Wider, Windheuser) — https://martinfowler.com/articles/cd4ml.html

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=54
```

1. **`ModelVersion` with full provenance** (1h) — Every field. Including the git dirty flag.
2. **`ModelRegistry.register`** (1h) — Immutable versions, incrementing.
3. **`promote` with the eval gate** (1.5h) — Refuse production without a passing eval run. No exceptions in code.
4. **Single-production-version enforcement** (45m) — Test it.
5. ****`rollback`**** (1.5h) — Restore the previous version. Then time it.
6. **Write the rollback runbook** (1h) — Executable by someone who did not build the system.
7. ****Test the rollback with a stranger**** (1h) — Hand the runbook to someone else. Whatever they get stuck on is the real quality.
8. **`lineage` and `compare`** (1h) — Full provenance and version diffing.
9. **Shadow deployment** (1.5h) — Serve the old model, log the new one's outputs, compare offline.

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
r
e
g
i
s
t
r
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
r
u
n
b
o
o
k
s
/
r
o
l
l
b
a
c
k
.
m
d
```

## Tests To Write

`tests/test_mlops.py` week-54 blocks. The rollback and eval-gate tests are the important ones.

## Portfolio Artifact

`src/registry.py`, the rollback runbook, and the measured rollback time.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (30 min).** **Recorded.** *A model is misbehaving at 2am. Walk me through it.* Detection, triage, decision, rollback, verification, and the follow-up. Give the measured time. This should be one of your strongest answers in the whole course.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Build a scheduled rollback drill: a weekly CI job that promotes a known-bad model to a staging environment, verifies the quality gate catches it, executes the rollback, and reports the elapsed time. Untested disaster recovery is not disaster recovery, and automating the drill is exactly the instinct that comes from having been on call.
