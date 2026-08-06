# Month 05 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**PyTorch autograd mechanics** (Week 17) — https://pytorch.org/docs/stable/notes/autograd.html
Read properly, not skimmed. It answers most of the questions people get wrong.

**PyTorch reproducibility notes** (Week 20) — https://pytorch.org/docs/stable/notes/randomness.html
The authoritative list of what to control. Your Week 20 answer comes from here.

**Karpathy, 'A Recipe for Training Neural Networks'** — https://karpathy.github.io/2019/04/25/recipe/
Second reading. It lands differently now that you have written the framework.

---

## Week 17 — PyTorch Tensors and Autograd

- **Primary:** PyTorch 60-minute blitz — https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- **Primary:** PyTorch autograd mechanics — https://pytorch.org/docs/stable/notes/autograd.html — read this properly, not skimmed
- d2l.ai ch. 2 (preliminaries) — https://d2l.ai/
- PyTorch broadcasting semantics — https://pytorch.org/docs/stable/notes/broadcasting.html
## Week 18 — Modules, Datasets, DataLoaders

- **Primary:** PyTorch data loading tutorial — https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
- **Primary:** PyTorch performance tuning guide — https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html — read the data loading section carefully
- d2l.ai ch. 6 (builders' guide) — https://d2l.ai/
- 'PyTorch DataLoader num_workers' discussions — the practical folklore is genuinely useful here
## Week 19 — Training Loops and Debugging

- **Primary:** PyTorch AMP recipe — https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html
- **Primary:** Karpathy, 'A Recipe for Training Neural Networks' — https://karpathy.github.io/2019/04/25/recipe/ — second reading
- PyTorch saving and loading — https://pytorch.org/tutorials/beginner/saving_loading_models.html
- 'Mixed Precision Training' (Micikevicius et al., 2017) — https://arxiv.org/abs/1710.03740
## Week 20 — Experiment Tracking and Reproducibility

- **Primary:** PyTorch reproducibility notes — https://pytorch.org/docs/stable/notes/randomness.html — the authoritative list
- **Primary:** MLflow tracking docs — https://mlflow.org/docs/latest/tracking.html
- Pydantic settings — https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- 'Reproducibility in Machine Learning' — read one of the several good posts on this; the common thread is that seeds are necessary and insufficient

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| PyTorch | https://pytorch.org/docs/stable/ | Months 5+ |
| d2l.ai | https://d2l.ai/ | The primary DL textbook for Phase 2-3 |
| Hugging Face | https://huggingface.co/docs | Months 7+ |
| pytest | https://docs.pytest.org/ | The workspace |
| NeetCode 150 | https://neetcode.io/practice | Weekly coding drills |
| MLflow | https://mlflow.org/docs/latest/ | Week 20 and Month 14 |
| Pydantic | https://docs.pydantic.dev/ | Config validation |
| Typer | https://typer.tiangolo.com/ | CLI |

---

## Deliberately Omitted

- **PyTorch Lightning / Fastai.** Excellent, and they hide exactly what you are
  trying to learn. Use them after this month if you like.
- **Distributed training.** Deferred to Month 13 where it is the subject.
- **`torch.compile` internals.** Use it as a tool; the compiler is a rabbit hole.
- **Custom CUDA kernels.** Week 49 covers the concepts; writing kernels is a
  specialization.
