"""
Graph Representation Patterns

What it is:
Fundamental techniques for representing graphs in memory:
1. Adjacency List: Dictionary mapping each node to a list of its neighboring nodes.
2. Adjacency Matrix: 2D array where `matrix[u][v]` indicates an edge between u and v.
3. Edge List: List of tuples `(u, v, weight)`.

When it is used:
- Adjacency List: Preferred for SPARSE graphs (E << V^2). Standard in almost all coding interviews.
- Adjacency Matrix: Preferred for DENSE graphs (E ~ V^2) or when O(1) edge lookup is critical.
- Edge List: Used directly in Kruskal's Minimum Spanning Tree algorithm.

Time & Space Complexity:
| Representation | Space | Add Edge | Check Edge (u, v) | Iterate Neighbors of u |
| :--- | :--- | :--- | :--- | :--- |
| Adjacency List | O(V + E) | O(1) | O(deg(u)) | O(deg(u)) |
| Adjacency Matrix | O(V^2) | O(1) | O(1) | O(V) |
| Edge List | O(E) | O(1) | O(E) | O(E) |
"""

from collections import defaultdict


def build_adjacency_list(
    num_nodes: int, edges: list[list[int]], directed: bool = False
) -> dict[int, list[int]]:
    """Constructs an adjacency list from edge pairs."""
    graph: defaultdict[int, list[int]] = defaultdict(list)
    # Ensure all nodes from 0 to num_nodes - 1 are represented
    for node in range(num_nodes):
        graph[node] = []

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return dict(graph)


def build_adjacency_matrix(
    num_nodes: int, edges: list[list[int]], directed: bool = False
) -> list[list[int]]:
    """Constructs a V x V adjacency matrix from edge pairs."""
    matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1

    return matrix


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    num_nodes = 4

    adj_list = build_adjacency_list(num_nodes, edges, directed=False)
    assert adj_list[0] == [1, 2]
    assert adj_list[3] == [2]

    adj_matrix = build_adjacency_matrix(num_nodes, edges, directed=False)
    assert adj_matrix[0][1] == 1
    assert adj_matrix[1][0] == 1
    assert adj_matrix[0][3] == 0

    print("All Graph Representation tests passed successfully.")
