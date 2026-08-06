"""Weeks 66-68 — experiment discipline and analysis."""

from __future__ import annotations

import pytest
from analysis import aggregate_across_seeds, multiple_comparison_correction, significance_test
from experiment import ExperimentSpec, RunResult


@pytest.mark.week(66)
class TestExperimentSpec:
    def test_requires_a_falsifier(self):
        """Pre-registration: state what would change your mind, before running."""
        spec = ExperimentSpec(
            name="lora-rank",
            hypothesis="quality saturates above rank 16",
            falsifier="quality continues improving linearly through rank 64",
            independent_variable="rank",
            levels=[1, 2, 4, 8, 16, 32, 64],
            control_variables={"lr": 1e-4, "epochs": 3},
            metrics=["eval_loss"],
            baselines=["full_finetune"],
        )
        assert spec.falsifier
        assert spec.baselines

    def test_defaults_to_multiple_seeds(self):
        """A single run is noise, not a result."""
        spec = ExperimentSpec(
            name="x",
            hypothesis="h",
            falsifier="f",
            independent_variable="v",
            levels=[1],
            control_variables={},
            metrics=["loss"],
            baselines=["base"],
        )
        assert len(spec.seeds) >= 3


@pytest.mark.week(68)
class TestAnalysis:
    @pytest.fixture
    def results(self, rng):
        rows = []
        for level in [8, 16]:
            for seed in range(5):
                loss = 2.0 - 0.3 * (level == 16) + rng.normal(scale=0.05)
                rows.append(
                    RunResult(
                        spec_name="s",
                        level=level,
                        seed=seed,
                        metrics={"loss": loss},
                        duration_s=1.0,
                        config={},
                    )
                )
        return rows

    def test_aggregation_reports_variance(self, results):
        table = aggregate_across_seeds(results, "loss")
        assert "std" in table.columns
        assert "ci_lower" in table.columns and "ci_upper" in table.columns

    def test_significance_detects_a_real_difference(self, results):
        result = significance_test(results, condition_a=8, condition_b=16, metric="loss")
        assert result["p_value"] < 0.05
        assert "effect_size" in result

    def test_significance_reports_effect_size_not_just_p(self, results):
        """A significant 0.2% improvement is not an interesting result."""
        assert "effect_size" in significance_test(results, 8, 16, "loss")

    def test_holm_correction_is_conservative(self):
        raw = [0.01, 0.02, 0.03, 0.04]
        corrected = multiple_comparison_correction(raw, method="holm")
        assert all(c >= r for c, r in zip(corrected, raw, strict=True))

    def test_correction_reduces_false_positives(self, rng):
        """Twenty tests at p<0.05 yields one false positive by chance."""
        null_p_values = list(rng.uniform(size=20))
        corrected = multiple_comparison_correction(null_p_values, method="holm")
        assert sum(p < 0.05 for p in corrected) <= sum(p < 0.05 for p in null_p_values)
