# Month 10 Capstone: Enterprise Knowledge Assistant

## Objective

Build a RAG system that could plausibly be deployed at a company: permission-aware, observable, cost-tracked, and measured against a hand-labeled evaluation set.

## Business Problem

Pick a corpus with a real access-control story. Good options: an engineering
knowledge base with team-scoped documents, a policy and runbook collection with
role-based visibility, or a documentation set with public and internal tiers.

The access-control dimension is not decoration. It is what makes the project
resemble a real deployment and it is what most portfolio RAG systems cannot do.

State who uses this, what question they are asking, and what a confidently wrong
answer costs them.

## Technical Requirements

- Resumable ingestion with provenance and permission metadata
- PostgreSQL + pgvector, HNSW index built after loading, parameters tuned
- Hybrid retrieval (dense + BM25 + RRF) in a single SQL query
- Cross-encoder reranking with the latency cost measured
- Citation-grounded generation with refusal
- **Permission-aware retrieval**, pre-filtered, with a test proving isolation
- FastAPI with streaming, health/readiness, and Prometheus metrics
- Response caching with ingestion invalidation
- Cost tracking per request
- **200-question labeled eval set**, 10% unanswerable
- Full metric suite with confidence intervals and per-category breakdown
- The eval harness in CI, gating on regression

## Theory Requirements

The README must explain:

1. Index choice, with your build times, sizes, and the recall/latency curve.
2. Chunking strategy, chosen by measurement, with the comparison table.
3. Why hybrid beats either method alone, with your category breakdown.
4. How permission filtering works, why post-filtering breaks top-k, and the
   query plan proving your filter is applied correctly.
5. How the faithfulness judge was validated, with the kappa.

## System Design Requirements

- Ingestion, indexing, and serving as separate concerns
- Stateless API; all state in Postgres
- Async request handling
- Structured logging with a trace ID, retrieved chunk IDs, scores, and cost
- Graceful degradation: if reranking fails, serve unreranked results and log it

## Implementation Plan

**Day 1** — Ingestion with permission metadata.

**Day 2** — Retrieval: hybrid in one query, reranking.

**Day 3** — Generation with citations and refusal.

**Days 4-5** — The eval set. 200 questions, labeled by hand. This is the bulk of
the work and the bulk of the value.

**Day 6** — Service: streaming, permissions, metrics, caching, cost.

**Day 7** — Measurement, README, CI, publish.

## Evaluation Plan

| Metric | Target |
| ------ | ------ |
| recall@5 | > 0.90 |
| MRR | > 0.75 |
| Faithfulness | > 0.85, with the judge's kappa reported |
| Citation accuracy | > 0.90 |
| Refusal on unanswerable | > 0.80, with the over-refusal rate also reported |
| p95 end-to-end latency | < 3s |
| Cost per query | Measured and reported |
| Cross-tenant leakage | Zero, proven by test |

Every number with a bootstrap confidence interval and a per-category breakdown.

## Expected Repository Structure

```text
enterprise-knowledge-assistant/
  README.md
  docker-compose.yml
  Dockerfile
  pyproject.toml
  Makefile
  .github/workflows/eval-gate.yml
  sql/
    schema.sql  indexes.sql  rls.sql
  src/
    ingest.py  chunk.py  embed.py  retrieve.py  rerank.py
    generate.py  api.py  metrics.py  cache.py
  evals/
    questions.jsonl        200 labeled questions
    judge_validation.jsonl 50 hand-labeled faithfulness judgments
    run_eval.py
    results/
  tests/
    test_retrieval.py  test_permissions.py  test_generation.py
  docs/
    design.md  evaluation.md  index_tuning.md  limitations.md
```

## README Requirements

Above the fold: one sentence, **the metrics table**, and `docker compose up`.

Then: the problem and the cost of a wrong answer; architecture diagram; the
index tuning results with the recall/latency curve; the chunking comparison; why
hybrid, with the category breakdown; **permission filtering with the query plan**;
the eval methodology including judge validation; the full metrics table with CIs;
the error taxonomy; cost per query; limitations.

**Lead with the metrics table.** Most RAG projects have no numbers at all. Yours
opens with eight of them, each with a confidence interval.

## Demo Requirements

`docker compose up && make demo` runs ten questions — including two unanswerable and two requiring permission filtering — and prints answers with citations, retrieval scores, latency, and cost.

## Blog Post Requirement

**Post #3 is due this month.** Working title: "Your RAG System Has No
Evaluation and That's a Production Incident Waiting."

The argument: shipping a retrieval system with no measured faithfulness is
shipping a system whose failure mode is confident wrongness, and that is an
operational risk, not an ML nicety. Frame it from the reliability perspective —
that framing is yours and it is not being written by others.

## Interview Story

> "Most RAG demos have no evaluation. Mine has 200 labeled questions including
> 20 unanswerable, and I validated the faithfulness judge against human labels at
> kappa 0.71. Faithfulness is 0.87. It also does permission-aware retrieval —
> filtered inside the index scan, not after, so top-k still returns k — and
> there's a test proving cross-tenant leakage is impossible."

60 seconds, and every clause is checkable.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 10 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 8 | A real access-control story. |
| Technical execution | 8 | Hybrid in one query, permission pre-filtering, reranking. |
| Evaluation rigor | 10 | **Target 10.** 200 labeled questions, validated judge, CIs, breakdowns. |
| Code quality | 8 | Clean separation, tested. |
| Documentation | 9 | Metrics table, query plan, methodology. |
| Reproducibility | 8 | `docker compose up` works. |
| Error analysis | 9 | The three-bucket taxonomy with counts. |
| Portfolio readiness | 9 | **Flagship #4.** Feature it. |

**Overall target: 8.5+. This is a flagship. Evaluation Rigor at 10.**

## Stretch Goals

1. **Row-level security with a proven-isolation test.** The strongest
   differentiator available in this project.
2. **Contextual retrieval** (Week 38's extension) measured on your eval set.
3. **A cost optimization pass**: prompt caching, a cheaper reranker, and the
   before/after cost per query.
4. **An eval-set quality analysis**: relabel 30 questions a week later and report
   your own agreement with yourself.

## Limitations To State Honestly

- The eval set is 200 questions labeled by one person; inter-annotator agreement
  is estimated from a self-relabeling exercise only.
- Faithfulness is measured by an LLM judge validated at kappa 0.71, which means
  roughly a third of disagreements with a human remain unexplained.
- Corpus size is modest; index behavior and latency differ substantially above
  10M chunks.
- No multi-hop reasoning; questions requiring synthesis across many documents
  fail and are tagged as such in the eval set.
- Permission model is document-level, not field-level.
