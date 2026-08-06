# Month 15 Capstone: Production AI Cluster

## Objective

Deploy the whole stack as an operated product, then prove it is operated: SLOs with error budgets, tested runbooks, a measured rollback, and a postmortem from a failure you induced on purpose.

## Business Problem

A database incident starts with a page and thirty minutes of triage by whoever
is awake. The Incident Commander compresses that: it ingests telemetry,
retrieves relevant runbooks and past postmortems, runs the diagnostic agent, and
presents a ranked set of candidate causes with cited evidence and risk-classified
remediations.

The human still decides and still executes. What changes is that they start from
a briefing rather than from a blank terminal at 3am.

Be honest about the scope: this accelerates triage. It does not resolve
incidents.

## Technical Requirements

- The Month 10 RAG system, Month 11 agent, and Month 13 eval pipeline, deployed
- Kubernetes manifests: Deployments, Services, ConfigMaps, Secrets, PVCs, HPAs, Jobs
- Correct probes, including startup probes for slow model loading
- Resource requests and limits informed by measurement
- Async workers with queue-depth autoscaling
- Graceful degradation and circuit breakers
- Prometheus and Grafana, with the Month 14 metric set
- SLOs with error budgets, including quality
- **Four tested runbooks**
- **A measured rollback**
- **A postmortem from an induced failure**
- Hardened images, documented size reduction

## Theory Requirements

The README must explain:

1. Liveness versus readiness versus startup probes, and why a model server needs
   all three.
2. Requests versus limits, with your measured numbers and the headroom reasoning.
3. The degradation chain: what happens as each dependency fails.
4. The SLOs, and why a quality SLO burn is a real incident.
5. **What the induced failure taught you that testing had not.**

## System Design Requirements

- One namespace per environment
- Config and secrets externalized
- Stateless services; state in Postgres and object storage
- Queue-backed async work
- Every alert linked to a runbook in the repository
- Rollback as a single documented command

## Implementation Plan

**Day 1** — Hardened images, size documented.

**Day 2** — Core manifests, probes, resources.

**Day 3** — Workers, queues, autoscaling.

**Day 4** — Assemble the Incident Commander: telemetry + RAG + agent.

**Day 5** — Observability, SLOs, alerts, runbooks.

**Day 6** — **Induce the failure. Respond. Write the postmortem.**

**Day 7** — README and publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Full stack deploys from manifests | `make deploy` on a clean kind cluster |
| Zero dropped requests during a rolling update | Verified under load |
| Probes correct | Model server survives a slow start |
| Autoscaling | Responds to queue depth, with the lag measured |
| Rollback | Under 5 minutes, executed from the runbook |
| Runbooks | Four, each tested by someone else or in a game day |
| **Postmortem** | **Written, with action items implemented** |
| Image size | Under 1GB, reduction documented |

## Expected Repository Structure

```text
db-incident-commander/
  README.md
  Makefile
  infra/
    docker/  k8s/  helm/  grafana/  prometheus/
    runbooks/
      quality-degradation.md  retrieval-failure.md
      model-api-outage.md  index-corruption.md
      rollback.md
  src/
    commander/         telemetry + RAG + agent, composed
    api/  workers/
  tests/
    unit/  integration/  chaos/
  docs/
    design.md
    slos.md
    postmortem-001.md      <- the artifact
    limitations.md
```

## README Requirements

Above the fold: one sentence, an architecture diagram, and a link to the
postmortem.

Then: the problem and the honest scope; the architecture; the deployment with
`make deploy`; probes and resources with the reasoning; the degradation chain;
SLOs and error budgets; the runbook catalogue; the measured rollback;
**the postmortem, prominently**; the image size reduction; limitations.

**Link the postmortem above the fold.** It is the most unusual thing in the
repository and the thing most likely to make a reviewer read further.

## Demo Requirements

A 4-minute recording: deploy, send traffic, show the dashboards, induce the failure, show the alert firing, execute the rollback, show recovery. That recording is the portfolio piece.

## Blog Post Requirement

Optional; post #5 was Month 14's. If you write one, the postmortem itself — lightly edited — is the post. Published postmortems get read.

## Interview Story

> "I deployed a deliberately bad model to see what my monitoring would catch.
> The prediction-distribution alert fired in six minutes; the accuracy signal
> would have taken two days. Rollback took three minutes forty from the runbook.
> The postmortem is in the repo — the interesting part is the two alerts I
> expected to fire and didn't, and what I changed."

60 seconds. Nobody else has this story.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 15 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 9 | A real operational problem, honestly scoped. |
| Technical execution | 9 | The full stack deployed and operating. |
| Evaluation rigor | 8 | Measured rollback, measured scaling, measured detection lag. |
| Code quality | 8 | Manifests clean and parameterized. |
| Documentation | 10 | **Runbooks and the postmortem. Target 10.** |
| Reproducibility | 9 | `make deploy` on a clean cluster. |
| Error analysis | 10 | **The postmortem is the error analysis.** Target 10. |
| Portfolio readiness | 10 | **Flagship #3.** The postmortem is the differentiator. |

**Overall target: 9.0+. Flagship. The postmortem is what earns it.**

## Stretch Goals

1. **A second postmortem** from a different failure class. Two is a pattern.
2. **A game day** with someone else responding from your runbooks.
3. **A Helm chart** so someone else can actually deploy it.
4. **Cost dashboard** showing spend by component.

## Limitations To State Honestly

- Runs on a local kind cluster. A real deployment adds cloud networking,
  managed databases, multi-zone concerns, and actual GPU scheduling.
- No GPU nodes; inference is CPU or API-based.
- Single environment. Real setups separate dev, staging, and production.
- The postmortem covers one induced failure of one class. Real incidents are
  more varied and less convenient.
- SLO targets are chosen by me without a real user base to inform them.
- Runbooks tested by one other person, not by an on-call rotation.
