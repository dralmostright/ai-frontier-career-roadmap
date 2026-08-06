# Monthly Capstones

Eighteen capstones. Each one is a tournament match: a bounded, shippable project
that proves a capability and produces a public artifact. Full specifications live
in `months/month-XX-*/capstone.md`. This file is the index and the standard.

---

## The Capstone Standard

Every capstone, regardless of month, must ship with:

| Requirement          | Why it exists                                                   |
| -------------------- | --------------------------------------------------------------- |
| `README.md`          | Recruiters read this and nothing else. It is the product.        |
| Reproducible env     | `pyproject.toml` + `Makefile`. `make setup && make test` works.  |
| Tests                | If it isn't tested, you can't claim it works.                    |
| Evaluation metrics   | A number. Not "it works well." A number, with a baseline.        |
| Error analysis       | Where it fails and why. This is what separates you from juniors. |
| `docs/design.md`     | The decision record. Interviewers ask "why did you do it that way?" |
| `docs/limitations.md`| Stating limits honestly is a seniority signal.                   |
| Clean git history    | Meaningful commits. Not "wip", "fix", "fix2".                    |
| Demo                 | A script, notebook, or 3-minute recording.                       |
| Architecture diagram | For anything with more than two components.                      |

Grade every capstone with `coach/capstone_review_rubric.md`. A capstone scoring
below 7/10 does not go in the portfolio — fix it or cut it.

---

## Phase 1: Foundations

### Month 1 — ML Math Toolkit
**Build:** An installable Python package implementing linear algebra primitives,
scalar reverse-mode autodiff, probability utilities, and information-theoretic
measures — all from scratch, all tested against NumPy/SciPy references.

**Proves:** You understand the math well enough to implement it, not just cite it.

**Interview story:** "I built my own autodiff engine before touching PyTorch, so
when a gradient is wrong I know where to look."

**Portfolio weight:** Low as a showpiece, high as a foundation. Keep it public;
it makes the rest of the portfolio credible.

---

### Month 2 — Titanic ML Pipeline
**Build:** A complete supervised learning pipeline on a beginner classification
dataset, comparing your from-scratch implementations against sklearn, with
serious EDA, feature engineering, and error analysis.

**Proves:** You can execute the standard ML workflow correctly end to end.

**Interview story:** "I implemented the models by hand and matched sklearn to
four decimal places, which is how I know my understanding is real."

**Portfolio weight:** Low. Everyone has a Titanic notebook. Yours is better than
average but it is not a differentiator. Keep it, don't feature it.

---

### Month 3 — End-to-End Kaggle Tabular System
**Build:** A real competition entry with a production-minded structure: config-
driven pipeline, cross-validation, calibration, explainability, and a written
report an engineering manager could read.

**Proves:** You can turn raw data into a measurable, defensible model.

**Interview story:** "I can turn raw data into a measurable, production-minded ML
model, and I can tell you exactly where it breaks."

**Portfolio weight:** Medium. The report matters more than the leaderboard rank.

---

## Phase 2: Deep Learning

### Month 4 — Neural Network Library From Scratch
**Build:** A miniature deep learning framework in NumPy: tensors with autograd,
`Linear`/`ReLU`/`Dropout`/`BatchNorm` layers, MSE and cross-entropy losses,
SGD/Momentum/RMSProp/Adam optimizers, and a training loop. Trains MNIST to >95%.

**Proves:** PyTorch holds no mysteries for you.

**Interview story:** "I wrote the framework, so when someone asks why the loss is
NaN I start from the computational graph, not from Stack Overflow."

**Portfolio weight:** Medium-high. This one impresses engineers, which matters
because engineers do the technical screens.

---

### Month 5 — MNIST Production Training Pipeline
**Build:** The same problem, done the way a company would do it: config files,
seeded reproducibility, experiment tracking, checkpointing, early stopping,
model export, CLI, tests, CI.

**Proves:** You bring production discipline to ML code. Rare and valuable.

**Interview story:** "Same model, but this version is reproducible bit-for-bit
across machines. Here's the config diffing tool I wrote to prove it."

**Portfolio weight:** Medium. Reviewers who have suffered through research code
will notice immediately.

---

### Month 6 — Image Classification Service
**Build:** A trained classifier behind FastAPI, containerized, with measured p50/
p95/p99 latency, batching, a model card, and load-test results.

**Proves:** You can ship a model, not just train one.

