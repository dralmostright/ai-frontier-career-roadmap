# Resource Index

Free or nearly-free resources, organized by topic and mapped to the months that
use them. Everything here is free unless marked **[$]**.

**Rule:** every resource in this index must be paired with implementation. A
lecture you watch and do not code is entertainment. Budget theory at no more than
30% of your weekly hours.

---

## How To Use Resources Efficiently

You have 15-20 hours a week and 18 months. You cannot complete CS229, CS231n,
CS224N, d2l.ai, and MML in full. Nobody does. Use them as **references indexed by
topic**, not as courses to complete.

The pattern for each week:

1. Read the week file's theory list first. That is the scope.
2. Find those specific topics in one or two resources below.
3. Watch/read *only* those sections. Skip everything else.
4. Implement immediately.
5. Return to the resource only when the implementation fails.

The exception: the 3Blue1Brown linear algebra series (Month 1) and the Karpathy
"Zero to Hero" series (Months 4 and 8) are worth watching end to end. They are
short and unusually high density.

---

## Company and Role Research

Read job descriptions monthly from Month 6 onward. They are the actual syllabus.

- OpenAI Careers — https://openai.com/careers/
- Anthropic Careers — https://www.anthropic.com/careers
- Anthropic Jobs — https://www.anthropic.com/careers/jobs
- Google DeepMind Careers — https://deepmind.google/about/careers/
- Meta AI Research — https://ai.meta.com/research/
- NVIDIA Careers — https://www.nvidia.com/en-us/about-nvidia/careers/
- Databricks Careers — https://www.databricks.com/company/careers

**Exercise (do this in Month 6, 12, and 18):** collect ten job descriptions for
your target roles. Extract every named skill into a spreadsheet. Count
frequencies. Compare against your portfolio. The gaps are your remediation list.

---

## Mathematics — Months 1, 3, 4

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| MIT OCW 18.06 Linear Algebra | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ | The canonical treatment. Reference. |
| MIT 18.06 video lectures | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/ | Lectures 1-11, 21-22, 29-30 cover the course needs |
| 3Blue1Brown, Essence of Linear Algebra | https://www.3blue1brown.com/topics/linear-algebra | **Watch all of it.** Week 1-2. Best intuition available. |
| 3Blue1Brown, Essence of Calculus | https://www.3blue1brown.com/topics/calculus | Week 3 |
| Mathematics for Machine Learning (book) | https://mml-book.github.io/ | Ch. 2-4 for Month 1, Ch. 6 for probability, Ch. 10 for PCA |
| Seeing Theory (probability visualizations) | https://seeing-theory.brown.edu/ | Week 4 intuition |
| MIT OCW 18.05 Probability and Statistics | https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/ | Week 4 reference |
| The Matrix Cookbook | https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf | Matrix derivative identities. Keep it open in Month 4. |

**Month 1 priority order:** 3Blue1Brown LA series → MML Ch. 2-3 → implement →
MIT 18.06 only for topics that remain unclear.

---

## Classical Machine Learning — Months 2, 3

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| Stanford CS229 | https://cs229.stanford.edu/ | Lecture notes are the best free ML derivations available |
| CS229 (older public materials) | https://see.stanford.edu/Course/CS229 | Full video set |
| Google ML Crash Course | https://developers.google.com/machine-learning/crash-course | Fast, practical, good on evaluation |
| Kaggle Learn | https://www.kaggle.com/learn | Short applied modules |
| Kaggle Intro to ML | https://www.kaggle.com/learn/intro-to-machine-learning | Month 2 warm-up |
| Kaggle Feature Engineering | https://www.kaggle.com/learn/feature-engineering | Week 10 |
| scikit-learn User Guide | https://scikit-learn.org/stable/user_guide.html | Reference for every classical algorithm |
| An Introduction to Statistical Learning | https://www.statlearning.com/ | Free PDF. Ch. 2-8 map to Months 2-3. |
| Elements of Statistical Learning | https://hastie.su.domains/ElemStatLearn/ | Free PDF. Deeper. Use for boosting (Ch. 10). |
| Kaggle Competitions | https://www.kaggle.com/competitions | Months 2-3 capstones |

**CS229 note:** the lecture notes on linear regression, logistic regression, GLMs,
and SVMs are the single best free source for the derivations you need in Month 2.

---

