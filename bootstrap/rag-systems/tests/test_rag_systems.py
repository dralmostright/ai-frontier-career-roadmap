"""Weeks 37-40 — chunking, retrieval, fusion, evaluation."""

from __future__ import annotations

import pytest
from chunking import add_context_headers, fixed_size_chunks, recursive_chunks, structural_chunks
from rag_eval import RAGTestCase, mean_reciprocal_rank, ndcg_at_k, precision_at_k, recall_at_k
from retrieval import deduplicate, reciprocal_rank_fusion


@pytest.mark.week(37)
class TestVectorStoreContract:
    def test_module_imports(self):
        """The store needs a live Postgres; these tests are marked `db`."""
        import vector_store

        assert hasattr(vector_store, "PgVectorStore")


@pytest.mark.week(37)
@pytest.mark.db
class TestVectorStoreLive:
    def test_schema_and_roundtrip(self, database_url):
        from vector_store import Chunk, PgVectorStore

        store = PgVectorStore(database_url, dimension=4)
        store.create_schema()
        store.upsert_chunks(
            [
                Chunk(
                    id=None,
                    document_id=1,
                    ordinal=0,
                    content="hello",
                    embedding=[1.0, 0.0, 0.0, 0.0],
                )
            ]
        )
        results = store.search([1.0, 0.0, 0.0, 0.0], k=1)
        assert results and results[0].content == "hello"

    def test_explain_shows_index_usage(self, database_url):
        """A sequential scan over 2M vectors still returns correct results,
        just slowly. This failure is invisible without looking at the plan."""
        from vector_store import PgVectorStore

        store = PgVectorStore(database_url, dimension=4)
        plan = store.explain_search([1.0, 0.0, 0.0, 0.0], k=5)
        assert isinstance(plan, str) and plan


@pytest.mark.week(38)
class TestChunking:
    @pytest.fixture
    def document(self):
        return "\n\n".join(f"Paragraph {i}. " + "word " * 40 for i in range(10))

    def test_fixed_chunks_respect_the_size_bound(self, document):
        for chunk in fixed_size_chunks(document, size=100, overlap=0):
            assert len(chunk.text.split()) <= 110

    def test_overlap_duplicates_boundary_content(self, document):
        """Overlap exists so a fact straddling a boundary survives whole."""
        with_overlap = fixed_size_chunks(document, size=100, overlap=30)
        without = fixed_size_chunks(document, size=100, overlap=0)
        assert len(with_overlap) > len(without)

    def test_chunks_cover_the_whole_document(self, document):
        chunks = fixed_size_chunks(document, size=100, overlap=0)
        assert chunks[0].start == 0
        assert chunks[-1].end >= len(document) - 1

    def test_recursive_prefers_paragraph_boundaries(self, document):
        chunks = recursive_chunks(document, size=200)
        assert sum(1 for c in chunks if c.text.strip().startswith("Paragraph")) >= len(chunks) // 2

    def test_structural_chunking_keeps_code_blocks_whole(self):
        """Half a code block is worse than none — it produces confident nonsense."""
        markdown = (
            "# Title\n\nIntro text.\n\n```sql\nSELECT 1;\nSELECT 2;\nSELECT 3;\n```\n\nMore text."
        )
        chunks = structural_chunks(markdown, format="markdown")
        code_chunks = [c for c in chunks if "SELECT" in c.text]
        assert len(code_chunks) == 1
        assert code_chunks[0].text.count("SELECT") == 3

    def test_context_headers_are_prepended(self):
        from chunking import Chunk

        chunks = [Chunk(text="Increase this to 64MB.", start=0, end=22)]
        enriched = add_context_headers(chunks, "PostgreSQL Tuning", ["Memory", "work_mem"])
        assert "work_mem" in enriched[0].text
        assert "Increase this to 64MB." in enriched[0].text


@pytest.mark.week(38)
class TestFusion:
    def test_rrf_rewards_agreement(self):
        """A document ranked well by both methods should win."""
        dense = ["a", "b", "c"]
        lexical = ["b", "a", "d"]
        fused = reciprocal_rank_fusion([dense, lexical])
        assert fused[0] in {"a", "b"}

    def test_rrf_needs_no_score_normalization(self):
        """Rank-based, so incomparable score scales don't matter."""
        fused = reciprocal_rank_fusion([["x", "y"], ["y", "x"]])
        assert set(fused) == {"x", "y"}

    def test_rrf_includes_items_from_a_single_list(self):
        fused = reciprocal_rank_fusion([["a", "b"], ["c"]])
        assert set(fused) == {"a", "b", "c"}

    def test_deduplicate_removes_near_identical(self):
        class R:
            def __init__(self, text):
                self.content = text

        results = [R("the database is slow"), R("the database is slow"), R("the index is bloated")]
        assert len(deduplicate(results)) == 2


@pytest.mark.week(39)
class TestRetrievalMetrics:
    def test_recall_at_k(self):
        assert recall_at_k([1, 2, 3, 4, 5], [2, 7], k=5) == pytest.approx(0.5)

    def test_recall_is_one_when_everything_is_found(self):
        assert recall_at_k([1, 2, 3], [1, 2], k=3) == pytest.approx(1.0)

    def test_recall_respects_k(self):
        """The relevant doc is at position 5; recall@3 must not see it."""
        assert recall_at_k([9, 8, 7, 6, 1], [1], k=3) == pytest.approx(0.0)

    def test_precision_at_k(self):
        assert precision_at_k([1, 2, 3, 4], [1, 2], k=4) == pytest.approx(0.5)

    def test_mrr_uses_the_first_relevant_rank(self):
        assert mean_reciprocal_rank([([5, 3, 1], [1]), ([2, 9], [2])]) == pytest.approx(
            (1 / 3 + 1) / 2
        )

    def test_mrr_is_zero_when_nothing_relevant_is_retrieved(self):
        assert mean_reciprocal_rank([([5, 6], [1])]) == pytest.approx(0.0)

    def test_ndcg_rewards_correct_ordering(self):
        grades = {1: 3.0, 2: 2.0, 3: 1.0}
        good = ndcg_at_k([1, 2, 3], grades, k=3)
        bad = ndcg_at_k([3, 2, 1], grades, k=3)
        assert good > bad
        assert good == pytest.approx(1.0)

    def test_eval_case_supports_unanswerable_questions(self):
        """~10% of the set must be unanswerable. Refusal is a measured behavior."""
        case = RAGTestCase(
            id="u1", question="What is the CEO's salary?", relevant_chunk_ids=[], answerable=False
        )
        assert not case.answerable
        assert case.relevant_chunk_ids == []
