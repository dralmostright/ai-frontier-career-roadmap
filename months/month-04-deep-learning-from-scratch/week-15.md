# Week 15: Optimization

## Outcome

By Sunday you have implemented five optimizers and four learning-rate schedules, and can explain each as the fix for a specific failure of the one before it.

Concretely: `tests/test_optimizers.py` passes, including `test_decoupled_decay_differs_from_l2_in_the_gradient`.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Why Adam?" is a standard question and the answer is a chain, not a fact: SGD
zigzags in ravines, momentum damps it, RMSProp handles scale variance, Adam
combines both, AdamW fixes the decay coupling.

The AdamW question specifically — what does the W do, and why does folding L2
into the gradient behave differently — is a genuinely discriminating one, because
most people use AdamW without knowing.

Warmup is the other high-value item. Skipping warmup on a transformer is one of
the reliable ways to make training diverge, and you will see that happen in
Week 35 if you try it.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7.5 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **SGD and its problems**
   1. The update rule
   2. Ravines: high curvature one way, low the other
   3. Zigzagging, and why smaller steps do not fix it
2. **Momentum**
   1. Velocity accumulation
   2. Why it damps oscillation and accelerates consistent directions
   3. Nesterov's look-ahead
3. **Adaptive methods**
   1. RMSProp: per-parameter steps from a running squared gradient
   2. Why this matters for rare-feature and rare-token gradients
   3. Adam: momentum plus RMSProp
   4. **Bias correction**, and what happens without it
4. **AdamW**
   1. L2-in-gradient versus decoupled decay
   2. Why Adam's adaptive denominator distorts the L2 penalty
   3. Why this is what actually trains transformers
5. **Schedules**
   1. Step, cosine, warmup-cosine, plateau
   2. Why transformers need warmup: unreliable second-moment estimates early
   3. The LR range test

## Required Free Resources

- **Primary:** d2l.ai ch. 12 (optimization algorithms) — https://d2l.ai/
- **Primary:** Distill, 'Why Momentum Really Works' — https://distill.pub/2017/momentum/ — the best explanation of momentum in existence, and interactive
- 'Adam: A Method for Stochastic Optimization' — https://arxiv.org/abs/1412.6980
- 'Decoupled Weight Decay Regularization' (AdamW) — https://arxiv.org/abs/1711.05101 — read section 2; it is the whole argument
- 'Cyclical Learning Rates' (Smith, 2015) — https://arxiv.org/abs/1506.01186 — the LR range test

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=15
```

1. **`SGD` with momentum and Nesterov** (1.5h) — Then run it on an ill-conditioned quadratic and see the ravine problem.
2. **`RMSProp`** (1h) — Test on a problem with 1000x scale differences between parameters.
3. **`Adam` without bias correction** (1h) — Plot the first 200 steps. Note how small they are.
4. **`Adam` with bias correction** (45m) — Plot again, overlaid. This comparison is the week's deliverable figure.
5. **`AdamW`** (1h) — Then construct the case where it diverges from Adam-with-weight-decay.
6. **`StepLR`, `CosineAnnealingLR`** (1h) — Plot both.
7. **`WarmupCosineLR`** (1h) — The schedule every LLM uses. Verify the ramp and the decay.
8. **`ReduceLROnPlateau`** (45m) — Reactive rather than scheduled.
9. **`compare_optimizers` on Rosenbrock** (1.5h) — All five, trajectories overlaid on one figure.
10. **`lr_range_test`** (1h) — Ten minutes of this replaces a day of guessing.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
m
l
-
f
r
o
m
-
s
c
r
a
t
c
h
/
s
r
c
/
o
p
t
i
m
i
z
e
r
s
.
p
y
```

## Tests To Write

`tests/test_optimizers.py`. Add one: a test that momentum reaches a target loss in measurably fewer steps than plain SGD on an ill-conditioned quadratic.

## Portfolio Artifact

`src/optimizers.py` plus two figures: optimizer trajectories on Rosenbrock, and the Adam bias-correction comparison.

## Interview Drills

**Coding (45 min).** Two problems, strings and sliding window.

**ML theory (25 min).** Recorded: *Why does Adam converge faster and sometimes generalize worse than SGD?* Then: *What does the W in AdamW do, and why does it matter?* Then: *Why do transformers need learning-rate warmup?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement Lion (EvoLved Sign Momentum) and compare it against AdamW on the same problem. Lion uses only the sign of the momentum, which makes its optimizer state half the size — a real memory saving at scale. Report whether the quality holds on your problem.
