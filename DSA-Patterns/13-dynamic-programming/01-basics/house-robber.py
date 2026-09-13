"""
House Robber Pattern

What it is:
You are a robber planning to rob houses along a street. Each house has a certain amount
of money stashed. Adjacent houses have security systems connected; robbing two adjacent
houses on the same night will automatically trigger the alarm.
Determine the maximum amount of money you can rob tonight without alerting the police.

When it is used:
- LeetCode 198 (House Robber).
- LeetCode 213 (House Robber II - circular street).
- Decision problems with non-adjacent selection constraints.

The Key Idea:
At house `i`, you have two choices:
1. Rob house `i`: Gain `nums[i]` + maximum money from houses up to `i - 2` (cannot rob house i - 1).
2. Skip house `i`: Maximum money is the same as up to house `i - 1`.
State transition:
`dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])`

Optimized with two rolling variables `rob_prev1` and `rob_prev2`.

Time Complexity:
- O(n) single pass.

Space Complexity:
- O(1) auxiliary space.
"""


def rob(nums: list[int]) -> int:
    """Finds maximum loot without robbing adjacent houses.

    Time: O(n), Space: O(1).
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = 0
    prev1 = 0

    for money in nums:
        curr = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = curr

    return prev1


def rob_circular(nums: list[int]) -> int:
    """House Robber II: Houses arranged in a circle.

    First and last houses are adjacent.
    Take max of robbing nums[0..n-2] vs nums[1..n-1].
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    return max(rob(nums[:-1]), rob(nums[1:]))


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4  # Rob house 1 ($1) and house 3 ($3)
    assert rob([2, 7, 9, 3, 1]) == 12  # Rob house 1 ($2), house 3 ($9), house 5 ($1)
    assert rob([5]) == 5
    assert rob([]) == 0

    # Circular
    assert rob_circular([2, 3, 2]) == 3
    assert rob_circular([1, 2, 3, 1]) == 4

    print("All House Robber tests passed successfully.")
