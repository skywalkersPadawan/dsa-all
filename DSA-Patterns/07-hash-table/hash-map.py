"""
Hash Map (Separate Chaining Implementation)

What it is:
A data structure that implements an associative array abstract data type,
mapping keys to values. It uses a hash function to compute an index into an array
of buckets, from which the desired value can be found.

When it is used:
- O(1) average lookup, insertion, and deletion by key.
- Caching/memoization.
- Counting, frequency indexing, symbol tables.
- (LeetCode 706 - Design HashMap).

The Key Idea:
Separate Chaining:
1. Initialize an array of fixed size `capacity` where each bucket is a list (chain) of `[key, value]` pairs.
2. Hash function: `index = hash(key) % capacity`.
3. To put `(key, value)`:
   - Compute bucket index.
   - If key already exists in that bucket's chain, update its value.
   - Otherwise, append `[key, value]` to the chain.
4. To get `key`:
   - Compute bucket index and search the chain for the key. Return value if found, else -1.
5. To remove `key`:
   - Search the chain and remove the pair if found.

Time Complexity:
- Average Case: O(1) for put, get, and remove.
- Worst Case: O(n) when all keys collide into a single bucket.

Space Complexity:
- O(n) to store key-value pairs.
"""

from typing import Any


class MyHashMap:
    """A standard separate-chaining HashMap implementation."""

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        # Buckets contain lists of [key, value] pairs
        self.buckets: list[list[list[Any]]] = [[] for _ in range(self.capacity)]

    def _hash(self, key: Any) -> int:
        """Hash helper to map key to bucket index."""
        return hash(key) % self.capacity

    def put(self, key: Any, value: Any) -> None:
        """Inserts or updates the value for key. O(1) avg."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key: Any) -> Any:
        """Returns the value for key, or -1 if key does not exist. O(1) avg."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: Any) -> None:
        """Removes the key-value pair if it exists. O(1) avg."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return


if __name__ == "__main__":
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    assert hm.get(3) == -1  # not found

    hm.put(2, 20)  # update
    assert hm.get(2) == 20

    hm.remove(2)
    assert hm.get(2) == -1

    # String keys
    hm.put("apple", 100)
    assert hm.get("apple") == 100

    print("All Hash Map tests passed successfully.")
