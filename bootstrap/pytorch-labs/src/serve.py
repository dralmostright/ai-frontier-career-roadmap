"""Inference serving — Week 24, extended in Weeks 52 and 59.

Your first deployed model. The Month 6 capstone is not "train a classifier";
it is "serve a classifier and know its p99."
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


class InferenceService:
    """Model loading, warmup, batching, and prediction.

    **Warmup is not optional.** The first few inferences are several times
    slower — lazy CUDA context creation, cuDNN algorithm selection, memory
    allocator warmup. Serve traffic before warming up and your first users
    get the worst latency. Run a dozen dummy batches at startup.
    """

    def __init__(self, checkpoint: Path, device: str = "cpu", warmup_iterations: int = 10) -> None:
        raise NotImplementedError("Week 24")

    def predict(self, inputs: Any) -> dict[str, Any]:
        raise NotImplementedError("Week 24")

    def predict_batch(self, inputs: list) -> list[dict[str, Any]]:
        raise NotImplementedError("Week 24")


class DynamicBatcher:
    """Collect requests for a few milliseconds, then run them as one batch.

    The single highest-leverage serving optimization, and the tradeoff is
    explicit: you add up to `max_wait_ms` to every request's latency and gain
    a large multiple in throughput. GPUs are massively underutilized by
    batch-size-1 inference.

    You will meet this again in Week 59 as continuous batching, which is the
    same idea adapted to autoregressive generation where sequences finish at
    different times.
    """

    def __init__(self, max_batch_size: int = 32, max_wait_ms: float = 10.0) -> None:
        raise NotImplementedError("Week 24")

    async def submit(self, request: Any) -> Any:
        raise NotImplementedError("Week 24")


def measure_latency(
    service: InferenceService, inputs: Any, iterations: int = 200
) -> dict[str, float]:
    """p50, p90, p95, p99, and throughput.

    **Report percentiles, not the mean.** A mean of 50ms hides that 1% of
    users wait two seconds, and those users are the ones who complain. This
    should be second nature to you already; most ML engineers report the mean.

    Discard the warmup iterations before computing statistics.
    """
    raise NotImplementedError("Week 24")


def latency_vs_batch_size(service: InferenceService, batch_sizes: list[int]) -> Any:
    """The curve for the Month 6 capstone README.

    Two lines: per-request latency (rises with batch size) and throughput
    (rises, then plateaus when the device saturates). The knee of the
    throughput curve is your operating point, and being able to point at a
    measured curve rather than assert a number is what makes the capstone
    credible.
    """
    raise NotImplementedError("Week 24")
