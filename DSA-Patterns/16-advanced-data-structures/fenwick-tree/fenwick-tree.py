"""
Fenwick Tree / Binary Indexed Tree (BIT)

What it is:
An ingenious array-based data structure that maintains prefix sums of an array of numbers,
supporting prefix sum queries and point updates both in O(log n) time with minimal code.

When it is used:
- Dynamic range sum queries with point updates (lighter, faster, easier to code than Segment Tree).
- Counting Inversions in an array.
- 2D Range Sum updates.

The Key Idea:
Lowest Set Bit magic `x & (-x)`:
- A Fenwick Tree uses a 1-indexed array `tree` of size `n + 1`.
- Each index `i` is responsible for storing the sum of `lowbit(i) = i & (-i)` elements!
- To Update `update(i, delta)`:
  Add delta to `tree[i]`, and add `i & (-i)` to `i` (moves up to parent ranges):
  `i += i & (-i)`.
- To Query prefix sum `query(i)`:
  Add `tree[i]` to sum, and subtract `i & (-i)` from `i` (strips lowest bit):
  `i -= i & (-i)`.

Comparison with Segment Tree:
| Feature | Fenwick Tree | Segment Tree |
| :--- | :--- | :--- |
| Space | O(n) (exact size n + 1) | O(4n) |
| Code Complexity | ~15 lines (very simple) | ~50 lines |
| Flexibility | Prefix sums, point updates | Arbitrary ranges, range updates, min/max |

Time Complexity:
- Update: O(log n)
- Prefix Sum Query: O(log n)
- Range Sum Query: `query(right) - query(left - 1)` in O(log n)

Space Complexity:
- O(n) space.
"""


class FenwickTree:
    """1-indexed Binary Indexed Tree for prefix sums and point updates."""

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        """Adds delta to element at 1-based index in O(log n)."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)  # add lowest set bit

    def query_prefix(self, index: int) -> int:
        """Returns sum of elements from 1 to index (1-based) in O(log n)."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)  # remove lowest set bit
        return total

    def query_range(self, left: int, right: int) -> int:
        """Returns sum of elements from left to right (inclusive, 1-based)."""
        return self.query_prefix(right) - self.query_prefix(left - 1)


if __name__ == "__main__":
    # Create Fenwick tree for 5 elements
    bit = FenwickTree(5)
    # Array: [1, 2, 3, 4, 5] (1-indexed)
    for i, val in enumerate([1, 2, 3, 4, 5], 1):
        bit.add(i, val)

    assert bit.query_prefix(3) == 6  # 1 + 2 + 3 = 6
    assert bit.query_prefix(5) == 15  # 1 + 2 + 3 + 4 + 5 = 15
    assert bit.query_range(2, 4) == 9  # 2 + 3 + 4 = 9

    # Add 5 to index 3 (value becomes 8)
    bit.add(3, 5)
    assert bit.query_prefix(3) == 11
    assert bit.query_range(2, 4) == 14

    print("All Fenwick Tree tests passed successfully.")
