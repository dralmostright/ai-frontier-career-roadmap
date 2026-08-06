# Month 16 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 16.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 61 | 7.5 | Theory — did you identify a real weakness in each paper? |
| 62 | 8.0 | Evaluation — three seeds and a baseline, or one run? |
| 63 | 8.0 | Evaluation — is the ablation actually controlled? |
| 64 | 8.5 | Write-up — is the failures section written honestly? |

---

## Month 16 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Summarize a paper in 90 seconds: claim, method, evidence, weakness
- [ ] Identify the weakest claim in a paper, cold
- [ ] Scope a reproduction to a stated compute budget
- [ ] Explain a discrepancy between your numbers and a paper's
- [ ] Design the ablation that would falsify a given claim

**4 of 5 required.**

### Implementation gate

- [ ] Two reproductions completed with 3+ seeds each
- [ ] A baseline present and fairly tuned for both
- [ ] At least one controlled ablation
- [ ] `make reproduce` regenerates the headline numbers
- [ ] Report published with discrepancy and failure sections

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 8 |
| Technical execution | 8 |
| Evaluation rigor | 9 |
| Code quality | 8 |
| Documentation | 10 |
| Reproducibility | 10 |
| Error analysis | 9 |
| Portfolio readiness | 8 |

Overall target: 8.5+, with Documentation and Reproducibility at 10.

---

## Interview Readiness

| Dimension | Expected at Month 16 |
| --- | --- |
| Python coding under time | 6 |
| ML theory depth | 6 |
| DL / transformer depth | 6 |
| LLM systems design | 6 |
| Infrastructure design | 8 |
| Project storytelling | 6 |
| Portfolio strength | 9 |
| **Total (of 35)** | **~47** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Single-seed results reported
- No baseline
- No discrepancy analysis
- Month average below 7.5

---

## Advancement Decision

```text
Month 16 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-16.md`.
