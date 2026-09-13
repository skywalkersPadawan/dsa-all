"""
Sieve of Eratosthenes

What it is:
An ancient and highly efficient algorithm for finding all prime numbers up to any
given limit `n`.

When it is used:
- Count Primes (LeetCode 204).
- Generating prime lookup tables for fast O(1) query checks.
- Precomputing primes for prime factorization of multiple queries.

The Key Idea:
1. Initialize a boolean array `is_prime = [True] * (n + 1)` with `is_prime[0] = is_prime[1] = False`.
2. For `p` from 2 up to `sqrt(n)`:
   If `is_prime[p]` is True:
     Mark all multiples of `p` starting from `p * p` up to `n` as False:
     `is_prime[p * p : n + 1 : p] = [False] * ...`
   (Starting at `p * p` works because any smaller multiple `k * p` (where k < p)
    has already been marked by a smaller prime factor k).

Time Complexity:
- O(n log(log n)) nearly linear time!

Space Complexity:
- O(n) auxiliary space for the boolean array.
"""


def sieve_of_eratosthenes(n: int) -> list[int]:
    """Returns a list of all primes <= n in O(n log(log n)) time."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark multiples starting from p * p
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]


def count_primes_less_than(n: int) -> int:
    """Counts primes strictly less than n (LeetCode 204)."""
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
        p += 1

    return sum(is_prime)


if __name__ == "__main__":
    primes_up_to_30 = sieve_of_eratosthenes(30)
    assert primes_up_to_30 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    assert count_primes_less_than(10) == 4  # 2, 3, 5, 7
    assert count_primes_less_than(0) == 0
    assert count_primes_less_than(1) == 0

    print("All Sieve of Eratosthenes tests passed successfully.")
