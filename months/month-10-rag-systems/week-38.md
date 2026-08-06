# Week 38: Chunking, Retrieval, Reranking

## Outcome

By Sunday you can show empirically which chunking and retrieval strategies win on your corpus, and you have a reranking stage with its quality/latency tradeoff measured.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Chunking caps recall before the embedding model gets a say, and most projects
choose a strategy by default rather than by measurement. This week you measure.

The reranking material is the highest-leverage single improvement available in a
RAG pipeline, and the bi-encoder versus cross-encoder distinction is a clean
interview question: bi-encoders embed separately so documents can be precomputed;
cross-encoders process the pair jointly so attention runs across both, which is
far more accurate and cannot be precomputed. That is the entire reason for a
two-stage architecture.

The lost-in-the-middle reordering is a free improvement most people have not
heard of: models attend more to the start and end of a long context, so ordering
results best-first is not optimal.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Chunking strategies**
   1. Fixed size with overlap: the baseline, and why overlap exists
   2. Recursive: split on the largest natural boundary that fits
   3. Semantic: split where sentence embeddings diverge
   4. Structural: headings, sections, code blocks — never split a table
   5. Context headers, and the recall they buy for almost nothing
2. **Retrieval strategies**
   1. Dense: strong on paraphrase, weak on exact terms
   2. Lexical/BM25: exactly complementary
   3. Hybrid with reciprocal rank fusion, and why rank-based fusion needs no score normalization
   4. Query expansion and HyDE
3. **Reranking**
   1. Bi-encoder versus cross-encoder, and why the distinction forces two stages
   2. Retrieve 50, rerank, keep 5
   3. The quality/latency tradeoff, measured
   4. LLM reranking, and when the cost is justified
4. **Context assembly**
   1. Lost in the middle: models attend to the ends
   2. Deduplication of near-identical chunks
   3. Context budget and truncation by relevance

## Required Free Resources

- **Primary:** 'Lost in the Middle' — https://arxiv.org/abs/2307.03172 — short, and the finding is actionable
- **Primary:** Sentence Transformers cross-encoder docs — https://www.sbert.net/examples/applications/cross-encoder/README.html
- 'Reciprocal Rank Fusion' (Cormack et al.) — the original RRF paper; k=60 comes from here
- 'Precise Zero-Shot Dense Retrieval without Relevance Labels' (HyDE) — https://arxiv.org/abs/2212.10496
- Anthropic, 'Contextual Retrieval' — https://www.anthropic.com/news/contextual-retrieval — the context-header idea, measured

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=38
```

1. **`fixed_size_chunks` with overlap** (1h) — Count tokens, not characters.
2. **`recursive_chunks`** (1.5h) — Paragraph, sentence, word, character.
3. **`structural_chunks` for markdown** (1.5h) — Never split a code block or table. There is a test.
4. **`semantic_chunks`** (1.5h) — Then measure whether it beats recursive. Often it does not.
5. **`add_context_headers`** (45m) — Cheap, and usually several points of recall.
6. **`lexical_retrieve` with BM25** (1h) — Via the tsvector column.
7. **`reciprocal_rank_fusion` and `hybrid_retrieve`** (1.5h) — One SQL query if you can.
8. **`CrossEncoderReranker`** (1.5h) — Retrieve 50, rerank, keep 5. Measure the latency cost.
9. **`lost_in_the_middle_reorder`** (45m) — Free improvement. Measure it.
10. ****`compare_strategies`**** (2h) — Every chunking strategy through the full pipeline. The deliverable table.

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
c
h
u
n
k
i
n
g
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
r
e
t
r
i
e
v
a
l
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
r
e
r
a
n
k
e
r
.
p
y
```

## Tests To Write

Week-38 blocks. `test_structural_chunking_keeps_code_blocks_whole` is the one that catches a real failure mode.

## Portfolio Artifact

The three modules plus the strategy comparison table — chunking strategy against recall@k, MRR, chunk count, and ingestion cost.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *Retrieval returns the right document but the answer is wrong. Diagnose it.* The answer walks the pipeline: was the right chunk retrieved, was it ranked highly, was it in the context window, did the model use it? Then: *Bi-encoder versus cross-encoder — why do you need both?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement contextual retrieval: before embedding each chunk, use a cheap model to generate a one-sentence description of how the chunk fits into its parent document, and prepend it. Anthropic reported substantial recall improvements from this. Measure it on your corpus and report whether it replicates — a replication attempt, positive or negative, is good Month 16 practice.
