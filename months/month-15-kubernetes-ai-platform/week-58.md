# Week 58: Kubernetes for AI Services

## Outcome

By Sunday the RAG system and DBA agent run on a local Kubernetes cluster with correct probes, resource contracts, config and secret management, and horizontal scaling.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The probe question is the one that separates people who have deployed model
servers from people who have deployed web services. A model server takes 60-120
seconds to load weights. A liveness probe with a 30-second initial delay will
kill it during startup, forever. The fix is a startup probe, and knowing that is
a specific, checkable piece of experience.

Resource requests and limits are the other one. Requests determine scheduling;
limits determine killing. For CPU, exceeding the limit throttles. For memory, it
OOMKills. An inference pod that occasionally spikes on a large batch needs
headroom between request and limit, and setting them equal is a choice with
consequences.

Everything else is standard deployment work, which is the point — this month
should feel like home with a few AI-specific wrinkles.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Core objects**
   1. Pod, Deployment, Service, Ingress
   2. ConfigMap and Secret
   3. PersistentVolumeClaim for model weights
   4. Job and CronJob for batch work
2. **Probes**
   1. Liveness: restart me
   2. Readiness: stop sending traffic, do not restart
   3. **Startup: I am slow to boot, hold off the liveness check**
   4. Why conflating liveness and readiness causes restart loops
3. **Resources**
   1. Requests schedule; limits kill
   2. CPU throttles, memory OOMKills
   3. QoS classes and eviction order
   4. Sizing from measurement, not guessing
   5. GPU resources and why they are not divisible
4. **Scaling**
   1. HorizontalPodAutoscaler on CPU, memory, or custom metrics
   2. Why queue depth is a better signal than CPU for inference
   3. Scale-up latency, and why model loading makes it worse
5. **Deployment**
   1. Rolling updates, maxSurge and maxUnavailable
   2. PodDisruptionBudgets
   3. preStop hooks and graceful drain

## Required Free Resources

- **Primary:** Kubernetes concepts documentation — https://kubernetes.io/docs/concepts/
- **Primary:** Kubernetes probe configuration — https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ — read this carefully; the startup probe is the AI-relevant part
- kind quick start — https://kind.sigs.k8s.io/docs/user/quick-start/
- 'Kubernetes resource management' — https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- KEDA — https://keda.sh/ — event-driven autoscaling, for queue-depth scaling

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=58
```

1. **Stand up a kind cluster** (1h) — Multi-node config. Get familiar with the tooling.
2. **Deploy the RAG API** (1.5h) — Deployment, Service, ConfigMap, Secret.
3. ****Probes, correctly**** (1.5h) — Startup probe for the model load. Then deliberately misconfigure liveness and watch the restart loop.
4. **Resource requests and limits** (1.5h) — Measure actual usage first, then set them. Justify the headroom.
5. **Trigger an OOMKill deliberately** (45m) — Set the memory limit too low and watch. Instructive.
6. **PersistentVolumeClaim for model weights** (1h) — Keeps the image small and lets weights change independently.
7. **Postgres in-cluster or as an external service** (1h) — Decide which and justify it. StatefulSet if in-cluster.
8. **HorizontalPodAutoscaler** (1.5h) — On CPU first, then on a custom metric. Note the scale-up latency.
9. **Rolling update with graceful drain** (1h) — preStop hook. Verify zero dropped requests during a deploy.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
m
l
o
p
s
-
p
l
a
t
f
o
r
m
/
i
n
f
r
a
/
k
8
s
/
```

## Tests To Write

Add: a test that applies the manifests to kind, waits for readiness, sends a request, and tears down. That test is the deployment contract.

## Portfolio Artifact

The manifests, and the probe misconfiguration write-up — what the restart loop looked like and how the startup probe fixed it.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (30 min).** Recorded: *Requests versus limits for a GPU inference pod — what do you set and what happens if you get it wrong?* Then: *Your model server takes 90 seconds to load. Configure the probes.*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Set up queue-depth autoscaling with KEDA. CPU utilization is a poor scaling signal for inference — a pod waiting on a GPU looks idle — while queue depth directly reflects unserved demand. Configure it, load test it, and compare the scaling behavior against CPU-based HPA. The comparison plot is a good artifact.
