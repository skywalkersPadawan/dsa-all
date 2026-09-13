"""
Prim's Algorithm (Minimum Spanning Tree)

What it is:
A greedy algorithm that finds a Minimum Spanning Tree (MST) by growing a single tree
one vertex at a time from an arbitrary starting vertex using a priority queue (min-heap).

When it is used:
- Dense graphs where E approaches V^2 (Prim with adjacency matrix/heap outperforms Kruskal).
- LeetCode 1584 (Min Cost to Connect All Points).

The Key Idea:
Greedy Vertex Expansion (similar to Dijkstra):
1. Start with an arbitrary vertex (e.g. node 0) in the MST. Mark it visited.
2. Push all edges outgoing from node 0 into a min-heap: `(weight, u, v)`.
3. While the min-heap is not empty and the MST has fewer than `V` vertices:
   - Pop the minimum weight edge `(weight, u, v)`.
   - If destination vertex `v` is already visited, continue (discard).
   - Otherwise, mark `v` as visited, add `weight` to total MST cost, and add edge to MST.
   - For each unvisited neighbor of `v`, push `(neighbor_weight, v, neighbor)` into min-heap.

Time Complexity:
- O(E log V) with a binary min-heap.

Space Complexity:
- O(V + E) for adjacency list and priority queue.
"""

from collections import defaultdict
import heapq


def prim_mst(
    num_nodes: int, edges: list[list[int]]
) -> tuple[int, list[list[int]]]:
    """Finds Minimum Spanning Tree using Prim's algorithm.

    edges format: [u, v, weight] (undirected).
    Returns (total_mst_weight, list_of_mst_edges).
    """
    # Build undirected adjacency list
    graph: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    visited: set[int] = set()
    mst_edges: list[list[int]] = []
    mst_weight = 0

    # Start from vertex 0: push initial edges into min-heap (weight, from_node, to_node)
    min_heap: list[tuple[int, int, int]] = []
    visited.add(0)
    for neighbor, weight in graph[0]:
        heapq.heappush(min_heap, (weight, 0, neighbor))

    while min_heap and len(visited) < num_nodes:
        weight, u, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        visited.add(v)
        mst_weight += weight
        mst_edges.append([u, v, weight])

        for next_neighbor, next_weight in graph[v]:
            if next_neighbor not in visited:
                heapq.heappush(min_heap, (next_weight, v, next_neighbor))

    return mst_weight, mst_edges


if __name__ == "__main__":
    edges = [
        [0, 1, 10],
        [0, 2, 6],
        [0, 3, 5],
        [1, 3, 15],
        [2, 3, 4],
    ]
    total_weight, chosen_edges = prim_mst(4, edges)
    assert total_weight == 19
    assert len(chosen_edges) == 3

    print("All Prim's Algorithm tests passed successfully.")
