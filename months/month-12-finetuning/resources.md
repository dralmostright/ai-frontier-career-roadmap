# Month 12 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**'LoRA'** (Week 46) — https://arxiv.org/abs/2106.09685
Short and directly examined. Read it fully; you will be asked to derive the
parameter count.

**'LIMA: Less Is More for Alignment'** (Week 47) — https://arxiv.org/abs/2305.11206
The evidence behind the data-quality argument, and the basis for your Week 47
scaling ablation.

**'Direct Preference Optimization'** (Week 48) — https://arxiv.org/abs/2305.18290
Sections 1-4. The three-sentence answer comes from here.

**Sebastian Raschka's LoRA articles** — the best practical guidance, with
experiments rather than assertions.

---

## Week 45 — Fine-Tuning Fundamentals

- **Primary:** Hugging Face fine-tuning guide — https://huggingface.co/docs/transformers/training
- **Primary:** 'Training language models to follow instructions' (InstructGPT) — https://arxiv.org/abs/2203.02155 — the SFT sections
- Sebastian Raschka's fine-tuning articles — consistently the clearest practical writing on this
- 'LIMA: Less Is More for Alignment' — https://arxiv.org/abs/2305.11206 — the data-quality argument, with evidence
- Anthropic, 'Prompt engineering vs fine-tuning' guidance in the Claude docs — https://docs.claude.com/
## Week 46 — LoRA and QLoRA

- **Primary:** 'LoRA' — https://arxiv.org/abs/2106.09685 — read it fully; it is short and directly examined
- **Primary:** 'QLoRA' — https://arxiv.org/abs/2305.14314 — read the NF4 section carefully
- PEFT documentation — https://huggingface.co/docs/peft/index — use after implementing yours
- Sebastian Raschka, 'Practical Tips for Finetuning LLMs Using LoRA' — the empirical guidance, with experiments
- Unsloth — https://github.com/unslothai/unsloth — makes QLoRA practical on modest hardware
## Week 47 — Instruction Datasets and Data Quality

- **Primary:** 'LIMA: Less Is More for Alignment' — https://arxiv.org/abs/2305.11206
- **Primary:** 'Self-Instruct' — https://arxiv.org/abs/2212.10560 — the generation-with-review method
- 'Datasheets for Datasets' (Gebru et al.) — https://arxiv.org/abs/1803.09010 — the dataset card standard
- Hugging Face chat templating — https://huggingface.co/docs/transformers/chat_templating
- The Dolly and OpenAssistant dataset construction writeups — good accounts of doing this at scale
## Week 48 — Evaluation and Model Comparison

- **Primary:** 'Direct Preference Optimization' — https://arxiv.org/abs/2305.18290 — read sections 1-4
- **Primary:** 'Constitutional AI' — https://arxiv.org/abs/2212.08073 — read for the AI-feedback idea
- TRL documentation — https://huggingface.co/docs/trl/index — DPO implementation
- 'Model Cards for Model Reporting' — https://arxiv.org/abs/1810.03993
- Anthropic's model cards — https://www.anthropic.com/ — read one as a format reference

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| pgvector | https://github.com/pgvector/pgvector | Months 10-11 |
| FastAPI | https://fastapi.tiangolo.com/ | Serving |
| Claude API | https://docs.claude.com/ | Months 10-12 |
| Hugging Face PEFT | https://huggingface.co/docs/peft/index | Month 12 |
| pytest | https://docs.pytest.org/ | The workspace |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| bitsandbytes | https://github.com/bitsandbytes-foundation/bitsandbytes | QLoRA |
| TRL | https://huggingface.co/docs/trl/index | DPO |
| Unsloth | https://github.com/unslothai/unsloth | Makes QLoRA practical on modest hardware |

---

## Deliberately Omitted

- **Full RLHF with PPO.** Understand it conceptually; DPO is the practical
  modern choice and implementing PPO for language models is a research project.
- **Distillation.** Worth knowing as a technique. Week 31's stretch touched it.
- **Continued pretraining at scale.** Out of compute budget and out of scope.
- **Constitutional AI implementation.** Read the paper. The implementation is
  substantial research.
