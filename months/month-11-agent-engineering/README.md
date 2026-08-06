# Month 11: Agent Engineering With DBA Differentiation

**Weeks 41-44 · Phase 4: LLM Engineering and Applied AI · Lab: `bootstrap/agent-systems/ and bootstrap/ai-dba-agent/`**

---

## The Month In One Sentence

Build the flagship: an agent that diagnoses database incidents, cites its evidence, classifies its recommendations by risk, and is graded against a benchmark you built because you know the ground truth.

## Why This Month Exists

**This is the most important month of the course.** If one project on your
resume gets you an interview, it is this one.

The reasoning is structural. Agents are everywhere in portfolios and almost all
of them are undifferentiated — a tool-calling loop over a generic domain with no
evaluation, because the author cannot grade the output. You can. Fifteen years of
production database work means you know what the right diagnosis is, which means
you can build the benchmark, which means you can report accuracy, failure modes,
and safety properties.

Almost nobody applying for these roles can do that. It is a genuine moat and this
month is where you build on it.

Give this month your best. Do not schedule it against a work deadline or a
vacation. If something has to slip elsewhere in the course, slip that instead.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 41 | Tool Calling and Function Interfaces | `tools.py` — a typed, validated, risk-classified tool registry |
| 42 | Planning, Reflection, and State | `agent_loop.py`, `state.py` — a bounded, terminating agent loop |
| 43 | Database Diagnostic Tools | `telemetry.py`, `diagnosis.py`, the tools package — the domain layer |
| 44 | Agent Evaluation and Safety | The benchmark, the safety model, and the Month 11 capstone |

**Capstone:** Autonomous DBA Assistant — ⭐ the flagship — an LLM agent that diagnoses PostgreSQL incidents, cites evidence, classifies risk, and is measured against a benchmark you built.

## The Through-Lines

**Tools are permission grants.** Week 41's design principles are the same
instincts you apply to database roles: narrow, validated, bounded, read-only by
default.

**Evidence or it did not happen.** Every claim cites a tool output. Enforced
structurally, not requested in the prompt.

**Safety is architecture, not prompting.** Read-only credentials, approval gates,
audit logs, and blast-radius analysis. "The agent is instructed not to write" is
not a safety property; "the role has no write grant" is.

**Variance is a finding.** Agents are stochastic. Run every scenario five times
and report the spread. Almost nobody does.

## Time and Compute

15-20 hours per week. No GPU. API costs rise this month — agent loops make many calls. Budget $40-60 and cache aggressively. `make db-up` for the telemetry database.

## Files

```text
month-11-agent-engineering/
  README.md      you are here
  week-41.md     tool calling and function interfaces
  week-42.md     planning, reflection, and state
  week-43.md     database diagnostic tools
  week-44.md     agent evaluation and safety
  capstone.md    autonomous dba assistant
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Weeks 43 and 44.** The tools and the benchmark. Do not compress either. Week 42 can be tightened if you must.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| A general `run_sql` tool | The agent writes queries you did not anticipate | Narrow, typed tools. Every degree of freedom gets explored. |
| Write access 'but the prompt says not to' | One bad day from an incident | Read-only role. Enforced by grant. |
| No benchmark | Cannot state accuracy | 30-50 scenarios with known root causes. This is the month's deliverable. |
| Single-run evaluation | A lucky run reported as capability | Five runs per scenario. Report the variance. |
| No ambiguous scenarios | Agent looks better than it is | Include cases where two causes are plausible. |
| Unbounded loops | Surprising API bill | Step, token, and cost budgets. Enforce all three. |

## Advancement

Before Month 12, you should be able to, without notes:

- [ ] Design a tool interface an LLM cannot misuse, and defend each constraint
- [ ] Explain when reflection helps and when it is theater
- [ ] Explain a bad query plan to a non-DBA
- [ ] State your agent's accuracy, evidence recall, and unsafe-recommendation rate
- [ ] Explain your safety architecture without using the word 'prompt'
- [ ] Point at a benchmarked, evidence-citing DBA agent

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 12 — Fine-Tuning. You will build an instruction dataset from this month's domain work.
