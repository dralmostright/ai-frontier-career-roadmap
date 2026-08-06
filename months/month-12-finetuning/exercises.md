# Month 12 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 45 — Fine-Tuning Fundamentals

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 45.1 | Build the decision framework | 1h | Medium |
| 45.2 | Set up a small model and dataset | 1.5h | Medium |
| 45.3 | Loss masking on completions | 1h | Medium |
| 45.4 | The full fine-tune | 2h | Medium |
| 45.5 | Target-task evaluation | 1h | Medium |
| 45.6 | **Regression check** | 1.5h | Hard |
| 45.7 | Overfitting demonstration | 1h | Medium |
| 45.8 | LR sensitivity | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 45.E1 | Mix general data into the fine-tune and measure whether forgetting reduces | 2.5h | High — a real mitigation, measured |
| 45.E2 | Compare fine-tuning against few-shot prompting on the same task | 2h | **High** — often the honest baseline, and often competitive |
| 45.E3 | Probe what changed: which layers moved most during fine-tuning | 2.5h | High — interpretability practice |

## Week 46 — LoRA and QLoRA

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 46.1 | Derive the parameter count | 30m | Easy |
| 46.2 | `LoRALayer` from scratch | 2h | Hard |
| 46.3 | `apply_lora` to a real model | 1.5h | Medium |
| 46.4 | `merge` and `unmerge` | 1h | Medium |
| 46.5 | Train with your LoRA | 2h | Medium |
| 46.6 | **`rank_ablation`** | 2.5h | Hard |
| 46.7 | Target-module ablation | 1.5h | Medium |
| 46.8 | `save_adapter` | 45m | Easy |
| 46.9 | QLoRA with bitsandbytes | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 46.E1 | Multi-adapter serving: one base model, three task adapters, swapped per request | 3h | **High** — a real serving pattern and a strong system design answer |
| 46.E2 | Implement DoRA (weight-decomposed LoRA) and compare | 2.5h | Medium — shows you track the field |
| 46.E3 | Measure which layers' adapters matter most by zeroing them one at a time | 2h | High — a nice interpretability result |

## Week 47 — Instruction Datasets and Data Quality

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 47.1 | Define the task taxonomy | 1h | Medium |
| 47.2 | Hand-write 50 gold examples | 3h | Hard |
| 47.3 | Template from Month 11's benchmark | 2h | Medium |
| 47.4 | Generate and review 500 more | 3h | Hard |
| 47.5 | Quality scoring and filtering | 1.5h | Medium |
| 47.6 | Deduplication | 1h | Medium |
| 47.7 | Format with a chat template | 1h | Medium |
| 47.8 | Held-out split by task type | 45m | Easy |
| 47.9 | **The dataset card** | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 47.E1 | Measure inter-rater agreement by having someone else review 50 examples | 2h | High — honest about your own labeling |
| 47.E2 | A data-scaling ablation: train on 100, 300, 1000 examples and plot quality | 3h | **High** — your own version of the LIMA finding |
| 47.E3 | Build a preference dataset (chosen/rejected pairs) for Week 48's DPO | 3h | High — needed for the stretch |

## Week 48 — Evaluation and Model Comparison

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 48.1 | Build the evaluation set | 1.5h | Medium |
| 48.2 | Base versus tuned, pairwise | 2h | Medium |
| 48.3 | **Well-prompted base as baseline** | 1.5h | Medium |
| 48.4 | **RAG versus fine-tuning** | 2h | Hard |
| 48.5 | General capability regression | 1.5h | Medium |
| 48.6 | Out-of-distribution probes | 1h | Medium |
| 48.7 | Validate the judge | 1.5h | Medium |
| 48.8 | Per-task-type breakdown | 1h | Easy |
| 48.9 | **The model card** | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 48.E1 | Implement DPO on your own preference pairs and compare against SFT | 4h | **High** — the most valuable stretch this month |
| 48.E2 | Build a small reward model and inspect what it rewards | 3h | High — and often reveals reward hacking |
| 48.E3 | Combine fine-tuning and RAG; measure whether they compose | 3h | **High** — usually the right production answer, and rarely measured |

---

## If You Finish Early

Priority: Week 48's DPO implementation, Week 48's fine-tuning-plus-RAG combination (usually the right production answer and rarely measured), Week 47's data-scaling ablation. Phase 4 ends here — check Gate G4 before advancing to Phase 5.
