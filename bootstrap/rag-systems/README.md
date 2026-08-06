# rag-systems

**Weeks 37-40 · Month 10 · Capstone: Enterprise Knowledge Assistant**

Retrieval-augmented generation, built the way someone who has to operate it
would build it: on PostgreSQL, with a real evaluation harness, and with the
permission model that every demo omits.

---

## Why This Lab Exists

"I built a RAG chatbot" is the single most common line in an AI engineering
portfolio, and it carries almost no signal. Nearly all of those projects share
three weaknesses:

1. **No evaluation.** The author cannot state how good it is.
2. **No permission filtering.** Every document is visible to every user, which
   makes it undeployable at any real company.
3. **Hosted vector service, no understanding.** The author cannot explain what
   the index is doing or what it costs.

Yours will differ on all three, and the differences are the interview story.
You are building it on Postgres with pgvector deliberately: it is your home
turf, it is what most companies actually have, and choosing it lets you talk
credibly about index maintenance, bloat, and query plans — which nobody else
interviewing for these roles can do.

---

## Layout

```text
rag-systems/
  src/
    ingestion.py     W37  loaders, cleaning, metadata extraction
    chunking.py      W38  fixed, recursive, semantic, and structural strategies
    vector_store.py  W37  pgvector: schema, indexes, ANN search, hybrid queries
    retrieval.py     W38  dense, lexical (BM25), hybrid, RRF fusion
    reranker.py      W38  cross-encoder reranking
    generation.py    W39  prompt assembly, citation grounding, refusal
    rag_eval.py      W39  retrieval and generation metrics, the labeled set
    api.py           W40  FastAPI service, streaming, observability
  evals/
    questions.jsonl        the 200-question labeled set — the real asset
    relevance_labels.jsonl
  tests/
  docker-compose.yml       Postgres + pgvector for this lab
```

---

## The Week 37 Index Decision

You will be asked "HNSW or IVFFlat?" in an interview. Have the real answer.

| | HNSW | IVFFlat |
| --- | --- | --- |
| Build time | Slow | Fast |
| Memory | High | Low |
| Query speed | Faster | Slower |
| Recall at equal speed | Better | Worse |
| Needs training data | No | Yes — build after loading |
| Incremental inserts | Good | Degrades; needs periodic rebuild |

Default to HNSW unless memory is constrained or you rebuild frequently. The
detail that shows operational experience: IVFFlat's `lists` parameter should
be roughly `rows/1000` for up to 1M rows and `sqrt(rows)` beyond, and building
the index *before* loading data produces a useless index. That last one is a
real, common production mistake.

---

## The Evaluation Set Is The Deliverable

Two hundred labeled questions. Build them by hand. This is the most tedious
and most valuable work in Month 10.

For each question, record: the question, the ground-truth answering
chunk(s), a reference answer, a difficulty tag, and a category tag. Include
deliberately unanswerable questions — roughly 10% — because the most important
behavior of a production RAG system is refusing to answer when the context
does not support one.

Metrics to report, all of them:

| Layer | Metric | What it catches |
| ----- | ------ | --------------- |
| Retrieval | recall@k | Is the answer even in the context? |
| Retrieval | MRR / nDCG | Is it ranked highly? |
| Generation | faithfulness | Is the answer supported by the retrieved text? |
| Generation | answer relevance | Does it address the question asked? |
| Generation | citation accuracy | Do the citations point at the right chunks? |
| System | refusal rate on unanswerable | Does it decline when it should? |
| System | p50/p95 latency, cost per query | Can you afford to run it? |

The distinction between retrieval and generation metrics is what makes the
system debuggable. "The answer was wrong" is not actionable. "Recall@5 was
0.94 but faithfulness was 0.61, so retrieval is fine and the generation step
is inventing content" is.

---

## Milestones

| Week | You can... |
| ---- | ---------- |
| 37 | Build vector search on pgvector and defend your index choice |
| 38 | Show empirically which chunking strategy wins on your corpus, and why |
| 39 | State your system's faithfulness score and hallucination rate |
| 40 | Serve it with streaming, tracing, and per-query cost accounting |

---

## Interview Drills

| Week | Drill |
| ---- | ----- |
| 37 | HNSW vs IVFFlat. Include the parameters and the failure modes. |
| 38 | Retrieval returns the right document but the answer is wrong. Diagnose. |
| 39 | Design an evaluation harness for a RAG system with no ground truth. |
| 40 | Design RAG over 10M documents at 1k QPS. Include permissions and cost. |

On that last one: permission-aware retrieval is the part every candidate
forgets. Filtering after retrieval breaks top-k (you asked for 10 and got 3);
filtering inside the index query requires the metadata to be indexed too. Say
that unprompted and you have distinguished yourself.

---

## Capstone

Enterprise Knowledge Assistant. See `months/month-10-rag-systems/capstone.md`.
