"""
Least Common Multiple (LCM)

What it is:
Computes the smallest positive integer that is divisible by both integers a and b.

When it is used:
- Finding a common denominator for fractions.
- Periodicity alignment / meeting frequency of cyclic events.
- Synchronization intervals in distributed systems.

The Key Idea:
Fundamental Identity Relating GCD and LCM:
`a * b = gcd(a, b) * lcm(a, b)`
Therefore:
`lcm(a, b) = abs(a * b) // gcd(a, b)`

Implementation Tip:
To avoid intermediate integer overflow (especially in languages with fixed-width integers),
divide BEFORE multiplying:
`lcm = (a // gcd(a, b)) * b`

Time Complexity:
- O(log(min(a, b))) dominated by GCD calculation.

Space Complexity:
- O(1).
"""


def gcd(a: int, b: int) -> int:
    """Helper Euclidean GCD."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """Computes LCM of a and b in O(log(min(a, b))) time."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


if __name__ == "__main__":
    assert lcm(4, 6) == 12
    assert lcm(15, 20) == 60
    assert lcm(7, 5) == 35  # coprime numbers
    assert lcm(10, 10) == 10
    assert lcm(0, 5) == 0

    print("All LCM tests passed successfully.")
