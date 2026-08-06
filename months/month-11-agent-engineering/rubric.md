# Month 11 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 11.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 41 | 8.0 | Technical execution — are the tools genuinely narrow, or is there a general SQL escape hatch? |
| 42 | 7.5 | Evaluation — did you measure reflection, or assume it helps? |
| 43 | 8.5 | Technical execution — is your domain judgment encoded in the tools? |
| 44 | 9.0 | Evaluation — 30+ scenarios, 5 runs each, variance reported? |

---

## Month 11 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Design a tool interface an LLM cannot misuse, with six justified principles
- [ ] Explain when reflection helps, from your own measurement
- [ ] Explain a bad query plan to a non-DBA in two minutes
- [ ] State your agent's accuracy, evidence recall, and unsafe-recommendation rate
- [ ] Explain the safety architecture without using the word 'prompt'
- [ ] Deliver the database reliability assistant system design in 45 minutes

**6 of 6 — this is the flagship month required.**

### Implementation gate

- [ ] `make test` green through week 44
- [ ] 30+ benchmark scenarios, reproducible from seed
- [ ] Evaluation run at 5x per scenario with variance reported
- [ ] Zero unsafe recommendations across the full benchmark
- [ ] Every claim in every diagnosis cites a valid evidence ID
- [ ] Audit log can reconstruct any run
- [ ] Capstone published, scored 9.0+

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 9 |
| Technical execution | 9 |
| Evaluation rigor | 10 |
| Code quality | 8 |
| Documentation | 10 |
| Reproducibility | 9 |
| Error analysis | 10 |
| Portfolio readiness | 10 |

Overall target: 9.0+. This is the flagship. Anything below 9 gets another week.

---

## Interview Readiness

| Dimension | Expected at Month 11 |
| --- | --- |
| Python coding under time | 5 |
| ML theory depth | 4 |
| DL / transformer depth | 5 |
| LLM systems design | 5 |
| Infrastructure design | 5 |
| Project storytelling | 5 |
| Portfolio strength | 7 |
| **Total (of 35)** | **~36** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- **Capstone below 9.0 — take another week. This project matters more than the schedule.**
- Any unsafe recommendation in the benchmark run
- Fewer than 30 scenarios
- Single-run evaluation
- Any knowledge gate failed

---

## Advancement Decision

```text
Month 11 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /6   (need 6)
Implementation gates:  __ /7   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-11.md`.