## Deep Learning — Months 4, 5, 6

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| Dive into Deep Learning (d2l.ai) | https://d2l.ai/ | The best free DL textbook with runnable code. Primary reference Months 4-9. |
| PyTorch Tutorials | https://pytorch.org/tutorials/ | Month 5. Start with the 60-minute blitz. |
| PyTorch Docs | https://pytorch.org/docs/stable/index.html | Reference throughout |
| Karpathy, Neural Networks: Zero to Hero | https://karpathy.ai/zero-to-hero.html | **Watch all of it.** Months 4 and 8. micrograd → makemore → GPT. |
| micrograd | https://github.com/karpathy/micrograd | Week 14. Read the whole thing; it's ~150 lines. |
| Stanford CS231n | https://cs231n.stanford.edu/ | Month 6 |
| CS231n notes | https://cs231n.github.io/ | Best free CNN explanations. Read the optimization and backprop notes in Month 4. |
| Fast.ai Practical Deep Learning | https://course.fast.ai/ | Optional. Good top-down complement. |
| Deep Learning Book (Goodfellow et al.) | https://www.deeplearningbook.org/ | Reference for theory. Ch. 6-8 for Month 4. |
| Distill.pub | https://distill.pub/ | Exceptional visual explanations. Momentum article for Week 15. |
| Weights & Biases docs | https://docs.wandb.ai/ | Week 20 alternative to MLflow |

**Karpathy note:** the "Zero to Hero" series is the highest-value 15 hours in this
entire index. Week 14 (micrograd) and Weeks 29-32 (nanoGPT build) should follow it
directly, typing every line yourself rather than cloning.

---

## NLP and LLMs — Months 7, 8, 9, 10, 11, 12

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| Stanford CS224N | https://web.stanford.edu/class/cs224n/ | Months 7-8. Lectures 1-9 are the core. |
| Hugging Face Learn | https://huggingface.co/learn | Hub for all HF courses |
| Hugging Face LLM Course | https://huggingface.co/learn/llm-course/chapter1/1 | Months 7, 9, 12 |
| Hugging Face Course GitHub | https://github.com/huggingface/course | Source and notebooks |
| Hugging Face NLP Course | https://huggingface.co/learn/nlp-course | Tokenizers chapter for Week 25 |
| Karpathy nanoGPT | https://github.com/karpathy/nanoGPT | Month 8. Read it after building your own. |
| Karpathy, Let's build GPT | https://www.youtube.com/watch?v=kCc8FmEb1nY | Weeks 29-32 |
| The Illustrated Transformer | https://jalammar.github.io/illustrated-transformer/ | Week 29 intuition |
| The Annotated Transformer | https://nlp.seas.harvard.edu/annotated-transformer/ | Week 30. Line-by-line implementation. |
| Lilian Weng's blog | https://lilianweng.github.io/ | Best survey posts on attention, agents, hallucination, prompt engineering |
| Transformer Circuits | https://transformer-circuits.pub/ | Month 8 stretch. Interpretability. |
| Hugging Face Transformers docs | https://huggingface.co/docs/transformers/index | Months 9-12 |
| PEFT docs | https://huggingface.co/docs/peft/index | Month 12 |
| TRL (Transformer Reinforcement Learning) | https://huggingface.co/docs/trl/index | Month 12, DPO |
| Unsloth | https://github.com/unslothai/unsloth | Month 12. Makes QLoRA viable on modest hardware. |
| llama.cpp | https://github.com/ggerganov/llama.cpp | Local inference, quantization |
| Ollama | https://ollama.com/ | Easiest local model runner for Months 10-12 |

---

## Papers — Months 8, 9, 12, 16

Read these in this order. Full reading method in Week 61.

**Core architecture**
- Attention Is All You Need — https://arxiv.org/abs/1706.03762
- BERT — https://arxiv.org/abs/1810.04805
- GPT-2: Language Models are Unsupervised Multitask Learners — https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- GPT-3: Language Models are Few-Shot Learners — https://arxiv.org/abs/2005.14165
- Llama 2 — https://arxiv.org/abs/2307.09288
- RoFormer (RoPE) — https://arxiv.org/abs/2104.09864
- GQA: Grouped-Query Attention — https://arxiv.org/abs/2305.13245
- Root Mean Square Layer Normalization — https://arxiv.org/abs/1910.07467

