# Month 09 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 33 — Modern Architecture: RoPE, RMSNorm, SwiGLU, GQA

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 33.1 | Implement RoPE | 2h | Hard |
| 33.2 | Test length extrapolation | 1h | Medium |
| 33.3 | Implement RMSNorm | 45m | Easy |
| 33.4 | Implement SwiGLU | 1h | Medium |
| 33.5 | Implement GQA | 1.5h | Hard |
| 33.6 | The modern block | 1h | Medium |
| 33.7 | Component ablation | 2h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 33.E1 | Implement sliding window attention and measure the long-context memory saving | 2.5h | High — Mistral's contribution |
| 33.E2 | Implement a minimal mixture-of-experts FFN with top-2 routing | 3h | High — increasingly relevant |
| 33.E3 | Test RoPE scaling methods (linear, NTK) for context extension | 2.5h | High — a live production technique |

## Week 34 — Tokenization and Data Curation

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 34.1 | Exact deduplication by hash | 45m | Easy |
| 34.2 | MinHash + LSH near-duplicate detection | 2.5h | Hard |
| 34.3 | Train/validation contamination check | 1h | Medium |
| 34.4 | Heuristic quality filters | 1.5h | Medium |
| 34.5 | Perplexity filtering | 1.5h | Medium |
| 34.6 | Chunking and packing | 1h | Medium |
| 34.7 | **The quality-vs-scale ablation** | 2.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 34.E1 | Implement substring deduplication with a suffix array | 3h | High — what the deduplication paper actually does |
| 34.E2 | Build a data mixture experiment: vary source weights, measure downstream quality | 3h | High |
| 34.E3 | Curate a database-domain corpus for Month 12's fine-tuning | 2.5h | **Highest** — you will need this dataset in Week 47 |

## Week 35 — Training Small Language Models

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 35.1 | Set up the training run | 1.5h | Medium |
| 35.2 | Train without warmup, deliberately | 45m | Easy |
| 35.3 | The real training run | 3h | Medium |
| 35.4 | `greedy` and observe repetition | 30m | Easy |
| 35.5 | `apply_temperature`, `top_k_filter`, `top_p_filter` | 1.5h | Medium |
| 35.6 | `repetition_penalty` and `min_p_filter` | 1h | Medium |
| 35.7 | `compare_strategies` | 1h | Easy |
| 35.8 | Perplexity evaluation | 1h | Medium |
| 35.9 | `estimate_mfu` | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 35.E1 | A four-point scaling study: loss vs parameters on log axes | 3h | High — previews Month 16 |
| 35.E2 | Measure and improve MFU: find the bottleneck and fix it | 3h | High — real optimization work |
| 35.E3 | Train on your database corpus and evaluate on SQL completion | 3h | High — on-brand, and useful for Month 12 |

## Week 36 — LLM Evaluation Basics

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 36.1 | `perplexity` on your Week 35 model | 45m | Easy |
| 36.2 | `exact_match`, `token_overlap_f1` | 1h | Easy |
| 36.3 | `semantic_similarity` and the negation failure | 1h | Medium |
| 36.4 | `LLMJudge` pointwise scoring | 1.5h | Medium |
| 36.5 | Pairwise comparison with order swapping | 1h | Medium |
| 36.6 | **Validate the judge** | 2h | Hard |
| 36.7 | Measure length bias | 1h | Medium |
| 36.8 | `EvalHarness` with caching | 1.5h | Medium |
| 36.9 | `regression_check` | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 36.E1 | Build a small human-preference dataset and train a reward model | 3h | High — previews Month 12 |
| 36.E2 | Compare three judge models against the same human labels | 2.5h | High — the methodology is the point |
| 36.E3 | Implement G-Eval style chain-of-thought judging and compare agreement | 2h | Medium |

---

## If You Finish Early

Priority: Week 34's database corpus curation (**you need this in Week 47**), Week 35's scaling study (Month 16 preparation), Week 36's multi-judge comparison. Phase 3 ends here — check Gate G3 in `SCORECARD.md` before advancing.
