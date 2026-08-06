# Month 07 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 7.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 25 | 7.0 | Implementation — did you write the optimized BPE trainer? |
| 26 | 7.0 | Theory — can you name embedding failure modes beyond 'they're approximate'? |
| 27 | 7.0 | Theory — can you derive the negative sampling objective? |
| 28 | 8.0 | Evaluation — did you actually hand-label 100 queries? |

---

## Month 7 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Explain why tokenization breaks arithmetic and reversed strings
- [ ] Explain the negation failure in embedding similarity
- [ ] Derive the negative sampling objective
- [ ] Explain HNSW vs IVFFlat with parameters and failure modes
- [ ] Explain why hybrid retrieval beats either method alone

**4 of 5 required.**

### Implementation gate

- [ ] `make test` green through week 28
- [ ] BPE tokenizer round-trips unicode exactly
- [ ] Semantic search running on pgvector with an index
- [ ] 100+ hand-labeled queries with relevance judgments
- [ ] Capstone published with the metrics table and query plan

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
| Portfolio readiness | 8 |

Overall target: 8.0+, with Evaluation Rigor and Documentation at 9.

---

## Interview Readiness

| Dimension | Expected at Month 7 |
| --- | --- |
| Python coding under time | 4 |
| ML theory depth | 4 |
| DL / transformer depth | 4 |
| LLM systems design | 3 |
| Infrastructure design | 4 |
| Project storytelling | 3 |
| Portfolio strength | 5 |
| **Total (of 35)** | **~27** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- Fewer than 4 of 5 knowledge gates
- No hand-labeled relevance set
- Month average below 7.0
- Capstone not built on pgvector — this discards the differentiator

---

## Advancement Decision

```text
Month 7 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 4)
Implementation gates:  __ /5   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-07.md`.
