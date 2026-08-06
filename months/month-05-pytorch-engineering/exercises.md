# Month 05 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 17 — PyTorch Tensors and Autograd

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 17.1 | `device_report` | 30m | Easy |
| 17.2 | `autograd_walkthrough` | 1h | Medium |
| 17.3 | `gradient_accumulation_demo` | 30m | Easy |
| 17.4 | `no_grad_vs_detach` | 1h | Medium |
| 17.5 | `broadcasting_rules` | 1h | Medium |
| 17.6 | `numpy_to_torch_port` | 2h | Hard |
| 17.7 | `benchmark_devices` | 1h | Medium |
| 17.8 | Rewrite the Month 4 training loop in PyTorch | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 17.E1 | Implement a custom `autograd.Function` with forward and backward | 2h | High — the escape hatch you need in Week 29 |
| 17.E2 | Explore `torch.compile` and measure the speedup | 1.5h | Medium |
| 17.E3 | Profile a simple model with `torch.profiler` and read the trace | 2h | High — previews Week 52 |

## Week 18 — Modules, Datasets, DataLoaders

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 18.1 | `TabularDataset` | 45m | Easy |
| 18.2 | `ImageFolderDataset` | 1h | Medium |
| 18.3 | `make_loaders` with all the flags | 1h | Medium |
| 18.4 | `diagnose_loader_bottleneck` | 1.5h | Hard |
| 18.5 | `collate_variable_length` | 1.5h | Medium |
| 18.6 | `compute_normalization_stats` | 45m | Easy |
| 18.7 | `count_parameters` and `model_summary` | 1.5h | Medium |
| 18.8 | `initialize_weights` | 45m | Easy |
| 18.9 | `freeze_layers` | 45m | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 18.E1 | Implement a caching dataset that memoizes decoded images to disk | 2h | High — a real pattern for slow decoding |
| 18.E2 | Benchmark num_workers from 0 to 16 and plot throughput | 1h | High — the figure that answers 'how many workers?' |
| 18.E3 | Implement a bucketing sampler that batches similar-length sequences | 2h | High — needed in Week 35 to reduce padding waste |

## Week 19 — Training Loops and Debugging

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 19.1 | `train_step` | 1h | Medium |
| 19.2 | `Trainer.train_epoch` | 1.5h | Medium |
| 19.3 | Gradient accumulation | 1.5h | Hard |
| 19.4 | Mixed precision with a scaler | 1.5h | Hard |
| 19.5 | `Trainer.validate` | 45m | Easy |
| 19.6 | `save_checkpoint` / `load_checkpoint` | 1.5h | Hard |
| 19.7 | `estimate_memory` | 1h | Medium |
| 19.8 | `find_lr` | 1h | Medium |
| 19.9 | `evaluate` and `predict_all` | 1h | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 19.E1 | Implement EMA (exponential moving average) of weights and compare final accuracy | 1.5h | High — a cheap, reliable improvement used in most production training |
| 19.E2 | Add TensorBoard logging with gradient histograms | 1.5h | Medium |
| 19.E3 | Implement gradient checkpointing with `torch.utils.checkpoint`; measure the memory/compute tradeoff | 2h | High |

## Week 20 — Experiment Tracking and Reproducibility

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 20.1 | `TrainConfig` with Pydantic | 1.5h | Medium |
| 20.2 | `load_config` with dotted overrides | 1h | Medium |
| 20.3 | `diff_configs` | 1h | Medium |
| 20.4 | `set_seed` | 1h | Medium |
| 20.5 | `capture_environment` | 1h | Medium |
| 20.6 | `verify_reproducibility` | 1.5h | Hard |
| 20.7 | Hunt down the first divergence | 1.5h | Hard |
| 20.8 | `ExperimentTracker` | 1.5h | Medium |
| 20.9 | `compare_runs` and `plot_training_curves` | 1h | Easy |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 20.E1 | Wire up MLflow and log 10 runs of a hyperparameter sweep | 2h | High — needed properly in Week 53 |
| 20.E2 | Measure the throughput cost of `use_deterministic_algorithms(True)` | 1h | High — quantifies the tradeoff you will be asked about |
| 20.E3 | Containerize the training run and verify reproducibility across two machines | 3h | High — the strongest possible version of the claim |

---

## If You Finish Early

Priority: the cross-machine reproducibility stretch goal, Week 19's EMA (a free accuracy point you will reuse), Week 18's bucketing sampler (needed in Week 35), and wiring up MLflow properly since Week 53 depends on it.
