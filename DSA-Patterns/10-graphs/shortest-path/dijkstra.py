"""
Dijkstra's Algorithm (Single-Source Shortest Path)

What it is:
Finds the shortest paths from a single source vertex to all other vertices in a
weighted graph with NON-NEGATIVE edge weights using a greedy min-heap approach.

When it is used:
- Network routing protocols (OSPF).
- GPS navigation and mapping systems.
- LeetCode 743 (Network Delay Time).
- LeetCode 787 (Cheapest Flights Within K Stops - variation).

The Key Idea:
Greedy expansion using a min-heap (`heapq` in Python):
1. Maintain `distances = [infinity] * V` with `distances[source] = 0`.
2. Push `(0, source)` into min-heap.
3. While min-heap is not empty:
   - Pop `(curr_dist, u)` with the minimum distance.
   - If `curr_dist > distances[u]`, skip it (stale entry).
   - For each neighbor `(v, weight)` of `u`:
     If `curr_dist + weight < distances[v]`:
       Relax the edge: `distances[v] = curr_dist + weight`.
       Push `(distances[v], v)` into min-heap.

Time Complexity:
- O((V + E) log V) with a binary min-heap.

Space Complexity:
- O(V + E) to store the graph and priority queue.

Common Pitfalls / Edge Cases:
- Graphs with NEGATIVE edge weights: Dijkstra fails because the greedy assumption is violated.
  Use Bellman-Ford instead.
- Forgetting to skip stale entries `if curr_dist > distances[u]` causes redundant edge checks.
"""

from collections import defaultdict
import heapq


def dijkstra(
    num_nodes: int, edges: list[list[int]], source: int
) -> dict[int, float]:
    """Finds shortest distance from source to all nodes 0..num_nodes-1.

    edges format: [u, v, weight] (directed edge).
    """
    graph: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))

    distances: dict[int, float] = {node: float("inf") for node in range(num_nodes)}
    distances[source] = 0

    # Min-heap stores tuples of: (distance_so_far, node)
    min_heap: list[tuple[float, int]] = [(0, source)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Skip stale entries with larger distance than already recorded
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


if __name__ == "__main__":
    # Graph:
    # 0 -> 1 (w=4), 0 -> 2 (w=1)
    # 2 -> 1 (w=2)
    # 1 -> 3 (w=1)
    # 2 -> 3 (w=5)
    edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]]
    dists = dijkstra(4, edges, source=0)

    assert dists[0] == 0
    assert dists[2] == 1
    assert dists[1] == 3  # 0 -> 2 -> 1 (1 + 2 = 3) is cheaper than 0 -> 1 (4)
    assert dists[3] == 4  # 0 -> 2 -> 1 -> 3 (1 + 2 + 1 = 4)

    print("All Dijkstra's Algorithm tests passed successfully.")
