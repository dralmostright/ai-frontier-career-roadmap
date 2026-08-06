# Week 60: Reliability and Incident Response

## Outcome

By Sunday the full stack is deployed with SLOs, runbooks, and health checks — and you have deliberately broken it, watched the response, executed the rollback, and written a blameless postmortem.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The week that produces your best interview story.**

Deploy a deliberately bad model or corrupt part of the retrieval index. Watch
what fires and — more informatively — what does not. Execute the rollback from
the runbook. Time it. Then write the postmortem: timeline, impact, contributing
factors, what went well, what did not, and action items.

Put it in the repository.

No other candidate will have one. It is unmistakably the work of someone who has
been on call, and it demonstrates something no amount of architecture description
can: that you think about the failure path as a first-class concern.

The rest of the week assembles the **Database Incident Commander** — telemetry
plus RAG over runbooks plus the agent, deployed as one product. That is
Flagship #3, and it is the project that shows the whole course composing.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 7 hours
- Project: 5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Reliability engineering for ML**
   1. SLIs, SLOs, error budgets — including a quality SLO
   2. Graceful degradation: serve stale, serve cached, serve a simpler model, refuse
   3. Circuit breakers around model calls
   4. Timeouts at every boundary
2. **Runbooks**
   1. What a good runbook contains: symptom, diagnosis, action, verification, escalation
   2. Written for someone who did not build the system
   3. Tested by having someone else follow it
3. **Incident response**
   1. Detect, triage, mitigate, resolve, review
   2. Mitigate before diagnose — restore service first
   3. Communication during an incident
4. **Postmortems**
   1. Blameless framing and why it matters
   2. Timeline, impact, contributing factors, action items
   3. Why 'human error' is never a root cause
5. **Chaos engineering**
   1. Inducing failure deliberately
   2. Starting small and in a controlled environment
   3. What you learn that testing does not tell you

## Required Free Resources

- **Primary:** Google SRE Book, 'Postmortem Culture' — https://sre.google/sre-book/postmortem-culture/
- **Primary:** Google SRE Workbook, 'Incident Response' — https://sre.google/workbook/incident-response/
- Google SRE Book, 'Embracing Risk' — error budgets — https://sre.google/sre-book/embracing-risk/
- 'The Field Guide to Understanding Human Error' (Dekker) — the blameless framing, argued properly
- Published postmortems from Cloudflare, GitLab, and AWS — read three as format references

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=60
```

1. **Define SLIs and SLOs for the stack** (1.5h) — Availability, latency, quality, freshness. With error budgets.
2. **Graceful degradation** (1.5h) — What happens when retrieval fails? When the model API is down? Implement the fallback chain.
3. **Circuit breakers** (1h) — Around the model API. Verify it opens and recovers.
4. **Write four runbooks** (2h) — Quality degradation, retrieval failure, model API outage, index corruption.
5. **Assemble the Incident Commander** (2h) — Telemetry + RAG over runbooks + agent, deployed as one product.
6. ****Induce a failure**** (1.5h) — Deploy a degraded model. Do not tell yourself which one.
7. ****Respond to it**** (1h) — Follow your own runbook. Time every phase. Note what your monitoring missed.
8. ****Write the postmortem**** (1.5h) — Blameless. Timeline, impact, contributing factors, what went well, action items.
9. **Implement the action items** (1.5h) — A postmortem without follow-through is theatre.

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
r
u
n
b
o
o
k
s
/


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
d
o
c
s
/
p
o
s
t
m
o
r
t
e
m
-
0
0
1
.
m
d
```

## Tests To Write

Add: a chaos test that kills a pod mid-request and verifies the client sees a retry rather than an error.

## Portfolio Artifact

The Month 15 capstone plus **the postmortem**. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (40 min).** **Recorded.** *Write the postmortem for an LLM outage.* Then: *Design the on-call setup for an AI platform — what pages, what the runbooks cover, what the escalation path is.* This is your strongest interview territory in the whole course.

**Quarterly (60 min).** **Q5 mock interview.** Infrastructure system design, 45 minutes, recorded. Your infrastructure design score should be at 6 or 7.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run a game day: hand your runbooks to someone else, induce a failure without telling them which, and have them respond. Time it. Note every place they got stuck or asked you a question — each one is a gap in the documentation. This is the real test of whether your runbooks work, and 'I ran a game day and the runbooks failed in three places, here is what I fixed' is a better story than 'I wrote runbooks.'
