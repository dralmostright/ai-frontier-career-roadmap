"""Tensors and autograd — Week 17.

Port everything from `ml-from-scratch` into PyTorch. The value is not in
learning an API; it is in the moment where `loss.backward()` stops being
magic because you wrote the equivalent three weeks ago.

Work through this file with the PyTorch docs open, and after each function
ask: what did my NumPy version do here, and what is PyTorch doing
differently?
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass


def device_report() -> dict[str, Any]:
    """What hardware is available, and what it implies for this course.

    Reports CUDA, MPS, CPU thread count, and available memory. Run it once,
    note the result in your Week 17 check-in, and plan Months 8-12 around it.
    Everything in this course is designed to run on modest hardware, but you
    should know which constraints you are working under before Month 8, not
    during it.
    """
    raise NotImplementedError("Week 17")


def autograd_walkthrough(x: float = 2.0) -> dict[str, Any]:
    """Trace a small graph and expose every intermediate.

    Build y = (x + 1)^2 * 3, call backward, and return `grad_fn` at each node
    plus the gradient. Compare against `math-labs/autodiff_scalar.py` — the
    graph structure is identical, which is the point.

    Returns:
        Keys ``value``, ``grad``, ``graph`` (grad_fn chain as strings).
    """
    raise NotImplementedError("Week 17")


def gradient_accumulation_demo() -> dict[str, Any]:
    """Show that gradients accumulate until you zero them.

    Call backward twice without `zero_grad()`; the gradient doubles. This is
    the same `+=` you implemented in Week 3, and it is why every PyTorch
    training loop starts with `optimizer.zero_grad()`.
    """
    raise NotImplementedError("Week 17")


def no_grad_vs_detach() -> dict[str, Any]:
    """Demonstrate the difference. A standard interview question.

    - `torch.no_grad()` is a context manager: nothing inside builds a graph.
      Use it for evaluation and inference.
    - `.detach()` returns a tensor sharing storage but severed from the
      graph. Use it to stop gradient flow at one specific point.

    The subtle part: `.detach()` shares memory, so mutating the detached
    tensor in place mutates the original. Demonstrate that too.
    """
    raise NotImplementedError("Week 17")


def broadcasting_rules() -> list[dict[str, Any]]:
    """Cases where broadcasting silently does the wrong thing.

    The classic: subtracting a shape-(n,) tensor from a shape-(n,1) tensor
    gives you an (n,n) matrix instead of an error. Your loss becomes a
    matrix, the mean is meaningless, and training quietly does nothing
    useful. Construct this bug on purpose so you recognize it later.
    """
    raise NotImplementedError("Week 17")


def numpy_to_torch_port(numpy_mlp_weights: Any) -> Any:
    """Load your Week 13-16 NumPy MLP weights into an equivalent nn.Module.

    If both produce identical outputs on the same input, you have proven your
    NumPy implementation was correct. Satisfying, and a real validation.
    """
    raise NotImplementedError("Week 17")


def benchmark_devices(size: int = 4096, iterations: int = 20) -> dict[str, float]:
    """Time a matmul on each available device.

    Include the CPU-to-GPU transfer in one variant and exclude it in another.
    The gap teaches you why you keep data on the device and why `.item()`
    inside a training loop is expensive.
    """
    raise NotImplementedError("Week 17")
