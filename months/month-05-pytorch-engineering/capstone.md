# Month 05 Capstone: MNIST Production Training Pipeline

## Objective

Build a training pipeline that is config-driven, seeded, tracked, checkpointed, tested, and reproducible bit-for-bit — and prove the last claim with a test.

## Business Problem

The modeling problem is trivial and that is deliberate. The engineering is the
subject.

The realistic framing: you are handed a model that works in a notebook and asked
to make it something a team can own. That is a real task, it is common, and most
ML engineers do it badly.

## Technical Requirements

- Every hyperparameter in a YAML config; zero magic numbers in code
- Seeded: Python, NumPy, torch, CUDA, and DataLoader workers
- Deterministic mode available, with its cost measured and documented
- Logging: per-step loss, per-epoch metrics, learning rate, gradient norm
- Checkpointing every N steps, plus best-by-validation kept separately
- Resume from any checkpoint with a continuous loss curve
- Early stopping with best-weight restoration
- Mixed precision, gradient clipping, gradient accumulation
- Experiment tracking with run comparison
- Model export (TorchScript or ONNX) plus a metrics JSON and the exact config
- CI running the tests on every push
- **A test that trains twice and asserts identical losses**

## Theory Requirements

The README must explain:

1. Every source of nondeterminism in a PyTorch training run, and how each is
   controlled.
2. Why weights-only checkpoints produce a discontinuity on resume.
3. Why gradient accumulation requires dividing the loss, and what happens if you
   forget.
4. What deterministic mode costs, measured on your hardware.

## System Design Requirements

- `src/` with a clean separation: data, model, training, evaluation, config
- CLI via Typer: `train`, `evaluate`, `export`, `resume`
- Configs composable: a base plus overrides
- Artifacts written to a run directory with the config, environment, and metrics
- Nothing in the notebook that belongs in `src/`

## Implementation Plan

**Days 1-2** — Config system and CLI. Do this first; retrofitting is painful.

**Day 3** — The training loop with all the production features wired in.

**Day 4** — Checkpointing and resume. Verify the loss curve is continuous.

**Day 5** — Reproducibility. This is the hard day. Getting bit-for-bit identical
runs usually requires hunting down one or two surprises.

**Day 6** — Tracking, export, CI.

**Day 7** — README and publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| MNIST test accuracy | > 99% (a CNN makes this easy; the accuracy is not the point) |
| Two runs, same config | Byte-identical losses |
| Resume from checkpoint | Loss curve continuous, no visible jump |
| `make setup && make train` from a clean clone | Works first try |
| Deterministic mode cost | Measured and reported |
| CI | Green on every push |

## Expected Repository Structure

```text
mnist-production-pipeline/
  README.md
  pyproject.toml
  Makefile
  .github/workflows/ci.yml
  configs/
    base.yaml
    mlp.yaml
    cnn.yaml
  src/mnist_pipeline/
    config.py
    data.py
    models.py
    train.py
    evaluate.py
    export.py
    tracking.py
    cli.py
  tests/
    test_config.py
    test_reproducibility.py
    test_training.py
    test_checkpointing.py
  runs/
  docs/
    design.md
    reproducibility.md
    limitations.md
```

## README Requirements

Above the fold: one sentence, the accuracy, and `make setup && make train`.

Then: what this is and why it exists (the notebook-to-production framing); the
reproducibility guarantee with the test that proves it; the config system with an
example; the feature list with a one-line justification each; the
deterministic-mode cost measurement; how to resume; limitations.

**Lead with reproducibility, not accuracy.** 99% on MNIST impresses nobody. A
test that proves bit-for-bit reproducibility across runs is unusual and it is
what makes this repository worth opening.

## Demo Requirements

`make demo` trains for 60 seconds, then `make demo-reproduce` trains again and prints a diff of the two loss sequences showing them identical.

## Blog Post Requirement

**Post #1 is due this month.** Recommended: "What a DBA Learns Building a
Neural Network From Scratch" (the Month 4 subject) or "Reproducible Training Runs
Are an Operations Problem, Not an ML Problem" (this month's).

The second is the more differentiated angle. Nobody in the ML world writes about
reproducibility from an operations perspective, and the framing — seeds are
necessary and insufficient, environment capture is configuration management,
checkpoints are state snapshots — is yours.

## Interview Story

> "Same model as the previous project, but this version is reproducible
> bit-for-bit across machines, and there's a test that proves it. I also measured
> what determinism costs — about 12% throughput on my hardware — so you can make
> that tradeoff knowingly rather than by accident."

45 seconds.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 5 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 7 | The notebook-to-production framing is real. |
| Technical execution | 8 | All the production features, working. |
| Evaluation rigor | 7 | Accuracy is trivial; the reproducibility verification is the rigor. |
| Code quality | 9 | **The point of the month.** This should be genuinely good code. |
| Documentation | 8 | Reproducibility guarantee front and center. |
| Reproducibility | 10 | **Target 10.** This is the capstone's entire thesis. |
| Error analysis | 6 | Limited scope. |
| Portfolio readiness | 8 | Reviewers who have suffered through research code will notice. |

**Overall target: 8.0+, with Reproducibility at 10 and Code Quality at 9.**

## Stretch Goals

1. **Cross-machine reproducibility**, containerized and verified. The strongest
   version of the claim.
2. **A hyperparameter sweep** with 20 runs, tracked and compared, with the
   comparison table in the README.
3. **ONNX export plus a serving benchmark** — previews Month 6.
4. **A pre-commit hook** that blocks commits when the reproducibility test fails.

## Limitations To State Honestly

- Full determinism costs throughput; the measured figure is in the README.
- Reproducibility is guaranteed on identical hardware and library versions.
  Across GPU architectures, floating-point reduction order differs.
- MNIST is a solved problem chosen to keep the engineering in focus.
- The tracking backend is local files; a team would need a shared server.
