# Week 26: Word Embeddings

## Outcome

By Sunday you can work fluently with embedding spaces: similarity, nearest neighbors, analogies, visualization, and bias probing.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Embeddings are the substrate for everything in Months 10 and 11. This week is
about developing intuition for the space rather than about a specific algorithm.

The interview-relevant parts: what cosine similarity actually measures over
learned representations, why embedding models normalize their outputs, and the
limitations — negation being the important one. "The database is healthy" and
"the database is not healthy" embed close together, which is a real problem for
any retrieval system where correctness flips on a negation.

The bias material matters too. Embeddings encode the statistical structure of
their training data including its prejudices, and being able to demonstrate that
on a real model is a good, concrete answer to a fairness question.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 6.5 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Distributional semantics**
   1. 'You shall know a word by the company it keeps'
   2. Co-occurrence matrices and their factorization
   3. Why dense beats sparse
2. **Embedding geometry**
   1. Cosine similarity over learned spaces
   2. Why models normalize outputs
   3. Analogies as vector arithmetic, and how well it actually works
3. **Static versus contextual**
   1. Word2Vec and GloVe give one vector per word
   2. The polysemy problem: 'bank'
   3. Why contextual embeddings replaced them
4. **Sentence embeddings**
   1. Pooling strategies: mean, CLS, max
   2. Why naive BERT CLS embeddings are poor for similarity
   3. Sentence-BERT and the contrastive fix
5. **Limitations**
   1. Negation: the failure that matters most for retrieval
   2. Bias, and how to probe for it
   3. Domain mismatch

## Required Free Resources

- **Primary:** Jay Alammar, 'The Illustrated Word2vec' — https://jalammar.github.io/illustrated-word2vec/
- **Primary:** Sentence Transformers docs — https://www.sbert.net/
- CS224N lecture 1-2 (word vectors) — https://web.stanford.edu/class/cs224n/
- 'Man is to Computer Programmer as Woman is to Homemaker?' — https://arxiv.org/abs/1607.06520 — the bias paper
- MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard — how embedding models are actually compared

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=26
```

1. **Load pretrained embeddings and explore** (1h) — GloVe or a sentence transformer. Nearest neighbors for 20 words.
2. **`nearest_neighbors` using Week 1's `top_k_similar`** (45m) — Your own function, at scale.
3. **Analogy arithmetic** (1h) — king - man + woman. Then find five that fail and characterize why.
4. **Visualize with PCA and t-SNE** (1h) — Week 2's PCA, applied. Note what each preserves.
5. **Pooling comparison** (1.5h) — Mean vs CLS vs max on a similarity task. The differences are large.
6. **The negation probe** (1h) — Measure similarity between a sentence and its negation. The result should worry you.
7. **Bias probing** (1.5h) — WEAT-style association tests on a real model.
8. **Domain mismatch demo** (45m) — General-purpose embeddings on database error messages. Measure the degradation.

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
e
m
b
e
d
d
i
n
g
s
.
p
y
```

## Tests To Write

Add: a test that normalized embeddings have unit norm; that cosine similarity of a sentence with itself is 1.0; and a test documenting the negation failure — assert that a sentence and its negation have similarity above 0.8, with a comment explaining why this is a problem.

## Portfolio Artifact

`src/embeddings.py` and a notebook with the embedding-space visualization, the analogy successes and failures, the negation probe, and the bias analysis.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (20 min).** Recorded: *What does cosine similarity actually measure over learned embeddings, and what are its failure modes?* The negation answer is the one that shows you have used them.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Measure the quality-versus-dimension curve by truncating embeddings and re-measuring retrieval quality. Modern embedding models trained with Matryoshka loss degrade gracefully; older ones do not. This is the empirical answer to 'do I need 1536 dimensions?', and the storage saving at scale is substantial — directly relevant to your Month 10 index sizing.
