"""
Modular Arithmetic Guide

What it is:
A system of arithmetic for integers, where numbers "wrap around" upon reaching
a certain value—the modulus. The common modulus in coding interviews is `10^9 + 7` (1000000007),
a large prime that fits in standard 32-bit signed integer math and prevents integer overflow.

Key Rules:
1. Addition: `(a + b) % M = ((a % M) + (b % M)) % M`
2. Subtraction: `(a - b) % M = ((a % M) - (b % M) + M) % M` (adding M prevents negative modulo in C/Java)
3. Multiplication: `(a * b) % M = ((a % M) * (b % M)) % M`
4. Division: `(a / b) % M = (a * mod_inverse(b, M)) % M`
   (Division modulo M is NOT `(a % M) / (b % M)`! Use Fermat's Little Theorem for prime M).

Fermat's Little Theorem:
If M is prime, then `b^(M - 1) ≡ 1 (mod M)`.
Multiplying both sides by `b^(-1)`:
`b^(-1) ≡ b^(M - 2) (mod M)`.
So `mod_inverse(b, M) = pow(b, M - 2, M)`.

Time Complexity:
- Add / Subtract / Multiply: O(1).
- Modular Inverse: O(log M) using binary exponentiation.
"""

MOD = 1_000_000_007


def mod_add(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) + (b % m)) % m


def mod_sub(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) - (b % m) + m) % m


def mod_mul(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) * (b % m)) % m


def mod_inverse(b: int, m: int = MOD) -> int:
    """Computes modular inverse b^(-1) mod m for prime m using Fermat's Little Theorem."""
    return pow(b, m - 2, m)


def mod_div(a: int, b: int, m: int = MOD) -> int:
    """Computes (a / b) % m."""
    return mod_mul(a, mod_inverse(b, m), m)


if __name__ == "__main__":
    assert mod_add(1_000_000_006, 5) == 4
    assert mod_sub(2, 5) == 1_000_000_004
    assert mod_mul(10, 20) == 200

    # Modular division: (12 / 4) % MOD should equal 3
    assert mod_div(12, 4) == 3
    # Check that (b * mod_inverse(b)) % MOD == 1
    assert (7 * mod_inverse(7)) % MOD == 1

    print("All Modular Arithmetic tests passed successfully.")
