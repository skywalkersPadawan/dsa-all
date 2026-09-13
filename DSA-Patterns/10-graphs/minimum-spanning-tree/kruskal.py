"""
Kruskal's Algorithm (Minimum Spanning Tree)

What it is:
A greedy algorithm that finds a Minimum Spanning Tree (MST) for a connected, weighted
undirected graph. An MST connects all vertices together with the minimum possible
total edge weight and without cycles.

When it is used:
- Network infrastructure design (telecom cabling, pipeline routing).
- Approximation algorithms for NP-hard problems (metric TSP).
- Clustering in machine learning (single-linkage clustering).
- LeetCode 1584 (Min Cost to Connect All Points).

The Key Idea:
Greedy Edge Selection with Union-Find (DSU):
1. Sort all edges in non-decreasing order of their weights.
2. Initialize a Disjoint Set Union (DSU) data structure with all V vertices.
3. For each edge `(u, v, weight)` in sorted order:
   - Check if `find(u) != find(v)` (they belong to different components).
   - If YES: union them, add the edge to MST, add weight to total cost.
   - If NO: discard the edge (it would form a cycle).
4. Stop when the MST contains exactly `V - 1` edges.

Time Complexity:
- O(E log E) or O(E log V) to sort the edges. DSU operations take near-O(1) time.

Space Complexity:
- O(V) for the Union-Find structure.
"""


class DisjointSetUnion:
    """Disjoint Set Union with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False  # Already connected

        # Union by rank
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        return True


def kruskal_mst(
    num_nodes: int, edges: list[list[int]]
) -> tuple[int, list[list[int]]]:
    """Finds Minimum Spanning Tree using Kruskal's algorithm.

    edges format: [u, v, weight]
    Returns (total_mst_weight, list_of_mst_edges).
    """
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    dsu = DisjointSetUnion(num_nodes)

    mst_weight = 0
    mst_edges: list[list[int]] = []

    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append([u, v, weight])
            if len(mst_edges) == num_nodes - 1:
                break

    return mst_weight, mst_edges


if __name__ == "__main__":
    # Graph with 4 nodes:
    # 0 - 1 (w=10), 0 - 2 (w=6), 0 - 3 (w=5), 1 - 3 (w=15), 2 - 3 (w=4)
    edges = [
        [0, 1, 10],
        [0, 2, 6],
        [0, 3, 5],
        [1, 3, 15],
        [2, 3, 4],
    ]
    # MST chooses: 2-3 (4), 0-3 (5), 0-1 (10) -> total weight = 19
    total_weight, chosen_edges = kruskal_mst(4, edges)
    assert total_weight == 19
    assert len(chosen_edges) == 3

    print("All Kruskal's Algorithm tests passed successfully.")
