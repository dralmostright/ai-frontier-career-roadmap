# Month 10 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Hamel Husain, 'Your AI product needs evals'** — https://hamel.dev/blog/posts/evals/
Read again, with RAG specifically in mind. It is the most practical writing on
this subject anywhere.

**pgvector README and performance guide** — https://github.com/pgvector/pgvector
Every index decision you defend comes from here.

**'Lost in the Middle'** — https://arxiv.org/abs/2307.03172
Short, and it changes how you order retrieved context.

**Anthropic, 'Contextual Retrieval'** — https://www.anthropic.com/news/contextual-retrieval
A measured technique with reported gains, and a good replication target.

---

## Week 37 — Embeddings and Vector Databases

- **Primary:** pgvector README and performance guide — https://github.com/pgvector/pgvector
- **Primary:** 'HNSW' — https://arxiv.org/abs/1603.09320 — read sections 1-3
- Jonathan Katz's pgvector performance posts — the most rigorous benchmarking available
- 'Billion-scale similarity search with GPUs' (FAISS) — https://arxiv.org/abs/1702.08734 — for the IVF background
- Supabase and Neon pgvector guides — practical tuning advice
## Week 38 — Chunking, Retrieval, Reranking

- **Primary:** 'Lost in the Middle' — https://arxiv.org/abs/2307.03172 — short, and the finding is actionable
- **Primary:** Sentence Transformers cross-encoder docs — https://www.sbert.net/examples/applications/cross-encoder/README.html
- 'Reciprocal Rank Fusion' (Cormack et al.) — the original RRF paper; k=60 comes from here
- 'Precise Zero-Shot Dense Retrieval without Relevance Labels' (HyDE) — https://arxiv.org/abs/2212.10496
- Anthropic, 'Contextual Retrieval' — https://www.anthropic.com/news/contextual-retrieval — the context-header idea, measured
## Week 39 — RAG Evaluation

- **Primary:** RAGAS documentation — https://docs.ragas.io/ — read the metric definitions, then implement your own
- **Primary:** Hamel Husain on evals — https://hamel.dev/blog/posts/evals/ — reread with RAG in mind
- 'ARES: An Automated Evaluation Framework for RAG' — https://arxiv.org/abs/2311.09476
- Anthropic, 'Building effective agents' — https://www.anthropic.com/engineering/building-effective-agents — the evaluation section applies here too
## Week 40 — Production RAG API

- **Primary:** FastAPI streaming and background tasks — https://fastapi.tiangolo.com/
- **Primary:** PostgreSQL row-level security — https://www.postgresql.org/docs/current/ddl-rowsecurity.html — the clean answer to multi-tenant filtering
- prometheus-client Python docs — https://prometheus.github.io/client_python/
- Anthropic prompt caching — https://docs.claude.com/en/docs/build-with-claude/prompt-caching — a real cost lever for RAG
- Google SRE Book, chapter on monitoring — https://sre.google/sre-book/monitoring-distributed-systems/ — apply the four golden signals here

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| pgvector | https://github.com/pgvector/pgvector | Months 10-11 |
| FastAPI | https://fastapi.tiangolo.com/ | Serving |
| Claude API | https://docs.claude.com/ | Months 10-12 |
| Hugging Face PEFT | https://huggingface.co/docs/peft/index | Month 12 |
| pytest | https://docs.pytest.org/ | The workspace |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| RAGAS | https://docs.ragas.io/ | Week 39 reference |
| Sentence Transformers | https://www.sbert.net/ | Embedding and reranking |
| Prometheus | https://prometheus.io/docs/ | Week 40 |

---

## Deliberately Omitted

- **LangChain / LlamaIndex as a dependency.** Read their source to see how they
  structure things, then build yours directly. Framework-shaped portfolio
  projects are hard to distinguish from tutorials.
- **Graph RAG.** Interesting, and a substantial additional scope. Know it exists
  and what it is for.
- **Multi-hop and agentic retrieval.** Month 11 covers the agent side.
- **Fine-tuning the embedding model.** Week 26's stretch goal touched it;
  Month 12 covers fine-tuning properly.
