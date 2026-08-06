# llm-labs

**Weeks 25-36, 45-48 · Months 7, 8, 9, 12 · Capstones: Semantic Search, Mini-GPT, Tiny LM, Fine-Tuned Model**

The core competency. Tokenizers, embeddings, attention, transformers, language
model training, evaluation, and parameter-efficient fine-tuning.

---

## Why This Lab Exists

Month 8 is the single most important month in the course for interview
outcomes. "Derive attention" and "explain what breaks without layer norm" are
asked in essentially every frontier lab loop, and they are asked because they
cleanly separate people who have implemented a transformer from people who
have read about one.

You are going to implement one, component by component, and then ablate each
component to see what it was doing. That ablation table is worth more than the
model.

---

## Layout

```text
llm-labs/
  src/
    tokenizer.py         W25  BPE training and encoding, from scratch
    embeddings.py        W26  embedding matrices, similarity, analogy, bias probes
    word2vec.py          W27  skip-gram with negative sampling
    text_classification.py W28  TF-IDF and neural baselines
    attention.py         W29  scaled dot-product, causal masking, multi-head
    transformer_block.py W30  MHA + FFN + residual + norm, pre-norm vs post-norm
    bert_finetune.py     W31  encoders, MLM, fine-tuning a small BERT
    mini_gpt.py          W32  the full decoder-only model, KV cache, generation
    modern_blocks.py     W33  RoPE, RMSNorm, SwiGLU, grouped-query attention
    data_curation.py     W34  dedup, quality filtering, chunking, packing
    train_lm.py          W35  the LM training loop
    sampling.py          W35  greedy, temperature, top-k, nucleus, repetition penalty
    eval_harness.py      W36  perplexity, task metrics, LLM-as-judge
    finetune.py          W45  full fine-tuning, catastrophic forgetting
    lora.py              W46  LoRA and QLoRA from scratch
    instruction_data.py  W47  instruction dataset construction and quality scoring
  configs/
    mini_gpt_tiny.yaml   W32
    mini_gpt_small.yaml  W35
    lora_dba.yaml        W46
```

---

## The Month 8 Build Order

Do not skip ahead. Each step is testable before the next one makes sense.

1. **Week 29 — one attention head.** Scaled dot product, no batching, no
   heads. Verify the output shape and that the attention weights sum to 1.
   Then add the causal mask and verify position i cannot see position i+1.
2. **Week 30 — multi-head, then the block.** Reshape into heads, run attention
   in parallel, concatenate, project. Then wrap it: residual, layer norm,
   feed-forward, residual.
3. **Week 31 — the encoder detour.** Masked language modeling and
   bidirectional attention, so you can articulate encoder-vs-decoder.
4. **Week 32 — the full model.** Embeddings, positional encoding, N blocks,
   output projection, weight tying. Then generation, then the KV cache.

Gradient-check every component as you go, using
`ml-from-scratch/src/backprop.py`. Finding an attention bug at Week 29 takes
ten minutes; finding it at Week 32 takes three days.

---

## The Ablation Table

The Month 8 capstone deliverable. Train the same tiny model with one component
removed at a time and report validation loss.

| Configuration | Val loss | What breaks |
| ------------- | -------- | ----------- |
| Full model | | baseline |
| No positional encoding | | permutation-invariant; word order is lost |
| No residual connections | | gradient vanishes; deep model won't train |
| No layer norm | | activations drift; training destabilizes |
| Post-norm instead of pre-norm | | needs warmup; less stable at depth |
| Single head | | one attention pattern instead of several |
| No causal mask | | trivially cheats by reading ahead; loss collapses |
| No √d scaling | | softmax saturates; gradients vanish |

That last row is the one to be able to explain from first principles: the dot
product of two d-dimensional vectors with unit-variance components has
variance d, so without the scaling the softmax inputs grow with dimension,
saturate, and produce near-zero gradients.

---

## Milestones

| Week | You can... |
| ---- | ---------- |
| 25 | Train a BPE tokenizer and explain why tokenization breaks arithmetic |
| 26 | Explain what cosine similarity measures in embedding space |
| 27 | Derive why negative sampling replaces the full softmax |
| 28 | Beat a neural model with TF-IDF, and say when that is expected |
| 29 | Derive scaled dot-product attention cold, including the √d term |
| 30 | Implement multi-head attention and justify pre-norm |
| 31 | Say when to reach for an encoder rather than a decoder |
| 32 | Build a working GPT and explain KV caching's memory cost |
| 33 | Explain what changed between GPT-2 and Llama, and why |
| 34 | Argue that data quality beats parameter count, with your own ablation |
| 35 | Train a small LM and interpret its perplexity honestly |
| 36 | Design an evaluation for a model with no ground truth |
| 45-48 | Fine-tune with LoRA and know when RAG was the better answer |

---

## Compute

Everything here is scoped to run on Colab Pro or a modest local GPU. Keep
models under 50M parameters through Month 9; the goal is understanding and
clean ablations, not scale. A well-executed 10M-parameter experiment with a
real ablation table beats a sloppy 7B run in every interview.

Month 12's QLoRA work needs a few hours on an A100 or equivalent — Colab Pro
or a spot instance. Budget roughly $20-40 for that month.

---

## Interview Drills

| Week | Drill |
| ---- | ----- |
| 25 | Why does tokenization break arithmetic and reversed strings? |
| 29 | Derive attention on a whiteboard. Why divide by √d? Why not √d²? |
| 30 | Why multi-head instead of one wide head? Why pre-norm over post-norm? |
| 31 | Encoder vs decoder: when do you pick which, and why? |
| 32 | Explain KV caching. Compute its memory for a 7B model at 8k context. |
| 33 | Why did grouped-query attention win? What does it trade away? |
| 35 | Temperature vs top-k vs top-p. What does each actually do to the distribution? |
| 36 | How do you evaluate an LLM with no ground truth? Name the judge biases. |
| 46 | Derive LoRA's parameter count for rank r on a d×d matrix. |
| 48 | Explain DPO versus RLHF in three sentences. |
