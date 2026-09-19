"""
Python `collections.defaultdict` Pattern

What it is:
A subclass of the built-in `dict` that overrides one method and adds one writable
instance variable: `default_factory`. When a non-existent key is accessed, it automatically
calls `default_factory` to supply a default value, eliminating explicit initialization checks.

When it is used:
- Adjacency lists for graph representations (`defaultdict(list)`).
- Grouping elements by key (e.g. Group Anagrams - LeetCode 49).
- Frequency counting (`defaultdict(int)`).
- Nested data structures (`defaultdict(set)`).

The Key Idea:
- `defaultdict(list)`: missing key generates `[]`.
- `defaultdict(int)`: missing key generates `0`.
- `defaultdict(set)`: missing key generates `set()`.
- Avoids repetitive `if key not in d: d[key] = []` before appending.

Time Complexity:
- Key lookup / insertion: O(1) average.

Space Complexity:
- O(n) where n is total key-value pairs stored.

Common Pitfalls / Edge Cases:
- Simply inspecting a missing key `d[missing_key]` CREATES the entry in the dictionary with the default value!
  To check existence without creating, use `key in d`.
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Groups anagrams together using defaultdict(list).

    (LeetCode 49)
    Time: O(n * k log k) where k is max string length. Space: O(n * k).
    """
    anagram_groups: defaultdict[str, list[str]] = defaultdict(list)
    for s in strs:
        # Sorted character tuple serves as the canonical hashable key
        sorted_key = "".join(sorted(s))
        anagram_groups[sorted_key].append(s)

    return list(anagram_groups.values())


def build_graph_adjacency_list(
    num_nodes: int, edges: list[list[int]]
) -> dict[int, list[int]]:
    """Builds an undirected graph adjacency list using defaultdict(list)."""
    graph: defaultdict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return dict(graph)


if __name__ == "__main__":
    # Group anagrams test
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    # Check that groups have correct sizes: 3, 2, 1
    group_sizes = sorted([len(g) for g in grouped])
    assert group_sizes == [1, 2, 3]

    # Graph adjacency list test
    edges = [[0, 1], [0, 2], [1, 2]]
    adj = build_graph_adjacency_list(3, edges)
    assert sorted(adj[0]) == [1, 2]
    assert sorted(adj[1]) == [0, 2]
    assert sorted(adj[2]) == [0, 1]

    print("All defaultdict tests passed successfully.")
