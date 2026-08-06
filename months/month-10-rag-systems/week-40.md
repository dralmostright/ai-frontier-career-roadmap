# Week 40: Production RAG API

## Outcome

By Sunday your RAG system is a running service with streaming, permission filtering, structured logging, Prometheus metrics, cost accounting, and the eval harness wired into CI.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The month's engineering payoff, and where your operational background shows.

Permission-aware retrieval is the part every demo omits and every real deployment
requires. Post-filtering breaks top-k; pre-filtering requires the permission
metadata to be indexed and the planner to use it. You can `EXPLAIN ANALYZE` that
and nobody else interviewing can.

The observability work is equally yours. The metrics that matter for a RAG system
are not obvious — retrieval score distribution as a drift signal, refusal rate as
a breakage signal, context truncation count as a silent-failure signal. Designing
that metric set is a system design answer most candidates cannot give.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 7 hours
- Project: 5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Service design**
   1. Streaming with server-sent events
   2. Liveness versus readiness, and why conflating them causes restart loops
   3. Graceful degradation when retrieval fails
2. **Permission-aware retrieval**
   1. Post-filter breaks top-k
   2. Pre-filter needs indexed metadata
   3. Row-level security as an alternative
   4. The multi-tenant case
3. **Observability for RAG**
   1. Latency split by stage: embed, retrieve, rerank, generate
   2. Retrieval score distribution as a drift signal
   3. Refusal rate as a breakage signal
   4. Context truncation count
   5. Tokens and cost per request
4. **Caching**
   1. Response caching by question and config hash
   2. Invalidation on ingestion
   3. Why a stale answer served confidently is worse than a slow one
5. **Cost control**
   1. Cost per query, measured
   2. Where the money actually goes
   3. Cheaper models for reranking and judging

## Required Free Resources

- **Primary:** FastAPI streaming and background tasks — https://fastapi.tiangolo.com/
- **Primary:** PostgreSQL row-level security — https://www.postgresql.org/docs/current/ddl-rowsecurity.html — the clean answer to multi-tenant filtering
- prometheus-client Python docs — https://prometheus.github.io/client_python/
- Anthropic prompt caching — https://docs.claude.com/en/docs/build-with-claude/prompt-caching — a real cost lever for RAG
- Google SRE Book, chapter on monitoring — https://sre.google/sre-book/monitoring-distributed-systems/ — apply the four golden signals here

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=40
```

1. **`build_prompt` with a delimited context block** (1h) — This is also your injection boundary. State that content inside is data.
2. **`generate_grounded` with citations** (1.5h) — Temperature 0. Validate citation indices.
3. **`should_refuse`** (1h) — Cheap pre-check on retrieval scores.
4. **`create_app` with all endpoints** (1.5h) — Including a correct liveness/readiness distinction.
5. **Streaming responses** (1.5h) — Server-sent events. Handle client disconnects.
6. ****Permission filtering**** (2h) — Pre-filter with indexed metadata. `EXPLAIN ANALYZE` it.
7. **`instrument` with the RAG metric set** (1.5h) — Design the metrics yourself before looking at examples.
8. **`ResponseCache` with ingestion invalidation** (1h) — Stale answers served confidently are the failure to avoid.
9. **Cost accounting per request** (1h) — Tokens and dollars, logged. You need this in Week 51.
10. **Wire the eval harness into CI** (1h) — Fail the build on a faithfulness regression. Previews Week 55.

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
a
g
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
g
e
n
e
r
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
r
a
g
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
a
p
i
.
p
y
```

## Tests To Write

Add: a test that a user without permission on a document never receives it in results, even when it is the top semantic match. That test is the one to point at in an interview.

## Portfolio Artifact

The Month 10 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (45 min).** **Recorded.** *Design RAG over 10 million documents at 1000 QPS.* Cover ingestion, index choice and sharding, permission filtering, caching, cost per query, the eval harness, and what breaks first. Permissions and cost are where you should be strongest.

**Behavioral (15 min).** Draft story #6: cross-team collaboration.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement multi-tenant isolation with PostgreSQL row-level security, and write a test that attempts cross-tenant retrieval and proves it returns nothing. Then `EXPLAIN ANALYZE` the filtered query to show the policy is applied in the index scan rather than after it. This is a genuinely strong artifact — it demonstrates security thinking, database depth, and the ability to prove a property rather than assert it.
