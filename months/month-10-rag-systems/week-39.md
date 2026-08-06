# Week 39: RAG Evaluation

## Outcome

By Sunday you have a 200-question labeled evaluation set and a harness that measures retrieval quality, generation faithfulness, citation accuracy, and refusal correctness — all with confidence intervals.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The week that makes this project different from every other RAG portfolio
piece.**

The core discipline is separating retrieval metrics from generation metrics.
"The answer was wrong" is unactionable. "recall@5 was 0.94 but faithfulness was
0.61, so retrieval is fine and generation is inventing content" tells you exactly
what to fix.

Faithfulness is the metric that matters most, because an unfaithful answer is a
hallucination and hallucination is what makes people distrust the system. Measure
it by decomposing answers into atomic claims and checking each against the
context — and return the unsupported claims, because reading twenty of them
teaches you more than the aggregate score.

The unanswerable questions matter too. The most important behavior of a
production RAG system is declining when the context does not support an answer,
and you cannot measure that without cases where "I don't know" is correct.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 6.5 hours
- Project: 5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Separating the layers**
   1. Retrieval metrics cap generation metrics
   2. The three failure buckets: retrieval miss, ranking failure, generation failure
   3. Why each has a different fix
2. **Retrieval metrics**
   1. recall@k as the ceiling
   2. precision@k, and why irrelevant context actively hurts
   3. MRR and nDCG
3. **Generation metrics**
   1. Faithfulness: is every claim supported by the context?
   2. Answer relevance: does it address the question?
   3. Context relevance: how much of what you retrieved was needed?
   4. Citation accuracy
4. **Refusal**
   1. Unanswerable questions in the eval set
   2. Both error directions: hallucinating and over-refusing
   3. The tradeoff curve
5. **Building the set**
   1. Hand-labeling versus generation
   2. Why generated questions skew easy
   3. Category and difficulty tags
   4. Versioning the eval set like code

## Required Free Resources

- **Primary:** RAGAS documentation — https://docs.ragas.io/ — read the metric definitions, then implement your own
- **Primary:** Hamel Husain on evals — https://hamel.dev/blog/posts/evals/ — reread with RAG in mind
- 'ARES: An Automated Evaluation Framework for RAG' — https://arxiv.org/abs/2311.09476
- Anthropic, 'Building effective agents' — https://www.anthropic.com/engineering/building-effective-agents — the evaluation section applies here too

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=39
```

1. **Design the eval set schema** (45m) — Question, relevant chunks, reference answer, answerable flag, category, difficulty.
2. **`build_eval_set_from_documents`** (1.5h) — Generate a first draft, then edit every one by hand.
3. ****Hand-label 200 questions**** (4h) — Including 20 unanswerable. Tedious. This is the asset.
4. **`recall_at_k`, `precision_at_k`, `mean_reciprocal_rank`, `ndcg_at_k`** (1.5h) — From Week 28, formalized.
5. **`faithfulness`** (2h) — Decompose into claims, check each. Return the unsupported ones.
6. **`answer_relevance`, `context_relevance`** (1h) — Distinct from faithfulness.
7. **`citation_accuracy`** (1h) — A wrong citation is worse than none.
8. **`refusal_correctness`** (1h) — Both error directions.
9. **`RAGEvaluator` with caching and CIs** (1.5h) — Content-hash caching; bootstrap CIs from Week 11.
10. **`error_analysis`** (1.5h) — The three-bucket taxonomy. Read twenty failures individually.

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
r
a
g
-
s
y
s
t
e
m
s
/
s
r
c
/
r
a
g
_
e
v
a
l
.
p
y


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
r
a
g
-
s
y
s
t
e
m
s
/
e
v
a
l
s
/
q
u
e
s
t
i
o
n
s
.
j
s
o
n
l
```

## Tests To Write

Week-39 blocks. Add: a test that faithfulness scores a fabricated answer below 0.3 and a fully-grounded answer above 0.9, on hand-constructed examples.

## Portfolio Artifact

`src/rag_eval.py` and the 200-question labeled set. **The eval set is the more valuable artifact** — models get replaced, a good eval set stays useful for years.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (35 min).** Recorded: *Design an evaluation harness for a RAG system.* Cover: separating retrieval from generation, the metric list, unanswerable questions, judge validation, CIs, and per-category breakdown. Six minutes, structured. This is a question you should now answer better than most working engineers.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Validate your faithfulness judge properly: hand-label 50 answer/context pairs as faithful or not, run your judge, and compute Cohen's kappa. Report the agreement in the capstone README. Below 0.6 means your faithfulness numbers are not measuring what you think, and finding that out is far better than not knowing.
