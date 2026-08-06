# Month 06 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 6.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 21 | 7.0 | Implementation — did you write convolution by hand, or only call it? |
| 22 | 7.5 | Theory — can you give the gradient argument for residuals? |
| 23 | 7.0 | Implementation — did you catch the BatchNorm freezing trap? |
| 24 | 7.5 | Evaluation — are you reporting percentiles or means? |

---

## Month 6 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Compute the receptive field of a given CNN stack
- [ ] Explain residual connections via gradient flow
- [ ] Give the four-cell transfer learning decision table
- [ ] Say when a ViT beats a CNN, with the data-scale reasoning
- [ ] Explain the batching latency/throughput tradeoff with your numbers

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 24
- [ ] CIFAR-10 above 80%
- [ ] The depth comparison plot shows plain networks degrading
- [ ] Service containerized with measured p99
- [ ] Capstone published with the latency curve

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 7 |
| Technical execution | 8 |
| Evaluation rigor | 8 |
| Code quality | 8 |
| Documentation | 8 |
| Reproducibility | 8 |
| Error analysis | 7 |
| Portfolio readiness | 7 |

Overall target: 7.5+, with the latency measurement genuinely rigorous.

---

## Interview Readiness

| Dimension | Expected at Month 6 |
| --- | --- |
| Python coding under time | 4 |
| ML theory depth | 3 |
| DL / transformer depth | 4 |
| LLM systems design | 2 |
| Infrastructure design | 4 |
| Project storytelling | 3 |
| Portfolio strength | 4 |
| **Total (of 35)** | **~24** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Fewer than 4 of 5 knowledge gates
- Gate G2 not met: cannot train and serve a model, or cannot debug a non-converging run out loud
- Month average below 7.0
- No deployed artifact

---

## Advancement Decision

```text
Month 6 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-06.md`.
