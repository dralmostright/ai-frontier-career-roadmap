# Week 17: PyTorch Tensors and Autograd

## Outcome

By Sunday you can use PyTorch confidently for tensors and autograd, and you have loaded your Week 13-16 NumPy weights into an equivalent `nn.Module` and confirmed identical outputs.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"What does `.backward()` actually do?" is a standard question, and having
written the answer in Month 4 means you can answer it mechanically rather than
by analogy.

The `no_grad` versus `detach` distinction is asked more often than people expect,
and the subtle part — that `detach` shares storage, so in-place mutation affects
the original — is where a good answer separates from a memorized one.

Broadcasting bugs are the most common silent failure in PyTorch code. Subtracting
a shape-(n,) tensor from a shape-(n,1) tensor gives an (n,n) matrix instead of an
error, your loss becomes a matrix, and training quietly does nothing. Construct
that bug deliberately this week so you recognize it later.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Tensors**
   1. Storage, shape, and stride
   2. Why `.view()` needs `.contiguous()` after a transpose
   3. Devices, and the cost of transfers
   4. dtype, and why float32 is the default
2. **Autograd**
   1. `requires_grad` and the graph
   2. `grad_fn` and walking the chain
   3. Leaf tensors and accumulation
   4. `no_grad` versus `detach`, including the shared-storage subtlety
3. **Broadcasting**
   1. The rules
   2. The (n,) minus (n,1) trap
   3. Why explicit shapes in comments save hours
4. **`nn.Module`**
   1. Parameter registration
   2. `state_dict` and what it does and does not contain
   3. Buffers versus parameters

## Required Free Resources

- **Primary:** PyTorch 60-minute blitz — https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- **Primary:** PyTorch autograd mechanics — https://pytorch.org/docs/stable/notes/autograd.html — read this properly, not skimmed
- d2l.ai ch. 2 (preliminaries) — https://d2l.ai/
- PyTorch broadcasting semantics — https://pytorch.org/docs/stable/notes/broadcasting.html

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=17
```

1. **`device_report`** (30m) — Know your hardware before Month 8.
2. **`autograd_walkthrough`** (1h) — Trace a small graph, expose every `grad_fn`. Compare to your Week 3 engine.
3. **`gradient_accumulation_demo`** (30m) — Backward twice without zeroing. The gradient doubles.
4. **`no_grad_vs_detach`** (1h) — Including the shared-storage demonstration.
5. **`broadcasting_rules`** (1h) — Construct the (n,) vs (n,1) bug on purpose.
6. **`numpy_to_torch_port`** (2h) — Load your Month 4 weights into an nn.Module. Identical outputs prove both were right.
7. **`benchmark_devices`** (1h) — With and without the transfer in the timing. The gap explains a lot.
8. **Rewrite the Month 4 training loop in PyTorch** (1.5h) — Note how much shorter it is, and that you know what was removed.

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
t
e
n
s
o
r
_
l
a
b
s
.
p
y
```

## Tests To Write

`tests/test_pytorch_labs.py` week-17 blocks. Add one: a test that your ported NumPy model and the PyTorch model produce outputs matching to 1e-5 on the same input.

## Portfolio Artifact

`src/tensor_labs.py` and a notebook showing the NumPy/PyTorch equivalence.

## Interview Drills

**Coding (45 min).** Two problems, trees.

**ML theory (20 min).** Recorded: *What does `.backward()` actually do?* Answer mechanically — topological sort, chain rule, accumulation. Then: *When would you use `no_grad` versus `detach`?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Write a custom `autograd.Function` implementing a numerically-stable log-sum-exp with a hand-written backward, and gradient-check it against the autograd version. You will need this pattern in Week 29 if you write a fused attention kernel.
