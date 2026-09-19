"""
Breadth-First Search (BFS) on Graphs

What it is:
A fundamental graph traversal algorithm that explores all vertices at the present depth
level before moving on to vertices at the next depth level, using a FIFO queue (`collections.deque`).

When it is used:
- Finding the SHORTEST PATH between two nodes in an unweighted graph.
- Multi-source BFS (e.g. Rotting Oranges, 01 Matrix).
- Finding connected components.
- Level-order distance measurement.

The Key Idea:
1. Initialize `queue = deque([start_node])` and `visited = {start_node}`.
2. While queue is not empty:
   - Pop front node: `current = queue.popleft()`.
   - Process `current`.
   - For each neighbor of `current`:
     If neighbor not in `visited`:
       Add neighbor to `visited` IMMEDIATELY upon enqueueing.
       `queue.append(neighbor)`.

Time Complexity:
- O(V + E) linear time.

Space Complexity:
- O(V) auxiliary space for queue and visited set.

Common Pitfalls / Edge Cases:
- Adding neighbor to `visited` when POPPED instead of when ENQUEUED:
  Allows duplicate identical nodes to be enqueued multiple times, causing O(V^2) blowup.
  ALWAYS mark visited immediately upon enqueueing!
"""

from collections import deque


def bfs_traversal(graph: dict[int, list[int]], start_node: int) -> list[int]:
    """Traverses graph level by level and returns order of visited nodes."""
    visited: set[int] = {start_node}
    queue: deque[int] = deque([start_node])
    traversal_order: list[int] = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)  # Mark visited IMMEDIATELY
                queue.append(neighbor)

    return traversal_order


def shortest_path_unweighted(
    graph: dict[int, list[int]], start_node: int, target_node: int
) -> int:
    """Returns minimum number of edges from start_node to target_node, or -1 if unreachable."""
    if start_node == target_node:
        return 0

    visited: set[int] = {start_node}
    queue: deque[tuple[int, int]] = deque([(start_node, 0)])  # (node, current_distance)

    while queue:
        node, distance = queue.popleft()

        if node == target_node:
            return distance

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


if __name__ == "__main__":
    # Graph:
    #   0 --- 1 --- 3
    #   |     |
    #   2 ----+
    test_graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}

    order = bfs_traversal(test_graph, 0)
    assert order == [0, 1, 2, 3]

    # Shortest path: 0 to 3 is 2 edges (0 -> 1 -> 3)
    assert shortest_path_unweighted(test_graph, 0, 3) == 2
    assert shortest_path_unweighted(test_graph, 0, 0) == 0

    print("All Graph BFS tests passed successfully.")
