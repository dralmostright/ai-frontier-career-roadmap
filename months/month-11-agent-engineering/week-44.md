# Week 44: Agent Evaluation and Safety

## Outcome

By Sunday you have 30-50 synthetic incidents with known root causes, a five-runs-per-scenario evaluation, a documented safety architecture, and a blast-radius analysis.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The week that makes the flagship a flagship.**

The benchmark is the deliverable. Anyone can build an agent; almost nobody can
grade one, because grading requires knowing the ground truth. You do. Building
30-50 reproducible incidents with known causes, acceptable diagnoses, required
evidence, and unsafe actions is the single most differentiated piece of work in
the entire course.

Two design points that make it a real evaluation rather than a demo:

**Five runs per scenario.** Agents are stochastic. An agent that solves a scenario
three times out of five is not a 60%-accurate agent, it is an unreliable one, and
those are different problems with different fixes. Reporting variance is unusual
and it is a strong signal.

**Ambiguous and red-herring scenarios.** The bloat scenario where the naive fix is
`VACUUM FULL` (an exclusive lock, an outage) tests safety rather than accuracy.
The stale-statistics scenario where the index exists tests whether the agent
pattern-matches or reasons. Those are where the interesting failures live.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Benchmark construction**
   1. Reproducible setup, workload, and fault injection
   2. Ground truth: root cause, acceptable diagnoses, required evidence, unsafe actions
   3. Difficulty stratification
   4. Ambiguous and red-herring cases
2. **Evaluation dimensions**
   1. Outcome: correct diagnosis
   2. Trajectory: evidence recall, tool precision, step efficiency
   3. Safety: unsafe recommendations, rollback coverage, evidence citation
   4. Efficiency: tokens, time, dollars
   5. **Robustness: variance across runs**
3. **The safety architecture**
   1. Read-only role, enforced by grant not by prompt
   2. Risk classification with fail-closed defaults
   3. Approval gates: specific, expiring, rollback-first
   4. Append-only audit log sufficient to reconstruct any run
   5. Prompt injection defense, architecturally
4. **Blast radius**
   1. What is the worst outcome if the agent is wrong?
   2. Scope, reversibility, time to detect, time to recover
   3. Why this section is absent from every other agent project
5. **Reporting**
   1. Accuracy with confidence intervals
   2. Per-difficulty breakdown
   3. The failure taxonomy
   4. What the agent should not be used for

## Required Free Resources

- **Primary:** Anthropic, 'Building effective agents' — the evaluation section
- **Primary:** Google SRE Book, postmortem culture — https://sre.google/sre-book/postmortem-culture/ — the framing for your safety documentation
- 'SWE-bench' — https://arxiv.org/abs/2310.06770 — a well-constructed agent benchmark; read how they built it
- OWASP Top 10 for LLM Applications — https://owasp.org/www-project-top-10-for-large-language-model-applications/ — the injection material
- 'Prompt Injection' writing by Simon Willison — the clearest treatment of why this is architecturally hard

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=44
```

1. **`IncidentScenario` schema** (45m) — Ground truth, required evidence, unsafe actions.
2. ****Build 30-50 scenarios**** (6h) — Missing index, stale stats, bloat, locks, N+1, work_mem, connections, replication lag, checkpoint storm, autovacuum starvation, plus ambiguous and red-herring cases.
3. **`build_benchmark` with fixed seeds** (1.5h) — Reproducible setup and teardown. A benchmark you cannot rerun is not a benchmark.
4. **`score_outcome` with acceptable diagnoses** (1h) — Not string match. 'Missing index on users.email' and 'seq scan because users.email is unindexed' are the same answer.
5. **`score_trajectory`** (1.5h) — Evidence recall is the key metric. A right answer without looking at the evidence is luck.
6. **`score_safety`** (1.5h) — Unsafe recommendations, rollback coverage, evidence citation. Gating.
7. **`ApprovalGate`** (1.5h) — Specific, expiring, rollback-required.
8. **`AuditLog` with run reconstruction** (1h) — If you cannot rebuild the trajectory from the log, the log is insufficient.
9. **`detect_prompt_injection` and the architectural defenses** (1.5h) — Detection is necessary and insufficient. Document all four defenses.
10. **`classify_action_risk`** (1.5h) — The CREATE INDEX vs CREATE INDEX CONCURRENTLY distinction is the example to feature.
11. ****Run the full evaluation, 5x per scenario**** (3h) — Report accuracy, variance, evidence recall, safety, and cost.
12. **`blast_radius` and the safety document** (1.5h) — Nobody else has this section.

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
a
i
-
d
b
a
-
a
g
e
n
t
/
e
v
a
l
s
/
g
e
n
e
r
a
t
e
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
a
i
-
d
b
a
-
a
g
e
n
t
/
e
v
a
l
s
/
r
u
n
_
e
v
a
l
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
a
g
e
n
t
-
s
y
s
t
e
m
s
/
s
r
c
/
s
a
f
e
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
a
g
e
n
t
-
s
y
s
t
e
m
s
/
s
r
c
/
e
v
a
l
u
a
t
i
o
n
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
a
i
-
d
b
a
-
a
g
e
n
t
/
d
o
c
s
/
s
a
f
e
t
y
.
m
d
```

## Tests To Write

Week-44 blocks in both test files. The risk classification, approval gate, and injection tests are the safety-critical ones.

## Portfolio Artifact

The Month 11 capstone. See `capstone.md`. **This is the flagship.**

## Interview Drills

**Coding (45 min).** Two problems.

**System design (45 min).** **Recorded.** *Design a database reliability assistant.* Telemetry ingestion, tool design, the agent loop, safety architecture, approval gates, audit, evaluation, and blast radius. This is your signature design and you should be able to deliver it in 45 minutes with confidence.

**Behavioral (15 min).** Refine story #10: building the DBA agent. Technical judgment, with the accuracy number.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Red-team your own agent. Craft prompt injection attempts embedded where the agent will actually read them — SQL comments, table comments, error message text, application names in pg_stat_activity. Try to make it report a broken database as healthy, or recommend a destructive action. Document what worked, what did not, and what you changed. A red-team write-up in an agent project is close to unheard of and it is exactly the instinct that says 'this person has operated production systems.'
