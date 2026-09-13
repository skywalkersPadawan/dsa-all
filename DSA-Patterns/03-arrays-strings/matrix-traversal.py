"""
Matrix Traversal Patterns

What it is:
Techniques for navigating and inspecting 2D grids (matrices), including:
1. Direction vectors for adjacent cell exploration (DFS/BFS grid navigation).
2. Boundary simulation (Spiral Matrix traversal).
3. Diagonal traversal.

When it is used:
- Spiral Matrix (LeetCode 54).
- Number of Islands, Flood Fill, Word Search (4-directional traversal).
- Image rotation / Transposition.

The Key Idea:
- Direction Vectors:
  Define `directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]` for (Right, Down, Left, Up).
  Next cell is `(row + dr, col + dc)`.
  Check valid bounds: `0 <= new_row < rows and 0 <= new_col < cols`.
- Spiral Traversal:
  Maintain four boundary boundaries: `top`, `bottom`, `left`, `right`.
  Traverse top row (left -> right), increment `top`.
  Traverse right col (top -> bottom), decrement `right`.
  Traverse bottom row (right -> left), decrement `bottom` (if `top <= bottom`).
  Traverse left col (bottom -> top), increment `left` (if `left <= right`).

Time Complexity:
- O(rows * cols) visiting every cell exactly once.

Space Complexity:
- O(1) auxiliary space (excluding output array).

Common Pitfalls / Edge Cases:
- Spiral traversal on non-square matrices (e.g. 1 x 5 or 5 x 1):
  Must check `if top <= bottom` and `if left <= right` before traversing backwards.
- Matrix with 0 rows or 0 columns.
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Traverses an m x n matrix in spiral order.

    (LeetCode 54 - Spiral Matrix)
    Time: O(m * n), Space: O(1) auxiliary.
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # 1. Traverse Right along current top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 2. Traverse Down along current right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # 3. Traverse Left along current bottom row (if row still remains)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # 4. Traverse Up along current left column (if column still remains)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def get_neighbors_4_dir(
    row: int, col: int, rows: int, cols: int
) -> list[tuple[int, int]]:
    """Generates valid 4-directional orthogonal neighbors for a given grid cell."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))

    return neighbors


if __name__ == "__main__":
    # Test spiral matrix 3x3
    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix_3x3) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test spiral matrix rectangular 3x4
    matrix_3x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(matrix_3x4) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]

    # Test single row
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]

    # Test single col
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]

    # Test neighbors helper
    neighbors = get_neighbors_4_dir(0, 0, 3, 3)
    assert neighbors == [(0, 1), (1, 0)]  # only Right and Down valid at (0, 0)

    print("All Matrix Traversal tests passed successfully.")
