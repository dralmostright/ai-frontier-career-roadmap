# Month 05 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 5.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 17 | 7.0 | Theory — can you explain `.backward()` mechanically? |
| 18 | 7.0 | Implementation — did you actually measure the loader bottleneck? |
| 19 | 7.5 | Implementation — does resume produce a continuous loss curve? |
| 20 | 8.0 | Testing — does the reproducibility test actually pass? |

---

## Month 5 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Explain mechanically what `.backward()` does
- [ ] Diagnose a 30%-utilization GPU in priority order
- [ ] Name every source of nondeterminism in a training run
- [ ] Compute training memory for a 7B model with Adam
- [ ] Explain why gradient accumulation divides the loss

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 20
- [ ] `test_two_short_runs_produce_identical_losses` passes
- [ ] Gradient accumulation matches a large batch exactly
- [ ] Resume from checkpoint gives a continuous loss curve
- [ ] Capstone published with CI green

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 7 |
| Technical execution | 8 |
| Evaluation rigor | 7 |
| Code quality | 9 |
| Documentation | 8 |
| Reproducibility | 10 |
| Error analysis | 6 |
| Portfolio readiness | 8 |

Overall target: 8.0+, with Reproducibility at 10 and Code Quality at 9.

---

## Interview Readiness

| Dimension | Expected at Month 5 |
| --- | --- |
| Python coding under time | 3 |
| ML theory depth | 3 |
| DL / transformer depth | 3 |
| LLM systems design | 2 |
| Infrastructure design | 4 |
| Project storytelling | 3 |
| Portfolio strength | 4 |
| **Total (of 35)** | **~22** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Reproducibility test does not pass
- Fewer than 4 of 5 knowledge gates
- Month average below 7.0
- No Q2 mock interview recorded

---

## Advancement Decision

```text
Month 5 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-05.md`.
