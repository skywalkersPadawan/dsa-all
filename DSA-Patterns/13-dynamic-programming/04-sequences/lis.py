"""
Longest Increasing Subsequence (LIS)

What it is:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

When it is used:
- LeetCode 300 (Longest Increasing Subsequence).
- Russian Doll Envelopes (LeetCode 354).
- Patience Sorting card games and scheduling.

The Key Idea:
Approach 1: Classic DP - O(n^2)
`dp[i]` = length of LIS ending at index `i`.
For each `i`:
  For each `j` from 0 to `i - 1`:
    If `nums[j] < nums[i]`: `dp[i] = max(dp[i], dp[j] + 1)`.

Approach 2: Patience Sorting + Binary Search - O(n log n) (Optimal!)
Maintain an array `tails` where `tails[i]` stores the smallest tail of all increasing
subsequences of length `i + 1`.
For each `x` in `nums`:
  Use binary search (`bisect_left`) to find the first element in `tails` >= `x`.
  If found, overwrite it with `x` (lowers the bar for that length).
  If not found, append `x` to `tails` (extends the longest LIS found so far).
The length of `tails` at the end is the length of the LIS!

Time Complexity:
- Classic DP: O(n^2)
- Binary Search: O(n log n)

Space Complexity:
- O(n) auxiliary space.
"""

from bisect import bisect_left


def length_of_lis_dp(nums: list[int]) -> int:
    """Computes LIS using O(n^2) DP."""
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def length_of_lis_optimal(nums: list[int]) -> int:
    """Computes LIS using O(n log n) Patience Sorting + Binary Search."""
    tails: list[int] = []

    for x in nums:
        # Find index of first element >= x
        idx = bisect_left(tails, x)

        if idx == len(tails):
            tails.append(x)  # x extends LIS
        else:
            tails[idx] = x  # x replaces tails[idx] to maintain minimum tail

    return len(tails)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # LIS is [2, 3, 7, 101] -> length 4
    assert length_of_lis_dp(nums) == 4
    assert length_of_lis_optimal(nums) == 4

    assert length_of_lis_optimal([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis_optimal([7, 7, 7, 7]) == 1
    assert length_of_lis_optimal([]) == 0

    print("All LIS tests passed successfully.")
