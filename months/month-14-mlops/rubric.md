# Month 14 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 14.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 53 | 7.5 | Write-up — is the 'why' note actually filled in on every run? |
| 54 | 8.0 | Implementation — have you *timed* the rollback with someone else executing it? |
| 55 | 8.5 | Evaluation — did the gate catch a real regression, with a log? |
| 56 | 8.5 | System design — is the metric set yours, or copied? |

---

## Month 14 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] State what belongs in an experiment record, with the reasoning per field
- [ ] Walk through a 2am rollback with a measured time
- [ ] Name the ML-specific tests that gate a deployment
- [ ] Design LLM alerting, distinguishing pages from tickets
- [ ] Explain silent failure and the leading indicators you monitor for it

**5 of 5 — this is your strongest month; the bar is higher required.**

### Implementation gate

- [ ] `make test` green through week 56
- [ ] Rollback measured and executed by someone else from the runbook
- [ ] Quality gate caught a real regression, with the CI log saved
- [ ] Drift detection caught a simulated shift, with the lag measured
- [ ] Every alert has a runbook link
- [ ] Capstone published with the CI log above the fold

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 9 |
| Technical execution | 8 |
| Evaluation rigor | 9 |
| Code quality | 8 |
| Documentation | 9 |
| Reproducibility | 9 |
| Error analysis | 8 |
| Portfolio readiness | 9 |

Overall target: 8.5+. This should be one of your best-scoring capstones.

---

## Interview Readiness

| Dimension | Expected at Month 14 |
| --- | --- |
| Python coding under time | 5 |
| ML theory depth | 5 |
| DL / transformer depth | 5 |
| LLM systems design | 5 |
| Infrastructure design | 7 |
| Project storytelling | 5 |
| Portfolio strength | 8 |
| **Total (of 35)** | **~40** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- No caught regression — the month's central artifact
- Rollback untested or untimed
- Any knowledge gate failed
- Month average below 8.0 — **this month should be your strongest**

---

## Advancement Decision

```text
Month 14 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 5)
Implementation gates:  __ /6   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-14.md`.
