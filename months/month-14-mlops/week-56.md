# Week 56: Monitoring and Drift

## Outcome

By Sunday you have production monitoring designed for a system that fails silently: quality metrics, drift detection, SLOs with error budgets, and an alert set where every page has a runbook.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The defining problem: **ML systems fail silently.** A degraded model returns 200
for every request.

The metric that matters most is not accuracy — you usually cannot measure it in
real time, because labels arrive late or never. It is the prediction distribution,
which is available immediately and is a leading indicator. When your model's
output distribution shifts three standard deviations from its training baseline,
something is wrong, and you know that before anyone complains.

The drift material has one trap worth internalizing: at scale, every statistical
test is significant. At a million requests a day the KS test flags drift
constantly and none of it matters. Alert on effect size, not p-value. Teams make
this mistake repeatedly.

SLOs and error budgets are yours. The ML-specific addition is a *quality* SLO
alongside availability and latency, and treating a quality-budget burn as a real
incident with real escalation.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7.5 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Silent failure**
   1. Why conventional monitoring misses model degradation
   2. Leading versus lagging indicators
   3. Delayed ground truth, and designing for it
2. **The metric set**
   1. System: rate, errors, latency, saturation
   2. Model: prediction distribution, confidence, refusal rate, fallback rate
   3. Cost: tokens and dollars per request
   4. Quality: accuracy against delayed labels
3. **Drift**
   1. Data drift: P(X) changes. Cheap to detect, sometimes matters.
   2. Concept drift: P(y|X) changes. Always matters, needs labels.
   3. Label drift: P(y) changes.
   4. PSI, KL, KS, and embedding drift
   5. **Effect size, not p-value**, as the alert condition
4. **SLOs and error budgets**
   1. Availability, latency, and **quality** SLOs
   2. Error budgets and burn rate
   3. Why a quality burn is a real incident
5. **Alerting**
   1. Symptoms over causes
   2. Page versus ticket
   3. Every page has a runbook
   4. Alerting on the absence of data
   5. `for:` durations, so transients do not fire

## Required Free Resources

- **Primary:** Google SRE Book, 'Monitoring Distributed Systems' — https://sre.google/sre-book/monitoring-distributed-systems/ — the four golden signals, applied here
- **Primary:** Google SRE Workbook, 'Alerting on SLOs' — https://sre.google/workbook/alerting-on-slos/
- Evidently AI documentation — https://docs.evidentlyai.com/ — practical drift detection
- Chip Huyen, 'Designing Machine Learning Systems' — chapter 8, data distribution shifts
- 'Monitoring and Explainability of Models in Production' — https://arxiv.org/abs/2007.06299

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=56
```

1. ****Design the metric set before reading examples**** (1.5h) — Write down what you would monitor for an LLM feature. Then compare against the module's list.
2. **`ModelMonitor` with real-time and batch tiers** (1.5h) — Prediction distribution and confidence in real time; drift and accuracy in batch.
3. **`population_stability_index`** (1h) — With the conventional thresholds, and a note that they are conventions.
4. **`kolmogorov_smirnov_test` and the significance trap** (1h) — Demonstrate that at 500k samples a negligible shift is 'significant'.
5. **`embedding_drift`** (1h) — For your RAG system. Detects the questions changing.
6. **`DriftDetector` with the baseline stored alongside the model version** (1.5h) — They must move together or a rollback produces nonsense alerts.
7. **`define_slos`** (1h) — Availability, latency, quality, freshness. With error budgets.
8. **`alert_rules`** (1.5h) — Every page gets a runbook link. Include an absence-of-data alert.
9. **Grafana dashboards** (1.5h) — One for system health, one for model quality. Make them readable at 3am.

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
s
r
c
/
m
o
n
i
t
o
r
i
n
g
.
p
y


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
s
r
c
/
d
r
i
f
t
.
p
y


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
g
r
a
f
a
n
a
/
```

## Tests To Write

`tests/test_mlops.py` week-56 blocks. `test_large_samples_make_p_values_useless` is the one that encodes the trap.

## Portfolio Artifact

The monitoring stack, the dashboards, and the alert set with runbook links. This feeds the Month 14 capstone.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (35 min).** **Recorded.** *Design alerting for a production LLM feature.* Metric set, what pages versus tickets, SLOs, error budgets, and the runbook requirement. Then: *How do you detect that a model has silently degraded?* This is your strongest topic — make the answer show it.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Simulate a silent degradation — swap in a deliberately worse model, or corrupt part of the retrieval index — and verify that your leading indicators fire before the delayed accuracy metric would have. Measure the detection lag. Being able to say 'the prediction-distribution alert fires within eight minutes; the accuracy signal would have taken three days' is a compelling, specific demonstration of why the metric set is designed the way it is.
