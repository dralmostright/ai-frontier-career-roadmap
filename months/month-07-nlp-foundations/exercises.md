# Month 07 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 25 — Text Preprocessing and Tokenization

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 25.1 | Byte-level encoding and decoding | 1h | Medium |
| 25.2 | Naive BPE training | 1.5h | Medium |
| 25.3 | Optimized BPE training | 2h | Hard |
| 25.4 | `encode` applying the merge table | 1.5h | Hard |
| 25.5 | `save` / `load` | 45m | Easy |
| 25.6 | `compression_ratio` | 45m | Easy |
| 25.7 | `tokenization_pathologies` | 1h | Medium |
| 25.8 | Compare against tiktoken | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 25.E1 | Implement WordPiece and compare merge choices against BPE | 2.5h | High |
| 25.E2 | Train tokenizers at vocab 1k, 8k, 32k and plot compression vs size | 1.5h | High — the vocabulary-size tradeoff, measured |
| 25.E3 | Analyze tokenization of SQL and query plans | 1.5h | High — directly relevant to Month 11 |

## Week 26 — Word Embeddings

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 26.1 | Load pretrained embeddings and explore | 1h | Easy |
| 26.2 | `nearest_neighbors` using Week 1's `top_k_similar` | 45m | Easy |
| 26.3 | Analogy arithmetic | 1h | Medium |
| 26.4 | Visualize with PCA and t-SNE | 1h | Medium |
| 26.5 | Pooling comparison | 1.5h | Medium |
| 26.6 | The negation probe | 1h | Medium |
| 26.7 | Bias probing | 1.5h | Hard |
| 26.8 | Domain mismatch demo | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 26.E1 | Fine-tune a sentence embedding model with contrastive loss on domain text | 3h | High — previews Month 12 and directly useful for Month 11 |
| 26.E2 | Implement Matryoshka-style truncation and measure quality vs dimension | 2h | High — the practical answer to embedding storage cost |
| 26.E3 | Compare three embedding models on your own labeled set | 2h | High — the methodology matters more than the result |

## Week 27 — Word2Vec and Negative Sampling

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 27.1 | Build the vocabulary and co-occurrence pairs | 1.5h | Medium |
| 27.2 | The negative sampling distribution | 45m | Medium |
| 27.3 | Derive the objective on paper | 1h | Hard |
| 27.4 | Skip-gram forward and backward | 2h | Hard |
| 27.5 | Train on a real corpus | 2h | Medium |
| 27.6 | Evaluate with nearest neighbors and analogies | 1h | Medium |
| 27.7 | Ablate the number of negatives | 1h | Medium |
| 27.8 | Ablate the sampling distribution | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 27.E1 | Implement hierarchical softmax and compare against negative sampling | 3h | High — the other solution to the same problem |
| 27.E2 | Train on database documentation and inspect the domain-specific neighbors | 2h | High — directly useful, and a nice Month 11 asset |
| 27.E3 | Implement GloVe and compare against your skip-gram | 3h | Medium — count-based versus predictive |

## Week 28 — Classical NLP Tasks and Semantic Search

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 28.1 | TF-IDF text classification | 1.5h | Medium |
| 28.2 | BM25 implementation | 1.5h | Medium |
| 28.3 | Set up pgvector | 1h | Easy |
| 28.4 | Ingest and embed a corpus | 1.5h | Medium |
| 28.5 | Exact search, then HNSW | 1.5h | Medium |
| 28.6 | The index parameter sweep | 2h | Hard |
| 28.7 | `EXPLAIN ANALYZE` the search | 1h | Medium |
| 28.8 | Hand-label 100 queries | 2h | Medium |
| 28.9 | Measure recall@k, MRR, nDCG | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 28.E1 | Hybrid retrieval in one SQL query with RRF fusion | 2.5h | Highest — the architectural argument for Postgres |
| 28.E2 | Compare pgvector against FAISS on the same data | 2h | High — a real, defensible comparison |
| 28.E3 | Per-query-category breakdown showing where dense and lexical each win | 1.5h | High — the finding that makes the write-up interesting |

---

## If You Finish Early

Priority: Week 28's hybrid-in-one-SQL-query (the architectural argument), Week 26's domain fine-tuning of embeddings (useful in Month 11), Week 25's SQL tokenization analysis. Then start reading the Week 29 attention material early — Month 8 is the month to arrive at fresh.
