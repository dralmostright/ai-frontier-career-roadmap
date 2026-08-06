# Month 07 Capstone: Semantic Search Engine

## Objective

Build a semantic search system on Postgres, beat a BM25 baseline, and prove it with hand-labeled relevance judgments and a measured recall/latency curve.

## Business Problem

Choose a corpus you can judge relevance for. Strong options: the PostgreSQL
documentation, a collection of engineering runbooks, arXiv abstracts in a field
you know, or your own technical notes.

**Prefer the PostgreSQL documentation.** You can label relevance accurately, the
queries are natural, and it sets up Month 10 and Month 11 directly.

State who searches this, what they are looking for, and what a bad result costs
them.

## Technical Requirements

- Ingestion pipeline: load, clean, chunk, embed, store
- PostgreSQL with pgvector; schema with a generated `tsvector` column
- Both HNSW and IVFFlat indexes, compared
- Dense search, BM25 search, and hybrid with RRF fusion
- 100+ hand-labeled queries with relevance judgments
- recall@k, MRR, and nDCG for all three retrieval modes
- The recall-versus-latency curve across index parameters
- `EXPLAIN ANALYZE` output in the docs, showing index usage
- A per-query-category breakdown showing where each method wins
- A simple search API or CLI

## Theory Requirements

The README must explain:

1. HNSW versus IVFFlat: how you chose, with your build times and index sizes.
2. Why hybrid retrieval beats either alone, with your category breakdown as
   evidence.
3. What chunking strategy you used and why.
4. Why you built this on Postgres rather than a dedicated vector database — the
   operational argument, made honestly including where it is weaker.

## System Design Requirements

- Ingestion separate from serving
- Resumable ingestion; 100k documents will fail partway at some point
- Index build as an explicit, documented step after loading
- Connection pooling
- The search query as a single SQL statement where possible

## Implementation Plan

**Days 1-2** — Corpus, ingestion, embedding, storage. Get data in first.

**Day 3** — Indexes. Build both, measure build time and size.

**Day 4** — The three retrieval modes.

**Day 5** — Label 100 queries. Tedious. Do it properly; this is the asset.

**Day 6** — Measurement: the metrics table, the parameter sweep, the category
breakdown.

**Day 7** — API, README, publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| BM25 baseline | Measured and reported |
| Dense beats BM25 overall | Or explained why not — either is a finding |
| Hybrid beats both | Expected; report the margin with a CI |
| recall@10 | > 0.85 on your labeled set |
| p95 search latency | < 100ms at your corpus size |
| Recall/latency curve | Plotted across `ef_search` |
| Index build time and size | Reported for both index types |
| Category breakdown | Shows where dense and lexical each win |

## Expected Repository Structure

```text
semantic-search-pgvector/
  README.md
  docker-compose.yml
  pyproject.toml
  Makefile
  sql/
    schema.sql
    indexes.sql
  src/
    ingest.py
    embed.py
    search.py
    evaluate.py
    api.py
  evals/
    queries.jsonl
    relevance.jsonl
  tests/
  docs/
    design.md
    index_comparison.md
    evaluation.md
    limitations.md
```

## README Requirements

Above the fold: one sentence, the retrieval metrics table (BM25 / dense /
hybrid), and `docker compose up && make ingest`.

Then: the corpus and use case; architecture diagram; the index comparison with
build times and sizes; the recall/latency curve; the metrics table with CIs; the
per-category breakdown; **the `EXPLAIN ANALYZE` output**; why Postgres; the
labeling methodology; limitations.

The query plan in the README is the detail that marks this as different. No other
semantic search portfolio project has one.

## Demo Requirements

`make demo` runs ten queries through all three retrieval modes and prints results side by side with scores and timings.

## Blog Post Requirement

Recommended. The angle: "Semantic Search on Postgres: What the Query Plan Told
Me." Nobody writes about pgvector from a DBA's perspective, and the index
tuning, build-order gotcha, and hybrid-in-one-query argument are all things you
can say credibly and others cannot.

## Interview Story

> "The embedding model lost to BM25 on exact-identifier queries — error codes,
> function names — which I only found because I broke the evaluation down by
> query category. So I built hybrid retrieval as a single SQL query against one
> Postgres table, no second system to keep in sync. Recall@10 went from 0.79 to
> 0.91."

45 seconds, and it demonstrates measurement, diagnosis, and an architectural
decision.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 7 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 8 | A corpus you can judge, with a stated use. |
| Technical execution | 8 | Three retrieval modes, two index types, one SQL query. |
| Evaluation rigor | 9 | **The differentiator.** Hand-labeled set, CIs, category breakdown. |
| Code quality | 8 | Resumable ingestion, clean separation. |
| Documentation | 9 | Index comparison and query plan are unusual and valuable. |
| Reproducibility | 8 | `docker compose up` and one make target. |
| Error analysis | 8 | The category breakdown is the error analysis. |
| Portfolio readiness | 8 | **First fusion project.** Feature it. |

**Overall target: 8.0+, with Evaluation Rigor and Documentation at 9.**

## Stretch Goals

1. **Hybrid in one SQL query.** The architectural argument, made concrete.
2. **pgvector versus FAISS** on identical data — recall, latency, memory, and
   operational complexity.
3. **Index maintenance analysis** — measure recall degradation as rows are
   inserted without a rebuild. Nobody does this and it is exactly your angle.
4. **A reranking stage** with a cross-encoder, and the quality/latency table.

## Limitations To State Honestly

- The relevance set is 100 queries labeled by one person. Inter-annotator
  agreement is unmeasured.
- The corpus is modest; index behavior differs at 10M+ rows.
- Embedding model chosen off the MTEB leaderboard rather than evaluated on this
  domain specifically.
- No permission filtering, which any real deployment would require.
- Chunking strategy was chosen with limited comparison; Week 38 does this
  properly.
