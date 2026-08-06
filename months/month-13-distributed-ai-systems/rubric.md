# Month 13 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 13.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 49 | 8.0 | Theory — can you derive the memory arithmetic, or only quote it? |
| 50 | 7.5 | Write-up — is the reference document something you would hand a colleague? |
| 51 | 7.5 | Implementation — does it actually resume after being killed? |
| 52 | 8.0 | Evaluation — did you measure an optimization, or just profile? |

---

## Month 13 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Compute training memory for a 7B model from first principles, then with LoRA and ZeRO-3
- [ ] Explain ZeRO stages 1, 2, 3 with memory and communication cost
- [ ] Explain when tensor parallelism beats pipeline parallelism
- [ ] Diagnose a p99/p50 latency gap systematically
- [ ] Explain why decode is memory-bandwidth-bound

**5 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 52
- [ ] Memory calculator validated within 15% of measurement
- [ ] Distributed eval results match serial exactly
- [ ] Job resumes correctly after being killed
- [ ] Scaling curve produced with the plateau explained
- [ ] Capstone published with the cost report

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 8 |
| Technical execution | 8 |
| Evaluation rigor | 8 |
| Code quality | 8 |
| Documentation | 8 |
| Reproducibility | 8 |
| Error analysis | 8 |
| Portfolio readiness | 8 |

Overall target: 8.0+.

---

## Interview Readiness

| Dimension | Expected at Month 13 |
| --- | --- |
| Python coding under time | 5 |
| ML theory depth | 5 |
| DL / transformer depth | 5 |
| LLM systems design | 5 |
| Infrastructure design | 6 |
| Project storytelling | 5 |
| Portfolio strength | 7 |
| **Total (of 35)** | **~38** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Cannot derive the memory arithmetic unaided
- No measured optimization in Week 52
- Any knowledge gate failed
- Month average below 7.5

---

## Advancement Decision

```text
Month 13 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 5)
Implementation gates:  __ /6   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-13.md`.
