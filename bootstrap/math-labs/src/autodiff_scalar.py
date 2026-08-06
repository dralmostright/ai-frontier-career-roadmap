"""Scalar reverse-mode automatic differentiation — Week 3.

A minimal autodiff engine. Every value knows how it was computed, so the whole
computation forms a graph; calling ``backward()`` walks that graph in reverse
topological order applying the chain rule.

This is the most important file in Month 1. When you finish it, PyTorch's
``.backward()`` stops being magic — it is this, with tensors instead of floats
and C++ instead of Python. In Week 14 you will extend the same idea to arrays,
and in Week 29 the thing you differentiate will be attention.

Directly inspired by Karpathy's micrograd. Watch the video, then write this
yourself without looking. Copying it teaches you nothing; rebuilding it teaches
you everything.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable


class Value:
    """A scalar with a gradient and a record of how it was produced.

    Attributes:
        data: The forward value.
        grad: d(output)/d(self), accumulated during the backward pass. Zero
            until ``backward()`` runs.
        _backward: Closure that propagates gradient from this node to its
            parents. A no-op for leaves.
        _prev: The nodes this one was computed from.
        _op: Label for the producing operation, for debugging and graph drawing.
    """

    def __init__(
        self,
        data: float,
        _children: Iterable[Value] = (),
        _op: str = "",
        label: str = "",
    ) -> None:
        self.data = float(data)
        self.grad = 0.0
        self._backward: Callable[[], None] = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self) -> str:
        return f"Value(data={self.data:.6g}, grad={self.grad:.6g})"

    # -- arithmetic ---------------------------------------------------------
    #
    # For each operation: compute the forward value, build the output node, and
    # attach a closure that adds this node's local derivative times the
    # incoming gradient to each parent's ``.grad``.
    #
    # It must be ``+=``, never ``=``. When a value feeds two consumers its
    # gradients sum — that is the multivariable chain rule. Using ``=`` produces
    # silently wrong gradients in any graph with a reused intermediate, which is
    # every interesting graph.

    def __add__(self, other: Value | float) -> Value:
        """d(a+b)/da = 1, d(a+b)/db = 1. Addition routes gradient unchanged."""
        raise NotImplementedError("Week 3")

    def __mul__(self, other: Value | float) -> Value:
        """d(a*b)/da = b, d(a*b)/db = a. Multiplication swaps the operands."""
        raise NotImplementedError("Week 3")

    def __pow__(self, exponent: float) -> Value:
        """d(a**n)/da = n * a**(n-1). Constant exponents only."""
        raise NotImplementedError("Week 3")

    def __neg__(self) -> Value:
        raise NotImplementedError("Week 3")

    def __sub__(self, other: Value | float) -> Value:
        raise NotImplementedError("Week 3")

    def __truediv__(self, other: Value | float) -> Value:
        raise NotImplementedError("Week 3")

    def __radd__(self, other: float) -> Value:
        return self + other

    def __rmul__(self, other: float) -> Value:
        return self * other

    def __rsub__(self, other: float) -> Value:
        return (-self) + other

    def __rtruediv__(self, other: float) -> Value:
        return (self**-1.0) * other

    # -- activations and transcendentals ------------------------------------

    def exp(self) -> Value:
        """d(e^a)/da = e^a. The only function that is its own derivative."""
        raise NotImplementedError("Week 3")

    def log(self) -> Value:
        """Natural log. d(ln a)/da = 1/a.

        Raises:
            ValueError: if data <= 0.
        """
        raise NotImplementedError("Week 3")

    def tanh(self) -> Value:
        """d(tanh a)/da = 1 - tanh(a)^2.

        Note that the derivative is expressible in terms of the output. That
        trick — cache the forward result, reuse it in the backward pass — is
        why activation functions are cheap to differentiate and why frameworks
        store activations during the forward pass. It is also why activation
        memory dominates training memory for large models (Week 49).
        """
        raise NotImplementedError("Week 3")

    def relu(self) -> Value:
        """max(0, a). Derivative is 1 where a > 0, else 0.

        The derivative at exactly 0 is undefined; every framework picks 0 and
        moves on. Knowing that this is a convention rather than mathematics is
        a small but real signal of depth.
        """
        raise NotImplementedError("Week 3")

    def sigmoid(self) -> Value:
        """1 / (1 + e^-a). Derivative is s * (1 - s) where s is the output.

        Implement it directly rather than composing exp and division, then
        compare gradients between the two. They should match — a useful check
        that your composite ops are wired correctly.
        """
        raise NotImplementedError("Week 3")

    # -- backward pass ------------------------------------------------------

    def backward(self) -> None:
        """Populate ``.grad`` on every node in this node's ancestry.

        Three steps:

        1. Topologically sort the graph (DFS post-order from self).
        2. Seed ``self.grad = 1.0`` — the derivative of the output with respect
           to itself.
        3. Walk the sort in reverse, calling each node's ``_backward``.

        The topological order is what guarantees a node's gradient is fully
        accumulated before it propagates to its parents. Get this wrong and you
        get partially-summed gradients, which look almost right and are not.
        """
        raise NotImplementedError("Week 3")

    def zero_grad(self) -> None:
        """Reset gradients across this node's ancestry.

        Because gradients accumulate, failing to zero them between steps means
        step 2 sees the sum of steps 1 and 2. This is the single most common
        bug in hand-written training loops, in this file and in PyTorch alike.
        """
        raise NotImplementedError("Week 3")

    def topological_sort(self) -> list[Value]:
        """Return this node's ancestry, parents before children."""
        raise NotImplementedError("Week 3")


