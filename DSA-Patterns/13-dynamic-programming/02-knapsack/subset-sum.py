"""
Subset Sum Problem

What it is:
Given a set of non-negative integers `nums` and a value `target_sum`, determine if there
is a subset of the given set with sum equal to `target_sum`.

When it is used:
- Partition problems.
- Making change / exact balancing.
- Foundation for Partition Equal Subset Sum (LeetCode 416).

The Key Idea:
0/1 Knapsack Boolean Variation:
Let `dp[s]` be a boolean: can we form sum `s` using a subset of the processed numbers?
Initialize: `dp[0] = True` (empty subset has sum 0).
For each number `num` in `nums`:
Iterate `s` BACKWARDS from `target_sum` down to `num`:
`dp[s] = dp[s] or dp[s - num]`

Time Complexity:
- O(n * target_sum) time.

Space Complexity:
- O(target_sum) auxiliary space.
"""


def has_subset_sum(nums: list[int], target_sum: int) -> bool:
    """Returns True if there exists a subset summing to target_sum."""
    dp = [False] * (target_sum + 1)
    dp[0] = True  # sum of 0 is always possible with empty subset

    for num in nums:
        # Iterate backwards to ensure each element is used at most once
        for s in range(target_sum, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

        if dp[target_sum]:
            return True  # Early exit if target already formed

    return dp[target_sum]


if __name__ == "__main__":
    assert has_subset_sum([3, 34, 4, 12, 5, 2], 9) is True  # 4 + 5 = 9
    assert has_subset_sum([3, 34, 4, 12, 5, 2], 30) is False  # no subset sums to 30
    assert has_subset_sum([1, 2, 3, 7], 6) is True  # 1 + 2 + 3 = 6
    assert has_subset_sum([], 0) is True

    print("All Subset Sum tests passed successfully.")
