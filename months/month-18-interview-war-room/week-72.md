# Week 72: Deep Learning Interviews

## Outcome

By Sunday you can derive attention and backpropagation cold in under six minutes each, and answer the full DL question bank fluently.

## Why This Matters For OpenAI/Anthropic-Level Interviews

This is the depth screen, and attention is the single most examined topic.

The standard for attention: derive it on a whiteboard, cold, in under six
minutes, including the √d variance argument, the causal mask, and the multi-head
rationale. Then hold up under "what breaks without layer norm?" — which you can
answer with your own Month 8 ablation data, which almost nobody can.

The KV cache calculation is the other high-frequency question, and it connects to
Week 49's memory arithmetic. Being able to move between them fluently
demonstrates that the knowledge is connected rather than memorized in pieces.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 3 hours
- Project: 0 hours
- Interview practice: 13 hours
- Review/write-up: 4 hours

## Theory Lessons

1. **The derivation set**
   1. Backprop for a two-layer MLP
   2. Scaled dot-product attention with the √d argument
   3. Softmax + cross-entropy
   4. LayerNorm forward and backward
   5. LoRA's parameter count
   6. Adam's update with bias correction
2. **The question bank**
   1. Training mechanics, architecture, inference, training regimes, evaluation, safety
   2. All of Track 3 in `INTERVIEW_PREP.md`
3. **Using your own data**
   1. The Month 8 ablation table as evidence
   2. The Month 9 training report
   3. Your own measurements beat citations

## Required Free Resources

- **Primary:** `INTERVIEW_PREP.md` Track 3
- **Primary:** Your Month 8 ablation table and Month 9 training report
- Your Week 49 memory arithmetic notebook

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=72
```

1. **Attention, cold, five times** (2h) — Until it is under six minutes with no hesitation.
2. **Backprop, cold, three times** (1.5h) — Two-layer MLP, shapes stated.
3. **The remaining derivations** (2.5h) — LayerNorm, LoRA, Adam, softmax+CE.
4. ****15 recorded derivations**** (4h) — Watch them back and score.
5. **Question bank sweep** (2.5h) — Every question in Track 3, out loud. Note the ones you fumble.
6. **Ablation-backed answers** (1.5h) — Practice answering 'what breaks without X?' with your own numbers.
7. **One full DL mock** (1h) — 45 minutes, recorded, scored.

## Bootstrap Files To Create

```text
c
o
a
c
h
/
i
n
t
e
r
v
i
e
w
s
/
d
l
_
t
h
e
o
r
y
_
l
o
g
.
m
d
```

## Tests To Write

The recordings, scored.

## Portfolio Artifact

Fifteen recorded derivations.

## Interview Drills

**Full mock (45 min).** DL depth, recorded, scored.

**Whiteboard set (60 min).** Attention, backprop, LayerNorm, LoRA, back to back, timed.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Prepare a two-minute whiteboard walkthrough of your Mini-GPT architecture that ends by pointing at your ablation table. It is a natural bridge from a theory question to your portfolio, it demonstrates depth and evidence together, and it gives you something to steer toward when an interviewer asks an open question.
