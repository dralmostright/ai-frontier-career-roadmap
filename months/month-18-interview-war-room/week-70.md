# Week 70: Coding Sprint 2

## Outcome

By Sunday you handle tree and graph problems fluently and can attempt a DP problem with a structured approach rather than pattern-matching.

## Why This Matters For OpenAI/Anthropic-Level Interviews

These are the categories that will feel least natural. Database work exercises
set operations and query optimization; it does not exercise recursive tree
traversal or DP state definition.

Trees and graphs are the priority — they appear more often than DP and they are
more learnable in a week. For DP, the realistic goal is a structured approach:
identify the state, write the recurrence, memoize, then optionally convert to
tabulation. Being able to get to a working memoized solution is usually enough.

Also from this week: the AI-flavored coding problems in `INTERVIEW_PREP.md`.
Implementing attention or top-k sampling in an interview is increasingly common
at labs and you should be fast at it.

## Time Budget: 15-20 Hours

- Theory: 0 hours
- Coding: 13 hours
- Project: 0 hours
- Interview practice: 5 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Trees**
   1. DFS variants and when each applies
   2. BFS and level-order
   3. BST properties
   4. Recursive versus iterative
2. **Graphs**
   1. Representations and their tradeoffs
   2. BFS for shortest path in unweighted graphs
   3. DFS for cycles and connectivity
   4. Topological sort
   5. Union-find
3. **Heaps**
   1. Top-k, merge-k, running median
4. **Dynamic programming**
   1. Identify the state, write the recurrence, memoize, then tabulate
   2. The common patterns: knapsack, LCS, edit distance, coin change
   3. Why getting to memoization is usually sufficient
5. **AI-flavored problems**
   1. Attention in NumPy
   2. Top-k and nucleus sampling
   3. BPE training
   4. Batching variable-length sequences
   5. Vector similarity search

## Required Free Resources

- **Primary:** NeetCode 150, trees, graphs, heap, 1-D and 2-D DP — https://neetcode.io/practice
- **Primary:** `INTERVIEW_PREP.md` AI-flavored problem list
- 'Grokking Dynamic Programming' patterns, or any structured DP pattern list

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=70
```

1. **Trees: 12 problems** (3h) — Timed. Both recursive and iterative where applicable.
2. **Graphs: 12 problems** (3.5h) — BFS, DFS, topological sort, union-find.
3. **Heaps: 6 problems** (1.5h) — Top-k patterns.
4. **DP: 10 problems** (3h) — State, recurrence, memoize. Tabulation optional.
5. ****AI-flavored: 5 problems**** (2h) — Attention, sampling, BPE, batching, similarity search. You should be fast at these.
6. ****Five recorded solves**** (2h) — Mixed categories. Watch them back.

## Bootstrap Files To Create

```text
c
o
a
c
h
/
i
n
t
e
r
v
i
e
w
s
/
c
o
d
i
n
g
_
l
o
g
.
m
d
```

## Tests To Write

The log. Compare Week 70's times against Week 69's.

## Portfolio Artifact

The completed log across both weeks, with your weakest categories identified.

## Interview Drills

**Timed set (2h).** Four problems, mixed categories, back to back.

**Recorded solve (30 min).** One graph problem and one AI-flavored problem.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Time yourself on the five AI-flavored problems and get each under fifteen minutes. Implementing scaled dot-product attention or nucleus sampling cleanly and quickly is a home advantage — you have written all of these — and being visibly fast at them signals depth in a way a LeetCode medium does not.
