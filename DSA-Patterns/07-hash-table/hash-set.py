"""
Hash Set (Separate Chaining Implementation)

What it is:
A data structure that stores unique keys with no associated values.
It uses a hash function to place elements into buckets, guaranteeing fast
membership testing and duplicate prevention.

When it is used:
- Deduplication of collections.
- O(1) average membership testing (`x in set`).
- Tracking visited nodes/states in graph algorithms (DFS/BFS).
- (LeetCode 705 - Design HashSet).

The Key Idea:
Separate Chaining:
1. Maintain an array of `capacity` buckets, where each bucket is a list of keys.
2. `_hash(key) = hash(key) % capacity`.
3. `add(key)`: compute index. If key is not in that bucket, append it.
4. `contains(key)`: compute index. Return True if key is found in that bucket, else False.
5. `remove(key)`: compute index. Remove key from the bucket if present.

Time Complexity:
- Average Case: O(1) for add, contains, and remove.
- Worst Case: O(n) under severe hash collisions.

Space Complexity:
- O(n) auxiliary space to store n unique keys.
"""

from typing import Any


class MyHashSet:
    """A standard separate-chaining HashSet implementation."""

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.buckets: list[list[Any]] = [[] for _ in range(self.capacity)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def add(self, key: Any) -> None:
        """Adds key to set if not already present. O(1) avg."""
        index = self._hash(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: Any) -> None:
        """Removes key from set if present. O(1) avg."""
        index = self._hash(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: Any) -> bool:
        """Returns True if key is in set, False otherwise. O(1) avg."""
        index = self._hash(key)
        bucket = self.buckets[index]
        return key in bucket


if __name__ == "__main__":
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)
    assert hs.contains(1) is True
    assert hs.contains(3) is False

    hs.add(2)  # Duplicate addition
    assert hs.contains(2) is True

    hs.remove(2)
    assert hs.contains(2) is False

    # String keys
    hs.add("hello")
    assert hs.contains("hello") is True
    assert hs.contains("world") is False

    print("All Hash Set tests passed successfully.")
