# Week 31: Encoder Models: BERT Concepts

## Outcome

By Sunday you understand masked language modeling and bidirectional attention, and you can articulate when to reach for an encoder rather than a decoder.

## Why This Matters For OpenAI/Anthropic-Level Interviews

This is the compressible week of Month 8, and it still matters for one reason:
"encoder or decoder?" is a real design question with a real answer, and
candidates who only know decoders answer it badly.

The short version: encoders see the whole sequence bidirectionally and produce
representations, so they are the right choice for classification, retrieval, and
reranking. Decoders are causal and generate. If your task is "score this
document against this query," a cross-encoder beats a generative model on cost
and often on quality — which is exactly the Week 38 reranking decision.

The MLM objective is also worth understanding as a contrast to next-token
prediction, because the difference explains why encoders cannot generate.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 6.5 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Bidirectional attention**
   1. No causal mask: every position sees every other
   2. Why this makes generation impossible
   3. What it buys for representation
2. **Masked language modeling**
   1. Mask 15%, predict the masked tokens
   2. The 80/10/10 corruption scheme and why
   3. Why MLM is less sample-efficient than next-token prediction
3. **BERT specifics**
   1. The CLS token and pooling
   2. Segment embeddings and next-sentence prediction, and why NSP was later dropped
   3. RoBERTa's corrections
4. **Encoder versus decoder**
   1. Classification, retrieval, reranking: encoder
   2. Generation: decoder
   3. Cross-encoder versus bi-encoder, and the cost argument
   4. Why encoder-only models remain the right tool for reranking in 2026
5. **Fine-tuning an encoder**
   1. Head replacement
   2. Layer-wise learning rates
   3. Why encoders fine-tune on small data better than decoders

## Required Free Resources

- **Primary:** 'BERT' (Devlin et al.) — https://arxiv.org/abs/1810.04805
- **Primary:** Jay Alammar, 'The Illustrated BERT' — https://jalammar.github.io/illustrated-bert/
- 'RoBERTa' — https://arxiv.org/abs/1907.11692 — read the ablations; they are a good example of careful empirical work
- Hugging Face fine-tuning tutorial — https://huggingface.co/docs/transformers/training

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=31
```

1. **Implement the MLM masking scheme** (1h) — 80/10/10. Verify the proportions.
2. **Train a tiny encoder with MLM** (2h) — On your Week 25 tokenizer's output. Watch the loss.
3. **Compare MLM and next-token loss curves** (1h) — Same model, same data. Note the sample efficiency difference.
4. **Fine-tune a small pretrained BERT** (1.5h) — Classification head, on a small dataset.
5. **Pooling comparison** (1h) — CLS vs mean pooling for classification and for similarity. The answers differ.
6. **Cross-encoder versus bi-encoder** (1.5h) — On your Week 28 relevance set. Quality and latency.

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
b
e
r
t
_
f
i
n
e
t
u
n
e
.
p
y
```

## Tests To Write

Add: a test that bidirectional attention lets position 0 attend to position n-1 (unlike causal), and a test that the MLM masking produces the expected 80/10/10 split over many samples.

## Portfolio Artifact

`src/bert_finetune.py` plus the cross-encoder versus bi-encoder comparison on your Week 28 relevance set. That comparison feeds directly into Week 38.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *Encoder or decoder — when do you pick which, and why?* Then: *Why can't a BERT-style model generate text?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Probe what different BERT layers encode: train linear probes on each layer's representations for a syntactic task (part-of-speech) and a semantic task (word sense). The typical finding — syntax in middle layers, semantics later — is a nice result, and layer probing is a standard interpretability technique you will want in Month 16.
