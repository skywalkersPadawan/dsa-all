"""
Depth-First Search (DFS) on Graphs

What it is:
A fundamental graph traversal algorithm that explores as deep as possible along each
branch before backtracking, using a recursion call stack (or explicit LIFO stack) and
a `visited` set to avoid infinite loops in cyclic graphs.

When it is used:
- Finding connected components.
- Cycle detection in directed and undirected graphs.
- Topological sorting.
- Solving mazes and path-finding puzzles.

The Key Idea:
1. Mark the current node as `visited`.
2. Process the current node.
3. For each unvisited neighbor of current node:
   Recursively call `dfs(neighbor)`.

Time Complexity:
- O(V + E) where V is vertices and E is edges (every vertex and edge visited once).

Space Complexity:
- O(V) auxiliary space for visited set and call stack.
"""


def dfs_recursive(
    graph: dict[int, list[int]],
    start_node: int,
    visited: set[int] | None = None,
) -> list[int]:
    """Traverses graph using recursive DFS and returns order of visited nodes."""
    if visited is None:
        visited = set()

    traversal_order: list[int] = []

    def dfs(node: int) -> None:
        visited.add(node)
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_node)
    return traversal_order


def dfs_iterative(graph: dict[int, list[int]], start_node: int) -> list[int]:
    """Traverses graph using iterative DFS with an explicit stack."""
    visited: set[int] = set()
    traversal_order: list[int] = []
    stack: list[int] = [start_node]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        traversal_order.append(node)

        # Reverse neighbors to preserve natural left-to-right order
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return traversal_order


if __name__ == "__main__":
    # Graph:
    #   0 --- 1 --- 3
    #   |     |
    #   2 ----+
    test_graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}

    rec_order = dfs_recursive(test_graph, 0)
    assert rec_order[0] == 0
    assert len(rec_order) == 4

    iter_order = dfs_iterative(test_graph, 0)
    assert iter_order[0] == 0
    assert len(iter_order) == 4

    print("All Graph DFS tests passed successfully.")
