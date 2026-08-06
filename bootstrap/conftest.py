"""Workspace-wide pytest configuration for the AI Frontier Career Roadmap labs.

Two jobs:

1. **Week gating.** Tests are tagged ``@pytest.mark.week(n)``. Anything tagged
   for a week later than the current one is skipped, so the suite stays green
   as you progress instead of drowning you in failures for material you have
   not reached. The current week comes from ``--week`` or the ``CURRENT_WEEK``
   file at the workspace root.

2. **Shared fixtures.** Deterministic RNG, tolerance helpers, and the skip
   conditions for tests that need Docker, a GPU, or an API key.

Each lab has its own ``tests/conftest.py`` that puts its sibling ``src/`` on
``sys.path``. Copy that file if you add a lab.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

BOOTSTRAP_ROOT = Path(__file__).parent
WEEK_FILE = BOOTSTRAP_ROOT / "CURRENT_WEEK"

TOTAL_WEEKS = 78


# ---------------------------------------------------------------------------
# Week gating
# ---------------------------------------------------------------------------


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--week",
        action="store",
        default=None,
        help=(
            "Course week to test up to. Tests marked for a later week are "
            "skipped. Defaults to the contents of bootstrap/CURRENT_WEEK. "
            "Pass a large number (e.g. 999) to run everything."
        ),
    )
    parser.addoption(
        "--only-week",
        action="store",
        default=None,
        type=int,
        help=(
            "Run only the tests for this exact week, skipping every other week. "
            "Note that `-m 'week(5)'` does NOT work: pytest's -m expression "
            "takes marker names, not marker calls."
        ),
    )


def _current_week(config: pytest.Config) -> int:
    """Resolve the current course week: CLI flag, then file, then 0."""
    from_cli = config.getoption("--week")
    if from_cli is not None:
        return int(from_cli)

    from_env = os.environ.get("CURRENT_WEEK")
    if from_env:
        return int(from_env)

    if WEEK_FILE.exists():
        text = WEEK_FILE.read_text().strip()
        if text:
            return int(text)

    return 0


def pytest_configure(config: pytest.Config) -> None:
    config._current_week = _current_week(config)  # type: ignore[attr-defined]


def pytest_report_header(config: pytest.Config) -> str:
    week = config._current_week  # type: ignore[attr-defined]
    month = min(18, (week + 3) // 4) if week else 0
    return f"course week: {week}/{TOTAL_WEEKS}  (month {month})"


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    current = config._current_week  # type: ignore[attr-defined]
    only = config.getoption("--only-week")

    for item in items:
        marker = item.get_closest_marker("week")
        if marker is None:
            if only is not None:
                item.add_marker(pytest.mark.skip(reason=f"not part of week {only}"))
            continue

        target = int(marker.args[0])

        if only is not None:
            if target != only:
                item.add_marker(
                    pytest.mark.skip(reason=f"week {target} — running only week {only}")
                )
            continue

        if target > current:
            item.add_marker(pytest.mark.skip(reason=f"week {target} — you are on week {current}"))


# ---------------------------------------------------------------------------
# Environment capability skips
# ---------------------------------------------------------------------------


def _have_database() -> bool:
    """True if the lab Postgres appears reachable."""
    import socket

    try:
        with socket.create_connection(("localhost", 5432), timeout=0.5):
            return True
    except OSError:
        return False


def _have_gpu() -> bool:
    try:
        import torch
    except ImportError:
        return False
    if torch.cuda.is_available():
        return True
    return bool(getattr(torch.backends, "mps", None) and torch.backends.mps.is_available())


@pytest.fixture(scope="session")
def database_url() -> str:
    """Connection string for the lab Postgres. Skips if it isn't running."""
    if not _have_database():
        pytest.skip("lab Postgres not reachable — run `make db-up`")
    return os.environ.get(
        "DATABASE_URL", "postgresql://airoadmap:airoadmap@localhost:5432/airoadmap"
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    if item.get_closest_marker("db") and not _have_database():
        pytest.skip("needs the lab Postgres — run `make db-up`")

    if item.get_closest_marker("gpu") and not _have_gpu():
        pytest.skip("needs a GPU (CUDA or MPS)")

    if item.get_closest_marker("llm") and not (
        os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("OPENAI_API_KEY")
    ):
        pytest.skip("needs an LLM API key in bootstrap/.env")


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

SEED = 20260806
"""Fixed seed for every stochastic test.

Reproducibility is a course-wide standard, not a Month 5 topic. A test that
passes on Tuesday and fails on Wednesday teaches you nothing.
"""


@pytest.fixture
def rng():
    """A seeded NumPy generator. Use this instead of np.random.* in tests."""
    import numpy as np

    return np.random.default_rng(SEED)


@pytest.fixture
def seed() -> int:
    return SEED


@pytest.fixture(autouse=True)
def _deterministic_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Pin the sources of nondeterminism that bite most often."""
    monkeypatch.setenv("PYTHONHASHSEED", str(SEED))
    monkeypatch.setenv("TOKENIZERS_PARALLELISM", "false")

    import random

    random.seed(SEED)

    try:
        import numpy as np

        np.random.seed(SEED)
    except ImportError:
        pass


@pytest.fixture
def tol() -> dict[str, float]:
    """Numerical tolerances.

    ``tight`` for closed-form results you should match nearly exactly,
    ``loose`` for iterative methods, ``grad`` for finite-difference checks.
    """
    return {"tight": 1e-10, "loose": 1e-4, "grad": 1e-5}


@pytest.fixture
def assert_close():
    """Wrapper around numpy.testing.assert_allclose with a useful message."""
    import numpy as np

    def _assert(actual, expected, rtol: float = 1e-7, atol: float = 0.0, msg: str = ""):
        np.testing.assert_allclose(
            np.asarray(actual, dtype=float),
            np.asarray(expected, dtype=float),
            rtol=rtol,
            atol=atol,
            err_msg=msg,
        )

    return _assert
