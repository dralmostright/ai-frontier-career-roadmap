# Week 36: LLM Evaluation Basics

## Outcome

By Sunday you can evaluate generated text with task metrics and rubric-based judging, and — crucially — you have validated your judge against human labels and reported the agreement.

## Why This Matters For OpenAI/Anthropic-Level Interviews

**The bridge from Phase 3 to Phase 4**, and the skill that most distinguishes a
serious LLM engineer.

The central difficulty: for most generative tasks there is no single correct
output, so there is no ground truth to compare against. Every technique here is a
strategy for making progress despite that.

LLM-as-judge is the standard approach and it carries documented biases —
position, length, self-preference, rubric sensitivity — that you must be able to
name and control for. The most important discipline: **validate the judge**. Hand-
label 50 examples, measure agreement with Cohen's kappa, and report it. A judge
you have not validated is a random number generator with good manners.

Everything in Months 10-17 depends on this week. Week 39's RAG evaluation,
Week 44's agent benchmark, and Week 68's research all inherit the methodology.

## Time Budget: 15-20 Hours

- Theory: 3.5 hours
- Coding: 7 hours
- Project: 4 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The evaluation problem**
   1. No single correct output for most generative tasks
   2. Why perplexity does not measure usefulness
   3. Why human evaluation is the gold standard and impractical at scale
2. **Reference-based metrics**
   1. Exact match: brittle, and honest for extraction tasks
   2. Token F1: partial credit
   3. BLEU and ROUGE, and their known weaknesses
   4. Embedding similarity, and the negation failure
3. **LLM-as-judge**
   1. Pointwise scoring versus pairwise comparison
   2. **Position bias**, and swapping to cancel it
   3. **Length bias**: longer answers score higher regardless of quality
   4. **Self-preference**: models favor their own family
   5. Rubric sensitivity, and versioning the rubric like code
4. **Validating the judge**
   1. Hand-label a sample
   2. Cohen's kappa, not raw agreement
   3. What agreement level is usable
   4. Reporting the agreement alongside the scores
5. **Harness design**
   1. Caching by content hash
   2. Cost and token tracking
   3. Per-tag breakdowns
   4. Confidence intervals, from Week 11
   5. Regression gating against a baseline

## Required Free Resources

- **Primary:** 'Judging LLM-as-a-Judge' (Zheng et al.) — https://arxiv.org/abs/2306.05685 — the paper that catalogued the biases. Read it properly.
- **Primary:** Hamel Husain, 'Your AI product needs evals' — https://hamel.dev/blog/posts/evals/ — the most practical writing on this topic anywhere
- 'Holistic Evaluation of Language Models' (HELM) — https://arxiv.org/abs/2211.09110 — read the methodology section
- Eugene Yan's writing on LLM evaluation patterns — consistently good
- RAGAS documentation — https://docs.ragas.io/ — preview of Week 39

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=36
```

1. **`perplexity` on your Week 35 model** (45m) — State the tokenizer caveat.
2. **`exact_match`, `token_overlap_f1`** (1h) — With normalization. Know when each is honest.
3. **`semantic_similarity` and the negation failure** (1h) — Demonstrate it. It is the reason not to rely on this metric alone.
4. **`LLMJudge` pointwise scoring** (1.5h) — With a versioned rubric.
5. **Pairwise comparison with order swapping** (1h) — Measure the position bias before and after swapping.
6. ****Validate the judge**** (2h) — Hand-label 50 examples. Compute Cohen's kappa. Report it.
7. **Measure length bias** (1h) — Score short and long answers of equal quality. The bias is usually large.
8. **`EvalHarness` with caching** (1.5h) — Content-hash caching. You will re-run this constantly.
9. **`regression_check`** (1h) — Fail on a quality drop against a baseline. Wired into CI in Week 55.

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
e
v
a
l
_
h
a
r
n
e
s
s
.
p
y
```

## Tests To Write

Add: a test that pairwise judging with order swapping produces a smaller position-bias measurement than without; and a test that the cache prevents duplicate API calls for identical inputs.

## Portfolio Artifact

The Month 9 capstone report. See `capstone.md`.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *How do you evaluate an LLM when there is no ground truth?* Name the judge biases and how you control for each. Then: *How do you know your judge is any good?* The kappa answer is the one that lands.

**Quarterly (60 min).** **Q3 mock interview.** Transformer deep dive plus coding, 45 minutes, recorded. This is the quarter where your DL depth score should jump.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Compare three different judge models — a large one, a small one, and one from a different family — against the same 50 hand-labeled examples. Report agreement for each. The finding is usually that a smaller model agrees nearly as well for a fraction of the cost, which is a practical, money-saving result and a good demonstration that you validate rather than assume.
