# Month 08 Capstone: Mini-GPT

## Objective

Implement a complete GPT-style transformer from first principles, train it to generate coherent text, and produce an ablation study measuring what each architectural component contributes.

## Business Problem

None, and that is fine. This is the credibility artifact.

Its job is to make everything else you claim about LLMs believable. A reviewer
who sees a from-scratch transformer with a real ablation table reads your later
RAG and agent work as built on understanding rather than API calls.

## Technical Requirements

- Complete implementation: tokenizer (Week 25), embeddings, positional encoding,
  multi-head causal attention, FFN, residuals, pre-norm, weight tying
- Every component gradient-checked
- Trained on a small corpus to coherent generation
- KV caching with a measured speedup
- Sampling: greedy, temperature, top-k, top-p
- **The ablation study**: seven configurations, same seed, same steps
- Attention visualizations from trained weights
- The parameter breakdown by component
- A README explaining every architectural choice and what breaks without it

## Theory Requirements

The README must explain, in your own words:

1. Attention, derived, including why √d.
2. Why multi-head, and why the output projection is required.
3. Why pre-norm, with the residual-stream argument.
4. KV caching, with the memory formula and a worked example.
5. What each ablation showed, and any result that surprised you.

## System Design Requirements

- Config-driven (Month 5's system, reused)
- Model code separate from training code separate from generation code
- Checkpointing and resume
- The ablation runner as a script, not a notebook — it must be re-runnable

## Implementation Plan

**Days 1-2** — Assemble and verify. Initial loss must be ln(V) before anything
else.

**Day 3** — Train to coherent generation.

**Day 4** — KV caching, and measure the speedup.

**Days 5-6** — The ablation study. Seven runs, controlled. This is the deliverable.

**Day 7** — Visualizations, README, publish.

## Evaluation Plan

| Check | Target |
| ----- | ------ |
| Initial loss | ln(vocab_size), verified by a test |
| Validation loss | Converges; report the curve |
| Generation | Coherent at the character or word level for the corpus size |
| Every gradient checked | Relative error < 1e-5 |
| KV cache | Identical output, measured speedup reported |
| Ablation study | All seven configurations, same seed, table reported |
| Reproducibility | Same loss curve on a re-run |

## Expected Repository Structure

```text
mini-gpt-from-scratch/
  README.md
  pyproject.toml
  Makefile
  configs/
    tiny.yaml
    ablations/*.yaml
  src/mini_gpt/
    tokenizer.py
    attention.py
    block.py
    model.py
    train.py
    generate.py
    ablate.py
  tests/
  notebooks/
    01_attention_derivation.ipynb
    02_training.ipynb
    03_attention_visualization.ipynb
    04_ablation_results.ipynb
  docs/
    architecture.md      every component, explained
    ablations.md         the table and the analysis
    limitations.md
```

## README Requirements

Above the fold: one sentence, a generated text sample, and **the ablation table**.

Then: the architecture with a diagram; each component explained with what breaks
without it; the derivation of attention including √d; the training curve; KV
caching with the memory formula and the measured speedup; attention
visualizations; the parameter breakdown; limitations.

**The ablation table is the headline.** Put it above the fold. It is the thing
that distinguishes this from the thousands of other from-scratch GPT
repositories, all of which stop at "it generates text."

Sample table:

| Configuration | Val loss | Δ | What broke |
| ------------- | -------- | - | ---------- |
| Full model | 1.82 | — | baseline |
| No positional encoding | 2.94 | +1.12 | word order lost; output is a bag of words |
| No residual connections | 5.81 | +3.99 | stopped improving after epoch 2 |
| No layer norm | 3.40 | +1.58 | unstable; two of five seeds diverged |
| Post-norm | 2.10 | +0.28 | trainable but needed warmup |
| Single head | 2.31 | +0.49 | one attention pattern instead of six |
| No causal mask | 0.04 | -1.78 | **reads the answer; learns nothing** |
| No √d scaling | 3.15 | +1.33 | softmax saturated; gradients vanished |

## Demo Requirements

`make demo` loads a trained checkpoint and generates 200 tokens from a prompt, then prints the attention heatmap for the first layer.

## Blog Post Requirement

**Post #2 is due this month.** Working title: "Every Component of a Transformer,
and What Breaks Without It."

This is the highest-distribution post in the whole plan. From-scratch transformer
tutorials are everywhere; a measured ablation table showing exactly what each
piece contributes is not. Lead with the table.

## Interview Story

> "I can derive and implement every line of a transformer, and I ran the
> ablations to find out what each part actually does. Removing residual
> connections took validation loss from 1.8 to 5.8. Removing the causal mask
> dropped it to 0.04, because the model just reads ahead. Ask me about any
> component and I'll tell you what breaks without it."

45 seconds, and it invites exactly the follow-up you want.

## Rubric

Score with `coach/capstone_review_rubric.md`. Month 8 targets:

| Dimension | Target | Note |
| --- | --- | --- |
| Problem framing | 7 | Credibility artifact. Frame it as such, honestly. |
| Technical execution | 9 | **Every component correct and gradient-checked.** |
| Evaluation rigor | 9 | **The ablation study.** Controlled, seeded, reported. |
| Code quality | 8 | Clean separation, config-driven. |
| Documentation | 9 | The architecture document is the artifact. |
| Reproducibility | 9 | Month 5's pipeline, reused. |
| Error analysis | 7 | The ablations serve this role. |
| Portfolio readiness | 9 | **Flagship #5.** Feature it. |

**Overall target: 8.5+. This is a flagship — aim for 9.**

## Stretch Goals

1. **A scaling study**: four model sizes, loss against parameters, on log axes.
   Previews Month 9 and Month 16.
2. **Speculative decoding** with a draft model.
3. **Attention pattern taxonomy**: classify the heads in your trained model —
   previous-token, delimiter, induction. Genuine interpretability work.
4. **Train on SQL** and see whether it learns valid syntax. On-brand, and the
   failure modes are interesting.

## Limitations To State Honestly

- Roughly 10M parameters, trained on a small corpus. It generates locally
  coherent text and nothing more.
- No RoPE, RMSNorm, SwiGLU, or GQA — those are Week 33.
- Naive attention: O(n²) memory, no FlashAttention.
- Single GPU, no distributed training.
- Ablations run at one model size and one seed per configuration for most rows;
  the ones marked with variance were run with five.
