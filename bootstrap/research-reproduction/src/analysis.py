"""Analysis and reporting — Week 68.

Turning runs into a defensible claim.
"""

from __future__ import annotations

from typing import Any


def aggregate_across_seeds(results: Any, metric: str) -> Any:
    """Mean, std, and CI per condition.

    **Never report a single-seed number.** Variance across seeds is frequently
    larger than the effect being claimed, and a single run cannot distinguish
    the two. This is the most common flaw in applied ML papers and the easiest
    to avoid.
    """
    raise NotImplementedError("Week 68")


def significance_test(
    results: Any, condition_a: str, condition_b: str, metric: str
) -> dict[str, float]:
    """Is the difference real?

    Paired test where the design supports it — same seeds, same data — because
    pairing removes the run-to-run variance and is far more sensitive.

    Report the effect size alongside the p-value. A statistically significant
    0.2% improvement is not an interesting result, and reporting only the
    p-value obscures that.
    """
    raise NotImplementedError("Week 68")


def multiple_comparison_correction(p_values: list[float], method: str = "holm") -> list[float]:
    """Adjust for testing many hypotheses.

    Test twenty conditions at p < 0.05 and you expect one false positive by
    chance. Ablation studies test many conditions, so this applies directly to
    your work.

    Applying a correction is a small thing that signals genuine statistical
    care, and its absence is something a research-minded interviewer will
    notice.
    """
    raise NotImplementedError("Week 68")


def plot_results(
    results: Any, x: str, y: str, hue: str | None = None, error_bars: str = "ci"
) -> Any:
    """The main figure.

    Rules for a figure that survives review:

    - Error bars always. Say in the caption what they represent.
    - Label the axes, with units.
    - The caption states the finding, not the contents. "LoRA quality
      saturates at rank 8" beats "quality vs rank".
    - Readable in greyscale.
    - Y-axis starting at zero unless you have a reason, and state the reason.
    """
    raise NotImplementedError("Week 68")


def generate_report(spec: Any, results: Any, template: str = "reproduction") -> str:
    """Assemble the report.

    Structure for a reproduction report:

    1. **The claim** being tested, and the original numbers
    2. **What you changed** to make it feasible, and why that preserves the claim
    3. **Setup** — data, model, hyperparameters, hardware, seeds
    4. **Results** — your numbers next to theirs
    5. **Discrepancies** — where you differ and your best explanation
    6. **Ablations**
    7. **What did not work** — the failed attempts, honestly
    8. **Conclusion** — does the claim hold at this scale?
    9. **Reproducibility appendix** — configs, environment, commands

    Sections 5 and 7 are the ones that make it credible. A report where
    everything worked on the first try is a report nobody believes.
    """
    raise NotImplementedError("Week 68")
