"""
Min Cost Climbing Stairs Pattern

What it is:
You are given an integer array `cost` where `cost[i]` is the cost of i-th step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or index 1.
Find the minimum cost to reach the top of the floor (past the last step).

When it is used:
- LeetCode 746 (Min Cost Climbing Stairs).
- Cost-minimization along step-wise path transitions.

The Key Idea:
Let `min_cost[i]` be the minimum cost to reach step `i`.
To reach step `i`, you came from either `i - 1` or `i - 2`.
`min_cost[i] = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])`

Optimized with two rolling variables:
`prev2 = 0` (cost to reach index 0)
`prev1 = 0` (cost to reach index 1)
For `i` from 2 to n:
`curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])`

Time Complexity:
- O(n) single pass.

Space Complexity:
- O(1) auxiliary space.
"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    """Calculates min cost to reach top of staircase in O(n) time and O(1) space."""
    prev2 = 0  # cost to reach step 0
    prev1 = 0  # cost to reach step 1

    for i in range(2, len(cost) + 1):
        curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2 = prev1
        prev1 = curr

    return prev1


if __name__ == "__main__":
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

    print("All Min Cost Climbing Stairs tests passed successfully.")
