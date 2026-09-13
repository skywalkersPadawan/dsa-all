"""
Segment Tree (Range Sum and Point Update)

What it is:
A binary tree data structure used for storing information about intervals or segments.
It allows querying range sums, minimums, or maximums, and updating array elements,
both in O(log n) time.

When it is used:
- Dynamic Range Sum Query (LeetCode 307 - Range Sum Query - Mutable).
- Range Minimum / Maximum queries with frequent point or range updates.
- Skyline problem, counting inversions.

The Key Idea:
Array Representation:
For an array of size n, a segment tree of size `4 * n` stores:
- Root at index 1: stores sum of entire array range `[0..n-1]`.
- Left child at `2 * node`: stores left half `[0..mid]`.
- Right child at `2 * node + 1`: stores right half `[mid + 1..end]`.

Operations:
1. `build(node, start, end)`: recursively builds left and right subtrees; `tree[node] = tree[left] + tree[right]`.
2. `update(node, start, end, index, val)`: recursively updates the leaf and recalibrates ancestors in O(log n).
3. `query(node, start, end, left, right)`:
   - If segment `[start..end]` is completely inside query range `[left..right]`: return `tree[node]`.
   - If completely disjoint: return 0.
   - Else: query left and right children and return their sum in O(log n).

Time Complexity:
- Build: O(n)
- Point Update: O(log n)
- Range Query: O(log n)

Space Complexity:
- O(n) auxiliary space (size 4 * n array).
"""


class SegmentTree:
    """Segment Tree for Range Sum Query with Point Updates."""

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums[:]
        # 4 * n is the safe upper bound for segment tree size
        self.tree = [0] * (4 * self.n) if self.n > 0 else []
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.nums[start]
            return

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index: int, val: int) -> None:
        """Updates nums[index] = val in O(log n)."""
        self._update(1, 0, self.n - 1, index, val)

    def _update(
        self, node: int, start: int, end: int, index: int, val: int
    ) -> None:
        if start == end:
            self.nums[index] = val
            self.tree[node] = val
            return

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        if index <= mid:
            self._update(left_child, start, mid, index, val)
        else:
            self._update(right_child, mid + 1, end, index, val)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query_range(self, left: int, right: int) -> int:
        """Returns sum of nums[left..right] (inclusive, 0-indexed) in O(log n)."""
        return self._query(1, 0, self.n - 1, left, right)

    def _query(
        self, node: int, start: int, end: int, left: int, right: int
    ) -> int:
        # Out of bounds
        if right < start or end < left:
            return 0

        # Current segment is completely within query range
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap: query both children
        mid = (start + end) // 2
        sum_left = self._query(2 * node, start, mid, left, right)
        sum_right = self._query(2 * node + 1, mid + 1, end, left, right)

        return sum_left + sum_right


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(nums)

    # Sum of range [1, 3]: 3 + 5 + 7 = 15
    assert st.query_range(1, 3) == 15
    # Sum of range [0, 5]: 1 + 3 + 5 + 7 + 9 + 11 = 36
    assert st.query_range(0, 5) == 36

    # Update index 1 from 3 to 10 -> [1, 10, 5, 7, 9, 11]
    st.update(1, 10)
    # Sum of range [1, 3] is now 10 + 5 + 7 = 22
    assert st.query_range(1, 3) == 22

    print("All Segment Tree tests passed successfully.")
