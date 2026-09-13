"""
Bipartite Graph Validation (2-Coloring Pattern)

What it is:
A graph is bipartite if its vertices can be divided into two independent sets,
A and B, such that every edge connects a vertex in A to a vertex in B
(no two adjacent vertices share the same set / color).

When it is used:
- Is Graph Bipartite? (LeetCode 785).
- Possible Bipartition (LeetCode 886).
- Matching problems and timetable/scheduling conflict resolution.

The Key Idea:
BFS / DFS 2-Coloring:
1. Maintain a `color` array where each node is uncolored (`0`), or colored with `1` or `-1`.
2. Iterate through all nodes 0 to n-1 (to handle disconnected components).
3. If a node is uncolored:
   - Assign color `1`.
   - Use BFS or DFS: for each neighbor, if uncolored, assign `-color[node]`.
   - If neighbor is already colored and has the SAME color as `color[node]`:
     The graph CANNOT be bipartite! Return False immediately.
4. If all components are validly 2-colored, the graph is bipartite.

Theorem:
A graph is bipartite if and only if it contains no odd-length cycles!

Time Complexity:
- O(V + E) linear time.

Space Complexity:
- O(V) auxiliary space for color array and queue/call stack.
"""

from collections import deque


def is_bipartite(graph: list[list[int]]) -> bool:
    """Returns True if the undirected graph is bipartite (LeetCode 785)."""
    n = len(graph)
    # 0 = uncolored, 1 = red, -1 = blue
    color = [0] * n

    for start_node in range(n):
        if color[start_node] != 0:
            continue

        # BFS 2-coloring
        queue: deque[int] = deque([start_node])
        color[start_node] = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    # Color neighbor with opposite color
                    color[neighbor] = -color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # Conflict: two adjacent nodes have same color!
                    return False

    return True


if __name__ == "__main__":
    # Bipartite graph (even cycle of 4 nodes: 0-1-2-3-0)
    # 0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]
    graph_even = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert is_bipartite(graph_even) is True

    # Non-bipartite graph (odd cycle of 3 nodes: 0-1-2-0)
    # 0: [1, 2], 1: [0, 2], 2: [0, 1]
    graph_odd = [[1, 2], [0, 2], [0, 1]]
    assert is_bipartite(graph_odd) is False

    print("All Bipartite Graph tests passed successfully.")
