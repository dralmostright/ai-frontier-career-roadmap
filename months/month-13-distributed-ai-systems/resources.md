# Month 13 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**'Transformer Inference Arithmetic'** (Week 49) — https://kipp.ly/transformer-inference-arithmetic/
The single best resource for the memory and throughput reasoning. Read it twice.

**'Making Deep Learning Go Brrrr From First Principles'** (Weeks 49, 52) — https://horace.io/brrr_intro.html
The compute/memory/overhead framing that makes profiling systematic.

**'ZeRO'** (Week 50) — https://arxiv.org/abs/1910.02054
Sections 1-5. Your answer to the stage question comes from here.

**Ray patterns and anti-patterns** (Week 51) — https://docs.ray.io/en/latest/ray-core/patterns/index.html
Short, and it prevents the common mistakes.

---

## Week 49 — GPU and CUDA Basics

- **Primary:** 'Transformer Inference Arithmetic' (Kipply) — https://kipp.ly/transformer-inference-arithmetic/ — the single best resource for this week
- **Primary:** 'Making Deep Learning Go Brrrr From First Principles' (Horace He) — https://horace.io/brrr_intro.html — the compute/memory/overhead framing
- NVIDIA, 'Matrix Multiplication Background User's Guide' — https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/
- 'Mixed Precision Training' — https://arxiv.org/abs/1710.03740
- '8-bit Optimizers via Block-wise Quantization' — https://arxiv.org/abs/2110.02861
## Week 50 — Distributed Training Concepts

- **Primary:** 'ZeRO: Memory Optimizations Toward Training Trillion Parameter Models' — https://arxiv.org/abs/1910.02054 — read sections 1-5
- **Primary:** Hugging Face, 'Model Parallelism' guide — https://huggingface.co/docs/transformers/perf_train_gpu_many — the clearest practical taxonomy
- 'Megatron-LM' — https://arxiv.org/abs/1909.08053 — tensor parallelism
- 'GPipe' — https://arxiv.org/abs/1811.06965 — pipeline parallelism and the bubble
- PyTorch FSDP tutorial — https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html — ZeRO-3 in PyTorch
- The OPT-175B training logbook — https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/ — read some of it. Large-scale training is mostly incident response.
## Week 51 — Ray for AI Workloads

- **Primary:** Ray Core documentation — https://docs.ray.io/en/latest/ray-core/walkthrough.html
- **Primary:** Ray Data — https://docs.ray.io/en/latest/data/data.html — the right abstraction for batch evaluation
- Ray patterns and anti-patterns — https://docs.ray.io/en/latest/ray-core/patterns/index.html — read this properly
- 'Ray: A Distributed Framework for Emerging AI Applications' — https://arxiv.org/abs/1712.05889
## Week 52 — Performance Profiling

- **Primary:** PyTorch profiler recipe — https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html
- **Primary:** 'Efficient Memory Management for LLM Serving' (vLLM) — https://arxiv.org/abs/2309.06180
- Horace He, 'Making Deep Learning Go Brrrr' — https://horace.io/brrr_intro.html — reread with profiling in mind
- vLLM documentation — https://docs.vllm.ai/
- 'LLM.int8()' — https://arxiv.org/abs/2208.07339 — the quantization paper

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| Ray | https://docs.ray.io/ | Month 13 |
| MLflow | https://mlflow.org/docs/latest/ | Month 14 |
| Kubernetes | https://kubernetes.io/docs/home/ | Month 15 |
| Prometheus | https://prometheus.io/docs/ | Months 14-15 |
| Google SRE Book | https://sre.google/sre-book/table-of-contents/ | Months 14-15 |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| vLLM | https://docs.vllm.ai/ | Week 52 |
| torch.profiler | https://pytorch.org/docs/stable/profiler.html | Weeks 49, 52 |
| bitsandbytes | https://github.com/bitsandbytes-foundation/bitsandbytes | Quantization |

---

## Deliberately Omitted

- **Writing production CUDA kernels.** Week 49's stretch touches Triton. Kernel
  engineering is a specialization and it is not what these roles screen for.
- **Actually training a large model.** Out of budget, and the arithmetic is what
  gets asked, not the experience.
- **Cluster orchestration (Slurm, Kubeflow).** Month 15 covers Kubernetes.
- **Networking hardware (InfiniBand, NVLink topology).** Know that interconnect
  bandwidth is often binding; the hardware detail is not asked.