# ---------------------------------------------------------------------------
# Gradient checking
# ---------------------------------------------------------------------------


def numerical_gradient(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """Central-difference approximation: (f(x+h) - f(x-h)) / 2h.

    Use the central difference, not the forward difference. Central is O(h^2)
    accurate versus O(h) for the same cost, and the difference matters at the
    tolerances you will be testing against.

    ``h`` is a tradeoff: too large and truncation error dominates, too small and
    floating-point cancellation does. 1e-5 is a good default for float64.
    """
    raise NotImplementedError("Week 3")


def gradient_check(
    f: Callable[..., Value],
    inputs: list[Value],
    tolerance: float = 1e-6,
    h: float = 1e-5,
) -> tuple[bool, list[float]]:
    """Compare analytic gradients against numerical ones.

    This is the function that will save you weeks. Every time you add an
    operation to this engine, or a layer in Week 14, or an attention variant in
    Week 29, gradient-check it before trusting it. A wrong gradient does not
    crash — it trains slowly to a worse optimum and you spend four days blaming
    the learning rate.

    Use *relative* error, ``|a - n| / max(|a|, |n|, eps)``, not absolute.
    Gradient magnitudes vary over many orders of magnitude and an absolute
    threshold will either pass everything or fail everything.

    Returns:
        (all_passed, relative_errors) with one error per input.
    """
    raise NotImplementedError("Week 3")


# ---------------------------------------------------------------------------
# Loss functions — the gradients you must be able to derive on a whiteboard
# ---------------------------------------------------------------------------


def mse_loss(prediction: Value, target: float) -> Value:
    """Squared error. dL/dprediction = 2 * (prediction - target).

    Interview drill: derive the gradient of MSE with respect to the *weights* of
    a linear model, not just the prediction. That chain — loss to prediction to
    weights — is the whole of Week 5.
    """
    raise NotImplementedError("Week 3")


def binary_cross_entropy(prediction: Value, target: float) -> Value:
    """Log loss for a probability in (0, 1).

    -[y*log(p) + (1-y)*log(1-p)].

    Clamp p away from 0 and 1 before taking the log, or a confident wrong
    prediction produces inf and then NaN, and the NaN propagates through every
    parameter in one backward pass.

    The elegant result to know: composing sigmoid with BCE gives dL/dlogit =
    p - y. All the messy terms cancel. Derive it by hand at least once — this
    is a standard interview question and the cancellation is genuinely pretty.
    """
    raise NotImplementedError("Week 3")


def softmax(logits: list[Value]) -> list[Value]:
    """Numerically stable softmax over a list of Values.

    Subtract the max logit before exponentiating. Mathematically it changes
    nothing (softmax is shift-invariant); numerically it is the difference
    between working code and ``inf/inf``. Every production softmax does this,
    including the one inside attention.
    """
    raise NotImplementedError("Week 3")


def cross_entropy(logits: list[Value], target_index: int) -> Value:
    """Softmax followed by negative log likelihood of the target class.

    Implement it fused rather than as two steps: log(softmax(x))[i] simplifies
    to ``x[i] - logsumexp(x)``, which is both faster and far more stable. This
    is why PyTorch gives you ``CrossEntropyLoss`` that takes raw logits and
    warns you not to apply softmax first.

    The gradient with respect to the logits is ``p - onehot(target)``. Derive it.
    You will be asked.
    """
    raise NotImplementedError("Week 3")
