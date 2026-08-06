# Week 16: Regularization and Generalization

## Outcome

By Sunday you can deliberately overfit a model, then fix it one technique at a time and measure what each was worth.

Concretely: `tests/test_neural_net.py` week-16 blocks pass, and `test_trains_mnist_subset_to_high_accuracy` — the Month 4 capstone gate — passes.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The diagnostic skill is the point. "Training loss drops, validation rises —
what now?" is asked constantly, and the strong answer is an *ordered* checklist,
not a list of techniques.

`overfit_single_batch` is the function you will use most for the rest of the
course. A correct model memorizes eight examples within a few hundred steps. If
it cannot, the bug is in your code, and no hyperparameter search will help. This
one check catches wrong loss reductions, detached gradients, misaligned labels,
and shuffled targets — four bugs that otherwise cost a day each.

BatchNorm's backward pass is the hardest derivation in the lab, and getting it
gradient-checked is the strongest possible evidence that you understand
backpropagation.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 7.5 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Weight penalties**
   1. L1's constant gradient produces exact zeros; L2's shrinking gradient does not
   2. Why biases and normalization parameters are never penalized
2. **Dropout**
   1. Random zeroing as an implicit ensemble
   2. Inverted dropout: scale at train time so inference needs no adjustment
   3. Why it must be a no-op in eval mode
3. **Normalization**
   1. BatchNorm: across the batch, with running statistics for eval
   2. The two-mode bug: good in training, bad in eval
   3. LayerNorm: across features, batch-independent
   4. Why transformers use LayerNorm — variable lengths and batch size 1 at inference
   5. Why the 'internal covariate shift' explanation is contested
4. **Early stopping**
   1. The cheapest regularizer
   2. Restoring the best weights, not the last
   3. min_delta, so noise does not reset patience
5. **Augmentation**
   1. Label smoothing, and its link to Week 4's count smoothing
   2. Mixup, and why training on convex combinations works
   3. Gaussian noise as L2 regularization for linear models
6. **Diagnosis**
   1. The symptom-to-action table
   2. Overfit a single batch first
   3. The ln(C) initial-loss check

## Required Free Resources

- **Primary:** d2l.ai ch. 5.6 (dropout), 8.5 (batch norm) — https://d2l.ai/
- **Primary:** Karpathy, 'A Recipe for Training Neural Networks' — https://karpathy.github.io/2019/04/25/recipe/ — read this twice. It is the single best practical guide to debugging training, and the overfit-a-single-batch advice comes from here.
- 'Batch Normalization' (Ioffe and Szegedy, 2015) — https://arxiv.org/abs/1502.03167
- 'How Does Batch Normalization Help Optimization?' (Santurkar et al., 2018) — https://arxiv.org/abs/1805.11604 — the paper that displaced the original explanation
- 'Layer Normalization' — https://arxiv.org/abs/1607.06450

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=16
```

1. **`l1_penalty`, `l2_penalty`, `add_penalty_gradients`** (45m) — Exclude biases and norm parameters.
2. **`Dropout`, inverted** (1h) — Verify it is a no-op in eval mode and preserves expected value in training.
3. **`BatchNorm1d` forward, both modes** (1.5h) — Running statistics for eval. Test both paths.
4. **`BatchNorm1d.backward`** (2h) — The hardest derivation in the lab. Three gradient paths per input. Derive on paper, then gradient-check.
5. **`LayerNorm`** (1h) — Then verify it is batch-size independent — the property that makes transformers use it.
6. **`EarlyStopping` with best-weight restoration** (1h) — Stopping at epoch 50 having peaked at 37 wastes the peak.
7. **`label_smoothing`, `mixup`** (1h) — Both are stranger than they sound and both work.
8. **`overfit_single_batch`** (45m) — **Run this before every training run from now on.**
9. **`diagnose_fit`** (1h) — The symptom-to-action table, as code. Test it on three synthetic curves.
10. **The ablation table** (2h) — Overfit deliberately, then fix one technique at a time. Report the table.

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
r
e
g
u
l
a
r
i
z
a
t
i
o
n
.
p
y
```

## Tests To Write

`tests/test_neural_net.py` and `test_backprop.py` week-16 blocks. The BatchNorm gradient check is the hard one. Add one: a test that a model in `train()` mode and the same model in `eval()` mode produce different outputs when dropout is active, and identical outputs when it is not.

## Portfolio Artifact

`src/regularization.py`, the ablation table, and the Month 4 capstone. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems, sorting and binary search.

**ML theory (30 min).** Recorded: *Loss is NaN at step 400. Debug it out loud, in priority order.* Then: *Training loss drops, validation rises. What are your next three actions and why in that order?*

**Behavioral (15 min).** Draft story #1: a production incident you led. Real numbers.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Implement RMSNorm and compare it against LayerNorm on the same model: quality, and wall-clock time. RMSNorm drops the mean-centering step, which makes it cheaper, and Llama and most modern LLMs use it. You will meet it again in Week 33; implementing it now means that week is a review.
