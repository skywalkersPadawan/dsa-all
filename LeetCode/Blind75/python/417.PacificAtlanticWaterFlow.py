from typing import List, Optional


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # pacific
        for r in range(ROWS):
            dfs(r, 0, pacific)
        for c in range(COLS):
            dfs(0, c, pacific)

        # atlantic
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)

        return list(pacific & atlantic)


# graph traversal just don't solve graph study the implementation take notes to understand the pattern
