"""
Unique Paths (Grid DP Pattern)

What it is:
A robot is located at the top-left corner of an m x n grid. The robot can only move
either down or right at any point in time. The robot is trying to reach the bottom-right corner.
How many possible unique paths are there?

When it is used:
- LeetCode 62 (Unique Paths).
- LeetCode 63 (Unique Paths II - with obstacles).
- Lattice path combinatorics.

The Key Idea:
To reach cell `(r, c)`, the robot must come from either:
- The cell above: `(r - 1, c)`
- The cell to the left: `(r, c - 1)`
State Transition:
`dp[r][c] = dp[r - 1][c] + dp[r][c - 1]`

Base Case:
The first row and first column have only 1 unique path: `dp[0][c] = 1`, `dp[r][0] = 1`.

Space Optimization:
Only the previous row is needed:
`dp[c] = dp[c] + dp[c - 1]`.

Time Complexity:
- O(m * n).

Space Complexity:
- O(n) using 1D space optimization (or O(m * n) 2D table).
"""


def unique_paths(m: int, n: int) -> int:
    """Calculates number of unique paths from (0, 0) to (m-1, n-1) in O(m * n) time and O(n) space."""
    # dp[c] stores ways to reach current cell in column c
    dp = [1] * n

    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]

    return dp[n - 1]


if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3  # (R->D->D), (D->R->D), (D->D->R)
    assert unique_paths(1, 1) == 1

    print("All Unique Paths tests passed successfully.")
