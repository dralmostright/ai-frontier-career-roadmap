# Month 04 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 4.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 13 | 7.0 | Theory — do you know *why* initialization matters, or just the formulas? |
| 14 | 7.5 | Implementation — is every layer gradient-checked, or only some? |
| 15 | 7.0 | Theory — can you explain the optimizer chain as a sequence of fixes? |
| 16 | 7.5 | Interview explanation — the NaN-debugging answer must be ordered |

---

## Month 4 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Derive backpropagation for a two-layer MLP on a whiteboard
- [ ] Explain vanishing gradients with the sigmoid 0.25 calculation
- [ ] Explain why Adam needs bias correction
- [ ] Explain AdamW's decoupled decay
- [ ] Debug a NaN loss out loud in priority order

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 16
- [ ] `test_end_to_end_gradient_check` passes at < 1e-6
- [ ] BatchNorm backward gradient-checked
- [ ] MNIST trained to >95% with the NumPy framework
- [ ] Framework published with the derivations document

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 6 |
| Technical execution | 9 |
| Evaluation rigor | 8 |
| Code quality | 8 |
| Documentation | 9 |
| Reproducibility | 9 |
| Error analysis | 6 |
| Portfolio readiness | 8 |

Overall target: 8.0+, with Technical Execution and Documentation at 9.

---

## Interview Readiness

| Dimension | Expected at Month 4 |
| --- | --- |
| Python coding under time | 3 |
| ML theory depth | 3 |
| DL / transformer depth | 3 |
| LLM systems design | 1 |
| Infrastructure design | 4 |
| Project storytelling | 3 |
| Portfolio strength | 3 |
| **Total (of 35)** | **~20** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Fewer than 4 of 5 knowledge gates passed
- Any implementation gate failed
- Cannot derive backprop for a two-layer MLP unaided
- Month average below 7.0

---

## Advancement Decision

```text
Month 4 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-04.md`.
