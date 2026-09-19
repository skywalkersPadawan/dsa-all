"""
0/1 Knapsack Problem

What it is:
Given weights and values of n items, and a knapsack of capacity W, find the maximum
value that can be put in the knapsack. Each item can be chosen at most ONCE (0 or 1).

When it is used:
- Resource selection under a strict constraint.
- Base archetype for Subset Sum, Partition Equal Subset Sum, Target Sum.

The Key Idea:
Let `dp[w]` be the maximum value achievable with capacity `w`.
For each item with `(weight, value)`:
Iterate capacity `w` BACKWARDS from `W` down to `weight`:
`dp[w] = max(dp[w], dp[w - weight] + value)`

Why Iterate Backwards in 1D DP?
Iterating backwards guarantees that each item is used at most ONCE!
(Forward iteration would allow the same item to be reused multiple times).

Time Complexity:
- O(n * W) pseudo-polynomial time.

Space Complexity:
- O(W) auxiliary space using 1D space optimization.
"""


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """Finds maximum value for 0/1 Knapsack with given capacity."""
    # dp[w] = max value with capacity w
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        # Iterate backwards to ensure 0/1 property (each item used at most once)
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]


if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    # Best choice: items 1 and 2 (weights 20 + 30 = 50, value 100 + 120 = 220)
    assert knapsack_01(weights, values, capacity) == 220

    # Capacity too small
    assert knapsack_01([10], [100], 5) == 0

    print("All 0/1 Knapsack tests passed successfully.")
