# Month 03 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 3.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 9 | 7.0 | Theory — can you explain boosting as gradient descent in function space? |
| 10 | 7.5 | Implementation — did you build the naive target encoder first and *see* the leak? |
| 11 | 7.5 | Write-up — are you actually reporting CIs, or still reporting point estimates? |
| 12 | 7.5 | Interview explanation — the slice analysis answer must be fluent |

---

## Month 3 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Identify the leakage in five described scenarios, 60 seconds each
- [ ] Explain out-of-fold target encoding and why the naive version fails
- [ ] Explain calibration and give a case where a miscalibrated model is unacceptable
- [ ] Explain why a 94%-accurate model can be worthless, via slice analysis
- [ ] Explain bagging vs boosting in terms of bias and variance

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 12
- [ ] `test_fit_transform_must_differ_from_fit_then_transform` passes
- [ ] Bootstrap CIs computed and reported on the capstone's metrics
- [ ] Calibration improves ECE on a tree ensemble
- [ ] Kaggle capstone published with a named-bucket error analysis

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 8 |
| Technical execution | 8 |
| Evaluation rigor | 9 |
| Code quality | 8 |
| Documentation | 8 |
| Reproducibility | 8 |
| Error analysis | 9 |
| Portfolio readiness | 7 |

Overall target: 8.0+, with Evaluation Rigor and Error Analysis at 9.

---

## Interview Readiness

| Dimension | Expected at Month 3 |
| --- | --- |
| Python coding under time | 3 |
| ML theory depth | 3 |
| DL / transformer depth | 1 |
| LLM systems design | 1 |
| Infrastructure design | 4 |
| Project storytelling | 3 |
| Portfolio strength | 2 |
| **Total (of 35)** | **~17** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Fewer than 4 of 5 knowledge gates passed
- Any implementation gate failed
- Month average below 7.0
- Gate G1 not met: cannot implement logistic regression and a decision tree from scratch, unaided, in under 45 minutes
- No public Kaggle artifact

---

## Advancement Decision

```text
Month 3 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-03.md`.
