# Weekly Plan: All 78 Weeks

One line of truth for the whole course. Each week lists its outcome, the concrete
artifact it produces, and the interview drill attached to it. Full detail lives in
`months/month-XX-*/week-YY.md`.

Legend: **A** = artifact committed publicly, **D** = interview drill, ⭐ = flagship-critical week.

---

## Phase 1: Mathematical and Classical ML Foundations

### Month 1 — ML Mathematics Bootcamp (`months/month-01-foundations/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 1 | Vectors, Matrices, Geometry | Implement vector/matrix ops from scratch; explain embeddings geometrically | `math-labs/src/linear_algebra.py` + tests | Why do embeddings live in vector spaces? |
| 2 | Matrix Factorization and SVD | Use SVD for dimensionality reduction and image compression | `src/pca.py`, `notebooks/svd_image_compression.ipynb` | Explain PCA and what information it destroys |
| 3 | Calculus and Gradients | Derive and implement gradients for common ML losses | `src/autodiff_scalar.py` + gradient checker | Derive gradient descent for linear regression |
| 4 | Probability, Statistics, Information Theory | Simulate distributions; explain likelihood, entropy, KL | `src/probability.py`, `src/information_theory.py` | Why is cross entropy the loss for classification? |

**Capstone:** ML Math Toolkit — an installable package covering linear algebra, autodiff, probability, and information theory.

---

### Month 2 — Classical Machine Learning From Scratch (`months/month-02-classical-ml/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 5 | Linear Regression | Implement closed-form and gradient-descent regression | `ml-from-scratch/src/linear_regression.py` | Explain bias, variance, and what regularization buys |
| 6 | Logistic Regression and Metrics | Implement a binary classifier and evaluate it correctly | `src/logistic_regression.py`, `src/metrics.py` | When is PR-AUC better than ROC-AUC? |
| 7 | Decision Trees | Implement a decision tree classifier with split logic | `src/decision_tree.py` | Why do trees overfit and how do you stop it? |
| 8 | Ensembles and Random Forests | Build bagging and a random forest from scratch | `src/random_forest.py` | Bagging vs boosting: variance or bias? |

**Capstone:** Titanic ML Pipeline — full EDA, feature engineering, from-scratch vs sklearn comparison, error analysis.

---

### Month 3 — Practical ML, Kaggle, and Model Debugging (`months/month-03-kaggle-ml/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 9 | Gradient Boosting | Explain boosting; train strong tabular models | `notebooks/gradient_boosting_lab.ipynb` | Walk through one boosting iteration by hand |
| 10 | Feature Engineering and Leakage | Build robust features with automated leakage tests | `src/features.py`, `tests/test_no_leakage.py` | Find the leakage in a described scenario |
| 11 | Model Evaluation and Calibration | Evaluate beyond accuracy; calibrate probabilities | `src/evaluation.py`, `src/calibration.py` | How would you evaluate a fraud model? |
| 12 | Explainability and Error Analysis | Produce a professional model report | `notebooks/error_analysis.ipynb` | Your model is 94% accurate and useless. Why? |

**Capstone:** End-to-End Kaggle Tabular System — competition entry with report, explainability, and write-up.

---

## Phase 2: Deep Learning Mastery

### Month 4 — Neural Networks From Scratch (`months/month-04-deep-learning-from-scratch/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 13 | Perceptrons and MLP Foundations | Implement a perceptron and one-hidden-layer network | `ml-from-scratch/src/neural_net.py` | Why can't a perceptron learn XOR? |
| 14 | Backpropagation | Derive and implement backprop; gradient-check every parameter | `src/backprop.py`, `tests/test_backprop.py` | Derive backprop for a 2-layer MLP |
| 15 | Optimization | Implement SGD, momentum, RMSProp, Adam | `src/optimizers.py` | Why does Adam converge fast and generalize worse? |
| 16 | Regularization and Generalization | Diagnose overfitting and stabilize training | `src/regularization.py`, overfit-then-fix notebook | Loss is NaN at step 400. Debug it out loud. |

**Capstone:** Neural Network Library From Scratch — a mini deep learning framework in NumPy with layers, losses, optimizers, and a training loop.

---

### Month 5 — PyTorch Engineering (`months/month-05-pytorch-engineering/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 17 | Tensors and Autograd | Use PyTorch confidently for tensors and autograd | `pytorch-labs/src/tensor_labs.py` | What does `.backward()` actually do? |
| 18 | Modules, Datasets, DataLoaders | Build reusable modules and data pipelines | `src/data.py`, `src/models.py` | Your GPU is at 30% utilization. Diagnose. |
| 19 | Training Loops and Debugging | Build robust training loops with logging and checkpoints | `src/train.py`, `src/evaluate.py` | Training loss drops, val loss rises. Next steps? |
| 20 | Experiment Tracking and Reproducibility | Track experiments and reproduce results bit-for-bit | `src/config.py`, `src/tracking.py` | How do you make a training run reproducible? |

