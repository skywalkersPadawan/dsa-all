"""
Topological Sort - DFS Postorder Reversal Pattern

What it is:
A recursive DFS approach to topological sorting. A vertex is pushed onto a stack
(or prepended to a list) ONLY AFTER all of its descendants have been fully explored.
Reversing the finish times yields a valid topological order.

When it is used:
- Alternative to Kahn's algorithm in recursive formulations.
- Course Schedule II (LeetCode 210).
- Strongly Connected Components (Tarjan's and Kosaraju's algorithms).

The Key Idea:
Use 3-Color DFS state to detect cycles and sort simultaneously:
- State 0: UNVISITED
- State 1: VISITING (in current recursion path; encountering this means CYCLE!)
- State 2: VISITED (finished exploring; safe)

When DFS finishes exploring all outgoing edges of node `u`, mark `state[u] = 2` and
append `u` to a result list.
Reversing this result list gives the correct topological order!

Time Complexity:
- O(V + E) linear time.

Space Complexity:
- O(V + E) for adjacency list and recursion stack.
"""


def topological_sort_dfs(num_nodes: int, edges: list[list[int]]) -> list[int]:
    """Computes topological sort using 3-color DFS."""
    graph: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)

    # 0 = UNVISITED, 1 = VISITING, 2 = VISITED
    state = [0] * num_nodes
    order: list[int] = []
    has_cycle = False

    def dfs(node: int) -> None:
        nonlocal has_cycle
        if has_cycle:
            return

        state[node] = 1  # Mark VISITING

        for neighbor in graph[node]:
            if state[neighbor] == 1:
                has_cycle = True
                return
            elif state[neighbor] == 0:
                dfs(neighbor)

        state[node] = 2  # Mark VISITED
        order.append(node)  # Postorder append

    for node in range(num_nodes):
        if state[node] == 0 and not has_cycle:
            dfs(node)

    if has_cycle:
        return []

    # Reversing postorder yields topological sort
    return order[::-1]


if __name__ == "__main__":
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    order = topological_sort_dfs(6, edges)
    assert len(order) == 6

    pos = {node: i for i, node in enumerate(order)}
    assert pos[5] < pos[2]
    assert pos[2] < pos[3]
    assert pos[3] < pos[1]

    # Cycle case
    assert topological_sort_dfs(3, [[0, 1], [1, 2], [2, 0]]) == []

    print("All DFS Topological Sort tests passed successfully.")