**Training and alignment**
- Scaling Laws for Neural Language Models — https://arxiv.org/abs/2001.08361
- Training Compute-Optimal LLMs (Chinchilla) — https://arxiv.org/abs/2203.15556
- InstructGPT — https://arxiv.org/abs/2203.02155
- Constitutional AI — https://arxiv.org/abs/2212.08073
- Direct Preference Optimization — https://arxiv.org/abs/2305.18290
- LoRA — https://arxiv.org/abs/2106.09685
- QLoRA — https://arxiv.org/abs/2305.14314

**Retrieval and agents**
- Retrieval-Augmented Generation — https://arxiv.org/abs/2005.11401
- Dense Passage Retrieval — https://arxiv.org/abs/2004.04906
- ReAct: Synergizing Reasoning and Acting — https://arxiv.org/abs/2210.03629
- Toolformer — https://arxiv.org/abs/2302.04761
- Chain-of-Thought Prompting — https://arxiv.org/abs/2201.11903
- Self-Consistency — https://arxiv.org/abs/2203.11171

**Systems**
- ZeRO: Memory Optimizations Toward Training Trillion Parameter Models — https://arxiv.org/abs/1910.02054
- FlashAttention — https://arxiv.org/abs/2205.14135
- Efficient Memory Management for LLM Serving (PagedAttention / vLLM) — https://arxiv.org/abs/2309.06180
- Megatron-LM — https://arxiv.org/abs/1909.08053
- Mixed Precision Training — https://arxiv.org/abs/1710.03740

**Discovery**
- arXiv cs.CL — https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG — https://arxiv.org/list/cs.LG/recent
- Papers with Code — https://paperswithcode.com/
- Semantic Scholar — https://www.semanticscholar.org/
- Hugging Face Daily Papers — https://huggingface.co/papers

---

## AI Engineering and Frameworks — Months 10-15

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| LangChain docs | https://python.langchain.com/docs/ | Month 10-11. Understand it; don't depend on it. |
| LangGraph docs | https://langchain-ai.github.io/langgraph/ | Month 11. Agent state machines. |
| LlamaIndex docs | https://docs.llamaindex.ai/ | Month 10 alternative |
| pgvector | https://github.com/pgvector/pgvector | Months 7, 10. Your home turf. |
| pgvector performance guide | https://github.com/pgvector/pgvector#performance | Week 37. Index tuning. |
| FAISS | https://github.com/facebookresearch/faiss | Week 37 comparison |
| Sentence Transformers | https://www.sbert.net/ | Months 7, 10 |
| RAGAS (RAG evaluation) | https://docs.ragas.io/ | Week 39 |
| FastAPI | https://fastapi.tiangolo.com/ | Months 6, 10, 15 |
| Pydantic | https://docs.pydantic.dev/ | Tool schemas, Month 11 |
| MLflow | https://mlflow.org/docs/latest/index.html | Months 5, 14 |
| Ray | https://docs.ray.io/ | Month 13 |
| Ray Data | https://docs.ray.io/en/latest/data/data.html | Week 51 |
| Kubernetes docs | https://kubernetes.io/docs/home/ | Month 15 |
| kind (Kubernetes in Docker) | https://kind.sigs.k8s.io/ | Week 58 |
| Prometheus | https://prometheus.io/docs/ | Week 56, 60 |
| Grafana | https://grafana.com/docs/ | Week 56 |
| vLLM | https://docs.vllm.ai/ | Weeks 52, 59 |
| Evidently (drift detection) | https://docs.evidentlyai.com/ | Week 56 |
| DVC | https://dvc.org/doc | Week 54 |

---

## Anthropic and Claude-Specific

Relevant both as a target employer and as tooling you will use.

- Claude Docs — https://docs.claude.com/
- Anthropic Cookbook — https://github.com/anthropics/anthropic-cookbook
- Claude Agent SDK — https://docs.claude.com/en/api/agent-sdk/overview
- Model Context Protocol — https://modelcontextprotocol.io/
- Anthropic Research — https://www.anthropic.com/research
- Anthropic Engineering blog — https://www.anthropic.com/engineering

**Month 11 note:** MCP is directly relevant to the DBA agent. Exposing your
database diagnostic tools as an MCP server is an excellent stretch goal and a
strong interview talking point.

---

## Databases and Your Specialization — Months 7, 10, 11, 15, 17

