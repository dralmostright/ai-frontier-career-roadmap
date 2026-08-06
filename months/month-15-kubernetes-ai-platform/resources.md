# Month 15 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Google SRE Book, 'Postmortem Culture'** (Week 60) — https://sre.google/sre-book/postmortem-culture/
The framing for the month's most important artifact.

**Kubernetes probe documentation** (Week 58) — https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
Read carefully. The startup probe is the AI-relevant detail most people miss.

**Published postmortems** — Cloudflare, GitLab, AWS. Read three before writing
yours. The good ones are specific about what surprised them.

**Kleppmann, 'Designing Data-Intensive Applications'** ch. 10-11 (Week 59) —
you may know this; it applies directly to batch inference.

---

## Week 57 — Docker Hardening

- **Primary:** Docker best practices — https://docs.docker.com/build/building/best-practices/
- **Primary:** Google distroless images — https://github.com/GoogleContainerTools/distroless
- 'Docker for Python developers' — the multi-stage patterns for Python specifically
- Trivy — https://trivy.dev/ — vulnerability scanning
- OCI image spec labels — for provenance metadata
## Week 58 — Kubernetes for AI Services

- **Primary:** Kubernetes concepts documentation — https://kubernetes.io/docs/concepts/
- **Primary:** Kubernetes probe configuration — https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ — read this carefully; the startup probe is the AI-relevant part
- kind quick start — https://kind.sigs.k8s.io/docs/user/quick-start/
- 'Kubernetes resource management' — https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- KEDA — https://keda.sh/ — event-driven autoscaling, for queue-depth scaling
## Week 59 — Scaling, Queues, and Batch Inference

- **Primary:** 'Designing Data-Intensive Applications' (Kleppmann) — chapters 10-11 on batch and stream processing. You may know this material; it applies directly.
- **Primary:** vLLM continuous batching documentation — https://docs.vllm.ai/
- Celery or ARQ documentation — whichever queue library you choose
- KEDA scalers — https://keda.sh/docs/latest/scalers/ — for worker autoscaling
## Week 60 — Reliability and Incident Response

- **Primary:** Google SRE Book, 'Postmortem Culture' — https://sre.google/sre-book/postmortem-culture/
- **Primary:** Google SRE Workbook, 'Incident Response' — https://sre.google/workbook/incident-response/
- Google SRE Book, 'Embracing Risk' — error budgets — https://sre.google/sre-book/embracing-risk/
- 'The Field Guide to Understanding Human Error' (Dekker) — the blameless framing, argued properly
- Published postmortems from Cloudflare, GitLab, and AWS — read three as format references

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| MLflow | https://mlflow.org/docs/latest/ | Month 14 |
| Kubernetes | https://kubernetes.io/docs/home/ | Month 15 |
| kind | https://kind.sigs.k8s.io/ | Week 58 |
| Prometheus | https://prometheus.io/docs/ | Weeks 56, 60 |
| Google SRE Book | https://sre.google/sre-book/table-of-contents/ | Weeks 56, 60 |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| KEDA | https://keda.sh/ | Queue-depth autoscaling |
| Trivy | https://trivy.dev/ | Image scanning |
| Helm | https://helm.sh/docs/ | Packaging |

---

## Deliberately Omitted

- **Service mesh (Istio, Linkerd).** Real value at scale, substantial
  complexity, and not what these interviews probe. Know what problem it solves.
- **Multi-cluster and federation.** Out of scope.
- **Cloud-specific managed services (EKS, GKE, SageMaker).** The concepts
  transfer; the specifics are vendor documentation.
- **GPU cluster scheduling in depth.** Week 51's system design covers the
  concepts; running a real GPU cluster is beyond the compute budget.
