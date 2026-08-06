# Course Map

The 18-month arc, why it is ordered this way, and what you can do at each gate.

---

## Design Logic

The course moves through six phases. The ordering is not arbitrary and it is not
the order most self-taught engineers use. Most people start at the top of the
stack (call an API, build a chatbot) and never acquire the layer underneath.
That produces candidates who fail the first "derive attention on the whiteboard"
question and who cannot debug a training run.

This course goes bottom-up with a deliberate exception: interview drills and
production discipline start in Week 1 and never stop.

```text
Phase 1  Months 1-3    Math + Classical ML         The conditioning work
Phase 2  Months 4-6    Deep Learning               Building the engine
Phase 3  Months 7-9    NLP + Transformers          The core competency
Phase 4  Months 10-12  LLM Engineering             Where you get paid
Phase 5  Months 13-15  AI Systems Engineering      Where your DBA past compounds
Phase 6  Months 16-18  Research + Interviews       Proving it and selling it
```

Your existing strengths — Linux, Python, SQL, production operations, incident
response, data engineering — mean Phase 5 will feel like home. Phase 1 will feel
slow and it is the phase most likely to get skipped. Do not skip it. The
Month 1-4 material is precisely what separates a candidate who can talk about
transformers from one who can derive them.

---

## Phase 1: Mathematical and Classical ML Foundations (Months 1-3)

**Gate condition:** you can derive gradient descent for logistic regression on a
whiteboard, implement a random forest from scratch, and explain why your model's
validation score is a lie when there is leakage.

| Month | Focus                             | Capstone                        |
| ----- | --------------------------------- | ------------------------------- |
| 1     | Linear algebra, calculus, probability | ML Math Toolkit             |
| 2     | Classical ML implemented by hand  | Titanic ML Pipeline             |
| 3     | Practical ML, evaluation, debugging | End-to-End Kaggle Tabular System |

**Why first.** Everything later is a special case of this. Attention is a
similarity matrix times a value matrix. Training is gradient descent with
scheduling tricks. Evaluation is the same precision/recall reasoning applied to
generated text. Skipping this makes the rest memorization.

**Your leverage.** Error analysis and evaluation discipline are just root-cause
analysis, which you already do professionally. Lean into it.

---

## Phase 2: Deep Learning Mastery (Months 4-6)

**Gate condition:** you have written a working autodiff engine, you can debug a
training run that is not converging, and you have shipped a model behind an API
with measured latency.

| Month | Focus                          | Capstone                            |
| ----- | ------------------------------ | ----------------------------------- |
| 4     | Neural networks from scratch   | NumPy Deep Learning Library         |
| 5     | PyTorch engineering            | MNIST Production Training Pipeline  |
| 6     | Computer vision                | Image Classification Service        |

**Why here.** Month 4 makes PyTorch legible instead of magical. Month 5 turns you
into someone who can be handed a training script and make it reproducible.
Month 6 is the cheapest domain in which to practice full training pipelines —
vision datasets are small, fast, and visually debuggable.

**Your leverage.** Month 5's reproducibility, config management, and checkpointing
work is operations work. You will be better at it than most ML researchers.

---

## Phase 3: NLP and Transformers (Months 7-9)

**Gate condition:** you can implement multi-head attention from memory, explain
every component of a GPT block including why it is there, and train a small
language model to a sane perplexity.

| Month | Focus                        | Capstone                        |
| ----- | ---------------------------- | ------------------------------- |
| 7     | NLP foundations, embeddings  | Semantic Search Engine          |
| 8     | Transformers first principles | Mini-GPT                       |
| 9     | Modern LLM architecture and training | Tiny Language Model Report |

**Why here.** This is the single most-tested body of knowledge in frontier lab
interviews. Month 8 in particular is the month that most determines whether you
pass an ML-depth screen. Budget extra time for it.

**Your leverage.** Month 7's semantic search capstone is your first project that
naturally sits on PostgreSQL. Build it on pgvector, not on a hosted vector
service — that choice becomes an interview story about operational tradeoffs.

---

## Phase 4: LLM Engineering and Applied AI (Months 10-12)

**Gate condition:** you have a RAG system with a real evaluation harness, an
agent with measured reliability, and a fine-tuned model with a model card.

| Month | Focus                    | Capstone                          |
| ----- | ------------------------ | --------------------------------- |
| 10    | Retrieval-augmented generation | Enterprise Knowledge Assistant |
| 11    | Agent engineering        | Autonomous DBA Assistant  ⭐        |
| 12    | Fine-tuning and preference optimization | Fine-Tuned DBA Assistant Model |

**Why here.** This is the work most AI engineering job descriptions actually
describe. It is also where the market is saturated with weak portfolios — nearly
every candidate has "a RAG chatbot." Yours will be distinguishable only through
evaluation rigor and the database specialization.

