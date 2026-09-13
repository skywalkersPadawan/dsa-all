"""
Fibonacci Numbers (Dynamic Programming Progression)

What it is:
Computes the n-th Fibonacci number: F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2).
Serves as the canonical introduction to Dynamic Programming, illustrating:
1. Top-Down DP (Memoization)
2. Bottom-Up DP (Tabulation)
3. Space-Optimized DP (Rolling Variables)

When it is used:
- Teaching state transitions and memoization.
- Counting ways to reach a state.

The Key Idea:
- Naive recursion recomputes subproblems exponentially: O(2^n).
- Storing subproblem results reduces time to O(n).
- Since each state only depends on the previous TWO values, we only need 2 variables instead of an array!

Time Complexity:
- O(n) linear time.

Space Complexity:
- Space-Optimized: O(1) auxiliary space.
- Tabulation: O(n).
- Memoization: O(n) (call stack + memo dict).
"""


def fib_memo(n: int, memo: dict[int, int] | None = None) -> int:
    """Top-Down DP with Memoization. Time: O(n), Space: O(n)."""
    if memo is None:
        memo = {}

    if n <= 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tabulation(n: int) -> int:
    """Bottom-Up DP with Tabulation array. Time: O(n), Space: O(n)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fib_optimal(n: int) -> int:
    """Space-Optimized DP using two rolling variables. Time: O(n), Space: O(1)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0
    prev1 = 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


if __name__ == "__main__":
    for f in [fib_memo, fib_tabulation, fib_optimal]:
        assert f(0) == 0
        assert f(1) == 1
        assert f(2) == 1
        assert f(5) == 5
        assert f(10) == 55

    print("All Fibonacci DP tests passed successfully.")
