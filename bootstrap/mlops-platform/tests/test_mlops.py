"""Weeks 53-56 — registry, monitoring, drift."""

from __future__ import annotations

import pytest
from drift import DriftDetector, kolmogorov_smirnov_test, population_stability_index
from registry import ModelRegistry


@pytest.mark.week(54)
class TestRegistry:
    @pytest.fixture
    def registry(self, tmp_path):
        return ModelRegistry(backend="local", uri=tmp_path)

    def test_register_assigns_incrementing_versions(self, registry, tmp_path):
        artifact = tmp_path / "model.pt"
        artifact.write_bytes(b"weights")
        first = registry.register("classifier", artifact, {"accuracy": 0.9})
        second = registry.register("classifier", artifact, {"accuracy": 0.91})
        assert second.version == first.version + 1

    def test_promotion_requires_a_passing_eval(self, registry, tmp_path):
        """No exceptions. Not even once."""
        artifact = tmp_path / "model.pt"
        artifact.write_bytes(b"weights")
        version = registry.register("classifier", artifact, {"accuracy": 0.9})
        with pytest.raises(ValueError):
            registry.promote(
                "classifier", version.version, "production", actor="me", reason="looks fine"
            )

    def test_only_one_production_version_at_a_time(self, registry, tmp_path):
        artifact = tmp_path / "model.pt"
        artifact.write_bytes(b"weights")
        for i in range(2):
            v = registry.register(
                "classifier", artifact, {"accuracy": 0.9 + i / 100}, eval_run_id=f"eval-{i}"
            )
            registry.promote("classifier", v.version, "production", actor="me", reason="ship")
        production = [v for v in registry.list_versions("classifier") if v.stage == "production"]
        assert len(production) == 1

    def test_rollback_restores_the_previous_version(self, registry, tmp_path):
        """The 2am path. Test it on a schedule, not only when you need it."""
        artifact = tmp_path / "model.pt"
        artifact.write_bytes(b"weights")
        good = registry.register("classifier", artifact, {"accuracy": 0.92}, eval_run_id="e1")
        registry.promote("classifier", good.version, "production", actor="me", reason="ship")
        bad = registry.register("classifier", artifact, {"accuracy": 0.71}, eval_run_id="e2")
        registry.promote("classifier", bad.version, "production", actor="me", reason="ship")

        restored = registry.rollback("classifier", actor="oncall", reason="quality regression")
        assert restored.version == good.version
        assert registry.get_production("classifier").version == good.version

    def test_version_records_code_and_data_provenance(self, registry, tmp_path):
        """Weights alone are not a version. Rolling back weights without code
        can produce a model that no longer matches its serving path."""
        artifact = tmp_path / "model.pt"
        artifact.write_bytes(b"weights")
        v = registry.register(
            "classifier", artifact, {"accuracy": 0.9}, git_sha="abc123", dataset_version="v3"
        )
        lineage = registry.lineage("classifier", v.version)
        assert lineage["git_sha"] == "abc123"
        assert lineage["dataset_version"] == "v3"

    def test_dirty_git_tree_is_recorded(self, registry, tmp_path):
        """A checkpoint from uncommitted code is not reproducible. Say so."""
        artifact = tmp_path / "model.pt"
        artifact.write_bytes(b"weights")
        v = registry.register("classifier", artifact, {"accuracy": 0.9}, git_dirty=True)
        assert v.git_dirty is True


@pytest.mark.week(56)
class TestDrift:
    def test_psi_is_near_zero_for_identical_distributions(self, rng):
        sample = rng.normal(size=10_000)
        assert population_stability_index(sample, sample.copy()) < 0.01

    def test_psi_detects_a_mean_shift(self, rng):
        baseline = rng.normal(loc=0.0, size=10_000)
        shifted = rng.normal(loc=1.5, size=10_000)
        assert population_stability_index(baseline, shifted) > 0.25

    def test_psi_detects_a_variance_shift(self, rng):
        baseline = rng.normal(scale=1.0, size=10_000)
        wider = rng.normal(scale=3.0, size=10_000)
        assert population_stability_index(baseline, wider) > 0.1

    def test_psi_is_symmetric_enough_to_be_usable(self, rng):
        a = rng.normal(loc=0.0, size=10_000)
        b = rng.normal(loc=1.0, size=10_000)
        assert population_stability_index(a, b) == pytest.approx(
            population_stability_index(b, a), rel=0.3
        )

    def test_ks_test_returns_statistic_and_p_value(self, rng):
        result = kolmogorov_smirnov_test(rng.normal(size=500), rng.normal(loc=1.0, size=500))
        assert {"statistic", "p_value"} <= result.keys()
        assert result["p_value"] < 0.05

    def test_large_samples_make_p_values_useless(self, rng):
        """The trap: at scale everything is significant. Alert on effect size."""
        baseline = rng.normal(size=500_000)
        barely_different = rng.normal(loc=0.01, size=500_000)
        result = kolmogorov_smirnov_test(baseline, barely_different)
        assert result["p_value"] < 0.05
        assert result["statistic"] < 0.05, "the effect is negligible despite significance"

    def test_detector_flags_drifted_features_only(self, rng):
        baseline = {"stable": rng.normal(size=5000), "drifting": rng.normal(size=5000)}
        detector = DriftDetector(baseline, method="psi", threshold=0.25)
        current = {"stable": rng.normal(size=5000), "drifting": rng.normal(loc=2.0, size=5000)}
        result = detector.check(current)
        assert "drifting" in result["drifted_features"]
        assert "stable" not in result["drifted_features"]
