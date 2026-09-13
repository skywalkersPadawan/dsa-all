"""
Cycle Detection in Graphs

What it is:
Determines whether a graph contains at least one cycle.
The algorithms differ significantly between directed and undirected graphs:
1. Undirected Graph: DFS with a `parent` pointer.
2. Directed Graph: DFS with 3-color states (Unvisited, Visiting/In-Stack, Visited/Done).

When it is used:
- Deadlock detection in operating systems.
- Circular dependency checking (Course Schedule - LeetCode 207).
- Validating tree structures (a tree is a connected graph with no cycles).

The Key Idea:
- Undirected Graph:
  During DFS from node `u` to neighbor `v`:
  If `v` is already visited AND `v != parent`, then an alternative path exists back to `v` -> CYCLE!
- Directed Graph (3-Color State):
  State 0 = UNVISITED
  State 1 = VISITING (currently in active recursion call stack)
  State 2 = VISITED (all descendants fully explored)
  If we encounter a neighbor in state 1 (VISITING), it is a BACK-EDGE -> CYCLE!

Time Complexity:
- O(V + E) for both.

Space Complexity:
- O(V) for visited arrays / recursion stack.
"""


def has_cycle_undirected(
    num_nodes: int, edges: list[list[int]]
) -> bool:
    """Detects cycles in an undirected graph using DFS + parent pointer."""
    graph: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited: set[int] = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Visited and not parent means cycle!
                return True
        return False

    for node in range(num_nodes):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


def has_cycle_directed(num_nodes: int, edges: list[list[int]]) -> bool:
    """Detects cycles in a directed graph using 3-color DFS (LeetCode 207)."""
    graph: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)

    # 0 = UNVISITED, 1 = VISITING, 2 = VISITED
    state = [0] * num_nodes

    def dfs(node: int) -> bool:
        state[node] = 1  # Mark VISITING

        for neighbor in graph[node]:
            if state[neighbor] == 1:
                return True  # Found cycle (back edge)
            if state[neighbor] == 0:
                if dfs(neighbor):
                    return True

        state[node] = 2  # Mark VISITED
        return False

    for node in range(num_nodes):
        if state[node] == 0:
            if dfs(node):
                return True

    return False


if __name__ == "__main__":
    # Undirected with cycle: 0 - 1 - 2 - 0
    assert has_cycle_undirected(3, [[0, 1], [1, 2], [2, 0]]) is True
    # Undirected without cycle: 0 - 1 - 2
    assert has_cycle_undirected(3, [[0, 1], [1, 2]]) is False

    # Directed with cycle: 0 -> 1 -> 2 -> 0
    assert has_cycle_directed(3, [[0, 1], [1, 2], [2, 0]]) is True
    # Directed without cycle (DAG): 0 -> 1 -> 2
    assert has_cycle_directed(3, [[0, 1], [1, 2]]) is False

    print("All Cycle Detection tests passed successfully.")
