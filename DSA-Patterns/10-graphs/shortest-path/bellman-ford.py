"""
Bellman-Ford Algorithm (Single-Source Shortest Path with Negative Weights)

What it is:
Computes shortest paths from a single source vertex to all other vertices in a weighted digraph.
Unlike Dijkstra's algorithm, Bellman-Ford can handle graphs with NEGATIVE edge weights and
can DETECT NEGATIVE WEIGHT CYCLES.

When it is used:
- Graphs that contain negative edge weights.
- Detecting arbitrage in currency exchange rates.
- Distance-Vector routing protocols (e.g., RIP).

The Key Idea:
Principle of Relaxation:
In any graph with V vertices, the shortest simple path between any two vertices has
at most V - 1 edges.
1. Initialize `distances = [infinity] * V`, `distances[source] = 0`.
2. Relax ALL edges `(u, v, weight)` repeatedly `V - 1` times:
   `if distances[u] + weight < distances[v]: distances[v] = distances[u] + weight`.
3. Negative Cycle Check (The V-th Pass):
   Relax all edges one more time. If any distance can STILL be improved,
   a NEGATIVE WEIGHT CYCLE exists!

Time Complexity:
- O(V * E) time (slower than Dijkstra, but works with negative weights).

Space Complexity:
- O(V) auxiliary space for distances.
"""


def bellman_ford(
    num_nodes: int, edges: list[list[int]], source: int
) -> tuple[dict[int, float] | None, bool]:
    """Computes shortest paths from source.

    Returns (distances, has_negative_cycle).
    If a negative cycle is detected, returns (None, True).
    """
    distances: dict[int, float] = {node: float("inf") for node in range(num_nodes)}
    distances[source] = 0

    # Step 1: Relax all edges (V - 1) times
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        if not updated:
            break  # Early termination if distances stop changing

    # Step 2: Check for negative-weight cycles (V-th relaxation)
    for u, v, weight in edges:
        if distances[u] != float("inf") and distances[u] + weight < distances[v]:
            # Negative cycle detected!
            return None, True

    return distances, False


if __name__ == "__main__":
    # Graph without negative cycles
    edges = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3],
    ]
    dists, has_cycle = bellman_ford(5, edges, source=0)
    assert has_cycle is False
    assert dists is not None
    assert dists[0] == 0
    assert dists[1] == -1
    assert dists[2] == 2
    assert dists[3] == -2
    assert dists[4] == 1

    # Graph with negative cycle: 0 -> 1 (1), 1 -> 2 (-3), 2 -> 0 (1) -> cycle sum = -1
    cycle_edges = [[0, 1, 1], [1, 2, -3], [2, 0, 1]]
    _, has_cycle = bellman_ford(3, cycle_edges, source=0)
    assert has_cycle is True

    print("All Bellman-Ford tests passed successfully.")
