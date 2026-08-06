# Week 28: Classical NLP Tasks and Semantic Search

## Outcome

By Sunday you have built text classification with a strong lexical baseline, and a semantic search engine on PostgreSQL with pgvector, measured against hand-labeled relevance judgments.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Two things.

**The baseline lesson.** TF-IDF with a linear model is fast, cheap, interpretable,
and frequently competitive. Knowing when it beats a neural model — small data,
narrow domain, exact-term-heavy queries — and *saying so* is a strong signal,
because it shows you choose on evidence rather than fashion.

**The first fusion project.** Semantic search on pgvector is where AI meets your
database expertise for the first time. Build it on Postgres deliberately, learn
the index tradeoffs properly, and you will be able to discuss ANN indexing,
recall tuning, and query plans in a Month 10 or Month 11 interview in a way
almost nobody else can.

The relevance-labeling work is tedious and it is the deliverable. An eval set is
worth more than a model.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7 hours
- Project: 4.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Lexical retrieval**
   1. TF-IDF, and what each term does
   2. BM25: saturation and length normalization
   3. Why BM25 is still a strong baseline in 2026
2. **Text classification**
   1. Bag of words, n-grams, and linear models
   2. When TF-IDF beats a transformer
   3. Feature interpretability as a real advantage
3. **Vector search**
   1. Exact search: O(n·d) and when it is fine
   2. Approximate nearest neighbors: the recall/latency tradeoff
   3. HNSW: graph-based, fast queries, high memory, incremental-friendly
   4. IVFFlat: cluster-based, fast build, low memory, needs rebuilding
4. **pgvector specifics**
   1. Distance operators and choosing one
   2. Index parameters: `m`, `ef_construction`, `ef_search`, `lists`, `probes`
   3. **Build the index after loading data**
   4. Metadata filtering, and why post-filtering breaks top-k
5. **Retrieval evaluation**
   1. recall@k as the ceiling on everything downstream
   2. MRR and nDCG
   3. Building a relevance set by hand

## Required Free Resources

- **Primary:** pgvector README, including the performance section — https://github.com/pgvector/pgvector
- **Primary:** 'Introduction to Information Retrieval' (Manning et al., free) — https://nlp.stanford.edu/IR-book/ — chapters 6 and 8 for TF-IDF and evaluation
- Sentence Transformers semantic search — https://www.sbert.net/examples/applications/semantic-search/README.html
- 'HNSW' paper — https://arxiv.org/abs/1603.09320 — read the intuition sections
- Jo Kristian Bergum's writing on hybrid retrieval — consistently the most practical material on this topic

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=28
```

1. **TF-IDF text classification** (1.5h) — Your Week 6 logistic regression on TF-IDF features. Establish the baseline.
2. **BM25 implementation** (1.5h) — Then compare against TF-IDF on retrieval.
3. **Set up pgvector** (1h) — `make db-up`. Schema, extension, table with a vector column.
4. **Ingest and embed a corpus** (1.5h) — Batch inserts. Row-at-a-time takes hours.
5. **Exact search, then HNSW** (1.5h) — Build the index *after* loading. Measure both.
6. **The index parameter sweep** (2h) — `ef_search` against recall and latency. The curve is the deliverable.
7. **`EXPLAIN ANALYZE` the search** (1h) — Confirm the index is used. Nobody else's RAG project has a query plan in the README.
8. **Hand-label 100 queries** (2h) — Tedious, necessary, and the real asset.
9. **Measure recall@k, MRR, nDCG** (1h) — Dense, lexical, and hybrid. The comparison table.

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
l
l
m
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
e
x
t
_
c
l
a
s
s
i
f
i
c
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
```

## Tests To Write

Add: a test that BM25 outperforms dense retrieval on exact-identifier queries and loses on paraphrase queries — the complementarity, demonstrated. Mark it `db`.

## Portfolio Artifact

The Month 7 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *HNSW versus IVFFlat — explain the tradeoff, the parameters, and the failure modes.* This is a question you should answer better than almost anyone.

**System design (30 min).** Design semantic search over 10 million documents with sub-100ms p95. Index choice, sharding, caching, and what breaks first.

**Behavioral (15 min).** Draft story #3: automation that removed toil.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement hybrid retrieval as a single SQL query — dense similarity and full-text ranking fused by reciprocal rank, in one statement against one table. Then write up the architectural argument: one system, one query, no synchronization problem between a vector store and a search engine. That argument is a genuinely good answer in a system design interview and it comes directly from your background.