**⭐ Month 11 is the flagship month.** The Autonomous DBA Assistant is the single
project most likely to get you an interview. Give it your best month.

---

## Phase 5: AI Systems Engineering (Months 13-15)

**Gate condition:** you can reason about GPU memory and throughput, deploy an
inference service to Kubernetes, and explain how you would run an LLM platform
on call.

| Month | Focus                    | Capstone                       |
| ----- | ------------------------ | ------------------------------ |
| 13    | Distributed AI systems   | Distributed Evaluation Pipeline |
| 14    | MLOps                    | Full MLOps Pipeline            |
| 15    | Kubernetes AI platform   | Production AI Cluster          |

**Why here.** This is your home phase and it is deliberately placed late so you
arrive with enough ML context to make the infrastructure decisions meaningfully
rather than generically. An AI Infrastructure Engineer who understands
attention's memory profile is worth several who do not.

**Your leverage.** Enormous. Reliability, monitoring, incident response,
capacity planning, and cost control are your professional native language.
Most ML engineers are visibly weak here. Interview accordingly.

---

## Phase 6: Research Engineering and Interview Execution (Months 16-18)

**Gate condition:** you have reproduced a published result, produced one original
piece of applied research, and passed mock loops at the level you are targeting.

| Month | Focus                    | Capstone                                   |
| ----- | ------------------------ | ------------------------------------------ |
| 16    | Paper reproduction       | Published Reproduction Report              |
| 17    | Original applied research | Original AI-for-Databases Research Project |
| 18    | Interview war room       | Frontier AI Portfolio Package              |

**Why last.** Research reproduction requires everything before it. Month 17's
original work is what separates a strong engineer from a Research Engineer
candidate. Month 18 assumes the learning is done and converts it into offers.

---

## Skill Progression By Quarter

| End of  | You can...                                                                |
| ------- | ------------------------------------------------------------------------- |
| Month 3  | Build, evaluate, and debug a classical ML model to a professional standard |
| Month 6  | Train deep networks reliably and serve them behind a tested API           |
| Month 9  | Implement a transformer from scratch and train a small LM end to end      |
| Month 12 | Ship RAG and agent systems with measured quality, and fine-tune a model   |
| Month 15 | Operate an AI platform: distributed, monitored, deployed, on-call ready   |
| Month 18 | Reproduce research, produce original findings, and interview at frontier labs |

---

## Dependency Graph

Some months can be reordered under pressure; most cannot.

```text
M1 ──> M2 ──> M3 ──┐
                   ├──> M4 ──> M5 ──> M6 ──┐
                   │                       ├──> M7 ──> M8 ──> M9 ──┐
                   │                       │                       │
                   └───────────────────────┴───────────────────────┼──> M10 ──> M11 ──> M12
                                                                   │             │
                                                       M13 ──> M14 ┴─> M15       │
                                                                   │             │
                                                                   └──> M16 ──> M17 ──> M18
```

Hard dependencies:

- **M8 requires M5.** You cannot implement attention without PyTorch fluency.
- **M11 requires M10.** Agents without retrieval is a toy.
- **M16 requires M8 and M12.** You reproduce what you can already build.
- **M17 requires M11.** The research question comes from the flagship agent.
- **M18 requires everything.** It is the only month with no new learning.

Soft dependencies (reorderable if a job opportunity forces it):

- **M6 (vision)** can be compressed to two weeks if you are certain you are
  targeting LLM-only roles. You lose CNN interview coverage; accept that trade
  knowingly, not by drift.
- **M13-M15** can move earlier if you land an infrastructure-flavored interview
  loop sooner than expected.

---

## The Nine Flagship Artifacts

Everything in the course funnels into these. See `PORTFOLIO_STRATEGY.md`.

1. Autonomous DBA Agent (M11)
2. PostgreSQL/Oracle Query Plan Explainer (M11, spun out)
3. Database Incident Commander: LLM + RAG + telemetry (M15)
4. Enterprise Knowledge RAG System (M10)
5. Tiny Transformer From Scratch (M8)
6. Fine-Tuned DBA Assistant (M12)
7. Distributed LLM Evaluation Platform (M13)
8. AI Reliability / MLOps Platform (M14)
9. Research report on agent reliability for database incidents (M17)

---

## What Failure Looks Like

Be able to recognize these early:

- **Tutorial drift.** Watching lectures without implementing. Symptom: no commits.
- **Portfolio hoarding.** Ten half-finished repos. Symptom: no READMEs.
- **Skipping evaluation.** Building systems with no measured quality. Symptom:
  you cannot state a number when asked how good your RAG system is.
- **Deferring interview prep.** Symptom: Month 18 becomes Month 18 through 24.
- **Hiding the DBA background.** Symptom: your portfolio looks like everyone
  else's. This is the most expensive mistake available to you.
