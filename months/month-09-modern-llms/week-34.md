# Week 34: Tokenization and Data Curation

## Outcome

By Sunday you have a data preparation pipeline with deduplication, quality filtering, and packing — and evidence from your own ablation that data quality beats parameter count.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The most underrated week of Phase 3.

The claim "data quality beats model scale" is repeated constantly and rarely
demonstrated. You are going to demonstrate it: train the same architecture on a
deduplicated, filtered corpus and on a raw one of the same token count, and
report the difference. Then train a larger model on the raw data and show it
still loses.

That ablation is a genuinely strong portfolio item because it is a claim you
verified rather than repeated.

Deduplication specifically matters more than people expect. Near-duplicates in
the training set inflate validation performance (the model has seen the answer)
and encourage memorization over generalization. Detecting them at scale — MinHash
and LSH — is a nice engineering exercise that connects to your data background.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Why data quality dominates**
   1. The scaling laws assume a fixed data distribution
   2. What Chinchilla actually said about the compute-optimal ratio
   3. Evidence from the open-model literature
2. **Deduplication**
   1. Exact duplicates via hashing
   2. Near-duplicates via MinHash and LSH
   3. Why train/validation contamination inflates every number
   4. Substring deduplication and suffix arrays
3. **Quality filtering**
   1. Heuristic filters: length, symbol ratio, repetition
   2. Perplexity filtering with a reference model
   3. Classifier-based filtering
   4. The risk: filtering toward a narrow distribution
4. **Preparation**
   1. Chunking to the context length
   2. Packing multiple documents per sequence, and the document separator
   3. Why packing matters for throughput
   4. Train/validation splits that avoid contamination
5. **Data mixtures**
   1. Weighting sources
   2. Why repeating high-quality data can beat adding low-quality data
   3. Curriculum ordering, and the mixed evidence for it

## Required Free Resources

- **Primary:** 'The RefinedWeb Dataset' — https://arxiv.org/abs/2306.01116 — the clearest account of a real curation pipeline
- **Primary:** 'Deduplicating Training Data Makes Language Models Better' — https://arxiv.org/abs/2107.06499
- 'Training Compute-Optimal Large Language Models' (Chinchilla) — https://arxiv.org/abs/2203.15556
- 'The Pile' — https://arxiv.org/abs/2101.00027 — a well-documented dataset construction
- Hugging Face datatrove — https://github.com/huggingface/datatrove — a production curation toolkit worth reading

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=34
```

1. **Exact deduplication by hash** (45m) — On a real corpus. Report the duplicate rate; it will surprise you.
2. **MinHash + LSH near-duplicate detection** (2.5h) — The engineering exercise of the week.
3. **Train/validation contamination check** (1h) — Near-duplicates across the split. This is Week 10's lesson, at corpus scale.
4. **Heuristic quality filters** (1.5h) — Length, symbol ratio, repetition, language ID. Inspect what each removes.
5. **Perplexity filtering** (1.5h) — Score with a small reference model, drop the tail. Inspect both ends.
6. **Chunking and packing** (1h) — With document separators. Measure the padding waste avoided.
7. ****The quality-vs-scale ablation**** (2.5h) — Same tokens, curated vs raw. Then a bigger model on raw. The week's deliverable.

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
d
a
t
a
_
c
u
r
a
t
i
o
n
.
p
y
```

## Tests To Write

Add: a test that MinHash detects planted near-duplicates (a document with 10% of words changed) while leaving genuinely distinct documents alone; and a test that packing produces sequences of exactly the context length with correct separators.

## Portfolio Artifact

`src/data_curation.py` and the quality-versus-scale ablation table. That table is the artifact.

## Interview Drills

**Coding (45 min).** Two problems, hashing — thematically apt.

**ML theory (25 min).** Recorded: *Would you rather have 10x more data or a 10x bigger model?* Answer with your own ablation numbers, not with citations. Then: *Why does deduplication matter so much?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Curate a database-domain corpus now: PostgreSQL documentation, mailing list archives, Stack Overflow database questions, your own runbooks. Deduplicate it, filter it, and document the pipeline. You need this dataset in Week 47 for the instruction-tuning work, and building it now while the curation tooling is fresh saves a difficult week later.
