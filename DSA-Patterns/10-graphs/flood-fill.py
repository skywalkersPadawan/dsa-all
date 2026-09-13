"""
Flood Fill Algorithm

What it is:
An algorithm that determines and alters the area connected to a given node in a
multi-dimensional array. It is the algorithm behind the "paint bucket" tool in graphics programs.

When it is used:
- LeetCode 733 (Flood Fill).
- Color replacement in 2D image matrices.
- Territory conquest in grid games (Minesweeper, Go).

The Key Idea:
Starting from cell `(sr, sc)`:
1. Record `original_color = image[sr][sc]`.
2. If `original_color == new_color`, return image immediately (avoids infinite loops).
3. Use DFS or BFS to traverse all 4-directionally adjacent cells that have `original_color`
   and change their color to `new_color`.

Time Complexity:
- O(m * n) where m is rows and n is columns.

Space Complexity:
- O(m * n) call stack space in worst case.
"""


def flood_fill(
    image: list[list[int]], sr: int, sc: int, color: int
) -> list[list[int]]:
    """Performs flood fill starting at (sr, sc) with new color."""
    original_color = image[sr][sc]
    if original_color == color:
        return image

    rows = len(image)
    cols = len(image[0])

    def dfs(r: int, c: int) -> None:
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or image[r][c] != original_color
        ):
            return

        image[r][c] = color

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    filled = flood_fill(img, 1, 1, 2)
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert filled == expected

    # Already matching color
    img2 = [[0, 0, 0], [0, 0, 0]]
    assert flood_fill(img2, 0, 0, 0) == img2

    print("All Flood Fill tests passed successfully.")
