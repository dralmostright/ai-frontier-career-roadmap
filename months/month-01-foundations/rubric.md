# Month 01 Rubric

How this month is graded. Score honestly — the standards in `SCORECARD.md` apply,
and Month 1 is where inflated scores cost the most, because everything after it
assumes this material.

---

## Weekly Scores

Score all four weeks on the six standard axes. Month 1 targets:

| Week | Target average | The axis most likely to be inflated |
| ---- | -------------- | ----------------------------------- |
| 1 | 7.0 | Theory — "I watched 3Blue1Brown" is not understanding |
| 2 | 7.0 | Interview explanation — can you actually explain what PCA loses? |
| 3 | 7.5 | Theory — can you derive it, or only implement it? |
| 4 | 7.0 | Write-up — the capstone README is due this week |

---

## Month 1 Specific Gates

Pass/fail, assessed without notes at the end of Week 4.

### Derivation gate

On a whiteboard, cold, in under 10 minutes total:

- [ ] Gradient of MSE with respect to the weights of a linear model
- [ ] Derivative of the sigmoid, and why it caps at 0.25
- [ ] Gradient of sigmoid composed with binary cross entropy → `p - y`
- [ ] Gradient of softmax composed with cross entropy → `p - onehot(y)`

**Three of four required.** Below that, take a remediation week before Month 2.
Week 5 begins with "derive gradient descent for linear regression" and Week 14
requires all of these.

### Explanation gate

Spoken, no notes, 3 minutes each:

- [ ] Why do embeddings live in vector spaces? What does cosine similarity
      discard, and when does that matter?
- [ ] What does PCA destroy? Name three distinct things.
- [ ] Why is cross entropy the loss for classification? Three different answers.
- [ ] Why does reverse-mode autodiff win over forward mode for ML?

**Three of four required.** Record at least one and score it as a stranger would.

### Implementation gate

- [ ] `make test` green at week 4 — all of Weeks 1-4
- [ ] `test_gradient_descent_fits_a_line` passes (your engine trains a model)
- [ ] `test_pca_two_ways_agree` passes and you can explain why
- [ ] `test_the_identity` passes (H(p,q) = H(p) + D(p‖q))
- [ ] Capstone package installs from a clean clone

**All five required.** These are not judgment calls.

---

## Capstone Score

Full rubric in `coach/capstone_review_rubric.md`. Month 1 targets and their
rationale:

| Dimension | Target | Why this target |
| --------- | ------ | --------------- |
| Problem framing | 6 | Conditioning work. Do not oversell it. |
| Technical execution | 8 | Correctness is the whole point here. |
| Evaluation rigor | 7 | Reference agreement + benchmarks. |
| Code quality | 8 | Set the standard while the code is easy. |
| Documentation | 8 | The theory sections are the real deliverable. |
| Reproducibility | 9 | Pure Python. No excuse for less. |
| Error analysis | 5 | Limited applicability this month. |
| Portfolio readiness | 6 | Foundation, not showpiece. |
| **Overall** | **7.0+** | |

Do not chase 9.0 overall. The marginal hour is worth more in Month 2.

---

## Interview Readiness Baseline

Score 1-5 per dimension. This is your **baseline measurement** — establishing
where you started matters for the Month 18 comparison.

| Dimension | Expected at Month 1 |
| --------- | ------------------- |
| Python coding under time | 3 — you are already strong here |
| ML theory depth | 2 |
| DL / transformer depth | 1 |
| LLM systems design | 1 |
| Infrastructure design | 4 — your existing background |
| Project storytelling | 2 |
| Portfolio strength | 1 |
| **Total (of 35)** | **~14** |

If your infrastructure score is not 4 or 5, you are underselling your background.
That number should be your highest for the entire course, and it starts high.

---

## Self-Deception Checks

Specific to this month.

1. **Did you write the autodiff engine, or transcribe it?** Open a blank file and
   reimplement `Value.__mul__` with its backward closure from memory. Two
   minutes. If you cannot, you transcribed it.

2. **Do the tests actually test anything?** Break one function deliberately —
   change a sign in `cosine_similarity` — and confirm a test fails. If nothing
   fails, your tests are decorative.

3. **Can you derive, or only recognize?** Recognizing a derivation when you see
   it feels identical to being able to produce it. It is not. Blank paper, no
   references, ten minutes.

4. **Is the README written or assembled?** If the theory sections were written
   with a reference open, rewrite them closed. The gap between what you can write
   with help and what you can write without is exactly the gap an interviewer
   will find.

---

## Remediation Triggers

Take a catch-up week before Month 2 if any of these hold:

- Fewer than three of four derivation gates passed
- Fewer than three of four explanation gates passed
- Any implementation gate failed
- Month average below 7.0
- Total hours below 50 across the four weeks

A remediation week is not a setback. Advancing on a shaky Month 1 means failing
Week 14 and Week 29 later, at much greater cost, with the failure disguised as
"transformers are hard."

---

## Advancement Decision

```text
Month 1 average:        __ /10
Capstone score:         __ /10
Derivation gates:       __ /4     (need 3)
Explanation gates:      __ /4     (need 3)
Implementation gates:   __ /5     (need 5)
Interview readiness:    __ /35    (baseline)

Decision:  [ ] Advance to Month 2   [ ] Remediation week first
```

Record it in `coach/reviews/month-01.md`.
