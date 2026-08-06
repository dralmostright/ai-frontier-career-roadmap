# pytorch-labs

**Weeks 17-24 · Months 5, 6 · Capstones: MNIST Production Pipeline, Image Classification Service**

The port. Everything you built by hand in Month 4, rebuilt in PyTorch — and then
wrapped in the engineering discipline that separates research code from software.

---

## Why This Lab Exists

Month 5 is where your background pays off for the first time in this course.

Most people learning PyTorch write a script, get a number, and move on. You are
going to write a *pipeline*: config-driven, seeded, checkpointed, tracked,
tested, and reproducible bit-for-bit across machines. That is not a nicety. It
is the difference between "I trained a model" and "I can hand this to someone
else and they get my numbers," and hiring managers who have inherited research
code notice the difference within thirty seconds of opening a repo.

Month 6 uses computer vision as the cheapest possible domain for practising full
training pipelines. Vision datasets are small, fast, and visually debuggable —
when a CNN is broken you can *look* at what it got wrong. That feedback loop
does not exist for language models, which is why you learn the pipeline here and
apply it there.

---

## Layout

```text
pytorch-labs/
  src/
    tensor_labs.py      W17  tensors, autograd, device handling, the .backward() walkthrough
    data.py             W18  Dataset, DataLoader, transforms, the input-pipeline bottleneck
    models.py           W18  nn.Module patterns, weight init, parameter counting
    train.py            W19  the training loop: AMP, clipping, accumulation, checkpointing
    evaluate.py         W19  evaluation loop, metric aggregation, confusion matrices
    config.py           W20  Pydantic config schema, YAML loading, config diffing
    tracking.py         W20  experiment tracking, run comparison, artifact logging
    reproducibility.py  W20  seeding everything, determinism flags, environment capture
    cnn.py              W21  convolution from scratch, then nn.Conv2d, receptive fields
    resnet.py           W22  residual blocks, why skip connections fix depth
    transfer.py         W23  freezing, discriminative LRs, feature extraction vs fine-tuning
    vit.py              W24  patch embedding, ViT vs CNN, inductive bias
    serve.py            W24  FastAPI inference, dynamic batching, latency measurement
  configs/
    mnist.yaml          W20  the config that drives the Month 5 capstone
    cifar10.yaml        W21
    resnet18.yaml       W22
    finetune.yaml       W23
    vit_tiny.yaml       W24
  tests/
```

---

## Install PyTorch First

Not in `requirements.txt`, because the right wheel depends on your hardware.

```bash
source ../.venv/bin/activate
pip install torch torchvision                                             # Apple Silicon (MPS)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121  # Linux + CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu    # CPU only
```

Everything in Months 5-6 runs on CPU, slowly, or on Colab's free tier, quickly.
You do not need to buy a GPU. See `RESOURCE_INDEX.md` for the compute strategy.

---

## The Month 5 Standard

By Week 20, `python -m src.train --config configs/mnist.yaml` must:

- Read every hyperparameter from the config. Zero magic numbers in the code.
- Seed Python, NumPy, and PyTorch, and set the determinism flags.
- Log per-step loss, per-epoch metrics, learning rate, and gradient norm.
- Checkpoint every N steps, and keep the best-by-validation separately.
- Resume cleanly from any checkpoint, including optimizer and scheduler state.
- Early-stop with best-weight restoration.
- Export the trained model plus a metrics JSON and the exact config used.
- Produce identical numbers on a second run. Verified by a test.

That last one is the hard one and it is the one worth demonstrating. Write a
test that trains for 50 steps twice and asserts the losses match exactly.

---

## Milestones

| Week | You can... |
| ---- | ---------- |
| 17 | Explain mechanically what `.backward()` does, and when to use `no_grad` vs `detach` |
| 18 | Diagnose a data-loading bottleneck and fix GPU starvation |
| 19 | Write a training loop with AMP, gradient clipping, and accumulation, and say why each is there |
| 20 | Reproduce a training run bit-for-bit on a different machine |
| 21 | Compute a receptive field, and implement convolution before calling `nn.Conv2d` |
| 22 | Explain why residual connections make 50-layer networks trainable |
| 23 | Decide what to freeze, and set discriminative learning rates |
| 24 | Say when a ViT beats a CNN and when it does not, with the data-scale reasoning |

---

## The Debugging Checklist

Print this. You will use it for the next fourteen months.

**The model does not learn at all**
1. Overfit 8 examples. Cannot? The bug is in your code, not your hyperparameters.
2. Check the initial loss: ln(C) for C classes. Wrong? Labels or loss are wrong.
3. Did you call `optimizer.zero_grad()`? Missing it accumulates across steps.
4. Did you call `loss.backward()` before `optimizer.step()`?
5. Are the parameters actually in the optimizer? `len(list(model.parameters()))`.
6. Is anything `.detach()`ed or under `no_grad` that shouldn't be?
7. Print gradient norms. All zero means a broken graph; all NaN means overflow.

**It learns, then diverges**
1. Learning rate too high. Divide by 10.
2. No warmup on a deep or attention-based model. Add it.
3. Missing gradient clipping. `clip_grad_norm_(model.parameters(), 1.0)`.
4. A `log(0)` or a divide-by-zero in your loss. Add an epsilon.
5. Under AMP: the loss scaler is missing or misconfigured.

**Training is slow**
1. Profile before guessing. `torch.profiler`, or just time the data loader alone.
2. GPU utilization low → the input pipeline is the bottleneck, not the model.
   Raise `num_workers`, set `pin_memory=True`, `persistent_workers=True`.
3. Are you calling `.item()` or `.cpu()` inside the inner loop? Each one
   synchronizes and stalls the GPU.
4. Batch too small to saturate the device. Raise it, and raise the LR with it.
5. AMP not enabled. On modern hardware this is typically a 1.5-2x win.

**Validation is worse than expected**
1. Did you call `model.eval()`? Dropout and BatchNorm are mode-dependent.
2. Did you wrap evaluation in `torch.no_grad()`? Not a correctness issue, but a
   memory one.
3. Are train and validation transforms different in a way you did not intend?
4. Leakage. Go back to `ml-from-scratch/tests/test_no_leakage.py`.

---

## Interview Drills

| Week | Drill |
| ---- | ----- |
| 17 | What does `.backward()` actually do? Walk the graph out loud. |
| 18 | Your GPU sits at 30% utilization. Diagnose it, in priority order. |
| 19 | Training loss drops, validation rises. What are your next three actions? |
| 20 | How do you make a training run reproducible? Name every source of nondeterminism. |
| 21 | Compute the receptive field of a 3-layer CNN with 3x3 kernels and one stride-2 layer. |
| 22 | Why do residual connections fix deep networks? Answer with gradient flow, not intuition. |
| 23 | Which layers do you freeze when fine-tuning, and why does the answer depend on dataset size? |
| 24 | When does a ViT beat a CNN? What does the CNN's inductive bias buy you? |

---

## Capstones

- **Month 5** — MNIST Production Training Pipeline. The reproducibility test is
  the artifact.
- **Month 6** — Image Classification Service. FastAPI, Docker, and a
  latency-versus-batch-size curve you measured yourself.

Full specifications in `months/month-05-pytorch-engineering/capstone.md` and
`months/month-06-computer-vision/capstone.md`.
