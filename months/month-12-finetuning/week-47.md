# Week 47: Instruction Datasets and Data Quality

## Outcome

By Sunday you have a hand-curated instruction dataset for database diagnostics, with every example reviewed, quality-scored, and documented in a dataset card.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The dataset is the month's real deliverable.** A great dataset with a mediocre
training run beats a mediocre dataset with a perfect one, and the LIMA result —
that a thousand carefully-curated examples can outperform far larger noisy sets —
is the evidence.

This is also where Month 11 compounds. Your benchmark scenarios, your diagnosis
outputs, your query plan explanations, and your curated database corpus from
Week 34 all feed this. You are not starting from nothing; you are converting
domain work into training data.

The discipline that matters: review every example by hand. Generated instruction
data carries the generator's errors and its stylistic tics, and training on it
teaches the model to imitate both. Reviewing a thousand examples takes hours and
it is the difference between a dataset and a pile.

The dataset card is not paperwork. Provenance, licensing, construction method,
known biases, and intended use are what let someone else — including future you —
trust the artifact.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **What makes instruction data good**
   1. Diversity of task type, phrasing, and difficulty
   2. Consistency of output format
   3. Correctness — obviously, and it is the thing generated data lacks
   4. The LIMA finding: quality over quantity
2. **Construction methods**
   1. Hand-writing: highest quality, slowest
   2. Templating from structured data: consistent, risks being formulaic
   3. Model generation with human review: the practical middle
   4. Distillation from a stronger model, and its licensing questions
3. **Quality scoring**
   1. Heuristic filters: length, format compliance, duplication
   2. Model-based scoring
   3. Human review, and why it does not scale but must happen anyway
4. **Format**
   1. Chat templates and why they matter
   2. System, user, assistant turns
   3. Loss masking on the completion only
   4. Consistency between training format and inference format
5. **Documentation**
   1. The dataset card: provenance, construction, size, licensing, biases, intended use
   2. Why the biases section is the one that builds trust

## Required Free Resources

- **Primary:** 'LIMA: Less Is More for Alignment' — https://arxiv.org/abs/2305.11206
- **Primary:** 'Self-Instruct' — https://arxiv.org/abs/2212.10560 — the generation-with-review method
- 'Datasheets for Datasets' (Gebru et al.) — https://arxiv.org/abs/1803.09010 — the dataset card standard
- Hugging Face chat templating — https://huggingface.co/docs/transformers/chat_templating
- The Dolly and OpenAssistant dataset construction writeups — good accounts of doing this at scale

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=47
```

1. **Define the task taxonomy** (1h) — Plan explanation, index recommendation, incident triage, config review, query rewriting. Aim for six to eight types.
2. **Hand-write 50 gold examples** (3h) — Across all task types. These set the standard for everything else.
3. **Template from Month 11's benchmark** (2h) — Your scenarios, diagnoses, and plan explanations are training data.
4. **Generate and review 500 more** (3h) — Generate with a strong model, **review every one**. Expect to reject 20-30%.
5. **Quality scoring and filtering** (1.5h) — Heuristic plus model-based. Inspect what each filter removes.
6. **Deduplication** (1h) — Week 34's tooling. Near-duplicates in instruction data cause memorization.
7. **Format with a chat template** (1h) — Consistent with your inference format. Mismatches are a common silent bug.
8. **Held-out split by task type** (45m) — Stratified, so every task type appears in evaluation.
9. ****The dataset card**** (1.5h) — Provenance, method, size, licensing, biases, intended use, limitations.

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
l
l
m
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
i
n
s
t
r
u
c
t
i
o
n
_
d
a
t
a
.
p
y


d
a
t
a
/
d
b
a
_
i
n
s
t
r
u
c
t
i
o
n
s
/
```

## Tests To Write

Add: a test that every example conforms to the chat template schema; a test that no near-duplicates exist within the set or across the train/held-out split; and a test that every task type appears in both splits.

## Portfolio Artifact

The dataset and its card. **This is the month's most valuable artifact** — it is domain expertise converted into a reusable asset, and it is not something someone without your background could produce.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *A thousand excellent examples or a hundred thousand mediocre ones?* Answer with the LIMA reasoning and your own scaling ablation if you ran it. Then: *How do you assess instruction data quality?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run the data-scaling ablation: fine-tune on 100, 300, and 1000 examples and plot quality against dataset size. This is your own version of the LIMA finding, on your own domain. If quality saturates early — as it often does with high-quality data — that is a genuinely useful result and a strong claim to be able to make with your own evidence.
