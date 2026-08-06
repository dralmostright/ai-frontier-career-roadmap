"""LLM evaluation — Week 36, extended in Weeks 39, 44, and 48.

The hardest unsolved problem in applied LLM work, and the skill that most
distinguishes a serious engineer from someone who ships demos.

The core difficulty: for most generative tasks there is no single correct
output, so there is no ground truth to compare against. Everything here is a
strategy for making progress despite that.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class EvalCase:
    """One test case. Version these, review them, and treat them as code.

    Your eval set is a more valuable asset than your model. Models get
    replaced every few months; a well-curated eval set stays useful for years
    and is what lets you switch models safely.
    """

    id: str
    input: str
    expected: str | None = None
    rubric: str | None = None
    tags: list[str] | None = None
    metadata: dict[str, Any] | None = None


def perplexity(model: Any, dataset: Any, device: str = "cpu") -> dict[str, float]:
    """Perplexity on held-out text.

    The caveat to always state: perplexity is tokenizer-dependent, so two
    models with different vocabularies are not comparable on it. This bites
    in Week 62 when you try to match a paper's number and cannot.
    """
    raise NotImplementedError("Week 36")


def exact_match(predictions: list[str], references: list[str], normalize: bool = True) -> float:
    """Strict string match after normalization.

    Brittle, and useful precisely because it is brittle: for extraction and
    classification tasks where there *is* a right answer, exact match is
    honest in a way that fuzzy metrics are not.
    """
    raise NotImplementedError("Week 36")


def token_overlap_f1(predictions: list[str], references: list[str]) -> float:
    """Token-level F1. Partial credit for partially-correct answers."""
    raise NotImplementedError("Week 36")


def semantic_similarity(
    predictions: list[str], references: list[str], model: Any = None
) -> list[float]:
    """Embedding cosine similarity.

    Better than string overlap, and it has a specific failure mode worth
    knowing: negation. "The database is healthy" and "The database is not
    healthy" embed close together and score high. Never use this as your only
    metric for anything where correctness flips on a negation.
    """
    raise NotImplementedError("Week 36")


class LLMJudge:
    """Use a strong model to score another model's outputs.

    The standard approach for open-ended tasks, and it carries documented
    biases you must control for and be able to name:

    - **Position bias.** The first option in a pairwise comparison wins more
      often. Mitigate by running both orderings and averaging.
    - **Length bias.** Longer answers score higher regardless of quality.
      Control by reporting length alongside score.
    - **Self-preference.** Models rate their own family's outputs higher. Use
      a different model family as judge where you can.
    - **Rubric sensitivity.** Small prompt changes move scores materially.
      Version your rubric like code and re-baseline when it changes.

    Validate the judge before trusting it: hand-label 50 examples, measure
    agreement with the judge, and report that agreement number. A judge you
    have not validated is a random number generator with good manners.
    """

    def __init__(
        self, model: str = "claude-sonnet-5", rubric: str = "", temperature: float = 0.0
    ) -> None:
        raise NotImplementedError("Week 36")

    def score(self, case: EvalCase, output: str) -> dict[str, Any]:
        raise NotImplementedError("Week 36")

    def compare(
        self, case: EvalCase, output_a: str, output_b: str, swap: bool = True
    ) -> dict[str, Any]:
        """Pairwise comparison, run in both orderings to cancel position bias."""
        raise NotImplementedError("Week 36")

    def validate_against_humans(self, labeled: list[dict]) -> dict[str, float]:
        """Agreement between judge and human labels.

        Report Cohen's kappa, not raw agreement — raw agreement looks great on
        a skewed label distribution. Below 0.6 means the judge is not
        measuring what you think it is.
        """
        raise NotImplementedError("Week 36")


class EvalHarness:
    """Run a suite, aggregate, and compare against a baseline.

    Requirements that make it useful rather than decorative:

    - **Cache by (model, prompt, params) hash.** You will re-run the same eval
      dozens of times; paying for it dozens of times is a choice.
    - **Track cost and tokens per run.** You need this for Week 51's report
      anyway, and retrofitting instrumentation is worse than building it in.
    - **Report per-tag breakdowns.** The aggregate hides that you are at 95%
      on easy cases and 40% on the hard ones that motivated the project.
    - **Bootstrap confidence intervals.** From `ml-from-scratch/evaluation.py`.
      Same discipline, new domain.
    """

    def __init__(self, cases: list[EvalCase], cache_dir: Path | None = None) -> None:
        raise NotImplementedError("Week 36")

    def run(self, model_fn: Any, metrics: list[str] | None = None) -> Any:
        raise NotImplementedError("Week 36")

    def compare_models(self, model_fns: dict[str, Any]) -> Any:
        """Head-to-head on the same cases, with a paired significance test."""
        raise NotImplementedError("Week 36")

    def regression_check(self, baseline: Path, threshold: float = 0.02) -> dict[str, Any]:
        """Fail if quality dropped by more than `threshold` against a baseline.

        This is what you wire into CI in Week 55. An eval gate that blocks a
        regressing PR is the single most valuable piece of ML infrastructure
        most teams do not have.
        """
        raise NotImplementedError("Week 36")