**Interview story:** "Throughput went from 12 to 180 requests/sec when I added
dynamic batching. Here's the latency-vs-batch-size curve."

**Portfolio weight:** Medium. First real systems artifact.

---

## Phase 3: NLP and Transformers

### Month 7 — Semantic Search Engine
**Build:** Embedding-based search over a real corpus, backed by PostgreSQL with
pgvector, with a lexical (BM25) baseline, hybrid retrieval, and measured
recall@k and MRR against a hand-built relevance set.

**Proves:** You can build retrieval systems and prove they retrieve.

**Interview story:** "The embedding model lost to BM25 on exact-match queries, so
I built hybrid retrieval. Here's the query-category breakdown that showed me."

**Portfolio weight:** Medium-high. First project that fuses AI with your database
expertise. Build it on Postgres deliberately.

---

### Month 8 — Mini-GPT
**Build:** A decoder-only transformer implemented from scratch in PyTorch —
tokenizer, embeddings, positional encoding, multi-head causal attention, MLP,
residuals, layer norm, weight tying — trained on a small corpus with generated
samples and a README explaining every component and why it exists.

**Proves:** The core competency. This is the project that gets you past ML depth
screens.

**Interview story:** "I can derive and implement every line of a transformer.
Ask me about any component and I'll tell you what breaks without it."

**Portfolio weight:** **High.** Flagship #5. Do this one properly.

---

### Month 9 — Tiny Language Model Training Report
**Build:** A small LM trained on a curated dataset, with a training report:
data curation decisions, loss curves, perplexity, sampling comparisons,
scaling observations, failure modes, and a full reproducibility appendix.

**Proves:** You can run and reason about an actual training job.

**Interview story:** "Deduping the training corpus dropped validation perplexity
more than doubling the parameter count did. Here's the ablation."

**Portfolio weight:** Medium-high. The report is the artifact, not the model.

---

## Phase 4: LLM Engineering

### Month 10 — Enterprise Knowledge Assistant
**Build:** A production-style RAG system: PostgreSQL + pgvector, ingestion
pipeline, configurable chunking, hybrid retrieval, reranking, citation-grounded
generation, a FastAPI service, structured logging, and — critically — an
evaluation harness with a hand-labeled eval set measuring retrieval precision,
answer faithfulness, and hallucination rate.

**Proves:** You build RAG the way someone who has to operate it builds RAG.

**Interview story:** "Most RAG demos have no eval. Mine has 200 labeled
questions, and I can tell you the faithfulness score for each chunking strategy."

**Portfolio weight:** **High.** Flagship #4.

---

### Month 11 — Autonomous DBA Assistant ⭐
**Build:** The flagship. An LLM agent that ingests synthetic PostgreSQL telemetry
(pg_stat_statements, query plans, lock waits, bloat, replication lag), diagnoses
incidents, explains its reasoning, recommends safe remediations with an explicit
risk classification, and cites the evidence for every claim. Read-only by
default; any mutating action requires a human approval gate.

Ships with a scenario-based evaluation suite: N synthetic incidents with known
root causes, measuring diagnostic accuracy, evidence citation rate, false-alarm
rate, and unsafe-recommendation rate.

**Proves:** Everything. Agent engineering, evaluation, safety thinking, domain
depth, and the exact intersection almost no other candidate occupies.

**Interview story:** "I built an agent for the domain I have fifteen years in, so
I could actually grade it. It diagnoses 82% of incidents correctly and I can tell
you precisely which 18% it fails and why."

**Portfolio weight:** **Highest.** Flagship #1. This is the project on the top of
your resume. Give it the best month of the entire program.

---

### Month 12 — Fine-Tuned DBA Assistant Model
**Build:** A parameter-efficient fine-tune (LoRA/QLoRA) of a small open model on
a hand-curated DBA instruction dataset, with a dataset card, model card, and a
rigorous base-vs-tuned evaluation including regression checks on general
capability.

**Proves:** You can fine-tune, and more importantly you know when not to.

**Interview story:** "The fine-tune beat the base model on plan explanation but
regressed on general reasoning. Here's the tradeoff curve and here's why I'd use
RAG instead for two of the three use cases."

**Portfolio weight:** **High.** Flagship #6.

---

## Phase 5: AI Systems Engineering

### Month 13 — Distributed Evaluation Pipeline
**Build:** A Ray-based system that evaluates LLM/RAG outputs in parallel across
workers: sharded work queues, retries, cost accounting, result aggregation,
failure isolation, and a throughput/cost report.

