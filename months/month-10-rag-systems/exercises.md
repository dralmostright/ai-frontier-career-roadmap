# Month 10 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 37 — Embeddings and Vector Databases

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 37.1 | Schema with a generated tsvector column | 1h | Medium |
| 37.2 | `IngestionPipeline`, resumable | 2h | Hard |
| 37.3 | Batch embedding with rate limiting | 1h | Medium |
| 37.4 | Build both index types, measure | 1.5h | Medium |
| 37.5 | **The build-order demonstration** | 45m | Medium |
| 37.6 | The parameter sweep | 2h | Hard |
| 37.7 | `explain_search` | 1h | Medium |
| 37.8 | Filtering comparison | 1.5h | Hard |
| 37.9 | `index_health` | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 37.E1 | Measure recall degradation as rows are inserted without a rebuild | 2.5h | **Highest** — nobody does this and it is exactly your angle |
| 37.E2 | Compare pgvector against FAISS and Qdrant on identical data | 3h | High |
| 37.E3 | Implement binary quantization and measure the memory/recall tradeoff | 2.5h | High — a real technique for large indexes |

## Week 38 — Chunking, Retrieval, Reranking

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 38.1 | `fixed_size_chunks` with overlap | 1h | Easy |
| 38.2 | `recursive_chunks` | 1.5h | Medium |
| 38.3 | `structural_chunks` for markdown | 1.5h | Medium |
| 38.4 | `semantic_chunks` | 1.5h | Hard |
| 38.5 | `add_context_headers` | 45m | Easy |
| 38.6 | `lexical_retrieve` with BM25 | 1h | Medium |
| 38.7 | `reciprocal_rank_fusion` and `hybrid_retrieve` | 1.5h | Medium |
| 38.8 | `CrossEncoderReranker` | 1.5h | Medium |
| 38.9 | `lost_in_the_middle_reorder` | 45m | Easy |
| 38.10 | **`compare_strategies`** | 2h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 38.E1 | Contextual retrieval: prepend an LLM-generated chunk summary before embedding | 3h | High — Anthropic's technique, measurable gains |
| 38.E2 | Parent-document retrieval: search small chunks, return larger parents | 2h | High — often the best of both |
| 38.E3 | Query classification to route between dense and lexical | 2.5h | High — uses your category breakdown |

## Week 39 — RAG Evaluation

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 39.1 | Design the eval set schema | 45m | Easy |
| 39.2 | `build_eval_set_from_documents` | 1.5h | Medium |
| 39.3 | **Hand-label 200 questions** | 4h | Medium |
| 39.4 | `recall_at_k`, `precision_at_k`, `mean_reciprocal_rank`, `ndcg_at_k` | 1.5h | Medium |
| 39.5 | `faithfulness` | 2h | Hard |
| 39.6 | `answer_relevance`, `context_relevance` | 1h | Medium |
| 39.7 | `citation_accuracy` | 1h | Medium |
| 39.8 | `refusal_correctness` | 1h | Medium |
| 39.9 | `RAGEvaluator` with caching and CIs | 1.5h | Medium |
| 39.10 | `error_analysis` | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 39.E1 | Validate your faithfulness judge against 50 hand-labeled examples | 2h | **Highest** — an unvalidated judge is decoration |
| 39.E2 | Measure inter-annotator agreement by relabeling 30 questions a week later | 1.5h | High — honest about your own label noise |
| 39.E3 | Build the refusal tradeoff curve: threshold against hallucination and over-refusal | 2h | High — the mature answer to a real design question |

## Week 40 — Production RAG API

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 40.1 | `build_prompt` with a delimited context block | 1h | Medium |
| 40.2 | `generate_grounded` with citations | 1.5h | Medium |
| 40.3 | `should_refuse` | 1h | Medium |
| 40.4 | `create_app` with all endpoints | 1.5h | Medium |
| 40.5 | Streaming responses | 1.5h | Medium |
| 40.6 | **Permission filtering** | 2h | Hard |
| 40.7 | `instrument` with the RAG metric set | 1.5h | Medium |
| 40.8 | `ResponseCache` with ingestion invalidation | 1h | Medium |
| 40.9 | Cost accounting per request | 1h | Easy |
| 40.10 | Wire the eval harness into CI | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 40.E1 | Row-level security for multi-tenant isolation, with a test proving cross-tenant leakage is impossible | 3h | **Highest** — this is a serious differentiator |
| 40.E2 | Prompt caching to cut cost; measure the saving | 2h | High |
| 40.E3 | A Grafana dashboard for the RAG metrics | 2h | High — previews Week 56 |

---

## If You Finish Early

Priority: Week 40's row-level security with a proven-isolation test (**the strongest differentiator in this month**), Week 39's judge validation, Week 37's index-degradation measurement. All three are things nobody else's RAG project will have.
