"""
Fast Exponentiation (Binary Exponentiation / Modular Pow)

What it is:
Computes `base^exponent` (and `(base^exponent) % mod`) in O(log exponent) time
instead of naive O(exponent) repeated multiplication.

When it is used:
- Pow(x, n) (LeetCode 50).
- Modular Exponentiation in cryptography (RSA, Diffie-Hellman).
- Matrix Exponentiation for computing N-th Fibonacci in O(log n).

The Key Idea:
Divide and Conquer on Exponent:
- If exponent is even: `base^exp = (base^(exp // 2))^2`
- If exponent is odd: `base^exp = base * (base^(exp - 1))`

Iterative Binary Exponentiation:
Inspect each bit of `exponent` from right to left:
- If the current bit is 1: multiply `result` by current `base`.
- Square `base = base * base` at each bit position.
- Shift `exponent >>= 1`.

Time Complexity:
- O(log exponent).

Space Complexity:
- O(1) auxiliary space.
"""


def fast_pow(base: float, exponent: int) -> float:
    """Computes base^exponent (LeetCode 50). Handles negative exponents."""
    if exponent == 0:
        return 1.0

    if exponent < 0:
        base = 1.0 / base
        exponent = -exponent

    result = 1.0
    current_product = base

    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_product
        current_product *= current_product
        exponent //= 2

    return result


def mod_pow(base: int, exponent: int, mod: int) -> int:
    """Computes (base^exponent) % mod in O(log exponent) time."""
    result = 1
    base = base % mod

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2

    return result


if __name__ == "__main__":
    assert fast_pow(2.0, 10) == 1024.0
    assert fast_pow(2.0, -2) == 0.25
    assert fast_pow(3.0, 0) == 1.0

    # Modular pow
    assert mod_pow(2, 10, 1000) == 24  # 1024 % 1000 = 24
    assert mod_pow(3, 5, 7) == 5  # 243 % 7 = 5

    print("All Fast Exponentiation tests passed successfully.")
