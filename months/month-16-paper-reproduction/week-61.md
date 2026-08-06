# Week 61: Paper Reading Method

## Outcome

By Sunday you have a repeatable three-pass reading method and five completed summaries, each identifying the paper's weakest claim.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Reading papers efficiently is a learnable skill and most people never learn it.
Reading linearly wastes hours on related work and proofs you do not need.

The three-pass method: five minutes for the claim, thirty for the method and
evidence, two-plus hours only for papers you are reproducing. Most papers stop at
pass one, and that is the correct outcome.

The section that builds research taste is "what I'd question." Every paper has a
weak point — an unfair baseline, a missing ablation, a cherry-picked benchmark, an
unreported failure. Finding it is what separates reading from absorbing, and it is
directly examined: "what did this paper get wrong?" is a standard question and a
candidate who says "nothing, it's a great paper" has revealed something.

The 90-second summary is the interview drill. Practice it.

## Time Budget: 15-20 Hours

- Theory: 6 hours
- Coding: 3.5 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The three-pass method**
   1. Pass 1 (5 min): title, abstract, figures, conclusion. Do I care?
   2. Pass 2 (30 min): intro, method, results. Skip related work and proofs.
   3. Pass 3 (2h+): everything, with intent to reimplement. Rare.
2. **Reading critically**
   1. Is the baseline fair, or deliberately weak?
   2. Is the benchmark the right one, or the one they win on?
   3. Are the ablations complete, or do they stop where it gets awkward?
   4. Are failures reported?
   5. How many seeds? Are error bars present?
3. **Finding the literature**
   1. arXiv listings, Papers with Code, Semantic Scholar
   2. Following citations forward and backward
   3. Reading the critiques and replications, not just the paper
4. **Keeping notes**
   1. The summary template
   2. Why writing the method in your own words is the test of understanding
   3. Building a searchable personal index

## Required Free Resources

- **Primary:** 'How to Read a Paper' (S. Keshav) — the three-pass method, two pages. Read it first.
- **Primary:** Andrew Ng's advice on reading research papers (CS230 lecture) — practical and specific
- arXiv cs.CL and cs.LG — https://arxiv.org/list/cs.CL/recent
- Papers with Code — https://paperswithcode.com/ — for implementations and reported results
- Semantic Scholar — https://www.semanticscholar.org/ — for citation graphs

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=61
```

1. **Read 'How to Read a Paper'** (30m) — Two pages. Then use the method for everything below.
2. **Pass 1 on ten papers** (1.5h) — Five minutes each. Decide which five deserve pass 2.
3. **Pass 2 on five papers** (3h) — Fill in the template for each. Include the weakness section.
4. **Write the method in your own words** (1h) — For each. If you cannot without re-reading, you have not understood it.
5. **Identify the weakest claim** (1h) — For each paper. Be specific.
6. **Find a critique or replication** (1h) — For at least two of the five. Compare your criticism against the published one.
7. **Practice the 90-second summary** (1h) — Out loud, timed, for each. Record one.
8. **Choose the reproduction target** (1h) — Something whose claim you can test in under 8 GPU-hours.

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
e
s
e
a
r
c
h
-
r
e
p
r
o
d
u
c
t
i
o
n
/
p
a
p
e
r
s
/
```

## Tests To Write

No code tests. The test is the 90-second summary, delivered from memory.

## Portfolio Artifact

Five paper summaries in `papers/`, each with a stated weakness. Publish them; a well-organized set of critical paper notes is unusual and useful.

## Interview Drills

**Coding (45 min).** Two problems. Month 18 is close; keep the reps up.

**Research (30 min).** Recorded: *Summarize a paper you read this week in 90 seconds.* Claim, method, evidence, weakness. Then: *What would you have done differently?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Read the OpenReview discussion for a paper you summarized and compare the reviewers' criticisms against your own. This calibrates your critical reading directly — you will find some criticisms you missed and, encouragingly, some you found that the reviewers did not. It is the fastest way to develop research taste.
