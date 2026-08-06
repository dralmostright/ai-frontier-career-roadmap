# Portfolio Strategy

The portfolio is the scouting tape. It is what gets you the first conversation,
and it is what the interviewers read for ten minutes before your call.

---

## The One-Sentence Thesis

Every artifact in this portfolio exists to support one claim:

> **I am a production database expert who learned AI deeply enough to build
> reliable LLM systems for real operational problems. I can reason from math to
> models, from models to systems, and from systems to customer impact.**

If a project does not support that claim, it does not go in the portfolio, no
matter how much work it took.

---

## Why Differentiation Beats Volume

The applicant pool for AI Engineer roles is saturated with a specific profile:
a bootcamp or self-taught background, three RAG chatbots, a fine-tuned Llama, and
a LangChain agent that summarizes PDFs. These portfolios are interchangeable.
Reviewers spend 90 seconds on them and move on.

You cannot win by being a better version of that profile. You win by being a
different profile entirely:

| Their portfolio | Your portfolio |
| --------------- | -------------- |
| RAG chatbot over PDFs | RAG over database telemetry with a labeled eval set |
| "It gives good answers" | "82% diagnostic accuracy, here's the confusion matrix" |
| Runs in a notebook | Runs on Kubernetes with runbooks and SLOs |
| No failure analysis | A documented taxonomy of failure modes |
| Generic domain | Fifteen years of domain expertise nobody else has |
| Agent that calls tools | Agent with an approval gate, audit log, and blast-radius analysis |

**The asymmetry:** an ML engineer cannot easily acquire your operational
background. You can acquire their ML background in 18 months. That trade favors
you, but only if the portfolio makes the operational depth visible.

---

## The Nine Flagships

Ranked by portfolio weight. The top three carry the most.

### 1. Autonomous DBA Agent ⭐⭐⭐
**Built in:** Month 11 | **Repo:** `ai-dba-agent`

An LLM agent that ingests PostgreSQL telemetry, diagnoses performance incidents,
explains its reasoning with cited evidence, and proposes remediations classified
by risk. Read-only by default; mutating actions require explicit human approval.

**What it proves:** agent architecture, tool design, safety engineering,
evaluation rigor, and irreplaceable domain expertise.

**The differentiating detail:** the evaluation suite. Anyone can build an agent.
Almost nobody builds the benchmark to grade it, because almost nobody knows the
ground truth. You do. That is the whole point.

**README must lead with:** the accuracy number and the safety architecture.

---

### 2. Original Research: Agent Reliability for Database Incidents ⭐⭐⭐
**Built in:** Month 17 | **Repo:** `dba-agent-reliability-study`

Original applied research asking whether LLM agents can reliably diagnose
production database incidents, with a constructed benchmark, multiple agent
configurations, ablations, and honest reporting including negative results.

**What it proves:** research engineering. Question formulation, experimental
design, statistical honesty, and technical writing.

**Why it matters disproportionately:** Research Engineer roles screen for exactly
this and very few applied candidates have any of it. Even for non-research roles,
a candidate who has run a real experiment reads as fundamentally more serious.

**README must lead with:** the finding, including the uncomfortable part.

---

### 3. Database Incident Commander ⭐⭐⭐
**Built in:** Month 15 | **Repo:** `db-incident-commander`

The deployed product: telemetry ingestion + RAG over runbooks and postmortems +
the agent, running on Kubernetes with health checks, SLOs, structured logging,
rollback procedures, and an actual runbook for when the AI system itself fails.

**What it proves:** you can operate AI in production. This is the artifact that
makes an infrastructure hiring manager sit up.

**The differentiating detail:** a postmortem you wrote for a failure you induced
on purpose to test the rollback. Nobody does this. It is unmistakably the work of
someone who has been on call.

---

### 4. Enterprise Knowledge RAG System ⭐⭐
**Built in:** Month 10 | **Repo:** `enterprise-knowledge-assistant`

