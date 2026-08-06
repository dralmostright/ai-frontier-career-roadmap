# Week 25: Text Preprocessing and Tokenization

## Outcome

By Sunday you have trained a byte-level BPE tokenizer from scratch that round-trips any input exactly, and you can connect tokenizer properties to observed LLM failures.

## Why This Matters For OpenAI/Anthropic-Level Interviews

Tokenization is the least glamorous and most explanatory topic in LLM
engineering. "Why does GPT struggle with arithmetic?" has a real answer — numbers
tokenize inconsistently, so "1234" might be one token and "1235" two — and giving
that answer instead of "language models aren't good at math" is a clear
differentiator.

Byte-level is the key design choice: starting from the 256 possible bytes means
the vocabulary can represent *any* input, so there is no unknown token, ever.
That property is why GPT-2 and everything after it works this way.

The efficiency exercise matters too. The naive BPE trainer recounts every pair
after every merge; caching and incremental updates turn hours into minutes, and
doing that optimization is the most instructive part of the week.

## Time Budget: 15-20 Hours

- Theory: 3 hours
- Coding: 8 hours
- Project: 3 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Why tokenization exists**
   1. Character-level: long sequences, weak units
   2. Word-level: unbounded vocabulary, unknown tokens
   3. Subword: the compromise
2. **Byte-pair encoding**
   1. Start from bytes, merge the most frequent adjacent pair, repeat
   2. Why byte-level means no unknown token, ever
   3. The merge table and how encoding applies it
3. **Alternatives**
   1. WordPiece (BERT), and the likelihood-based merge criterion
   2. SentencePiece and Unigram
   3. Why GPT-family models use byte-level BPE
4. **Behavioral consequences**
   1. Arithmetic: inconsistent number splitting
   2. Reversal: the model sees tokens, not characters
   3. Multilingual cost: more tokens per word for under-represented scripts
   4. Trailing whitespace: ' the' and 'the' are different tokens
5. **Practical concerns**
   1. Special tokens and their reservation
   2. Compression ratio by content type
   3. Vocabulary size as a tradeoff

## Required Free Resources

- **Primary:** Karpathy, 'Let's build the GPT Tokenizer' — https://www.youtube.com/watch?v=zduSFxRajkE — two hours, and it is the definitive treatment. Watch, then build your own.
- **Primary:** Hugging Face NLP course, tokenizers chapter — https://huggingface.co/learn/nlp-course/chapter6/1
- 'Neural Machine Translation of Rare Words with Subword Units' (Sennrich et al.) — https://arxiv.org/abs/1508.07909 — the original BPE paper
- tiktoken source — https://github.com/openai/tiktoken — read after building yours

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=25
```

1. **Byte-level encoding and decoding** (1h) — Round-trip must be exact for emoji, accents, and whitespace.
2. **Naive BPE training** (1.5h) — Get it correct. Time it on a small corpus.
3. **Optimized BPE training** (2h) — Cache pair counts, update incrementally. Time it again.
4. **`encode` applying the merge table** (1.5h) — Greedy longest-match by merge order.
5. **`save` / `load`** (45m) — Round-trip the tokenizer itself.
6. **`compression_ratio`** (45m) — English, code, and a non-Latin script. The table is the deliverable.
7. **`tokenization_pathologies`** (1h) — Demonstrate each failure on your own tokenizer.
8. **Compare against tiktoken** (45m) — Same text, both tokenizers. Explain the differences.

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
t
o
k
e
n
i
z
e
r
.
p
y
```

## Tests To Write

`tests/test_llm_labs.py` week-25 blocks. The round-trip tests are the important ones.

## Portfolio Artifact

`src/tokenizer.py` and a notebook with the compression table by content type and the pathology demonstrations.

## Interview Drills

**Coding (45 min).** Two problems, strings — thematically apt.

**ML theory (25 min).** Recorded: *Why does tokenization break arithmetic?* Then: *Why is non-English text more expensive to process?* Both answers should reference your own measurements.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Analyze how your tokenizer handles SQL and `EXPLAIN` output, and compare against tiktoken. Query plans have distinctive structure — repeated keywords, numbers, indentation — and knowing how they tokenize matters for Month 11's context budget. This is a small, specific piece of domain analysis that nobody else will have done.
