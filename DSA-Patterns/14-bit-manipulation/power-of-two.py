"""
Power of Two Check

What it is:
Determines whether a given integer `n` is a power of two (i.e., `n == 2^x` for some integer x >= 0).

When it is used:
- LeetCode 231 (Power of Two).
- Memory alignment and power-of-two buffer allocations.

The Key Idea:
A positive number that is a power of two has EXACTLY ONE bit set in its binary representation!
Examples:
- 1  -> `0001`
- 2  -> `0010`
- 4  -> `0100`
- 8  -> `1000`

Subtracting 1 flips the single set bit to 0 and all trailing zeros to 1s:
- 4 (100) - 1 = 3 (011)
- 8 (1000) - 1 = 7 (0111)

Therefore: `n & (n - 1) == 0` for any power of two!
Must also ensure `n > 0` (0 and negative numbers are not powers of two).

Condition:
`n > 0 and (n & (n - 1)) == 0`

Time Complexity:
- O(1).

Space Complexity:
- O(1).
"""


def is_power_of_two(n: int) -> bool:
    """Returns True if n is a power of two in O(1) time."""
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    assert is_power_of_two(1) is True  # 2^0
    assert is_power_of_two(2) is True  # 2^1
    assert is_power_of_two(16) is True  # 2^4
    assert is_power_of_two(3) is False
    assert is_power_of_two(0) is False
    assert is_power_of_two(-16) is False

    print("All Power of Two tests passed successfully.")
