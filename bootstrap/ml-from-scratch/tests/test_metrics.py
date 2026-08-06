"""Week 6 — classification metrics.

Several tests here encode interview answers, not just correctness. The ROC-AUC
versus PR-AUC pair under imbalance is the one to be able to reproduce verbally.
"""

from __future__ import annotations

import numpy as np
import pytest
from metrics import (
    accuracy,
    average_precision,
    classification_report,
    confusion_matrix,
    f1_score,
    fbeta_score,
    find_optimal_threshold,
    matthews_corrcoef,
    precision,
    precision_recall_curve,
    recall,
    roc_auc,
    roc_curve,
    specificity,
)

pytestmark = pytest.mark.week(6)


@pytest.fixture
def binary():
    y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1])
    y_pred = np.array([0, 0, 1, 1, 0, 1, 1, 1])  # TN=2 FP=2 FN=1 TP=3
    return y_true, y_pred


@pytest.fixture
def imbalanced(rng):
    """1% positive rate — where accuracy stops meaning anything."""
    n = 5000
    y_true = (rng.random(n) < 0.01).astype(int)
    scores = np.clip(rng.normal(loc=0.2 + 0.35 * y_true, scale=0.2, size=n), 0, 1)
    return y_true, scores


class TestConfusionMatrix:
    def test_layout(self, binary):
        cm = confusion_matrix(*binary)
        np.testing.assert_array_equal(cm, np.array([[2, 2], [1, 3]]))

    def test_total_equals_sample_count(self, binary):
        assert confusion_matrix(*binary).sum() == 8

    def test_multiclass_shape(self):
        y_true = np.array([0, 1, 2, 2, 1])
        y_pred = np.array([0, 2, 2, 1, 1])
        assert confusion_matrix(y_true, y_pred).shape == (3, 3)


class TestBasicMetrics:
    def test_known_values(self, binary):
        y_true, y_pred = binary
        assert accuracy(y_true, y_pred) == pytest.approx(5 / 8)
        assert precision(y_true, y_pred) == pytest.approx(3 / 5)
        assert recall(y_true, y_pred) == pytest.approx(3 / 4)
        assert specificity(y_true, y_pred) == pytest.approx(2 / 4)

    def test_f1_is_the_harmonic_mean(self, binary):
        y_true, y_pred = binary
        p, r = precision(y_true, y_pred), recall(y_true, y_pred)
        assert f1_score(y_true, y_pred) == pytest.approx(2 * p * r / (p + r))

    def test_f1_punishes_a_zero_component(self):
        """Harmonic, not arithmetic. Perfect precision with zero recall scores 0."""
        y_true = np.array([1, 1, 1, 0])
        y_pred = np.array([0, 0, 0, 0])
        assert f1_score(y_true, y_pred) == pytest.approx(0.0)

    def test_fbeta_shifts_the_emphasis(self, binary):
        y_true, y_pred = binary
        assert fbeta_score(y_true, y_pred, beta=2.0) > f1_score(y_true, y_pred)
        assert fbeta_score(y_true, y_pred, beta=0.5) < f1_score(y_true, y_pred)

    def test_perfect_prediction(self):
        y = np.array([0, 1, 0, 1])
        assert accuracy(y, y) == pytest.approx(1.0)
        assert f1_score(y, y) == pytest.approx(1.0)

    def test_accuracy_lies_under_imbalance(self, imbalanced):
        """The reason this whole module exists."""
        y_true, _ = imbalanced
        all_negative = np.zeros_like(y_true)
        assert accuracy(y_true, all_negative) > 0.98
        assert f1_score(y_true, all_negative) == pytest.approx(0.0)


