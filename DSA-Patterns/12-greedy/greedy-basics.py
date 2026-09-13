"""
Greedy Algorithm Basics

What it is:
An algorithmic paradigm that follows the problem-solving heuristic of making the
locally optimal choice at each stage with the intent of finding a global optimum.

When it is used:
- When a problem exhibits the GREEDY-CHOICE PROPERTY: a global optimum can be arrived
  at by selecting a local optimum without ever backtracking or reconsidering.
- When the problem exhibits OPTIMAL SUBSTRUCTURE: an optimal solution to the problem
  contains within it optimal solutions to subproblems.

The Key Question to Ask:
"If I make the best decision right now, will I ever need to undo or reconsider it later?"
If NO -> Greedy works!
If YES (choices have trade-offs that restrict future options) -> Dynamic Programming or Backtracking.

Classic Examples:
- Making change with standard currency denominations (e.g. 25c, 10c, 5c, 1c).
- Dijkstra's shortest path (picking the currently closest unvisited node).
- Fractional Knapsack (picking items by highest value-to-weight ratio).
- Kruskal's and Prim's Minimum Spanning Tree.

Time Complexity:
- Usually dominated by sorting: O(n log n), followed by a single linear pass O(n).

Space Complexity:
- Typically O(1) or O(n).
"""


def min_coins_canonical(coins: list[int], amount: int) -> int:
    """Finds min coins needed for a canonical coin system (e.g. US coins [25, 10, 5, 1])

    where greedy is mathematically guaranteed to be optimal.
    NOTE: For general coin systems, use Dynamic Programming (Coin Change - LeetCode 322).
    """
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if amount == 0:
            break
        num_coins = amount // coin
        count += num_coins
        amount -= num_coins * coin

    return count if amount == 0 else -1


if __name__ == "__main__":
    us_coins = [25, 10, 5, 1]
    # 63 cents = 2 * 25 + 1 * 10 + 3 * 1 = 6 coins
    assert min_coins_canonical(us_coins, 63) == 6
    # 30 cents = 1 * 25 + 1 * 5 = 2 coins
    assert min_coins_canonical(us_coins, 30) == 2

    print("All Greedy Basics tests passed successfully.")
