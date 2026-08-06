# Month 14 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Google SRE Book, 'Monitoring Distributed Systems'** — https://sre.google/sre-book/monitoring-distributed-systems/
You may already know this. Reread it thinking specifically about a system whose
failure mode is confident wrongness.

**'Hidden Technical Debt in Machine Learning Systems'** — https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
Short, and it named the problem this month solves.

**'Beyond Accuracy: Behavioral Testing of NLP Models'** (Week 55) — https://arxiv.org/abs/2005.04118
The invariance/directional/minimum-functionality taxonomy.

**Chip Huyen, 'Designing Machine Learning Systems'** — chapters 6-8. Worth buying.

---

## Week 53 — Experiment Tracking

- **Primary:** MLflow tracking documentation — https://mlflow.org/docs/latest/tracking.html
- **Primary:** 'Hidden Technical Debt in Machine Learning Systems' — https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html — the paper that named the problem. Short and worth reading.
- DVC documentation — https://dvc.org/doc — for data versioning
- Chip Huyen, 'Designing Machine Learning Systems' — chapter 6
## Week 54 — Model Registry and Versioning

- **Primary:** MLflow Model Registry — https://mlflow.org/docs/latest/model-registry.html
- **Primary:** Google SRE Book, release engineering — https://sre.google/sre-book/release-engineering/
- Chip Huyen, 'Designing Machine Learning Systems' — chapter 7, deployment patterns
- 'Continuous Delivery for Machine Learning' (Sato, Wider, Windheuser) — https://martinfowler.com/articles/cd4ml.html
## Week 55 — CI/CD for ML

- **Primary:** 'Beyond Accuracy: Behavioral Testing of NLP Models with CheckList' — https://arxiv.org/abs/2005.04118 — the behavioral testing taxonomy
- **Primary:** GitHub Actions documentation — https://docs.github.com/en/actions
- 'The ML Test Score' (Breck et al.) — https://research.google/pubs/pub46555/ — a rubric for ML system readiness; score your own project against it
- Great Expectations — https://docs.greatexpectations.io/ — data validation
## Week 56 — Monitoring and Drift

- **Primary:** Google SRE Book, 'Monitoring Distributed Systems' — https://sre.google/sre-book/monitoring-distributed-systems/ — the four golden signals, applied here
- **Primary:** Google SRE Workbook, 'Alerting on SLOs' — https://sre.google/workbook/alerting-on-slos/
- Evidently AI documentation — https://docs.evidentlyai.com/ — practical drift detection
- Chip Huyen, 'Designing Machine Learning Systems' — chapter 8, data distribution shifts
- 'Monitoring and Explainability of Models in Production' — https://arxiv.org/abs/2007.06299

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
| Evidently | https://docs.evidentlyai.com/ | Week 56 drift |
| DVC | https://dvc.org/doc | Data versioning |
| Grafana | https://grafana.com/docs/ | Week 56 |

---

## Deliberately Omitted

- **Feature stores.** Relevant for tabular ML at scale, less so for LLM systems.
  Know what problem they solve.
- **Kubeflow / Airflow / Dagster.** Orchestration tools. GitHub Actions is
  sufficient here and the concepts transfer.
- **A/B testing infrastructure.** Week 54's shadow deployment covers the idea.
  Full experimentation platforms are their own discipline.
- **Model compression pipelines.** Week 52 covered quantization.
