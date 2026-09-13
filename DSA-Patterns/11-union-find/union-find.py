"""
Union-Find / Disjoint Set Union (DSU)

What it is:
A data structure that tracks a partition of a set into disjoint (non-overlapping) subsets.
It supports two primary operations near O(1) time:
1. `find(x)`: Determine which subset an element `x` belongs to (returns representative root).
2. `union(x, y)`: Merge the subset containing `x` with the subset containing `y`.

When it is used:
- Dynamic connectivity queries.
- Cycle detection in undirected graphs.
- Kruskal's Minimum Spanning Tree algorithm.
- Number of Connected Components (LeetCode 323), Redundant Connection (LeetCode 684).

The Two Essential Optimizations:
1. Path Compression (`find`):
   When traversing up to find the root, redirect every visited node directly to the root:
   `parent[i] = find(parent[i])`. Flattens tree to depth ~ 1.
2. Union by Rank or Size (`union`):
   Always attach the shallower tree under the root of the deeper tree. Prevents tree from degenerating.

Time Complexity:
- O(alpha(n)) amortized per operation, where alpha is the Inverse Ackermann function.
  For all practical purposes, alpha(n) <= 4, meaning O(1) in practice!

Space Complexity:
- O(n) auxiliary space for parent and rank arrays.
"""


class UnionFind:
    """Disjoint Set Union (DSU) with Path Compression and Union by Rank."""

    def __init__(self, size: int):
        # Initially, each element is its own parent (isolated set)
        self.parent = list(range(size))
        # Rank approximates tree depth to balance unions
        self.rank = [0] * size
        self.num_components = size

    def find(self, x: int) -> int:
        """Finds representative of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Merges sets containing x and y.

        Returns True if merged, False if already in the same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same component (indicates a cycle if edge is added)

        # Union by rank: attach smaller rank tree under larger rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.num_components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Returns True if x and y belong to the same component."""
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.num_components == 5

    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.connected(0, 2) is True
    assert uf.num_components == 3

    # Unioning elements already connected returns False
    assert uf.union(0, 2) is False

    assert uf.connected(0, 3) is False
    assert uf.union(3, 4) is True
    assert uf.connected(3, 4) is True
    assert uf.num_components == 2

    print("All Union-Find tests passed successfully.")