class TestROC:
    def test_curve_endpoints(self, rng):
        y_true = rng.integers(0, 2, size=200)
        scores = rng.random(200)
        fpr, tpr, _ = roc_curve(y_true, scores)
        assert fpr[0] == pytest.approx(0.0) and tpr[0] == pytest.approx(0.0)
        assert fpr[-1] == pytest.approx(1.0) and tpr[-1] == pytest.approx(1.0)

    def test_curve_is_monotonic(self, rng):
        y_true = rng.integers(0, 2, size=200)
        fpr, tpr, _ = roc_curve(y_true, rng.random(200))
        assert np.all(np.diff(fpr) >= -1e-12)
        assert np.all(np.diff(tpr) >= -1e-12)

    def test_perfect_separation_scores_one(self):
        y_true = np.array([0, 0, 0, 1, 1, 1])
        assert roc_auc(y_true, np.array([0.1, 0.2, 0.3, 0.7, 0.8, 0.9])) == pytest.approx(1.0)

    def test_random_scores_near_half(self, rng):
        y_true = rng.integers(0, 2, size=20000)
        assert roc_auc(y_true, rng.random(20000)) == pytest.approx(0.5, abs=0.03)

    def test_inverted_scores_give_zero(self):
        y_true = np.array([0, 0, 1, 1])
        assert roc_auc(y_true, np.array([0.9, 0.8, 0.2, 0.1])) == pytest.approx(0.0)

    def test_auc_equals_the_ranking_probability(self, rng):
        """AUC = P(random positive ranked above random negative). Verify it."""
        y_true = rng.integers(0, 2, size=300)
        scores = rng.random(300) + 0.4 * y_true
        pos, neg = scores[y_true == 1], scores[y_true == 0]
        wins = (pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()
        assert roc_auc(y_true, scores) == pytest.approx(wins, abs=1e-6)


class TestPrecisionRecall:
    def test_curve_lengths_agree(self, rng):
        y_true = rng.integers(0, 2, size=100)
        p, r, t = precision_recall_curve(y_true, rng.random(100))
        assert len(p) == len(r) == len(t) + 1

    def test_average_precision_of_a_perfect_ranker(self):
        y_true = np.array([0, 0, 1, 1])
        assert average_precision(y_true, np.array([0.1, 0.2, 0.8, 0.9])) == pytest.approx(1.0)

    def test_random_baseline_equals_the_positive_rate(self, rng):
        """The key contrast with ROC-AUC, whose baseline is always 0.5."""
        y_true = (rng.random(20000) < 0.1).astype(int)
        assert average_precision(y_true, rng.random(20000)) == pytest.approx(0.1, abs=0.02)

    def test_pr_auc_exposes_what_roc_auc_hides(self, imbalanced):
        """The interview answer, demonstrated.

        A mediocre model on 1%-positive data looks respectable by ROC-AUC and
        clearly weak by PR-AUC. That gap is the whole argument.
        """
        y_true, scores = imbalanced
        assert roc_auc(y_true, scores) > 0.75
        assert average_precision(y_true, scores) < 0.4


class TestReportAndMCC:
    def test_report_has_per_class_entries(self, binary):
        report = classification_report(*binary)
        assert "0" in report or 0 in report
        for value in report.values():
            if isinstance(value, dict):
                assert {"precision", "recall", "f1"} <= value.keys()

    def test_mcc_perfect_and_inverted(self):
        y = np.array([0, 1, 0, 1])
        assert matthews_corrcoef(y, y) == pytest.approx(1.0)
        assert matthews_corrcoef(y, 1 - y) == pytest.approx(-1.0)

    def test_mcc_of_a_constant_predictor_is_zero(self, imbalanced):
        y_true, _ = imbalanced
        assert matthews_corrcoef(y_true, np.zeros_like(y_true)) == pytest.approx(0.0, abs=1e-9)


class TestThresholdSelection:
    def test_returns_a_valid_threshold(self, imbalanced):
        y_true, scores = imbalanced
        threshold, score = find_optimal_threshold(y_true, scores, metric="f1")
        assert 0.0 <= threshold <= 1.0
        assert score >= f1_score(y_true, (scores >= 0.5).astype(int))

    def test_asymmetric_costs_move_the_threshold(self, imbalanced):
        """Expensive false negatives should lower the threshold. This is the
        reasoning that separates you from 'we used 0.5'."""
        y_true, scores = imbalanced
        cheap_fn, _ = find_optimal_threshold(y_true, scores, cost_fp=1.0, cost_fn=1.0)
        costly_fn, _ = find_optimal_threshold(y_true, scores, cost_fp=1.0, cost_fn=50.0)
        assert costly_fn < cheap_fn
