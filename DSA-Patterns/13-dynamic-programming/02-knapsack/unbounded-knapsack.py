"""
Unbounded Knapsack Problem

What it is:
Given weights and values of n items, and a knapsack of capacity W, find the maximum
value that can be put in the knapsack. Unlike 0/1 Knapsack, each item can be chosen
an UNLIMITED number of times.

When it is used:
- Coin Change II (LeetCode 518).
- Rod Cutting problem.
- Inventory restocking with unlimited item supplies.

The Key Idea:
Let `dp[w]` be the maximum value achievable with capacity `w`.
For each item with `(weight, value)`:
Iterate capacity `w` FORWARDS from `weight` up to `W`:
`dp[w] = max(dp[w], dp[w - weight] + value)`

Why Iterate Forwards?
Iterating forwards intentionally allows the current item to be selected multiple times!
`dp[w - weight]` may already include one or more copies of the current item.

Time Complexity:
- O(n * W) time.

Space Complexity:
- O(W) auxiliary space.
"""


def unbounded_knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """Finds maximum value when items can be reused an unlimited number of times."""
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        # Forward iteration enables unlimited reuse of the current item
        for w in range(weight, capacity + 1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]


if __name__ == "__main__":
    # Capacity = 100, items: (w=5, v=10), (w=10, v=30), (w=15, v=20)
    # Item 2 has best ratio: weight 10, value 30 -> take 10 of them -> value 300
    weights = [5, 10, 15]
    values = [10, 30, 20]
    capacity = 100

    assert unbounded_knapsack(weights, values, capacity) == 300

    # Single item reuse
    assert (
        unbounded_knapsack([2], [5], 7) == 15
    )  # 3 items of weight 2 = 6, value 3 * 5 = 15

    print("All Unbounded Knapsack tests passed successfully.")
