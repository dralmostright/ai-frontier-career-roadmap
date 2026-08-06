# Week 27: Word2Vec and Negative Sampling

## Outcome

By Sunday you have implemented skip-gram with negative sampling from scratch and trained embeddings that produce sensible nearest neighbors.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The negative sampling derivation is the point. Computing a full softmax over a
50,000-word vocabulary for every training example is prohibitively expensive;
negative sampling replaces it with a binary classification against a handful of
sampled negatives, turning an O(V) operation into O(k).

That trick — replace an expensive normalization with a sampled approximation —
recurs throughout machine learning, and being able to derive why it works is a
good depth signal.

It is also good practice for Month 8. Training embeddings from scratch on a real
corpus, with a real loss and real convergence problems, is a smaller version of
what you will do in Week 35.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Skip-gram**
   1. Predict context from center word
   2. The window, and what it captures
   3. Why skip-gram beats CBOW on rare words
2. **The softmax problem**
   1. O(V) per example, with V in the tens of thousands
   2. Hierarchical softmax as one solution
   3. Negative sampling as the other
3. **Negative sampling**
   1. Reframe as binary classification: real pair versus sampled pair
   2. The objective, derived
   3. Why the unigram distribution raised to 3/4 works better than uniform
   4. How many negatives, and why 5-20
4. **Training details**
   1. Subsampling frequent words
   2. Dynamic window size
   3. Two embedding matrices, and which one you keep
5. **Evaluation**
   1. Intrinsic: analogies and similarity benchmarks
   2. Extrinsic: performance on a downstream task
   3. Why intrinsic scores can mislead

## Required Free Resources

- **Primary:** 'Distributed Representations of Words and Phrases' (Mikolov et al.) — https://arxiv.org/abs/1310.4546 — the negative sampling paper
- **Primary:** 'word2vec Explained' (Goldberg and Levy) — https://arxiv.org/abs/1402.3722 — the clearest derivation of the negative sampling objective
- CS224N lecture 2 — https://web.stanford.edu/class/cs224n/
- Chris McCormick, 'Word2Vec Tutorial - Negative Sampling' — good, practical

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=27
```

1. **Build the vocabulary and co-occurrence pairs** (1.5h) — With subsampling of frequent words.
2. **The negative sampling distribution** (45m) — Unigram^0.75. Verify it differs meaningfully from uniform.
3. **Derive the objective on paper** (1h) — Before implementing. It is a short derivation.
4. **Skip-gram forward and backward** (2h) — Two embedding matrices, dot product, sigmoid, BCE.
5. **Train on a real corpus** (2h) — text8 or a Wikipedia dump subset. Watch the loss.
6. **Evaluate with nearest neighbors and analogies** (1h) — Compare against pretrained GloVe.
7. **Ablate the number of negatives** (1h) — 1, 5, 20. Quality and training time.
8. **Ablate the sampling distribution** (45m) — Uniform vs unigram vs unigram^0.75.

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
w
o
r
d
2
v
e
c
.
p
y
```

## Tests To Write

Add: a test that trained embeddings place semantically related words closer than unrelated ones on a small hand-built set; and a test that the negative sampling distribution matches unigram^0.75 within tolerance.

## Portfolio Artifact

`src/word2vec.py`, trained embeddings, and the two ablation tables.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *Why negative sampling instead of a full softmax? Derive the objective.* Then: *Why is the sampling distribution raised to the 3/4 power?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Train embeddings on database documentation — PostgreSQL manual, error message catalogs, your own runbooks — and inspect the domain-specific neighborhoods. Do 'deadlock' and 'lock timeout' end up close? Does 'vacuum' cluster with maintenance terms? This is both an interesting result and a genuinely useful asset for Month 11's retrieval.