**Proves:** You can scale AI workloads, not just run them on a laptop.

**Interview story:** "Evaluating 50k samples serially took 14 hours. Distributed,
it takes 22 minutes and costs $6. Here's the scaling curve and where it plateaus."

**Portfolio weight:** **High.** Flagship #7.

---

### Month 14 — Full MLOps Pipeline
**Build:** Training → evaluation → registry → deployment → monitoring, wired
together with CI/CD. Model versioning with lineage, automated eval gates on PRs,
drift detection, and alerting.

**Proves:** You can operate ML systems. Your incident-response background makes
this section genuinely strong rather than checkbox-complete.

**Interview story:** "The eval gate blocks any PR that regresses faithfulness by
more than 2%. I've had it catch three regressions. Here's the CI log."

**Portfolio weight:** **High.** Flagship #8.

---

### Month 15 — Production AI Cluster
**Build:** The DBA agent and RAG system deployed to local Kubernetes with
reproducible manifests: resource requests/limits, liveness and readiness probes,
horizontal scaling, async worker queues, structured logs, SLOs, runbooks, and a
rollback procedure. Includes the **Database Incident Commander** — the telemetry
+ RAG + agent system operating as one deployed product.

**Proves:** You can run this in production and be the person on call for it.

**Interview story:** "Here's the runbook for when the vector index degrades, and
here's the postmortem from the time I broke it on purpose to test the rollback."

**Portfolio weight:** **High.** Flagship #3.

---

## Phase 6: Research and Interviews

### Month 16 — Published Reproduction Report
**Build:** A rigorous small-scale reproduction of a published result (transformer
scaling behavior, LoRA rank ablation, or a DPO-style preference experiment) with
paper summary, implementation, experiments, ablations, discrepancies from the
published numbers, and honest lessons.

**Proves:** Research engineering. This is what Research Engineer roles screen for.

**Interview story:** "My numbers were 1.4 points off the paper's. Tracking down
why taught me more than matching them would have — it was the tokenizer."

**Portfolio weight:** **High.** Flagship #9 precursor.

---

### Month 17 — Original AI-for-Databases Research Project ⭐
**Build:** An original applied research project only someone with your background
would naturally produce. Recommended: *"Can LLM agents reliably diagnose
PostgreSQL performance incidents from telemetry and query plans?"* — with a
constructed benchmark, baselines, multiple agent configurations, ablations,
statistical treatment, and a written report.

**Proves:** You can identify a question, design an experiment, and produce a
finding. Negative results are acceptable and often more interesting.

**Interview story:** "I built the benchmark because none existed. Here's what
agents are good at in this domain and here's the specific class of incident where
they confidently produce dangerous recommendations."

**Portfolio weight:** **Highest.** Flagship #9. This plus Month 11 is the pair
that makes you memorable.

---

### Month 18 — Frontier AI Portfolio Package
**Build:** The landing page. A single GitHub profile README or static site that
presents all nine flagships with a coherent narrative, architecture diagrams,
demo recordings, blog posts, and a resume that a recruiter can scan in 20 seconds
and an engineer can dig into for an hour.

**Proves:** You can communicate. Underrated and frequently decisive.

**Portfolio weight:** This *is* the portfolio. Everything else feeds it.

**Must include:**
1. Autonomous DBA Agent
2. PostgreSQL/Oracle Query Plan Explainer
3. Database Incident Commander
4. Enterprise Knowledge RAG System
5. Tiny Transformer From Scratch
6. Fine-Tuned DBA Assistant
7. Distributed LLM Evaluation Platform
8. AI Reliability / MLOps Platform
9. Original research report on agent reliability for database incidents

---

## Capstone Difficulty Curve

```text
Effort
  ^
  |                                    ██ M11        ██ M17
  |                              ██ M10   ██ M12  ██ M15  ██ M16
  |                  ██ M08  ██ M09              ██ M13 ██ M14
  |        ██ M04 ██ M05 ██ M06 ██ M07                        ██ M18
  |  ██ M01 ██ M02 ██ M03
  +------------------------------------------------------------> Month
```

Months 11, 15, and 17 are the heaviest. Plan life around them: do not schedule
them against a major work deadline or a vacation. If something has to slip, slip
Month 6 (vision) or compress Month 2, never Month 11.
