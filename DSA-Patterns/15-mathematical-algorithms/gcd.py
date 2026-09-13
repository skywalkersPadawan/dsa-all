"""
Greatest Common Divisor (GCD) - Euclidean Algorithm

What it is:
Computes the greatest common divisor (highest common factor) of two non-negative integers a and b.

When it is used:
- Simplifying fractions.
- Computing Least Common Multiple (LCM).
- Bézout's identity and Extended Euclidean algorithm for modular inverses.
- Simplifying ratio representations in geometric slope calculations.

The Key Idea:
Euclidean Algorithm:
`gcd(a, b) = gcd(b, a % b)` with base case `gcd(a, 0) = a`.
Why? Any divisor of `a` and `b` must also divide their remainder `a % b`.

Time Complexity:
- O(log(min(a, b))) by Lamé's Theorem (worst case occurs with consecutive Fibonacci numbers).

Space Complexity:
- Iterative: O(1) space.
- Recursive: O(log(min(a, b))) call stack.
"""


def gcd_iterative(a: int, b: int) -> int:
    """Computes GCD of a and b using iterative Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a: int, b: int) -> int:
    """Computes GCD of a and b using recursive Euclidean algorithm."""
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


if __name__ == "__main__":
    assert gcd_iterative(48, 18) == 6
    assert gcd_iterative(101, 10) == 1
    assert gcd_iterative(20, 0) == 20
    assert gcd_iterative(0, 5) == 5

    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(101, 10) == 1

    print("All GCD tests passed successfully.")
