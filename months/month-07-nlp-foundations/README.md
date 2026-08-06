# Month 07: NLP Foundations

**Weeks 25-28 · Phase 3: NLP and Transformers · Lab: `bootstrap/llm-labs/`**

---

## The Month In One Sentence

Build tokenizers and embeddings from scratch, then fuse AI with your database expertise for the first time by building semantic search on pgvector.

## Why This Month Exists

Phase 3 is the core competency for the roles you are targeting, and this month
lays the groundwork.

Tokenization explains a surprising amount of LLM behavior — why arithmetic is
unreliable, why reversing strings is hard, why non-English text costs more, why
a trailing space breaks a completion. Being able to connect a tokenizer property
to an observed model behavior is a strong, specific interview signal.

Embeddings are the substrate for Months 10 and 11. Week 1's `cosine_similarity`
becomes real here.

**And this is your first AI+database project.** Build the Month 7 capstone on
PostgreSQL with pgvector, deliberately. It is your home turf, it is what most
companies actually have, and it lets you talk about index maintenance and query
plans in a retrieval interview — which nobody else can do.

## What You Build

| Week | Topic | Deliverable |
| --- | --- | --- |
| 25 | Text Preprocessing and Tokenization | `tokenizer.py` — a working byte-level BPE |
| 26 | Word Embeddings | `embeddings.py` — similarity, analogy, and bias probes |
| 27 | Word2Vec and Negative Sampling | `word2vec.py` — skip-gram with negative sampling, trained |
| 28 | Classical NLP Tasks and Semantic Search | The Month 7 capstone — semantic search on pgvector |

**Capstone:** Semantic Search Engine — embedding search over a real corpus on PostgreSQL and pgvector, with a lexical baseline and measured retrieval quality.

## The Through-Lines

**Similarity is still a dot product.** Week 1's function, now over learned
representations.

**Lexical baselines matter.** BM25 is strong and free. If your embedding pipeline
does not beat it, that is a finding, and a surprising number of RAG systems never
check.

**Postgres is the platform.** Everything retrieval-shaped in this course runs on
pgvector. That choice compounds across Months 7, 10, 11, and 15.

**Evaluation, again.** Week 28's relevance set is the same discipline as Week 11's
labeled data, and it is the direct ancestor of Week 39's RAG eval set.

## Time and Compute

15-20 hours per week. CPU is sufficient for Weeks 25-27. Sentence embedding models in Week 28 are small. Start the lab Postgres this month: `make db-up`.

## Files

```text
month-07-nlp-foundations/
  README.md      you are here
  week-25.md     text preprocessing and tokenization
  week-26.md     word embeddings
  week-27.md     word2vec and negative sampling
  week-28.md     classical nlp tasks and semantic search
  capstone.md    semantic search engine
  rubric.md      how this month is graded
  resources.md   everything, organized by week
  exercises.md   the full exercise list, including extras
```

## The One Week Not To Compress

**Week 28.** The capstone and the first fusion project. Weeks 26-27 can be compressed if you are comfortable with embeddings.

## Common Failure Modes

| Failure | Symptom | Fix |
| --- | --- | --- |
| No lexical baseline | Cannot tell whether embeddings helped | BM25 first. Always. |
| Building the ANN index before loading data | Index silently useless | IVFFlat clusters what it can see. Build after loading. |
| No relevance labels | Cannot measure retrieval at all | Hand-label 100 queries. Tedious and necessary. |
| Character-based chunk sizes | Wildly different context per document | Count tokens. |
| Using a hosted vector service | Discards your differentiator | pgvector. Deliberately. |

## Advancement

Before Month 8, you should be able to, without notes:

- [ ] Explain why tokenization breaks arithmetic and reversed strings
- [ ] Explain what cosine similarity measures over learned embeddings
- [ ] Derive why negative sampling replaces the full softmax
- [ ] Say when TF-IDF beats a neural model, and why
- [ ] Explain HNSW versus IVFFlat with parameters and failure modes
- [ ] Point at a semantic search engine on pgvector with measured recall@k

If two or more are shaky, take a catch-up week before advancing.

## Next

Month 8 — Transformers From First Principles. The most important month in the course for interview outcomes.