Production-grade RAG on PostgreSQL/pgvector with an ingestion pipeline, hybrid
retrieval, reranking, citation grounding, permission-aware filtering, and a
200-question labeled evaluation set.

**What it proves:** the bread-and-butter skill of applied AI engineering, done
with rigor.

**Differentiate it by:** the eval harness and the permission filtering. Those two
things separate a demo from a system somebody could actually deploy at a company.

---

### 5. Tiny Transformer From Scratch ⭐⭐
**Built in:** Month 8 | **Repo:** `mini-gpt-from-scratch`

A decoder-only transformer built component by component in PyTorch, trained on a
small corpus, with a README that explains every architectural decision and what
breaks without it.

**What it proves:** depth. This is the credibility artifact — it tells reviewers
that your higher-level work is built on understanding rather than API calls.

**Differentiate it by:** the ablation table. "Here's what happens to loss when I
remove residual connections / layer norm / positional encoding." That table is
worth more than the model.

---

### 6. Fine-Tuned DBA Assistant ⭐⭐
**Built in:** Month 12 | **Repo:** `dba-assistant-finetune`

LoRA fine-tune of a small open model on a hand-curated DBA instruction dataset,
with dataset card, model card, and rigorous base-vs-tuned comparison including
general-capability regression testing.

**What it proves:** you can fine-tune and, more importantly, you know when to.

**Differentiate it by:** the honest conclusion. If RAG beats the fine-tune for
two of three use cases, say so. That judgment is the senior signal.

---

### 7. Distributed LLM Evaluation Platform ⭐⭐
**Built in:** Month 13 | **Repo:** `distributed-llm-eval`

Ray-based parallel evaluation with sharding, retries, cost accounting, failure
isolation, and a scaling analysis.

**What it proves:** you can operate AI workloads at scale and think about cost.

**Differentiate it by:** the cost report. Engineers who track dollars per
evaluation run are rare and immediately trusted with budgets.

---

### 8. AI Reliability / MLOps Platform ⭐⭐
**Built in:** Month 14 | **Repo:** `ml-reliability-platform`

Training → eval → registry → deploy → monitor, with CI/CD, automated eval gates,
drift detection, and alerting.

**What it proves:** end-to-end ownership.

**Differentiate it by:** the eval gate catching a real regression, with the CI log
as evidence.

---

### 9. PostgreSQL/Oracle Query Plan Explainer ⭐
**Built in:** Month 11 (spun out) | **Repo:** `query-plan-explainer`

A focused tool that takes an `EXPLAIN ANALYZE` output and produces a
human-readable explanation, identifies the problem node, and suggests fixes.

**What it proves:** you ship useful things. This is the one that might get actual
users, which is its own signal.

**Why it's separate from the agent:** small, self-contained tools get starred and
shared. A monolith does not. This is your distribution play.

---

## Supporting Artifacts

Not flagships, but they make the flagships credible.

| Artifact | Month | Role |
| -------- | ----- | ---- |
| ML Math Toolkit | 1 | Proves the foundations are real |
| NumPy DL Library | 4 | Proves PyTorch isn't magic to you |
| MNIST Production Pipeline | 5 | Proves engineering discipline |
| Image Classification Service | 6 | Proves you can serve models |
| Semantic Search Engine | 7 | First AI+database fusion |
| Tiny LM Training Report | 9 | Proves you can run training jobs |
| Reproduction Report | 16 | Proves research capability |

Keep them public, keep them clean, but do not feature them. They are depth on
demand, not the front page.

---

## The README Standard

Every README, without exception:

