"""
Prefix Sum Pattern

What it is:
A preprocessing technique where an auxiliary array `prefix` is computed such that
`prefix[i]` stores the sum of all elements from index 0 up to index i-1.
This transforms any range sum query `sum(nums[left..right])` from O(n) into O(1).

When it is used:
- Multiple subarray sum queries on an unchanging array (Range Sum Query).
- Subarray sum equals k (combined with a hash map in O(n) time).
- Finding equilibrium index or pivot where left sum equals right sum.
- 2D grid range sum queries.

The Key Idea:
Formula with 1-based prefix array:
- `prefix = [0] * (n + 1)`
- `prefix[i] = prefix[i - 1] + nums[i - 1]`
- Range sum from index `left` to `right` (inclusive, 0-indexed):
  `range_sum = prefix[right + 1] - prefix[left]`

Time Complexity:
- Precomputation: O(n) time.
- Range Query: O(1) time.

Space Complexity:
- O(n) auxiliary space for prefix array (or O(1) if modifying input array in-place).

Common Pitfalls / Edge Cases:
- Using 0-indexed prefix without a leading 0 requires special-casing `left == 0`:
  `range_sum = prefix[right] - (prefix[left - 1] if left > 0 else 0)`.
  Using size `n + 1` with a leading 0 cleanly eliminates all index boundary checks.
"""


class PrefixSum:
    """Computes and queries prefix sums in O(1) time."""

    def __init__(self, nums: list[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + val

    def query(self, left: int, right: int) -> int:
        """Returns the sum of nums[left..right] (inclusive, 0-indexed)."""
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """Finds total number of contiguous subarrays that sum to k.

    Uses prefix sum + hash map pattern (LeetCode 560).
    Time: O(n), Space: O(n).
    """
    count = 0
    current_prefix_sum = 0
    # Map from prefix_sum -> number of times it has occurred
    prefix_counts: dict[int, int] = {0: 1}
    for num in nums:
        current_prefix_sum += num
        # If (current_prefix_sum - k) was seen before, those earlier points
        # mark the start of valid subarrays ending at the current position.
        target_prefix = current_prefix_sum - k
        if target_prefix in prefix_counts:
            count += prefix_counts[target_prefix]

        prefix_counts[current_prefix_sum] = prefix_counts.get(current_prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    ps = PrefixSum(nums)

    # Range [0, 2] -> 1 + 2 + 3 = 6
    assert ps.query(0, 2) == 6
    # Range [1, 4] -> 2 + 3 + 4 + 5 = 14
    assert ps.query(1, 4) == 14
    # Range [0, 5] -> 1 + 2 + 3 + 4 + 5 + 6 = 21
    assert ps.query(0, 5) == 21
    # Single element [3, 3] -> 4
    assert ps.query(3, 3) == 4

    # Subarray sum equals k tests
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2  # [1, 1] at (0,1) and (1,2)
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2  # [1, 2] at (0,1) and [3] at (2,2)
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3
    print("All Prefix Sum tests passed successfully.")
