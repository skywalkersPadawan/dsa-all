"""
N-Queens Pattern

What it is:
A classic constraint-satisfaction backtracking puzzle. The task is to place N non-attacking
queens on an N x N chessboard, such that no two queens share the same row, column, or diagonal.

When it is used:
- Classic interview problem testing deep understanding of backtracking and constraint checks.
- LeetCode 51 (N-Queens), LeetCode 52 (N-Queens II).

The Key Idea:
Place queens row by row from top to bottom (row 0 to N-1).
Since we place exactly one queen per row, row conflicts are automatically prevented.
We only need to track conflicts on:
1. Columns: `col in cols_used`
2. Positive Diagonals (bottom-left to top-right): `(row + col) in pos_diag_used`
3. Negative Diagonals (top-left to bottom-right): `(row - col) in neg_diag_used`

Using three hash sets allows checking conflict validity in O(1) time.

Time Complexity:
- O(N!) because the first queen has N choices, second has at most N-2 choices, etc.

Space Complexity:
- O(N) auxiliary space to store sets and current board configuration.

Common Pitfalls / Edge Cases:
- Calculating diagonal identifiers:
  - `row - col` is constant along '\' diagonals (negative slope).
  - `row + col` is constant along '/' diagonals (positive slope).
- N = 1 returns `[["Q"]]`.
- N = 2 and N = 3 have 0 solutions.
"""


def solve_n_queens(n: int) -> list[list[str]]:
    """Returns all distinct board configurations for the N-Queens puzzle.

    Time: O(N!), Space: O(N).
    """
    result: list[list[str]] = []
    # columns[r] = c means a queen is placed at board[r][c]
    queens_in_col = [-1] * n
    cols_used: set[int] = set()
    pos_diag_used: set[int] = set()  # row + col
    neg_diag_used: set[int] = set()  # row - col

    def build_board() -> list[str]:
        board = []
        for r in range(n):
            row_chars = ["."] * n
            row_chars[queens_in_col[r]] = "Q"
            board.append("".join(row_chars))

        return board

    def backtrack(row: int) -> None:
        if row == n:
            result.append(build_board())
            return

        for col in range(n):
            if (
                col in cols_used
                or (row + col) in pos_diag_used
                or (row - col) in neg_diag_used
            ):
                continue

            # Place queen
            queens_in_col[row] = col
            cols_used.add(col)
            pos_diag_used.add(row + col)
            neg_diag_used.add(row - col)
            backtrack(row + 1)

            # Undo placement
            cols_used.remove(col)
            pos_diag_used.remove(row + col)
            neg_diag_used.remove(row - col)
            queens_in_col[row] = -1

    backtrack(0)

    return result


if __name__ == "__main__":
    # N = 4 has exactly 2 solutions
    solutions_4 = solve_n_queens(4)
    assert len(solutions_4) == 2

    # N = 1 has 1 solution
    solutions_1 = solve_n_queens(1)
    assert solutions_1 == [["Q"]]

    # N = 2 and 3 have 0 solutions
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []

    # N = 8 has 92 solutions (standard chess board)
    solutions_8 = solve_n_queens(8)
    assert len(solutions_8) == 92
    print("All N-Queens tests passed successfully.")
