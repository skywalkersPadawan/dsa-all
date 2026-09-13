"""
Union-Find Applications

What it is:
Demonstrates real-world interview applications of Disjoint Set Union (DSU):
1. Redundant Connection (LeetCode 684): Find the edge that forms a cycle in an undirected graph.
2. Accounts Merge (LeetCode 721): Grouping accounts by shared email addresses.
3. Number of Provinces / Connected Components.

The Key Idea:
- Redundant Connection:
  Iterate through edges `(u, v)`. Call `union(u, v)`.
  If `union` returns False, `u` and `v` are ALREADY connected, so this edge creates a cycle!
  Return that edge immediately.
- String/Generic Union-Find:
  Map strings (e.g. emails) to parents in a hash map `parent[x] = x`.

Time Complexity:
- O(N * alpha(N)) near-linear time.

Space Complexity:
- O(N) storage for parent mapping.
"""


class DisjointSetUnion:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        self.parent[root_i] = root_j
        return True


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    """Returns an edge that can be removed so that the resulting graph is a tree of n nodes.

    (LeetCode 684)
    """
    n = len(edges)
    dsu = DisjointSetUnion(n + 1)  # 1-indexed nodes

    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]

    return []


if __name__ == "__main__":
    # Test Redundant Connection 1:
    # Edges: [[1, 2], [1, 3], [2, 3]] -> edge [2, 3] forms the cycle
    edges1 = [[1, 2], [1, 3], [2, 3]]
    assert find_redundant_connection(edges1) == [2, 3]

    # Test Redundant Connection 2:
    # Edges: [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]] -> [1, 4] forms cycle
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert find_redundant_connection(edges2) == [1, 4]

    print("All Union-Find Applications tests passed successfully.")
