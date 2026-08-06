# Month 02 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 2.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 5 | 7.0 | Theory — can you *show* bias-variance, or only define it? |
| 6 | 7.5 | Interview explanation — the imbalance question must be fluent |
| 7 | 7.0 | Implementation — did you do the optimized split search, or the naive one? |
| 8 | 7.0 | Theory — do you know *why* feature subsampling matters? |

---

## Month 2 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Derive the logistic regression gradient and explain the p-y cancellation
- [ ] Explain when PR-AUC beats ROC-AUC, with a concrete numeric example
- [ ] Explain why trees overfit, and name three distinct remedies
- [ ] Explain why bagging reduces variance and boosting reduces bias
- [ ] Derive the out-of-bag fraction (1 - 1/n)^n -> 1/e

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 8
- [ ] From-scratch models match sklearn within 2% on the same data
- [ ] The optimized split search is measurably faster than naive
- [ ] OOB score approximates test accuracy
- [ ] Titanic capstone published with a README and error analysis

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 6 |
| Technical execution | 8 |
| Evaluation rigor | 8 |
| Code quality | 8 |
| Documentation | 7 |
| Reproducibility | 9 |
| Error analysis | 8 |
| Portfolio readiness | 5 |

Overall target: 7.5+, with Error Analysis and Evaluation Rigor at 8 or above.

---

## Interview Readiness

| Dimension | Expected at Month 2 |
| --- | --- |
| Python coding under time | 3 |
| ML theory depth | 3 |
| DL / transformer depth | 1 |
| LLM systems design | 1 |
| Infrastructure design | 4 |
| Project storytelling | 2 |
| Portfolio strength | 2 |
| **Total (of 35)** | **~16** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Fewer than 4 of 5 knowledge gates passed
- Any implementation gate failed
- Month average below 7.0
- Cannot implement logistic regression unaided in under 30 minutes
- Total hours below 50 across the four weeks

---

## Advancement Decision

```text
Month 2 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-02.md`.
