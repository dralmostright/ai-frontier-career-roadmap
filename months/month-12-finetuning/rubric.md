# Month 12 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 12.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 45 | 7.5 | Theory — can you argue *against* fine-tuning convincingly? |
| 46 | 7.5 | Implementation — did you implement LoRA, or import PEFT? |
| 47 | 8.0 | Write-up — did you review every example by hand? |
| 48 | 8.0 | Evaluation — did you run the RAG comparison, and report it honestly? |

---

## Month 12 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] State three criteria for fine-tuning over RAG, with examples
- [ ] Derive LoRA's parameter count for a given rank and layer
- [ ] Explain why LoRA's B matrix is initialized to zero
- [ ] Explain DPO versus RLHF in three sentences
- [ ] Report your fine-tune's gain and its regression, and defend the tradeoff

**5 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 48
- [ ] LoRA implemented from scratch and verified against PEFT
- [ ] Rank ablation run and plotted
- [ ] Four-way comparison completed
- [ ] Dataset card and model card both published
- [ ] Capstone published with the honest verdict line

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 8 |
| Technical execution | 8 |
| Evaluation rigor | 9 |
| Code quality | 8 |
| Documentation | 9 |
| Reproducibility | 8 |
| Error analysis | 8 |
| Portfolio readiness | 9 |

Overall target: 8.5+. Flagship. The four-way comparison is what earns it.

---

## Interview Readiness

| Dimension | Expected at Month 12 |
| --- | --- |
| Python coding under time | 5 |
| ML theory depth | 5 |
| DL / transformer depth | 5 |
| LLM systems design | 5 |
| Infrastructure design | 5 |
| Project storytelling | 5 |
| Portfolio strength | 7 |
| **Total (of 35)** | **~37** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- No RAG comparison — the month's most valuable finding
- No general-capability regression measurement
- Any knowledge gate failed
- Gate G4 not met
- Month average below 7.5

---

## Advancement Decision

```text
Month 12 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 5)
Implementation gates:  __ /6   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-12.md`.
