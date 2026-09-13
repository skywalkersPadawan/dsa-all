"""
Count Set Bits (Hamming Weight)

What it is:
Counts the number of set bits ('1's) in the binary representation of an integer
(also known as the Hamming Weight or population count).

When it is used:
- LeetCode 191 (Number of 1 Bits).
- Counting Bits (LeetCode 338).
- Hamming Distance between two integers.

The Key Idea:
Method 1: Shift & Test
Right-shift by 1 at each step, checking `n & 1`. Takes 32 steps for 32-bit integer.

Method 2: Brian Kernighan's Algorithm
Repeatedly clear the lowest set bit using `n = n & (n - 1)`.
Loops ONLY as many times as there are set bits (extremely fast!).

Method 3: DP for Counting Bits from 0 to n (LeetCode 338)
`dp[i] = dp[i >> 1] + (i & 1)` in O(n) total time.

Time Complexity:
- Single number: O(number of set bits) using Brian Kernighan's.
- Array 0..n: O(n) using DP.

Space Complexity:
- O(1) auxiliary space.
"""


def count_set_bits(n: int) -> int:
    """Counts 1s in binary representation of n using Brian Kernighan's algorithm."""
    count = 0
    while n > 0:
        n &= n - 1  # Clears the lowest set bit
        count += 1
    return count


def count_bits_array(n: int) -> list[int]:
    """Returns array of bit counts for all numbers from 0 to n in O(n) time.

    (LeetCode 338)
    """
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        # Number of 1s in i = number of 1s in (i >> 1) + last bit (i & 1)
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


if __name__ == "__main__":
    assert count_set_bits(11) == 3  # 11 in binary: 1011 (three 1s)
    assert count_set_bits(128) == 1  # 10000000
    assert count_set_bits(0) == 0

    # Count bits array for n = 5
    assert count_bits_array(5) == [0, 1, 1, 2, 1, 2]

    print("All Count Set Bits tests passed successfully.")