**Capstone:** MNIST Production Training Pipeline — config-driven, tested, tracked, exportable.

---

### Month 6 — Computer Vision (`months/month-06-computer-vision/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 21 | CNNs | Implement and train convolutional networks | `pytorch-labs/src/cnn.py`, CIFAR-10 run | Compute the receptive field of a 3-layer CNN |
| 22 | ResNet and Modern CNNs | Explain residual connections; train a small ResNet | `src/resnet.py` | Why do residual connections fix deep networks? |
| 23 | Transfer Learning | Fine-tune pretrained vision models | `src/transfer.py` | Which layers do you freeze, and why? |
| 24 | Vision Transformers and Multimodal | Understand ViT; compare against CNNs | `src/vit.py`, comparison notebook | When does a ViT beat a CNN, and when doesn't it? |

**Capstone:** Image Classification Service — FastAPI + Docker + latency measurements + model card.

---

## Phase 3: NLP and Transformers

### Month 7 — NLP Foundations (`months/month-07-nlp-foundations/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 25 | Text Preprocessing and Tokenization | Build tokenizers, including a working BPE | `llm-labs/src/tokenizer.py` | Why does tokenization break arithmetic? |
| 26 | Word Embeddings | Train and evaluate embeddings; understand similarity | `src/embeddings.py` | What does cosine similarity actually measure? |
| 27 | Word2Vec and Negative Sampling | Implement simplified skip-gram with negative sampling | `src/word2vec.py` | Why negative sampling instead of full softmax? |
| 28 | Classical NLP Tasks | Build text classification with strong baselines | `src/text_classification.py` | Beat a BERT model with TF-IDF. When is that possible? |

**Capstone:** Semantic Search Engine — embedding search over a real corpus, backed by PostgreSQL + pgvector.

---

### Month 8 — Transformers From First Principles ⭐ (`months/month-08-transformers/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 29 | Attention ⭐ | Derive and implement scaled dot-product attention | `llm-labs/src/attention.py` | Derive attention on a whiteboard. Why the √d scaling? |
| 30 | Transformer Blocks ⭐ | Implement multi-head attention, MLP, residuals, layer norm | `src/transformer_block.py` | Why pre-norm instead of post-norm? |
| 31 | Encoder Models: BERT | Understand masked language modeling; fine-tune an encoder | `src/bert_finetune.py` | Encoder vs decoder: when do you pick which? |
| 32 | Decoder Models: GPT ⭐ | Implement a tiny decoder-only language model | `src/mini_gpt.py` | Explain KV caching and what it costs in memory |

**Capstone:** Mini-GPT — a working GPT trained on a small corpus, with every architectural choice explained in the README.

---

### Month 9 — Modern LLMs (`months/month-09-modern-llms/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 33 | Modern Architecture: RoPE, RMSNorm, SwiGLU, GQA | Explain what changed between GPT-2 and Llama | `src/modern_blocks.py` | Why did grouped-query attention win? |
| 34 | Tokenization and Data Curation | Build a data prep pipeline: dedupe, chunk, split | `src/data_curation.py` | How does training data quality beat model size? |
| 35 | Training Small Language Models | Train a tiny LM; evaluate perplexity; sample well | `src/train_lm.py`, `src/sampling.py` | Temperature vs top-k vs top-p. Explain each. |
| 36 | LLM Evaluation Basics | Evaluate generations with task metrics and rubrics | `src/eval_harness.py` | How do you evaluate an LLM without ground truth? |

**Capstone:** Tiny Language Model Training Report — trained model, curves, samples, limitations, reproducibility report.

---

## Phase 4: LLM Engineering and Applied AI

### Month 10 — Retrieval-Augmented Generation (`months/month-10-rag-systems/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 37 | Embeddings and Vector Databases | Build vector search on pgvector; understand ANN indexes | `rag-systems/src/vector_store.py` | HNSW vs IVFFlat: explain the tradeoff |
| 38 | Chunking, Retrieval, Reranking | Compare chunking and retrieval strategies empirically | `src/chunking.py`, `src/reranker.py` | Retrieval returns the right doc but the answer is wrong. Why? |
| 39 | RAG Evaluation | Build an eval set; measure retrieval and answer quality | `src/rag_eval.py`, `evals/` | Design an eval harness for a RAG system |
| 40 | Production RAG API | Ship an API with observability and eval reporting | `src/api.py`, `docker-compose.yml` | Design RAG for 10M documents and 1k QPS |

