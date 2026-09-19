"""
Connected Components in an Undirected Graph

What it is:
A connected component is a maximal set of vertices such that every pair of vertices
is connected by a path. This pattern identifies and counts all isolated subgraphs.

When it is used:
- Number of Connected Components in an Undirected Graph (LeetCode 323).
- Finding islands or isolated clusters of users/servers.
- Graph validity tests (trees must have exactly 1 connected component and V - 1 edges).

The Key Idea:
Outer Loop over all vertices 0 to n-1:
- Maintain a global `visited` set.
- For each vertex `i`:
  If `i` is not in `visited`:
    Increment component count!
    Trigger a DFS or BFS starting from `i` to mark all reachable nodes as visited.

Time Complexity:
- O(V + E) total time. Every vertex and edge is visited exactly once across all DFS/BFS calls.

Space Complexity:
- O(V) auxiliary space for visited set and recursion stack.
"""


def count_connected_components(
    num_nodes: int, edges: list[list[int]]
) -> tuple[int, list[list[int]]]:
    """Returns (total_components_count, list_of_components)."""
    # Build adjacency list
    graph: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited: set[int] = set()
    components: list[list[int]] = []

    def dfs(node: int, current_component: list[int]) -> None:
        visited.add(node)
        current_component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, current_component)

    for node in range(num_nodes):
        if node not in visited:
            component_nodes: list[int] = []
            dfs(node, component_nodes)
            components.append(component_nodes)

    return len(components), components


if __name__ == "__main__":
    # 5 nodes with edges [[0, 1], [1, 2], [3, 4]]
    # Component 1: {0, 1, 2}, Component 2: {3, 4} -> Total 2
    count, comp_list = count_connected_components(5, [[0, 1], [1, 2], [3, 4]])
    assert count == 2
    assert len(comp_list) == 2

    # Completely disconnected graph (5 nodes, 0 edges) -> Total 5
    count_iso, _ = count_connected_components(5, [])
    assert count_iso == 5

    print("All Connected Components tests passed successfully.")
