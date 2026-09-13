"""
XOR Tricks and Properties

What it is:
The bitwise exclusive OR (XOR, `^`) has remarkable algebraic properties:
1. Identity: `x ^ 0 = x`
2. Self-Inverse: `x ^ x = 0`
3. Commutative: `a ^ b = b ^ a`
4. Associative: `(a ^ b) ^ c = a ^ (b ^ c)`

When it is used:
- Single Number I (LeetCode 136): Every element appears twice except one. Find that one!
- Missing Number (LeetCode 268): Array contains n distinct numbers in range [0, n]. Find missing.
- In-place variable swap without temporary variable.
- Single Number III (LeetCode 260): Two unique numbers among pairs.

The Key Idea:
- In an array where every number appears twice except one, XOR-ing all elements together
  cancels all paired numbers (`x ^ x = 0`), leaving ONLY the unique number!

Time Complexity:
- O(n) single pass.

Space Complexity:
- O(1) auxiliary space.
"""


def single_number(nums: list[int]) -> int:
    """Finds the single non-duplicate number where all other numbers appear twice (LeetCode 136)."""
    unique = 0
    for num in nums:
        unique ^= num
    return unique


def missing_number(nums: list[int]) -> int:
    """Finds the missing number in range 0..n (LeetCode 268)."""
    n = len(nums)
    xor_all = 0
    # XOR all expected numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i
    # XOR all present numbers in nums
    for num in nums:
        xor_all ^= num
    return xor_all


def swap_without_temp(a: int, b: int) -> tuple[int, int]:
    """Swaps two numbers in-place using XOR."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == "__main__":
    # Single number
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([2, 2, 1]) == 1

    # Missing number
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

    # Swap without temp
    assert swap_without_temp(10, 25) == (25, 10)

    print("All XOR Tricks tests passed successfully.")
