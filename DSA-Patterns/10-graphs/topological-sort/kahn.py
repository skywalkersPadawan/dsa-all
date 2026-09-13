"""
Topological Sort - Kahn's Algorithm (BFS In-Degree Pattern)

What it is:
A linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every
directed edge u -> v, vertex u comes before vertex v in the ordering.
Kahn's algorithm accomplishes this iteratively using in-degrees and a queue.

When it is used:
- Build dependency resolution (e.g., Makefile, package managers like pip/npm).
- Course Schedule I & II (LeetCode 207, 210).
- Task scheduling with prerequisites.
- Cycle detection in directed graphs: if the topological sort does not contain all V vertices,
  the graph contains a cycle!

The Key Idea:
1. Compute the `in_degree` (number of incoming directed edges) for each vertex.
2. Initialize a queue with all vertices having `in_degree == 0` (nodes with zero dependencies).
3. While queue is not empty:
   - Pop vertex `u`. Append `u` to `topological_order`.
   - For each neighbor `v` of `u`:
     - Decrement `in_degree[v] -= 1` (simulates removing dependency `u`).
     - If `in_degree[v] == 0`: enqueue `v`.
4. If `len(topological_order) == num_nodes`, return the order.
   Otherwise, a cycle exists (return empty list).

Time Complexity:
- O(V + E) linear time.

Space Complexity:
- O(V + E) for adjacency list, in-degree array, and queue.
"""

from collections import deque


def topological_sort_kahn(
    num_nodes: int, edges: list[list[int]]
) -> list[int]:
    """Computes topological order of DAG nodes 0..num_nodes-1 using Kahn's algorithm."""
    graph: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    in_degree = [0] * num_nodes

    for u, v in edges:  # directed edge u -> v
        graph[u].append(v)
        in_degree[v] += 1

    # Queue contains all nodes with no incoming dependencies
    queue: deque[int] = deque(
        [node for node in range(num_nodes) if in_degree[node] == 0]
    )
    topological_order: list[int] = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If count of visited nodes != num_nodes, graph has a cycle
    if len(topological_order) == num_nodes:
        return topological_order
    else:
        return []  # Cycle detected


if __name__ == "__main__":
    # DAG: 5 -> 2, 5 -> 0, 4 -> 0, 4 -> 1, 2 -> 3, 3 -> 1
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    order = topological_sort_kahn(6, edges)
    assert len(order) == 6
    # Verify relative order of dependencies
    pos = {node: i for i, node in enumerate(order)}
    assert pos[5] < pos[2]
    assert pos[2] < pos[3]
    assert pos[3] < pos[1]
    assert pos[4] < pos[0]

    # Graph with cycle: 0 -> 1 -> 2 -> 0
    cycle_edges = [[0, 1], [1, 2], [2, 0]]
    assert topological_sort_kahn(3, cycle_edges) == []

    print("All Kahn's Algorithm tests passed successfully.")
