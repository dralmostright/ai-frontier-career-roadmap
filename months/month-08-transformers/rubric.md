# Month 08 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 8.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 29 | 8.0 | Theory — can you derive √d, or only state it? |
| 30 | 7.5 | Implementation — is MHA gradient-checked? |
| 31 | 7.0 | Theory — can you argue encoder vs decoder concretely? |
| 32 | 8.0 | Evaluation — did you run all seven ablations with a controlled seed? |

---

## Month 8 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Derive scaled dot-product attention cold, including √d
- [ ] Implement multi-head attention from memory
- [ ] Explain pre-norm versus post-norm with the residual-stream argument
- [ ] Explain KV caching and compute its memory for a 7B model at 8k context
- [ ] State what breaks without each transformer component, from your own data

**5 of 5 — this month's gates are not negotiable required.**

### Implementation gate

- [ ] `make test` green through week 32
- [ ] `test_changing_a_future_token_cannot_change_the_present` passes
- [ ] Initial loss equals ln(vocab_size)
- [ ] KV cache produces identical output with a measured speedup
- [ ] All seven ablations run and tabulated
- [ ] Mini-GPT published with the ablation table above the fold

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 7 |
| Technical execution | 9 |
| Evaluation rigor | 9 |
| Code quality | 8 |
| Documentation | 9 |
| Reproducibility | 9 |
| Error analysis | 7 |
| Portfolio readiness | 9 |

Overall target: 8.5+. This is a flagship — aim for 9.

---

## Interview Readiness

| Dimension | Expected at Month 8 |
| --- | --- |
| Python coding under time | 4 |
| ML theory depth | 4 |
| DL / transformer depth | 5 |
| LLM systems design | 3 |
| Infrastructure design | 4 |
| Project storytelling | 4 |
| Portfolio strength | 5 |
| **Total (of 35)** | **~29** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- **Any** knowledge gate failed — this month's material is non-negotiable
- Cannot derive attention on a whiteboard in under six minutes
- Ablation study incomplete
- Gate G3 not met
- Month average below 7.5

---

## Advancement Decision

```text
Month 8 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 5)
Implementation gates:  __ /6   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-08.md`.
