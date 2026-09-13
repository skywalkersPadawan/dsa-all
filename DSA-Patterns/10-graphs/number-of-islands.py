"""
Number of Islands (Grid BFS / DFS Pattern)

What it is:
Given an m x n 2D binary grid representing a map of '1's (land) and '0's (water),
returns the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.

When it is used:
- LeetCode 200 (Number of Islands).
- Max Area of Island (LeetCode 695).
- Connected component counting on 2D grids.

The Key Idea:
Scan through every cell in the grid:
- When land `'1'` is encountered:
  - Increment island count by 1.
  - Launch a DFS (or BFS) to "sink" the entire island (overwrite all reachable connected `'1'`s
    with `'0'` in-place, or mark in a visited set).
  - This guarantees each connected land mass is counted exactly once.

Time Complexity:
- O(m * n) where m is rows and n is columns. Every cell is visited at most a constant number of times.

Space Complexity:
- O(m * n) worst-case call stack depth (when grid is filled entirely with land).
"""


def num_islands(grid: list[list[str]]) -> int:
    """Counts number of 4-directionally connected islands."""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def dfs(r: int, c: int) -> None:
        # Check boundary and water condition
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        # Sink current land cell to water
        grid[r][c] = "0"

        # Explore 4 orthogonal neighbors
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                island_count += 1
                dfs(r, c)

    return island_count


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands(grid1) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid2) == 3

    print("All Number of Islands tests passed successfully.")
