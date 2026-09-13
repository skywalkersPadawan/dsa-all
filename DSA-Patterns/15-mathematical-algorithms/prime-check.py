"""
Primality Testing (O(sqrt(n)) Trial Division)

What it is:
Determines whether an integer n > 1 is a prime number (has no divisors other than 1 and itself).

When it is used:
- Single-number primality checks.
- Cryptography basics, hash table resizing (finding next prime bucket size).

The Key Idea:
Why test only up to sqrt(n)?
If `n = a * b`, then at least one factor must be `<= sqrt(n)`.
If no factor <= sqrt(n) divides n, then no factor > sqrt(n) can divide n either!

Optimization:
- Handle n <= 1: not prime.
- Handle 2 and 3: prime.
- If divisible by 2 or 3: not prime.
- All primes > 3 are of the form `6k ± 1`. Test divisors `d` and `d + 2` with step of 6!

Time Complexity:
- O(sqrt(n)) time.

Space Complexity:
- O(1) space.
"""


def is_prime(n: int) -> bool:
    """Determines whether n is prime in O(sqrt(n)) time."""
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime

    # Exclude multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check factors of form 6k ± 1 up to sqrt(n)
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6

    return True


if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97, 101]
    for p in primes:
        assert is_prime(p) is True

    non_primes = [-5, 0, 1, 4, 6, 8, 9, 15, 25, 100]
    for np in non_primes:
        assert is_prime(np) is False

    print("All Primality Testing tests passed successfully.")
