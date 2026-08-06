# Month 08 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**'Attention Is All You Need'** — https://arxiv.org/abs/1706.03762
Read it in Week 29, again in Week 32, and again in Week 62. It rewards rereading.

**Jay Alammar, 'The Illustrated Transformer'** — https://jalammar.github.io/illustrated-transformer/
Read this *before* the paper. The figures do most of the work.

**Karpathy, 'Let's build GPT'** — https://www.youtube.com/watch?v=kCc8FmEb1nY
Watch it **after** your own Week 29-30 attempt. Watching first turns Week 32 into
transcription.

**The Annotated Transformer** — https://nlp.seas.harvard.edu/annotated-transformer/
Line-by-line. The best reference when your implementation disagrees with itself.

---

## Week 29 — Attention

- **Primary:** 'Attention Is All You Need' — https://arxiv.org/abs/1706.03762 — read it properly this week. You will read it three more times.
- **Primary:** Jay Alammar, 'The Illustrated Transformer' — https://jalammar.github.io/illustrated-transformer/ — read this *before* the paper
- **Primary:** The Annotated Transformer — https://nlp.seas.harvard.edu/annotated-transformer/ — line-by-line implementation. Read after your own attempt.
- 3Blue1Brown, 'Attention in transformers' — https://www.3blue1brown.com/topics/neural-networks — the best visual treatment
- 'FlashAttention' — https://arxiv.org/abs/2205.14135 — read the introduction for the memory argument
## Week 30 — Transformer Blocks

- **Primary:** The Annotated Transformer — https://nlp.seas.harvard.edu/annotated-transformer/
- **Primary:** 'On Layer Normalization in the Transformer Architecture' — https://arxiv.org/abs/2002.04745 — the pre-norm paper, and the source of your interview answer
- d2l.ai ch. 11 (attention and transformers) — https://d2l.ai/
- Anthropic, 'A Mathematical Framework for Transformer Circuits' — https://transformer-circuits.pub/2021/framework/index.html — read the residual stream section; it is the best framing available
## Week 31 — Encoder Models: BERT Concepts

- **Primary:** 'BERT' (Devlin et al.) — https://arxiv.org/abs/1810.04805
- **Primary:** Jay Alammar, 'The Illustrated BERT' — https://jalammar.github.io/illustrated-bert/
- 'RoBERTa' — https://arxiv.org/abs/1907.11692 — read the ablations; they are a good example of careful empirical work
- Hugging Face fine-tuning tutorial — https://huggingface.co/docs/transformers/training
## Week 32 — Decoder Models: Mini-GPT

- **Primary:** Karpathy, 'Let's build GPT: from scratch, in code, spelled out' — https://www.youtube.com/watch?v=kCc8FmEb1nY — **watch after your own attempt**
- **Primary:** nanoGPT — https://github.com/karpathy/nanoGPT — read after yours works, then diff the designs
- 'Language Models are Unsupervised Multitask Learners' (GPT-2) — https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- 'Efficient Memory Management for LLM Serving' (vLLM/PagedAttention) — https://arxiv.org/abs/2309.06180 — read the motivation section

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| PyTorch | https://pytorch.org/docs/stable/ | Everything |
| d2l.ai | https://d2l.ai/ | The primary textbook |
| Hugging Face | https://huggingface.co/docs | Months 7+ |
| pgvector | https://github.com/pgvector/pgvector | Month 7 capstone |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |

---

## Deliberately Omitted

- **Encoder-decoder models (T5, BART).** Understand that they exist and where
  cross-attention goes. Decoder-only dominates and is what gets asked.
- **Efficient attention variants (Linformer, Performer, Longformer).** Know that
  the quadratic cost motivated a research area and that FlashAttention largely
  won by optimizing memory access rather than changing the math.
- **Mixture of experts.** Increasingly relevant; Week 33 mentions it. The
  implementation is a specialization.
- **Transformer interpretability in depth.** Fascinating; Week 31's stretch goal
  and Month 16 touch it. A full treatment is its own course.
