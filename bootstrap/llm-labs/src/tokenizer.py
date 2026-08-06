"""Tokenization — Week 25.

Byte-pair encoding from scratch. Start from bytes, repeatedly merge the most
frequent adjacent pair, stop at the target vocabulary size.

Tokenization explains a surprising share of LLM behavior, and being able to
connect the two is a good interview signal:

- **Arithmetic is unreliable** partly because numbers tokenize inconsistently
  — "1234" might be one token while "1235" is two.
- **Reversing a string is hard** because the model sees tokens, not
  characters, and has no direct access to the letters inside a token.
- **Non-English text costs more** because tokenizers trained mostly on
  English fragment other scripts into many more tokens per word.
- **Trailing whitespace breaks completions** because " the" and "the" are
  different tokens and the model has strong priors about which follows what.
"""

from __future__ import annotations

from pathlib import Path


class BPETokenizer:
    """Byte-level BPE.

    Byte-level, not character-level. Starting from the 256 possible bytes
    means the vocabulary can represent *any* input — no unknown token, ever.
    That property is why GPT-2 and everything after it works this way.
    """

    def __init__(self, vocab_size: int = 8192, special_tokens: list[str] | None = None) -> None:
        raise NotImplementedError("Week 25")

    def train(self, corpus: list[str], verbose: bool = True) -> BPETokenizer:
        """Learn merges from a corpus.

        The naive implementation recounts every pair after every merge and is
        O(merges x corpus). Cache pair counts and update only the affected
        positions. On a modest corpus the difference is minutes versus hours,
        and doing the optimization yourself is the most instructive part of
        the week.
        """
        raise NotImplementedError("Week 25")

    def encode(self, text: str) -> list[int]:
        raise NotImplementedError("Week 25")

    def decode(self, ids: list[int]) -> str:
        """Decode must round-trip exactly, including whitespace and unicode.

        Test with emoji, accented characters, and text ending in a space.
        Round-trip failures are usually a byte/str confusion, and they produce
        training data that is subtly corrupted.
        """
        raise NotImplementedError("Week 25")

    def save(self, path: Path) -> None:
        raise NotImplementedError("Week 25")

    @classmethod
    def load(cls, path: Path) -> BPETokenizer:
        raise NotImplementedError("Week 25")


def compression_ratio(tokenizer: BPETokenizer, text: str) -> dict[str, float]:
    """Characters per token, and bytes per token.

    English on a well-trained tokenizer runs about 4 characters per token.
    Code runs lower, non-English much lower. Measure it on several text types
    and put the table in your Week 25 write-up — it makes the multilingual
    cost disparity concrete.
    """
    raise NotImplementedError("Week 25")


def tokenization_pathologies(tokenizer: BPETokenizer) -> dict[str, list]:
    """Demonstrate the known failure modes on your own tokenizer.

    Number splitting, trailing whitespace, unicode fragmentation, and
    repeated-character handling. Each one connects a tokenizer property to an
    observable LLM behavior, which is exactly the kind of concrete detail that
    makes an interview answer memorable.
    """
    raise NotImplementedError("Week 25")
