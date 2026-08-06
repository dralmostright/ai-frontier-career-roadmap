"""RAG evaluation — Week 39. The heart of Month 10.

Separate retrieval quality from generation quality. Without that separation
"the answer was wrong" is unactionable; with it you know immediately which
half to fix.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class RAGTestCase:
    """One labeled question.

    Include unanswerable cases — about 10% of the set. The most important
    behavior of a production RAG system is declining to answer when the
    context does not support one, and you cannot measure that without cases
    where the correct answer is "I don't know."
    """

    id: str
    question: str
    relevant_chunk_ids: list[int]
    reference_answer: str | None = None
    answerable: bool = True
    category: str | None = None
    difficulty: str | None = None


# ---------------------------------------------------------------------
# Retrieval metrics
# ---------------------------------------------------------------------


def recall_at_k(retrieved_ids: list[int], relevant_ids: list[int], k: int) -> float:
    """Fraction of relevant chunks appearing in the top k.

    The ceiling on your whole system. If recall@k is 0.6, the generator sees
    no supporting evidence 40% of the time and no prompt engineering will fix
    that. Always measure this first.
    """
    raise NotImplementedError("Week 39")


def precision_at_k(retrieved_ids: list[int], relevant_ids: list[int], k: int) -> float:
    """Fraction of the top k that are relevant.

    Matters more than people think: irrelevant context does not merely waste
    tokens, it actively distracts the model and measurably degrades answers.
    """
    raise NotImplementedError("Week 39")


def mean_reciprocal_rank(results: list[tuple[list[int], list[int]]]) -> float:
    """Average of 1/rank of the first relevant result.

    Use it when there is essentially one right answer. Position matters:
    models attend more to the beginning and end of a long context, so a
    relevant chunk buried at position 8 may as well not be there.
    """
    raise NotImplementedError("Week 39")


def ndcg_at_k(retrieved_ids: list[int], relevance_grades: dict[int, float], k: int) -> float:
    """Normalized discounted cumulative gain, for graded relevance.

    Use when relevance is not binary — some chunks are perfect, some partially
    useful. More faithful than recall when your labels support it.
    """
    raise NotImplementedError("Week 39")


# ---------------------------------------------------------------------
# Generation metrics
# ---------------------------------------------------------------------


def faithfulness(answer: str, context: list[str], judge: Any = None) -> dict[str, Any]:
    """Is every claim in the answer supported by the retrieved context?

    **The most important metric in the module.** An unfaithful answer is a
    hallucination, and hallucination is the failure mode that makes people
    distrust the whole system.

    Implementation: decompose the answer into atomic claims, then check each
    against the context. Report the fraction supported, and return the
    unsupported claims — those are your error analysis, and reading twenty of
    them teaches you more than any aggregate number.
    """
    raise NotImplementedError("Week 39")


def answer_relevance(question: str, answer: str, judge: Any = None) -> float:
    """Does the answer address the question that was asked?

    Distinct from faithfulness. An answer can be perfectly grounded in the
    context and completely fail to answer the question — a common and
    under-measured failure.
    """
    raise NotImplementedError("Week 39")


def context_relevance(question: str, context: list[str], judge: Any = None) -> float:
    """What fraction of the retrieved context was actually needed?

    Low scores mean you are retrieving too much. Retrieving too much costs
    tokens, adds latency, and degrades answer quality through distraction.
    """
    raise NotImplementedError("Week 39")


def citation_accuracy(
    answer: str, citations: list[int], context: dict[int, str]
) -> dict[str, float]:
    """Do the cited chunks actually support the sentences citing them?

    Citations are the feature that makes RAG trustworthy, and a wrong citation
    is worse than none — it manufactures confidence. Measure it explicitly.
    """
    raise NotImplementedError("Week 39")


def refusal_correctness(cases: list[RAGTestCase], answers: list[str]) -> dict[str, float]:
    """Does it decline on unanswerable questions and answer the rest?

    Report both error directions: answering when it should refuse
    (hallucination), and refusing when it should answer (over-caution). Tuning
    one always moves the other, and showing you understand that tradeoff is
    the point.
    """
    raise NotImplementedError("Week 39")


# ---------------------------------------------------------------------
# The harness
# ---------------------------------------------------------------------


class RAGEvaluator:
    """Run the full suite and produce the report.

    Requirements:

    - Cache LLM judge calls by content hash. You will re-run this constantly.
    - Report per-category and per-difficulty breakdowns, not just aggregates.
    - Bootstrap confidence intervals on every number, from Week 11's module.
    - Track cost and latency per query.
    - Emit a markdown report suitable for pasting into the capstone README.
    """

    def __init__(self, cases: list[RAGTestCase], cache_dir: Path | None = None) -> None:
        raise NotImplementedError("Week 39")

    def evaluate(self, rag_pipeline: Any) -> Any:
        raise NotImplementedError("Week 39")

    def compare_configurations(self, pipelines: dict[str, Any]) -> Any:
        """Head-to-head across configurations, with a paired significance test.

        The Week 38 chunking comparison lives here. "Recursive chunking at 512
        tokens beat fixed 256 by 4 points of recall@5, p < 0.01" is a finding.
        "Recursive seemed better" is not.
        """
        raise NotImplementedError("Week 39")

    def error_analysis(self, results: Any, n: int = 20) -> Any:
        """The worst failures, with retrieval and generation diagnosed separately.

        Bucket each failure: retrieval miss (the answer was never retrieved),
        ranking failure (retrieved but buried), or generation failure
        (retrieved, ranked well, answered badly). Those three buckets have
        three completely different fixes, and this table tells you which one
        you have.
        """
        raise NotImplementedError("Week 39")


def build_eval_set_from_documents(
    documents: list[str], n_questions: int = 200, model: Any = None
) -> list[RAGTestCase]:
    """Bootstrap an eval set by generating questions from known chunks.

    Faster than writing 200 by hand, and the ground truth is free because you
    know which chunk generated each question.

    **Review every generated question by hand anyway.** Generated questions
    skew easy and often paraphrase the source chunk so closely that retrieval
    is trivial. Use generation for a first draft, then edit hard. Say this
    openly in your README — acknowledging the limitation of your own method is
    a credibility signal, not a weakness.
    """
    raise NotImplementedError("Week 39")
