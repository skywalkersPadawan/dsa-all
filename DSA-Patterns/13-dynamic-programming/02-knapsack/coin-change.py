"""
Coin Change Pattern

What it is:
1. Coin Change I (LeetCode 322): Minimum number of coins needed to make up amount.
2. Coin Change II (LeetCode 518): Total number of combinations to make up amount.
Both allow unlimited reuse of each coin denomination (Unbounded Knapsack).

When it is used:
- Canonical unbounded knapsack problems in technical interviews.

The Key Idea:
- Coin Change I (Min Coins):
  `dp[a]` = min coins to make amount `a`.
  Initialize `dp = [amount + 1] * (amount + 1)`, `dp[0] = 0`.
  For each coin:
    For `a` from `coin` to `amount`:
      `dp[a] = min(dp[a], dp[a - coin] + 1)`
  Return `dp[amount]` if `<= amount` else `-1`.

- Coin Change II (Number of Combinations):
  `dp[a]` = number of combinations to make amount `a`.
  Initialize `dp[0] = 1`.
  Outer loop MUST iterate over coins (to avoid counting permutations):
  For each coin:
    For `a` from `coin` to `amount`:
      `dp[a] += dp[a - coin]`

Time Complexity:
- O(coins * amount).

Space Complexity:
- O(amount) auxiliary space.
"""


def coin_change_min_coins(coins: list[int], amount: int) -> int:
    """Finds minimum coins needed to make up amount, or -1 if impossible (LeetCode 322)."""
    # Initialize with amount + 1 as infinity
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1


def coin_change_num_ways(coins: list[int], amount: int) -> int:
    """Finds number of distinct combinations to make up amount (LeetCode 518)."""
    dp = [0] * (amount + 1)
    dp[0] = 1

    # Outer loop on coins ensures combinations (not permutations)
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


if __name__ == "__main__":
    # Min coins
    assert coin_change_min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change_min_coins([2], 3) == -1  # impossible
    assert coin_change_min_coins([1], 0) == 0

    # Num ways
    assert (
        coin_change_num_ways([1, 2, 5], 5) == 4
    )  # 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1
    assert coin_change_num_ways([2], 3) == 0
    assert coin_change_num_ways([10], 10) == 1

    print("All Coin Change tests passed successfully.")
