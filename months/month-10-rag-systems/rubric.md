# Month 10 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 10.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 37 | 7.5 | Implementation — did you measure the parameter sweep, or accept defaults? |
| 38 | 7.5 | Evaluation — is the chunking choice measured or assumed? |
| 39 | 8.5 | Evaluation — did you label 200 questions *and* validate the judge? |
| 40 | 8.0 | Technical execution — does permission filtering actually pre-filter? |

---

## Month 10 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Explain HNSW vs IVFFlat including the build-order gotcha
- [ ] Diagnose 'right document retrieved, wrong answer' by walking the pipeline
- [ ] Design a RAG evaluation harness from scratch, in six minutes
- [ ] Explain why post-filtering by permission breaks top-k
- [ ] State your faithfulness score and how the judge was validated

**5 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 40
- [ ] 200-question labeled eval set with 10% unanswerable
- [ ] Faithfulness judge validated with kappa reported
- [ ] Permission isolation proven by test
- [ ] Eval harness in CI, gating on regression
- [ ] Capstone published with the metrics table above the fold

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 8 |
| Technical execution | 8 |
| Evaluation rigor | 10 |
| Code quality | 8 |
| Documentation | 9 |
| Reproducibility | 8 |
| Error analysis | 9 |
| Portfolio readiness | 9 |

Overall target: 8.5+. This is a flagship. Evaluation Rigor at 10.

---

## Interview Readiness

| Dimension | Expected at Month 10 |
| --- | --- |
| Python coding under time | 4 |
| ML theory depth | 4 |
| DL / transformer depth | 5 |
| LLM systems design | 5 |
| Infrastructure design | 5 |
| Project storytelling | 4 |
| Portfolio strength | 6 |
| **Total (of 35)** | **~33** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- No 200-question eval set — the month's central deliverable
- Judge used without validation
- Any knowledge gate failed
- Month average below 7.5

---

## Advancement Decision

```text
Month 10 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 5)
Implementation gates:  __ /6   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-10.md`.
