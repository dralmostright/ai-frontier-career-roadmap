# Month 15 Rubric

Standards from `SCORECARD.md` apply. This file adds the gates specific to
Month 15.

---

## Weekly Targets

| Week | Target average | The axis most likely to be inflated |
| --- | --- | --- |
| 57 | 7.5 | Implementation — did you document the size reduction step by step? |
| 58 | 8.0 | Implementation — did you deliberately misconfigure a probe and observe the loop? |
| 59 | 8.0 | System design — can you answer the 100M-document question fluently? |
| 60 | 9.0 | Documentation — **did you write the postmortem?** |

---

## Month 15 Gates

Assessed at the end of the final week, without notes.

### Knowledge gate

- [ ] Get an 8GB image under 1GB, with the sequence and savings
- [ ] Explain liveness vs readiness vs startup for a slow-loading model server
- [ ] Set and justify requests and limits for an inference pod
- [ ] Design batch inference over 100M documents with failure recovery
- [ ] Write a blameless postmortem for an LLM outage

**5 of 5 required.**

### Implementation gate

- [ ] Full stack deploys from manifests on a clean cluster
- [ ] Zero dropped requests during a rolling update, verified under load
- [ ] Rollback measured under 5 minutes from the runbook
- [ ] Four runbooks written and tested by someone else
- [ ] **Postmortem written with action items implemented**
- [ ] Capstone published, scored 9.0+

**All required.** These are not judgment calls.

---

## Capstone Score

| Dimension | Target |
| --- | --- |
| Problem framing | 9 |
| Technical execution | 9 |
| Evaluation rigor | 8 |
| Code quality | 8 |
| Documentation | 10 |
| Reproducibility | 9 |
| Error analysis | 10 |
| Portfolio readiness | 10 |

Overall target: 9.0+. Flagship. The postmortem is what earns it.

---

## Interview Readiness

| Dimension | Expected at Month 15 |
| --- | --- |
| Python coding under time | 5 |
| ML theory depth | 5 |
| DL / transformer depth | 5 |
| LLM systems design | 6 |
| Infrastructure design | 8 |
| Project storytelling | 6 |
| Portfolio strength | 9 |
| **Total (of 35)** | **~44** |

---

## Remediation Triggers

Take a catch-up week before the next month if any hold:

- **No postmortem — the month's defining artifact**
- Rollback untested
- Any knowledge gate failed
- Gate G5 not met
- Month average below 8.0

---

## Advancement Decision

```text
Month 15 average:       __ /10
Capstone score:        __ /10
Knowledge gates:       __ /5   (need 5)
Implementation gates:  __ /6   (need all)
Interview readiness:   __ /35

Decision:  [ ] Advance   [ ] Remediation week first
```

Record it in `coach/reviews/month-15.md`.
