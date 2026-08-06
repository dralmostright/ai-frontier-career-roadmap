# Week 18: Modules, Datasets, DataLoaders

## Outcome

By Sunday you can build reusable modules and data pipelines, and diagnose whether your model or your input pipeline is the bottleneck.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The input pipeline is the most common training bottleneck and the least
interesting one to debug, so people skip it and then wonder why the GPU sits at
30%.

"Your GPU is at 30% utilization — diagnose it" is a real interview question and
one you should answer well. The ordered checklist: measure the loader alone
before guessing; raise `num_workers`; set `pin_memory` and `persistent_workers`;
check for `.item()` calls in the loop; check the batch size.

The unseeded-worker bug is worth knowing because it is silent: without
`worker_init_fn`, every worker draws the same random augmentations, so your
"random" crops repeat and you lose accuracy for no visible reason.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The Dataset contract**
   1. `__init__`, `__len__`, `__getitem__`
   2. Eager versus lazy loading, and the memory/IO tradeoff
   3. Map-style versus iterable-style
2. **DataLoader**
   1. `num_workers` and process-based parallelism
   2. `pin_memory` and asynchronous transfer
   3. `persistent_workers`
   4. `drop_last`, and why a one-element final batch breaks BatchNorm
   5. `worker_init_fn`: the silent augmentation bug
3. **Collation**
   1. Default collation and its assumptions
   2. Variable-length sequences: padding and masks
   3. Why the mask matters — the model learns padding is meaningful without it
4. **nn.Module patterns**
   1. Composition, `apply`, hooks
   2. Parameter counting and where parameters actually live
   3. Freezing, and the BatchNorm caveat

## Required Free Resources

- **Primary:** PyTorch data loading tutorial — https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
- **Primary:** PyTorch performance tuning guide — https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html — read the data loading section carefully
- d2l.ai ch. 6 (builders' guide) — https://d2l.ai/
- 'PyTorch DataLoader num_workers' discussions — the practical folklore is genuinely useful here

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=18
```

1. **`TabularDataset`** (45m) — The three-method contract.
2. **`ImageFolderDataset`** (1h) — Lazy loading. Measure with num_workers=0 versus 4.
3. **`make_loaders` with all the flags** (1h) — Including `worker_init_fn` and a generator.
4. **`diagnose_loader_bottleneck`** (1.5h) — Time the loader alone, the model alone, and both. The week's key tool.
5. **`collate_variable_length`** (1.5h) — Padding and a mask. You need this again in Weeks 32 and 38.
6. **`compute_normalization_stats`** (45m) — Training set only. Leakage, again.
7. **`count_parameters` and `model_summary`** (1.5h) — Implement the summary with forward hooks.
8. **`initialize_weights`** (45m) — He, Xavier, zeros for biases.
9. **`freeze_layers`** (45m) — Note the BatchNorm caveat: freezing parameters does not freeze running statistics.

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
p
y
t
o
r
c
h
-
l
a
b
s
/
s
r
c
/
d
a
t
a
.
p
y


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
p
y
t
o
r
c
h
-
l
a
b
s
/
s
r
c
/
m
o
d
e
l
s
.
p
y
```

## Tests To Write

`tests/test_pytorch_labs.py` week-18 blocks. Add one: a test that two DataLoader workers with `worker_init_fn` produce *different* random augmentations, and without it produce the same — the silent bug, caught.

## Portfolio Artifact

`src/data.py`, `src/models.py`, and the num_workers throughput plot.

## Interview Drills

**Coding (45 min).** Two problems, graphs.

**ML theory (25 min).** Recorded: *Your GPU is at 30% utilization. Diagnose it.* Answer in priority order, starting with 'measure before guessing.' This is a question your background should let you answer better than most ML candidates.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Build a length-bucketing sampler: group sequences of similar length into batches so padding is minimized. Measure the wasted-token fraction with and without it. On variable-length text this is often a 30-50% throughput win, and you will want it in Week 35.