This is where you have an edge. Deepen it deliberately.

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| PostgreSQL docs: EXPLAIN | https://www.postgresql.org/docs/current/using-explain.html | Week 43 |
| pg_stat_statements | https://www.postgresql.org/docs/current/pgstatstatements.html | Weeks 43-44 |
| Use The Index, Luke | https://use-the-index-luke.com/ | Query plan reasoning |
| PgHero | https://github.com/ankane/pghero | Prior art for the DBA agent |
| pgvector | https://github.com/pgvector/pgvector | Vector search on Postgres |
| PostgreSQL wiki: Slow Query Questions | https://wiki.postgresql.org/wiki/Slow_Query_Questions | Ground truth for incident scenarios |
| Google SRE Book | https://sre.google/sre-book/table-of-contents/ | Weeks 56, 60. SLOs and postmortems. |
| Google SRE Workbook | https://sre.google/workbook/table-of-contents/ | Week 60 |

**Month 17 note:** there is no established public benchmark for LLM-based
database incident diagnosis. That absence is your research opportunity.

---

## Interview Preparation — All Months

| Resource | Link | Use it for |
| -------- | ---- | ---------- |
| NeetCode 150 | https://neetcode.io/practice | The efficient coding path. Weeks 1-78. |
| LeetCode | https://leetcode.com/ | Volume |
| Grokking the System Design Interview | https://www.educative.io/ **[$]** | Optional. Framework only. |
| System Design Primer | https://github.com/donnemartin/system-design-primer | Free alternative |
| Machine Learning System Design (Chip Huyen) | https://huyenchip.com/machine-learning-systems-design/toc.html | Months 9-15 |
| Designing Machine Learning Systems (book) | Chip Huyen **[$]** | Worth buying. Month 14. |
| Chip Huyen's blog | https://huyenchip.com/blog/ | Applied ML engineering |
| Pramp | https://www.pramp.com/ | Free peer mock interviews |
| interviewing.io | https://interviewing.io/ | Anonymous mocks, some free |
| Deep Learning Interviews (Shlomo Kashani) | https://arxiv.org/abs/2201.00650 | Free problem book |

---

## Paid Resources Worth The Money

Nothing here is required. Listed by value per dollar if you choose to spend.

| Resource | Approx cost | Verdict |
| -------- | ----------- | ------- |
| Google Colab Pro | $10/mo | **Buy it.** Months 8-12 need GPU time. Cheapest path. |
| Designing Machine Learning Systems | $40 once | **Buy it.** Best ML systems book. |
| A used RTX 3090/4090 | $700-1500 | Only if you're certain. Colab Pro + Lambda spot instances is cheaper for 18 months. |
| Lambda Labs / RunPod GPU | ~$0.40-2/hr | Pay-per-use for Month 12 fine-tuning and Month 16 reproduction |
| Claude / OpenAI API credits | $20-50/mo Months 10-17 | Necessary for RAG and agent work. Budget it. |
| Kaggle | Free | Free GPU hours weekly. Use them before paying for anything. |

**Total realistic spend over 18 months: $400-800.** Mostly Colab Pro and API
credits in Months 10-17. Everything else in this index is free.

---

## Compute Strategy

You do not need a GPU cluster. You need to be clever about scope.

| Months | Compute need | Solution |
| ------ | ------------ | -------- |
| 1-4 | None. CPU only. | Your laptop |
| 5-6 | Light GPU (MNIST, CIFAR) | Kaggle free tier or Colab free |
| 7-9 | Moderate (small LM training) | Colab Pro. Keep models under 50M params. |
| 10-11 | API inference, not training | Claude/OpenAI API + local Ollama |
| 12 | QLoRA on a 3-7B model | Colab Pro (A100 for a few hours) or RunPod spot |
| 13-15 | Distributed and serving | CPU-based Ray cluster locally; kind for k8s |
| 16-17 | Small-scale experiments | Colab Pro + spot instances |

**Scoping rule:** if an experiment needs more than 8 GPU-hours, redesign it
smaller. The point is understanding and evidence, not scale. A well-executed
125M-parameter experiment with clean ablations beats a sloppy 7B run in every
interview.

---

## Resource Anti-Patterns

| Anti-pattern | Why it fails |
| ------------ | ------------ |
| Completing whole courses | 40 hours of CS231n for 6 hours of relevant content |
| Collecting resources | Bookmarking is not learning |
| Reading papers without implementing | You retain almost none of it |
| Watching at 2x with no notes | Feels productive, is not |
| Switching resources when confused | Confusion is the work. Push through one source. |
| Reading the paper before the blog post | Read the accessible version first, then the paper |
| Never reading source code | The HF and PyTorch sources answer most questions faster than docs |
