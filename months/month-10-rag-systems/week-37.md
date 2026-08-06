# Week 37: Embeddings and Vector Databases

## Outcome

By Sunday you have a resumable ingestion pipeline and a tuned pgvector index, with the recall-versus-latency curve measured across index parameters.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Week 28 got you a working vector store. This week makes it operational.

The interview question — "HNSW or IVFFlat?" — deserves a real answer with
parameters, build times, and failure modes. The build-order detail (IVFFlat
clusters what it can see, so an index built before loading is useless) is the
kind of specific operational knowledge that marks you out.

Resumable ingestion is the other lesson. Ingesting 100k documents takes hours and
something will fail at hour two. Tracking processed IDs and skipping them on
restart is ordinary batch-job discipline and it is routinely absent from ML
pipelines.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **ANN indexing**
   1. Exact search cost, and when it is fine
   2. HNSW: hierarchical navigable small world graphs
   3. IVFFlat: inverted file with clustering
   4. The recall/latency/memory triangle
2. **Index parameters**
   1. HNSW: `m`, `ef_construction`, `ef_search`
   2. IVFFlat: `lists`, `probes`
   3. Build time versus query time versus recall
   4. **Build after loading**
3. **Filtering**
   1. Pre-filter versus post-filter
   2. Why post-filtering breaks top-k
   3. Indexed metadata and planner cooperation
   4. Permission filtering as the motivating case
4. **Ingestion at scale**
   1. Batch inserts, not row-at-a-time
   2. Resumability and state tracking
   3. Embedding batching and rate limits
   4. Idempotency
5. **Operational concerns**
   1. Index bloat under updates
   2. Reindexing without downtime
   3. Monitoring recall drift as the corpus grows

## Required Free Resources

- **Primary:** pgvector README and performance guide — https://github.com/pgvector/pgvector
- **Primary:** 'HNSW' — https://arxiv.org/abs/1603.09320 — read sections 1-3
- Jonathan Katz's pgvector performance posts — the most rigorous benchmarking available
- 'Billion-scale similarity search with GPUs' (FAISS) — https://arxiv.org/abs/1702.08734 — for the IVF background
- Supabase and Neon pgvector guides — practical tuning advice

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=37
```

1. **Schema with a generated tsvector column** (1h) — The setup that makes hybrid retrieval one query.
2. **`IngestionPipeline`, resumable** (2h) — Track processed IDs. It will fail partway; make that survivable.
3. **Batch embedding with rate limiting** (1h) — And a content-hash cache. Start caching now.
4. **Build both index types, measure** (1.5h) — Build time, index size, for each. Table it.
5. ****The build-order demonstration**** (45m) — Build IVFFlat before loading, measure recall. Then rebuild after. The gap is the lesson.
6. **The parameter sweep** (2h) — `ef_search` and `probes` against recall and p95 latency. The curve is the deliverable.
7. **`explain_search`** (1h) — Confirm index usage. Put the plan in the README.
8. **Filtering comparison** (1.5h) — Pre-filter versus post-filter at the same k. Show post-filtering under-returning.
9. **`index_health`** (1h) — Size, bloat, scan counts. Reused as a Month 11 agent tool.

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
v
e
c
t
o
r
_
s
t
o
r
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
i
n
g
e
s
t
i
o
n
.
p
y
```

## Tests To Write

`tests/test_rag_systems.py` week-37 blocks, marked `db`. Add: a test that an index built before loading has measurably worse recall than one built after.

## Portfolio Artifact

`src/vector_store.py`, `src/ingestion.py`, the index comparison table, and the recall/latency curve.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *HNSW versus IVFFlat — tradeoffs, parameters, and failure modes.* Include the build-order gotcha; it is the detail that shows operational experience.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Measure how retrieval recall degrades as rows are inserted into an existing index without a rebuild. Vector indexes bloat like any other index, nobody building RAG systems thinks about it, and you have the instincts to notice. Produce the curve — recall against inserted rows since last rebuild — and write up the maintenance implication. This is a small piece of genuinely novel-feeling analysis.
