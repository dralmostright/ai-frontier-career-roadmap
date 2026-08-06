# Month 18 Capstone: Frontier AI Portfolio Package

## Objective

Convert eighteen months of work into a coherent, scannable portfolio that makes a specific claim, plus the interview fluency to back it up.

## Business Problem

You are the product. The problem is that a reviewer will spend ninety seconds
deciding whether to spend an hour, and most of what makes you unusual is not
visible in ninety seconds unless you make it so.

The claim to make: a production database expert who learned AI deeply enough to
build reliable LLM systems for real operational problems, with the artifacts to
prove each half.

## Technical Requirements

The nine flagships, each finished to standard:

1. Autonomous DBA Agent (M11)
2. Original research: agent reliability for database incidents (M17)
3. Database Incident Commander (M15)
4. Enterprise Knowledge RAG System (M10)
5. Tiny Transformer From Scratch (M8)
6. Fine-Tuned DBA Assistant (M12)
7. Distributed LLM Evaluation Platform (M13)
8. AI Reliability / MLOps Platform (M14)
9. PostgreSQL Query Plan Explainer (M11, spun out)

Plus: a profile README, a one-page resume, six published posts, three demo
recordings, and twelve rehearsed STAR stories.

## Theory Requirements

You must be able to deliver, cold:

1. The four-minute portfolio walkthrough, and the 90-second and 20-second versions.
2. The 60-second career-change narrative, adapted to three company types.
3. Any of the twelve system designs in 45 minutes.
4. Any derivation from the core set on a whiteboard.
5. Any of the twelve STAR stories in 90-120 seconds.

## System Design Requirements

- Profile README as the entry point, positioning first
- Flagships pinned in priority order
- Every repository self-contained: clone, one command, working demo
- Consistent README structure so a reviewer learns the format once

## Implementation Plan

Week 75 polishes the repositories. Week 76 runs the loops and builds the
recruiter package. Week 77 executes the applications. Week 78 assesses honestly.

The capstone is assembled across all four.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Nine flagships published to standard | Yes |
| Every setup tested on a clean clone | Yes, timed |
| Results above the fold on every README | Yes |
| Architecture diagrams | Every repository with 3+ components |
| Demo recordings | 3 |
| Posts published | 6 |
| STAR stories rehearsed | 12 |
| Full loop score | 142+ / 180 |
| Interview readiness | 31+ / 35 |
| 90-second test | Passes with three outside readers |

## Expected Repository Structure

```text
github.com/<you>/
  README.md                        <- the profile, the landing page
  autonomous-dba-agent/            ⭐ pinned 1
  dba-agent-reliability-study/     ⭐ pinned 2
  db-incident-commander/           ⭐ pinned 3
  enterprise-knowledge-assistant/     pinned 4
  mini-gpt-from-scratch/              pinned 5
  query-plan-explainer/               pinned 6
  dba-assistant-finetune/
  distributed-llm-eval/
  ml-reliability-platform/
  ...supporting repositories
```

## README Requirements

The profile README:

```
# [Name]
**AI Systems Engineer | LLM Platform | Database Reliability**

[One paragraph: N years keeping production databases reliable at scale, now
building AI systems with the same operational rigor. Specialized in autonomous
database intelligence, retrieval systems, and LLM evaluation.]

## Flagship Work
[Three cards: image, one line, headline metric, link]

## What I Build
[2-3 sentences on the specialization]

## Writing
[Three best posts]

## Background
[Two sentences framing the database experience as the advantage it is]
```

Positioning first. Not a technology list.

## Demo Requirements

Three recordings: the DBA agent diagnosing an incident, the Incident Commander failing and recovering, and the RAG system answering with citations and refusing when it should. Three minutes each, linked from the relevant READMEs.

## Blog Post Requirement

All six posts published and linked. Posts 3, 4, 5, and 6 are the differentiated ones — the RAG evaluation argument, the honest agent failure analysis, the SLO framing, and the research finding.

## Interview Story

The four-minute walkthrough:

```
0:00-0:20  Positioning. One sentence on who you are and what you build.
0:20-1:30  The DBA agent. Problem, one hard decision, the measured result.
1:30-2:30  Breadth: Mini-GPT and the MLOps platform, 30 seconds each.
2:30-3:30  The research. Question, method, finding — including the surprise.
3:30-4:00  Why this company specifically.
```

Rehearse until automatic. Then the 90-second and 20-second versions.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 18 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 9 | The positioning claim is specific and defensible. |
| Technical execution | 9 | Nine finished flagships. |
| Evaluation rigor | 9 | Every project reports numbers. |
| Code quality | 8 | Consistent across repositories. |
| Documentation | 10 | **The portfolio is documentation. Target 10.** |
| Reproducibility | 9 | Clean-clone tested, all nine. |
| Error analysis | 9 | Every flagship has a limitations section. |
| Portfolio readiness | 10 | **This is the portfolio. Target 10.** |

**Overall target: 9.0+.**

## Stretch Goals

1. **A portfolio site** with the narrative and the demos embedded.
2. **A conference talk proposal** on the research or the agent work.
3. **The retrospective post**, which is also the best distribution channel.
4. **Open-source contributions** to a project you used — pgvector, PEFT, Ray.

## Limitations To State Honestly

Be honest with yourself about these:

- Eighteen months is enough to be genuinely competent and not enough to be
  senior in AI specifically. Your seniority comes from the operational side.
- The portfolio is strongest in applied engineering and evaluation, and lighter
  in research novelty and large-scale training experience.
- Every project is single-author and single-environment. You have not worked in
  a team on these systems.
- Your compute experience is capped by budget; you have reasoned about
  large-scale training without doing it.

State the first and last of these openly in interviews if asked. Being accurate
about the boundary of your experience is a seniority signal, not a weakness.
