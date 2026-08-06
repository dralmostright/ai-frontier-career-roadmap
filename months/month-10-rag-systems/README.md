# Month 10: Retrieval-Augmented Generation

**Weeks 37-40 · Phase 4: LLM Engineering and Applied AI · Lab: `bootstrap/rag-systems/`**

---

## The Month In One Sentence

Build RAG the way someone who has to operate it builds it: on Postgres, with permission filtering, and with an evaluation harness that produces a number.

## Why This Month Exists

Phase 4 is where the work becomes directly employable. Most AI engineering job
descriptions are describing this month.

It is also where the market is most saturated with weak portfolios. Nearly every
candidate has "a RAG chatbot," and nearly all of them share three weaknesses: no
evaluation, no permission model, and a hosted vector service the author cannot
reason about.

Yours differs on all three, and the differences are the interview story. The
evaluation harness in particular is the thing — being able to say "faithfulness
is 0.87 on a 200-question labeled set, and here is the breakdown by question
category" puts you in a different conversation from "it gives good answers."

Permission-aware retrieval is the detail nobody thinks about and every real
deployment requires. Post-filtering breaks top-k; pre-filtering needs indexed
metadata. Raising that unprompted in a system design interview is a strong
signal.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 37 | Embeddings and Vector Databases | `vector_store.py`, `ingestion.py` — pgvector at scale |
| 38 | Chunking, Retrieval, Reranking | `chunking.py`, `retrieval.py`, `reranker.py` + the strategy comparison |
| 39 | RAG Evaluation | `rag_eval.py` + a 200-question labeled eval set |
| 40 | Production RAG API | The Month 10 capstone — a served, observable, evaluated RAG system |

**Capstone:** Enterprise Knowledge Assistant — production-style RAG on PostgreSQL with permission filtering and a 200-question evaluation harness.

## The Through-Lines

**Retrieval quality caps everything.** If recall@k is 0.6, the generator sees no
supporting evidence 40% of the time and no prompt engineering fixes it. Measure
retrieval separately from generation.

**Hybrid beats either alone.** Week 28's finding, now with reranking on top.

**Postgres is the platform.** Hybrid retrieval in one SQL statement against one
table is a real architectural advantage, and it comes from your background.

**Evaluation, always.** Week 39 inherits the Week 36 methodology: labeled set,
validated judge, confidence intervals, per-category breakdown.

## Time and Compute

15-20 hours per week. No GPU needed. API costs are real from this month — budget $20-40/month and cache aggressively. `make db-up` for Postgres.

## Files

```text
month-10-rag-systems/
  README.md      you are here
  week-37.md     embeddings and vector databases
  week-38.md     chunking, retrieval, reranking
  week-39.md     rag evaluation
  week-40.md     production rag api
  capstone.md    enterprise knowledge assistant
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 39.** The evaluation harness is the differentiator. Week 37 can be compressed since Week 28 covered much of it.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| No labeled eval set | Cannot state a number | 200 questions, hand-labeled. Tedious and non-negotiable. |
| Not separating retrieval from generation metrics | 'The answer was wrong' is unactionable | recall@k and faithfulness, separately. |
| Post-filtering by permission | Asked for 10, served 3 | Filter inside the query, with indexed metadata. |
| No unanswerable questions in the eval set | Cannot measure refusal | 10% unanswerable. Refusal is a measured behavior. |
| Uncached LLM calls during development | Surprising API bill | Content-hash cache from day one. |
| Retrieving too much context | Slower, more expensive, and worse answers | Irrelevant context distracts. Measure context relevance. |

## Advancement

Before Month 11, you should be able to, without notes:

- [ ] Explain HNSW vs IVFFlat with parameters, build order, and failure modes
- [ ] Diagnose 'retrieval found it but the answer is wrong' correctly
- [ ] Design a RAG evaluation harness from scratch
- [ ] Explain permission-aware retrieval and why post-filtering breaks
- [ ] State your system's faithfulness score and hallucination rate
- [ ] Point at a production-style RAG system with a 200-question eval set

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 11 — Agent Engineering. The flagship month. Give it your best.
