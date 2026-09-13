"""
Sparse Table (Range Minimum Query - RMQ)

What it is:
A data structure that answers static Range Minimum/Maximum Queries (RMQ) in strictly
O(1) CONSTANT TIME after an O(n log n) preprocessing step.

When it is used:
- Static Range Minimum/Maximum Queries where the array is NEVER modified.
- Finding Lowest Common Ancestor (LCA) in trees in O(1) via Euler tour.
- Range GCD queries in O(1).

The Key Idea:
Binary Lifting / Power-of-Two Intervals:
Any range `[L..R]` of length `len = R - L + 1` can be covered by two overlapping intervals
of length `2^k`, where `k = floor(log2(len))`:
- Interval 1: `[L, L + 2^k - 1]`
- Interval 2: `[R - 2^k + 1, R]`
Because minimum is an IDEMPOTENT operation (`min(x, x) = x`), the overlap does not affect the result!
`RMQ(L, R) = min(table[L][k], table[R - 2^k + 1][k])`

Preprocessing:
`table[i][j]` stores minimum of range starting at `i` with length `2^j`.
`table[i][j] = min(table[i][j - 1], table[i + 2^(j - 1)][j - 1])`

Time Complexity:
- Preprocessing: O(n log n).
- Query: O(1) strictly constant time!

Space Complexity:
- O(n log n) for the table.
"""

import math


class SparseTable:
    """Sparse Table for Range Minimum Queries (RMQ) in O(1) query time."""

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        if self.n == 0:
            return

        max_power = math.floor(math.log2(self.n)) + 1
        # table[i][j] is the min in range [i, i + 2^j - 1]
        self.table = [[0] * max_power for _ in range(self.n)]

        # Base case: intervals of length 2^0 = 1
        for i in range(self.n):
            self.table[i][0] = nums[i]

        # Fill table for powers of 2
        for j in range(1, max_power):
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = min(
                    self.table[i][j - 1],
                    self.table[i + (1 << (j - 1))][j - 1],
                )

    def query_min(self, left: int, right: int) -> int:
        """Returns the minimum element in nums[left..right] in O(1) time."""
        length = right - left + 1
        k = math.floor(math.log2(length))

        # Combine two overlapping ranges of size 2^k
        return min(self.table[left][k], self.table[right - (1 << k) + 1][k])


if __name__ == "__main__":
    nums = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    st = SparseTable(nums)

    # Range [0, 4]: min([7, 2, 3, 0, 5]) = 0
    assert st.query_min(0, 4) == 0
    # Range [4, 7]: min([5, 10, 3, 12]) = 3
    assert st.query_min(4, 7) == 3
    # Single element [1, 1]: 2
    assert st.query_min(1, 1) == 2
    # Entire array
    assert st.query_min(0, len(nums) - 1) == 0

    print("All Sparse Table tests passed successfully.")
