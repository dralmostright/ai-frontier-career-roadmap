# Month 09 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**'Judging LLM-as-a-Judge'** (Week 36) — https://arxiv.org/abs/2306.05685
The paper that catalogued the judge biases. Everything in Months 10-17 depends on
understanding these.

**Hamel Husain, 'Your AI product needs evals'** (Week 36) — https://hamel.dev/blog/posts/evals/
The most practical writing on LLM evaluation anywhere. Read it twice.

**'Deduplicating Training Data Makes Language Models Better'** (Week 34) — https://arxiv.org/abs/2107.06499
The evidence behind the week's central claim.

**nanoGPT** (Week 35) — https://github.com/karpathy/nanoGPT
The practical reference for a small training run done well.

---

## Week 33 — Modern Architecture: RoPE, RMSNorm, SwiGLU, GQA

- **Primary:** 'Llama 2' — https://arxiv.org/abs/2307.09288 — the architecture section
- **Primary:** 'RoFormer' (RoPE) — https://arxiv.org/abs/2104.09864 — read sections 3-4
- 'GQA: Training Generalized Multi-Query Transformer Models' — https://arxiv.org/abs/2305.13245
- 'Root Mean Square Layer Normalization' — https://arxiv.org/abs/1910.07467
- 'GLU Variants Improve Transformer' — https://arxiv.org/abs/2002.05202 — the SwiGLU paper, and refreshingly honest about not knowing why
- Eleuther's blog on RoPE — the clearest explanation of the rotation intuition
## Week 34 — Tokenization and Data Curation

- **Primary:** 'The RefinedWeb Dataset' — https://arxiv.org/abs/2306.01116 — the clearest account of a real curation pipeline
- **Primary:** 'Deduplicating Training Data Makes Language Models Better' — https://arxiv.org/abs/2107.06499
- 'Training Compute-Optimal Large Language Models' (Chinchilla) — https://arxiv.org/abs/2203.15556
- 'The Pile' — https://arxiv.org/abs/2101.00027 — a well-documented dataset construction
- Hugging Face datatrove — https://github.com/huggingface/datatrove — a production curation toolkit worth reading
## Week 35 — Training Small Language Models

- **Primary:** nanoGPT training code and README — https://github.com/karpathy/nanoGPT — the practical reference for a small training run
- **Primary:** 'The Curious Case of Neural Text Degeneration' — https://arxiv.org/abs/1904.09751 — the nucleus sampling paper, and it explains *why* greedy fails
- 'Scaling Laws for Neural Language Models' — https://arxiv.org/abs/2001.08361
- Hugging Face, 'How to generate text' — https://huggingface.co/blog/how-to-generate
- EleutherAI's training logs — reading a real training run's log, including the failures, is unusually instructive
## Week 36 — LLM Evaluation Basics

- **Primary:** 'Judging LLM-as-a-Judge' (Zheng et al.) — https://arxiv.org/abs/2306.05685 — the paper that catalogued the biases. Read it properly.
- **Primary:** Hamel Husain, 'Your AI product needs evals' — https://hamel.dev/blog/posts/evals/ — the most practical writing on this topic anywhere
- 'Holistic Evaluation of Language Models' (HELM) — https://arxiv.org/abs/2211.09110 — read the methodology section
- Eugene Yan's writing on LLM evaluation patterns — consistently good
- RAGAS documentation — https://docs.ragas.io/ — preview of Week 39

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| PyTorch | https://pytorch.org/docs/stable/ | Everything |
| d2l.ai | https://d2l.ai/ | The primary textbook |
| Hugging Face | https://huggingface.co/docs | Months 7+ |
| pgvector | https://github.com/pgvector/pgvector | Month 7 capstone |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| Weights & Biases | https://docs.wandb.ai/ | Training run tracking |
| datatrove | https://github.com/huggingface/datatrove | Week 34 reference |
| Colab Pro | https://colab.research.google.com/ | The Week 35 GPU |

---

## Deliberately Omitted

- **Large-scale distributed pretraining.** Month 13 covers the concepts. You are
  not going to train a 7B model, and you do not need to.
- **RLHF implementation.** Month 12 covers DPO, which is the practical modern
  choice. Understand RLHF conceptually.
- **Constitutional AI in depth.** Read the paper in Month 12; the implementation
  is a research project.
- **Benchmark suites (MMLU, HellaSwag, etc.) in detail.** Know what they measure
  and their known contamination problems. Running them is not a good use of your
  compute budget.
