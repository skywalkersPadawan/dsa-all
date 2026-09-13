"""
Prime Factorization (Trial Division)

What it is:
Decomposes a composite number n into the product of prime numbers:
n = p1^a1 * p2^a2 * ... * pk^ak.

When it is used:
- Finding all divisors of a number.
- Euler's Totient function.
- Simplifying fractions and roots.
- Number theory problems in competitive programming.

The Key Idea:
Trial Division up to sqrt(n):
1. Extract all factors of 2: while `n % 2 == 0`: record 2, `n //= 2`.
2. For odd numbers `d` from 3 up to `sqrt(n)` (step 2):
   While `n % d == 0`: record `d`, `n //= d`.
3. If `n > 1` after the loop, the remaining `n` is itself a prime factor!

Time Complexity:
- O(sqrt(n)) worst case (when n is prime).

Space Complexity:
- O(log n) to store prime factors.
"""


def prime_factors(n: int) -> list[int]:
    """Returns the list of prime factors of n in non-decreasing order."""
    factors: list[int] = []

    # Handle factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd factors up to sqrt(n)
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2

    # If n is still greater than 1, it is prime
    if n > 1:
        factors.append(n)

    return factors


def prime_factorization_counts(n: int) -> dict[int, int]:
    """Returns a dictionary mapping prime_factor -> exponent."""
    counts: dict[int, int] = {}
    for p in prime_factors(n):
        counts[p] = counts.get(p, 0) + 1
    return counts


if __name__ == "__main__":
    assert prime_factors(12) == [2, 2, 3]  # 2^2 * 3 = 12
    assert prime_factors(315) == [3, 3, 5, 7]  # 9 * 35 = 315
    assert prime_factors(97) == [97]  # prime number
    assert prime_factors(1) == []

    assert prime_factorization_counts(360) == {
        2: 3,
        3: 2,
        5: 1,
    }  # 8 * 9 * 5 = 360

    print("All Prime Factorization tests passed successfully.")
