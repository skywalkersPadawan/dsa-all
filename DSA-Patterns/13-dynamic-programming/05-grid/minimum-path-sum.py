"""
Minimum Path Sum (Grid DP Pattern)

What it is:
Given an m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.
You can only move either down or right at any point in time.

When it is used:
- LeetCode 64 (Minimum Path Sum).
- Routing on cost grids / raster terrain elevation surfaces.

The Key Idea:
Let `dp[r][c]` be the minimum path sum to reach cell `(r, c)`.
To reach `(r, c)` from top-left, we must arrive from either the cell above `(r - 1, c)`
or the cell to the left `(r, c - 1)`:
`dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])`

Base Cases:
- Top-left: `dp[0][0] = grid[0][0]`
- First row: `dp[0][c] = dp[0][c - 1] + grid[0][c]` (can only come from left)
- First col: `dp[r][0] = dp[r - 1][0] + grid[r][0]` (can only come from above)

Space Optimization:
Can be done in-place inside `grid` or with a single 1D array of size n.

Time Complexity:
- O(m * n) visiting each cell once.

Space Complexity:
- O(n) using 1D DP array.
"""


def min_path_sum(grid: list[list[int]]) -> int:
    """Finds minimum path sum from (0, 0) to (m-1, n-1)."""
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])

    dp = [0] * n
    dp[0] = grid[0][0]

    # Initialize first row
    for c in range(1, n):
        dp[c] = dp[c - 1] + grid[0][c]

    # Process remaining rows
    for r in range(1, m):
        dp[0] += grid[r][0]  # first column can only come from above
        for c in range(1, n):
            dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

    return dp[n - 1]


if __name__ == "__main__":
    test_grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # Path: 1 -> 3 -> 1 -> 1 -> 1 = 7
    assert min_path_sum(test_grid) == 7

    assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12
    assert min_path_sum([[5]]) == 5

    print("All Minimum Path Sum tests passed successfully.")