**Capstone:** Enterprise Knowledge Assistant — production-style RAG on PostgreSQL/pgvector with a real evaluation harness.

---

### Month 11 — Agent Engineering With DBA Differentiation ⭐ (`months/month-11-agent-engineering/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 41 | Tool Calling and Function Interfaces ⭐ | Build safe, typed, tested tool-calling patterns | `agent-systems/src/tools.py` | Design a tool interface an LLM cannot misuse |
| 42 | Planning, Reflection, and State | Implement agent loops with state, retries, and budgets | `src/agent_loop.py`, `src/state.py` | When does reflection help and when is it theater? |
| 43 | Database Diagnostic Tools ⭐ | Build tools for query plans, indexes, slow queries | `ai-dba-agent/src/tools/` | Explain a bad query plan to a non-DBA |
| 44 | Agent Evaluation and Safety ⭐ | Measure agent reliability and characterize failure modes | `ai-dba-agent/evals/` | How do you know your agent is safe to run in prod? |

**Capstone:** ⭐ **Autonomous DBA Assistant** — the flagship. Diagnoses synthetic incidents, recommends safe actions, cites evidence, measured for reliability.

---

### Month 12 — Fine-Tuning and Preference Optimization (`months/month-12-finetuning/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 45 | Fine-Tuning Fundamentals | Full fine-tune a small open model | `llm-labs/src/finetune.py` | When is fine-tuning the wrong answer? |
| 46 | LoRA and QLoRA | Apply parameter-efficient fine-tuning | `src/lora.py` | Derive LoRA's parameter count for a given rank |
| 47 | Instruction Datasets and Data Quality | Build a high-quality DBA instruction dataset | `data/dba_instructions/`, dataset card | 1,000 great examples or 100,000 mediocre ones? |
| 48 | Evaluation and Model Comparison | Compare base vs tuned behavior rigorously | `evals/finetune_eval.py` | Explain DPO versus RLHF in three sentences |

**Capstone:** Fine-Tuned DBA Assistant Model — dataset card, model card, evaluation report, demo.

---

## Phase 5: AI Systems Engineering

### Month 13 — Distributed AI Systems (`months/month-13-distributed-ai-systems/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 49 | GPU and CUDA Basics | Reason about GPU memory, throughput, and batching | `notebooks/gpu_memory_math.ipynb` | How much memory to train a 7B model? Show the math. |
| 50 | Distributed Training Concepts | Explain DP, TP, PP, ZeRO, and gradient synchronization | `docs/distributed_training.md` | Explain ZeRO stages 1, 2, 3 |
| 51 | Ray for AI Workloads | Run distributed preprocessing and evaluation | `src/distributed_eval.py` | Design a job scheduler for a shared GPU cluster |
| 52 | Performance Profiling | Profile and fix bottlenecks in training and inference | `src/profiling.py`, profile report | Inference p99 is 4s, p50 is 200ms. Diagnose. |

**Capstone:** Distributed Evaluation Pipeline — parallel evaluation of LLM/RAG outputs at scale.

---

### Month 14 — MLOps (`months/month-14-mlops/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 53 | Experiment Tracking | Track experiments, metrics, and artifacts properly | `mlops-platform/src/tracking.py` | What belongs in an experiment record? |
| 54 | Model Registry and Versioning | Version models and datasets with lineage | `src/registry.py` | How do you roll back a bad model at 2am? |
| 55 | CI/CD for ML | Build GitHub Actions pipelines for an ML repo | `.github/workflows/` | What tests gate a model deployment? |
| 56 | Monitoring and Drift | Build monitoring for data drift and model quality | `src/monitoring.py`, dashboards | Design alerting for a production LLM feature |

**Capstone:** Full MLOps Pipeline — train, evaluate, register, deploy, monitor, with tests throughout.

---

### Month 15 — Kubernetes AI Platform (`months/month-15-kubernetes-ai-platform/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 57 | Docker Hardening | Build small, secure, reproducible production images | `infra/docker/` | Your image is 8GB. Get it under 1GB. |
| 58 | Kubernetes for AI Services | Deploy an inference API on kind/minikube | `infra/k8s/` | Requests vs limits for a GPU inference pod |
| 59 | Scaling, Queues, Batch Inference | Build async inference and evaluation workers | `src/workers.py` | Design batch inference for 100M documents |
| 60 | Reliability and Incident Response | Add health checks, SLOs, runbooks, rollbacks | `docs/runbooks/`, `infra/k8s/probes.yaml` | Write the postmortem for an LLM outage |

