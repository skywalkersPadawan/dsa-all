"""
Partition Equal Subset Sum

What it is:
Given an integer array `nums`, return True if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal.

When it is used:
- LeetCode 416 (Partition Equal Subset Sum).
- Partitioning workload/tasks equally between two processors.

The Key Idea:
Reduction to Subset Sum:
Let `total_sum = sum(nums)`.
1. If `total_sum` is odd: it is IMPOSSIBLE to partition into two equal integer sums -> return False!
2. If `total_sum` is even: the problem is equivalent to finding if there exists a subset
   with `target_sum = total_sum // 2`!
3. Use 0/1 Knapsack Boolean DP.

Time Complexity:
- O(n * target) where target = sum(nums) // 2.

Space Complexity:
- O(target) auxiliary space.
"""


def can_partition(nums: list[int]) -> bool:
    """Returns True if nums can be partitioned into two subsets of equal sum."""
    total_sum = sum(nums)

    # If sum is odd, cannot partition into two equal integer halves
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

        if dp[target]:
            return True

    return dp[target]


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True  # [1, 5, 5] and [11] (sum 11 each)
    assert can_partition([1, 2, 3, 5]) is False  # total sum = 11 (odd)
    assert can_partition([2, 2]) is True

    print("All Partition Equal Subset Sum tests passed successfully.")
