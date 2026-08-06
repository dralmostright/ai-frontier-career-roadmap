# Month 09 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 9.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 33 | 7.0 | Theory — can you give the motivation for each modern component? |
| 34 | 7.5 | Evaluation — did you actually run the quality-vs-scale ablation? |
| 35 | 7.5 | Implementation — did you log everything from step zero? |
| 36 | 8.0 | Evaluation — did you validate the judge against human labels? |

---

## Month 9 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Explain what changed between GPT-2 and Llama, and why each change
- [ ] Explain why grouped-query attention won, connecting to KV cache size
- [ ] Show from your own ablation that data quality beats parameter count
- [ ] Explain temperature, top-k, and top-p precisely
- [ ] Name the LLM-as-judge biases and how you control for each

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 36
- [ ] A language model trained with logged curves
- [ ] The data quality ablation run and tabulated
- [ ] Judge validated against 50 human labels with kappa reported
- [ ] Training report published

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 7 |
| Technical execution | 8 |
| Evaluation rigor | 8 |
| Code quality | 8 |
| Documentation | 9 |
| Reproducibility | 9 |
| Error analysis | 8 |
| Portfolio readiness | 8 |

Overall target: 8.0+, with Documentation and Reproducibility at 9.

---

## Interview Readiness

| Dimension | Expected at Month 9 |
| --- | --- |
| Python coding under time | 4 |
| ML theory depth | 4 |
| DL / transformer depth | 5 |
| LLM systems design | 4 |
| Infrastructure design | 4 |
| Project storytelling | 4 |
| Portfolio strength | 5 |
| **Total (of 35)** | **~30** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Fewer than 4 of 5 knowledge gates
- No completed training run
- Judge used without validation
- Month average below 7.0
- No Q3 mock interview recorded

---

## Advancement Decision

```text
Month 9 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-09.md`.
