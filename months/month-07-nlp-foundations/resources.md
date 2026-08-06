# Month 07 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Karpathy, 'Let's build the GPT Tokenizer'** (Week 25) — https://www.youtube.com/watch?v=zduSFxRajkE
Two hours and definitive. Watch it, then build your own without looking.

**pgvector README and performance guide** (Week 28) — https://github.com/pgvector/pgvector
Short, and it is the source for every index decision you will defend.

**'Introduction to Information Retrieval'** (Week 28, free) — https://nlp.stanford.edu/IR-book/
Chapters 6 and 8. BM25 and evaluation metrics, done properly.

---

## Week 25 — Text Preprocessing and Tokenization

- **Primary:** Karpathy, 'Let's build the GPT Tokenizer' — https://www.youtube.com/watch?v=zduSFxRajkE — two hours, and it is the definitive treatment. Watch, then build your own.
- **Primary:** Hugging Face NLP course, tokenizers chapter — https://huggingface.co/learn/nlp-course/chapter6/1
- 'Neural Machine Translation of Rare Words with Subword Units' (Sennrich et al.) — https://arxiv.org/abs/1508.07909 — the original BPE paper
- tiktoken source — https://github.com/openai/tiktoken — read after building yours
## Week 26 — Word Embeddings

- **Primary:** Jay Alammar, 'The Illustrated Word2vec' — https://jalammar.github.io/illustrated-word2vec/
- **Primary:** Sentence Transformers docs — https://www.sbert.net/
- CS224N lecture 1-2 (word vectors) — https://web.stanford.edu/class/cs224n/
- 'Man is to Computer Programmer as Woman is to Homemaker?' — https://arxiv.org/abs/1607.06520 — the bias paper
- MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard — how embedding models are actually compared
## Week 27 — Word2Vec and Negative Sampling

- **Primary:** 'Distributed Representations of Words and Phrases' (Mikolov et al.) — https://arxiv.org/abs/1310.4546 — the negative sampling paper
- **Primary:** 'word2vec Explained' (Goldberg and Levy) — https://arxiv.org/abs/1402.3722 — the clearest derivation of the negative sampling objective
- CS224N lecture 2 — https://web.stanford.edu/class/cs224n/
- Chris McCormick, 'Word2Vec Tutorial - Negative Sampling' — good, practical
## Week 28 — Classical NLP Tasks and Semantic Search

- **Primary:** pgvector README, including the performance section — https://github.com/pgvector/pgvector
- **Primary:** 'Introduction to Information Retrieval' (Manning et al., free) — https://nlp.stanford.edu/IR-book/ — chapters 6 and 8 for TF-IDF and evaluation
- Sentence Transformers semantic search — https://www.sbert.net/examples/applications/semantic-search/README.html
- 'HNSW' paper — https://arxiv.org/abs/1603.09320 — read the intuition sections
- Jo Kristian Bergum's writing on hybrid retrieval — consistently the most practical material on this topic

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| PyTorch | https://pytorch.org/docs/stable/ | Everything |
| d2l.ai | https://d2l.ai/ | The primary textbook |
| Hugging Face | https://huggingface.co/docs | Months 7+ |
| pgvector | https://github.com/pgvector/pgvector | Month 7 capstone |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| Sentence Transformers | https://www.sbert.net/ | Weeks 26-28 |
| tiktoken | https://github.com/openai/tiktoken | Week 25 comparison |
| psycopg | https://www.psycopg.org/psycopg3/docs/ | Week 28 |

---

## Deliberately Omitted

- **RNNs, LSTMs, GRUs.** Historically important, displaced by attention. Know
  the vanishing-gradient-over-time problem and that attention solved it.
- **Parsing, POS tagging, NER as classical pipelines.** Largely subsumed by
  LLMs. Know the task names.
- **Machine translation as a subfield.** The transformer paper came from it;
  that is the relevant history.
- **Topic modeling (LDA).** Superseded by embedding clustering for most uses.