**Capstone:** Production AI Cluster — the DBA agent and RAG system deployed to local Kubernetes with reproducible manifests. Includes the **Database Incident Commander** flagship.

---

## Phase 6: Research Engineering and Interview Execution

### Month 16 — Paper Reproduction (`months/month-16-paper-reproduction/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 61 | Paper Reading Method | Read and summarize papers: claims, method, results, limits | `papers/` summaries ×5 | Summarize a paper you read this week in 90 seconds |
| 62 | Attention Is All You Need Reproduction | Reproduce a small transformer result | `research-reproduction/src/transformer_repro.py` | What did the original paper get wrong? |
| 63 | LoRA or DPO Reproduction | Reproduce a PEFT or preference-learning result | `src/lora_repro.py` or `src/dpo_repro.py` | Design the ablation that would falsify this claim |
| 64 | Reproducibility Report | Write a polished reproduction report | `reports/reproduction_report.md` | Your numbers don't match the paper. What now? |

**Capstone:** Published Reproduction Report — summary, implementation, experiments, ablations, failures, lessons.

---

### Month 17 — Original Applied Research ⭐ (`months/month-17-original-research/`)

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 65 | Research Question Selection | Choose and scope one original applied question | `reports/research_proposal.md` | Why is this question worth answering? |
| 66 | Experiment Design | Define dataset, baselines, metrics, and ablations | `reports/experiment_design.md` | What result would change your mind? |
| 67 | Implementation and Experiments | Run the experiments; collect results honestly | `src/`, `results/` | Your result is negative. Is it publishable? |
| 68 | Analysis and Writing | Write the technical report; publish the repo | `reports/final_report.md` | Present your findings in 5 minutes |

**Capstone:** ⭐ Original AI-for-Databases Research Project — e.g. "Can LLM agents reliably diagnose PostgreSQL performance incidents from telemetry and query plans?"

---

### Month 18 — Interview War Room (`months/month-18-interview-war-room/`)

Ten weeks. No new learning. Conversion only.

| Wk | Title | Outcome | A | D |
| -- | ----- | ------- | - | - |
| 69 | Coding Sprint 1 | Arrays, strings, hash maps, two pointers, sliding window | 40 solved problems, logged | 4 problems under timed conditions |
| 70 | Coding Sprint 2 | Trees, graphs, heaps, DP basics | 40 solved problems, logged | 4 problems under timed conditions |
| 71 | ML Theory Interviews | Explain core ML from first principles | 20 recorded explanations | Full ML-depth mock |
| 72 | Deep Learning Interviews | Derive backprop, attention, optimization, regularization | 15 recorded derivations | Full DL-depth mock |
| 73 | LLM System Design | Design ChatGPT-like, enterprise RAG, eval platforms | 6 design write-ups | 45-minute design mock |
| 74 | AI Infrastructure System Design | Design training, evaluation, and inference platforms | 6 design write-ups | 45-minute infra design mock |
| 75 | Portfolio Polish | Rewrite READMEs, record demos, draw architecture diagrams | 9 polished flagship repos | 5-minute portfolio walkthrough |
| 76 | Mock Interviews and Recruiter Package | Complete full loops; finalize resume | Resume, cover template, 3 recorded loops | Full onsite simulation |
| 77 | Application Strategy | Build target matrix, referrals, outreach, pitches | `application_tracker.md` | Pitch yourself in 60 seconds |
| 78 | Final Championship Review | Full readiness review; close remaining gaps | `SCORECARD.md` final pass | Self-assessed hire/no-hire with evidence |

**Capstone:** Frontier AI Portfolio Package — the landing page tying all nine flagships together.

---

## Cumulative Checkpoints

Do not proceed past these without meeting the bar. See `SCORECARD.md`.

| After Week | Checkpoint | Bar |
| ---------- | ---------- | --- |
| 12 | Classical ML competence | Average weekly score ≥ 7; Kaggle system published |
| 24 | Deep learning competence | Can train + serve a model; 6 capstones published |
| 36 | Transformer competence | Mini-GPT works; can derive attention unaided |
| 48 | Applied LLM competence | DBA agent shipped with measured reliability |
| 60 | Systems competence | Full platform running on Kubernetes |
| 68 | Research competence | Reproduction + original research published |
| 78 | Interview readiness | Passing mock loops; applications submitted |