```markdown
# Project Name

> One sentence: what it does and who it's for.

[Demo GIF or architecture diagram — above the fold, always]

## The Problem
Why this exists. Two paragraphs. Concrete, not abstract.

## Results
The numbers. In a table. Compared against a baseline. Before anything else
technical, because this is what a reviewer is scanning for.

## Architecture
Diagram plus a walkthrough of the data flow.

## Key Technical Decisions
Three to five decisions, each with the alternative you rejected and why.
This section is what interviewers quote back at you.

## Setup
    make setup
    make test
    make demo
Three commands. If it takes more, fix the project, not the README.

## Evaluation
How you measured it. What the eval set is. How it was labeled.

## Limitations
Honest. Specific. This section builds more trust than any other.

## Future Work
Two or three things, with reasons.

## Interview Talking Points
The three things you'd want to be asked about.
```

**The above-the-fold rule.** A reviewer decides in 15 seconds. Diagram, one-line
description, and results table must all be visible without scrolling.

---

## Blog Posts

Six posts over 18 months. Publish on a personal site, dev.to, or Medium, and
cross-post to LinkedIn where recruiters actually look.

| # | Month | Working title |
| - | ----- | ------------- |
| 1 | 5 | "What a DBA Learns Building a Neural Network From Scratch" |
| 2 | 8 | "Every Component of a Transformer, and What Breaks Without It" |
| 3 | 10 | "Your RAG System Has No Evaluation and That's a Production Incident Waiting" |
| 4 | 12 | "I Built an AI Agent for the Domain I Know Best. Here's Where It Failed." |
| 5 | 15 | "SLOs for LLM Systems: Applying Database Reliability Practice to AI" |
| 6 | 17 | "Can LLM Agents Diagnose Database Incidents? A Benchmark and a Warning" |

Posts 3, 4, 5, and 6 are the ones with distribution potential — they say something
only you can say. Post 4 in particular (an honest failure analysis from a domain
expert) is the kind of thing that gets shared by people who hire.

---

## GitHub Profile

Your profile README is the landing page. Structure:

```markdown
# [Name]
**AI Systems Engineer | LLM Platform | Database Reliability**

[One-paragraph positioning statement]

## Flagship Work
[3 project cards: image, one line, key metric, link]

## What I Build
[2-3 sentences on the specialization]

## Writing
[3 best posts]

## Background
[2 sentences: N years production database engineering at scale, now applying
that operational rigor to AI systems]
```

Pin the top six repos. Order them: DBA Agent, Research Study, Incident Commander,
RAG System, Mini-GPT, Query Plan Explainer.

---

## Publishing Cadence

Do not wait until Month 18 to publish. Recruiters find people through activity.

| Cadence | Action |
| ------- | ------ |
| Weekly | Push commits. Green squares are weak evidence but visible evidence. |
| Monthly | Publish the capstone with a finished README. |
| Bimonthly | Post a technical write-up. |
| Quarterly | Update the profile README and resume. |
| Month 12+ | Start engaging publicly: comment substantively on AI infra discussions, answer questions in your specialty. |

---

## Common Portfolio Mistakes

| Mistake | Why it costs you |
| ------- | ---------------- |
| Twelve mediocre repos | Reviewers assume the mean, not the max. Curate to nine. |
| No numbers anywhere | Unmeasured work reads as unfinished work. |
| No limitations section | Reads as inexperience. Every real system has limits. |
| Hiding the DBA background | Discards your only structural advantage. |
| Tutorial projects unmodified | Reviewers recognize them instantly. |
| Private repos | Invisible work is not portfolio. |
| Broken setup instructions | The single fastest way to lose a reviewer. Test them on a clean machine. |
| No architecture diagrams | Forces the reviewer to read code to understand scope. They won't. |
| Last commit 8 months ago | Reads as abandoned. Keep at least one repo warm. |

---

## The Portfolio Audit

Every quarter, open your GitHub in a private browser window and spend exactly
90 seconds on it, as a stranger would. Then answer:

1. Can I tell what this person specializes in? (If not: fix the profile README.)
2. Is there a number visible anywhere? (If not: fix the flagship READMEs.)
3. Would I ask this person for an interview? (If not: identify the specific gap.)
4. What is the most impressive thing here, and is it in the first screen?

Write the answers into your monthly review. Fix whatever the 90 seconds exposed.
