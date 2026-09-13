"""
Floyd-Warshall Algorithm (All-Pairs Shortest Path)

What it is:
A dynamic programming algorithm for finding shortest paths between ALL pairs of vertices
in a weighted graph with positive or negative edge weights (with no negative cycles).

When it is used:
- Dense graphs with small number of vertices (V <= 400) where all-pairs distances are needed.
- Transitive closure / reachability analysis.
- Graph diameter computation.

The Key Idea:
Let `dist[i][j]` be the shortest path from vertex `i` to vertex `j` using only a subset
of intermediate vertices `{0, 1, ..., k}`.
For each intermediate vertex `k` from 0 to V-1:
  For each source `i`:
    For each destination `j`:
      `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

Order of loops is CRUCIAL:
`k` (intermediate vertex) MUST be the outermost loop!

Time Complexity:
- O(V^3) three nested loops over V vertices.

Space Complexity:
- O(V^2) for the 2D distance matrix.
"""


def floyd_warshall(
    num_nodes: int, edges: list[list[int]]
) -> list[list[float]]:
    """Computes all-pairs shortest paths matrix in O(V^3) time.

    edges format: [u, v, weight] (directed).
    """
    # Initialize matrix: dist[i][i] = 0, others = infinity
    dist = [[float("inf")] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0

    for u, v, weight in edges:
        dist[u][v] = weight

    # k MUST be outermost loop: intermediate vertex
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    # 4 vertices:
    # 0 -> 1 (w=5), 0 -> 3 (w=10), 1 -> 2 (w=3), 2 -> 3 (w=1)
    edges = [[0, 1, 5], [0, 3, 10], [1, 2, 3], [2, 3, 1]]
    matrix = floyd_warshall(4, edges)

    # 0 to 3 via 0 -> 1 -> 2 -> 3 costs 5 + 3 + 1 = 9 (< direct 10)
    assert matrix[0][3] == 9
    assert matrix[0][1] == 5
    assert matrix[1][3] == 4
    assert matrix[3][0] == float("inf")  # unreachable directed

    print("All Floyd-Warshall tests passed successfully.")
