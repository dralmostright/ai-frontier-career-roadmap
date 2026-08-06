# Capstone Review Rubric

Score every capstone on eight dimensions. This rubric is deliberately harsh —
it is calibrated against what a frontier lab reviewer would think, not against
what feels like a good effort.

**Pass:** ≥ 7.0 average, with no single dimension below 5.
**Portfolio-grade:** ≥ 8.0 average, with Documentation and Evaluation both ≥ 8.
**Flagship-grade:** ≥ 9.0 average. Only Months 8, 10, 11, 12, 13, 14, 15, 17 need this.

---

## 1. Problem Framing — /10

Does the project answer a question worth asking, and is that clear immediately?

| Score | Standard |
| ----- | -------- |
| 2 | No stated problem. It's a demo of a technology. |
| 4 | Problem stated but generic ("build a chatbot"). |
| 6 | Specific problem with a stated user and a reason it's hard. |
| 8 | Above, plus explicit scope boundaries and non-goals. |
| 10 | Above, plus a stated hypothesis or success criterion defined *before* building. |

**Check:** can a reader state the problem in one sentence after 15 seconds on the
README? If not, cap at 5.

---

## 2. Technical Execution — /10

Does it work, and is the approach sound?

| Score | Standard |
| ----- | -------- |
| 2 | Doesn't run, or only runs on your machine with undocumented state. |
| 4 | Works on the happy path. Breaks on anything unexpected. |
| 6 | Works reliably. Handles common failure cases. Reasonable architecture. |
| 8 | Above, plus deliberate technical choices with rejected alternatives documented. |
| 10 | Above, plus a non-obvious engineering decision that materially improved the result, with the evidence. |

**Check:** is there at least one place where you did something harder than the
tutorial approach because the tutorial approach didn't work? If not, cap at 6.

---

## 3. Evaluation Rigor — /10

The dimension most portfolios fail. Also the one that most distinguishes you.

| Score | Standard |
| ----- | -------- |
| 0 | No evaluation. "It seems to work." |
| 2 | Anecdotal examples only. |
| 4 | A metric, computed once, with no baseline. |
| 6 | A metric with a baseline comparison and a defined test set. |
| 8 | Multiple metrics, a real baseline, a held-out set, and stated methodology. |
| 10 | Above, plus per-category breakdown, uncertainty quantification (CI or multiple seeds), and an explanation of what the metric fails to capture. |

**Check:** can you state a single number that summarizes how good this is, and
say what it's compared against? If not, cap at 4.

**Check:** is your eval set separate from anything you tuned on? If not, cap at 5
regardless of how good the number looks.

---

## 4. Code Quality — /10

| Score | Standard |
| ----- | -------- |
| 2 | One long script or notebook. No structure. |
| 4 | Some functions. Inconsistent style. Dead code present. |
| 6 | Modular, `src/` layout, type hints, meaningful names, no dead code. |
| 8 | Above, plus tests covering the core logic, linting configured, config externalized. |
| 10 | Above, plus code you would happily submit for review at a company you respect. |

**Check:** run `ruff check` and `mypy`. Any output? Deduct.

**Check:** is there a notebook doing work that belongs in `src/`? Deduct 2.

---

## 5. Documentation — /10

| Score | Standard |
| ----- | -------- |
| 2 | No README, or a stub. |
| 4 | README says what it is. No setup instructions or results. |
| 6 | Problem, approach, setup, and results all present and accurate. |
| 8 | Above, plus an architecture diagram, key technical decisions, and limitations. |
| 10 | Above, plus a reader with no context could understand the whole system in ten minutes and reproduce it in thirty. |

**Check:** does the README have a results table above the fold? If not, cap at 6.

**Check:** does the diagram exist? For anything with 3+ components, no diagram
caps this at 6.

---

## 6. Reproducibility — /10

| Score | Standard |
| ----- | -------- |
| 2 | Undocumented dependencies. Hardcoded paths. |
| 4 | `requirements.txt` exists but is incomplete or unpinned. |
| 6 | Pinned dependencies, documented setup, seeds set. |
| 8 | `make setup && make test && make demo` works from a clean clone. |
| 10 | Above, plus containerized, plus results reproduce numerically across machines. |

**Test this for real.** Clone into a fresh directory (or container), follow only
the README, and time yourself. Whatever breaks is the score.

---

## 7. Error Analysis — /10

What separates senior work from competent work.

| Score | Standard |
| ----- | -------- |
| 0 | None. |
| 2 | "It sometimes gets things wrong." |
| 4 | A few example failures shown. |
| 6 | Failures categorized into named buckets with counts. |
| 8 | Above, plus root-cause analysis for the top two categories. |
| 10 | Above, plus a change made in response to the analysis, with the before/after measurement. |

**Check:** can you name the top three failure modes and their approximate
frequency? If not, cap at 4.

---

## 8. Portfolio Readiness — /10

Would you put this in front of a hiring manager?

| Score | Standard |
| ----- | -------- |
| 2 | No. Embarrassing. |
| 4 | Only with an apology and an explanation. |
| 6 | Yes, as supporting evidence of breadth. |
| 8 | Yes, and it would come up in the interview positively. |
| 10 | This is a reason someone would want to interview you. |

**Check:** does it have a demo (GIF, video, or hosted)? No demo caps at 7.

**Check:** does it differentiate you, or could 500 other candidates show the same
thing? Undifferentiated caps at 6.

---

## Scoring Sheet

```text
Project:  _______________________________
Month:    __
Date:     ____-__-__

1. Problem framing        __ /10
2. Technical execution    __ /10
3. Evaluation rigor       __ /10
4. Code quality           __ /10
5. Documentation          __ /10
6. Reproducibility        __ /10
7. Error analysis         __ /10
8. Portfolio readiness    __ /10
--------------------------------
   Average                __ /10

Verdict:  [ ] Fail (<7)   [ ] Pass (7-8)   [ ] Portfolio (8-9)   [ ] Flagship (9+)
```

---

## Required Actions By Verdict

**Fail (< 7.0, or any dimension < 5)**
Do not move on to the next capstone until fixed. Identify the two lowest
dimensions and allocate a focused week. Re-score. Most failures are Evaluation
Rigor and Documentation, and both are fixable in under ten hours.

**Pass (7.0 - 7.9)**
Publish it. Note the weakest dimension and target it in the next capstone. Do not
feature this project in your portfolio's top three.

**Portfolio (8.0 - 8.9)**
Publish it, write the blog post, and add it to the profile README.

**Flagship (9.0+)**
Publish it, write the blog post, record a demo, draw the architecture diagram,
pin the repo, and build an interview story around it. Then leave it alone —
resist the urge to keep polishing at the expense of the next month.

---

## Self-Deception Checklist

Before finalizing any score, answer these:

1. Did I score Evaluation Rigor above 6 without a real held-out test set? *(Then
   it's not above 6.)*
2. Did I test the setup instructions on a clean environment, or did I assume?
   *(Assumed = cap Reproducibility at 5.)*
3. Am I scoring the effort I put in, or the artifact that exists? *(Score the
   artifact. Effort is invisible to reviewers.)*
4. Would I be comfortable if the interviewer had read every line of this repo
   before the call? *(If not, Code Quality is lower than I scored it.)*
5. Is there a number in the README? *(If not, this is not a Pass yet.)*
