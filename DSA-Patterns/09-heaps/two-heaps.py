"""
Two Heaps Pattern (Find Median from Data Stream)

What it is:
A pattern where two heaps are used simultaneously to track the median (or split boundaries)
of a dynamically growing stream of numbers.

When it is used:
- LeetCode 295 (Find Median from Data Stream - Hard).
- Sliding Window Median (LeetCode 480).
- Real-time percentile tracking.

The Key Idea:
Divide all numbers into two equal halves:
1. `max_heap` (stores smaller half of numbers): stores negated values so max is at top.
2. `min_heap` (stores larger half of numbers): min is at top.

Invariants:
- All elements in `max_heap <=` all elements in `min_heap`.
- Size Balance: `len(max_heap)` is either equal to `len(min_heap)` or greater by exactly 1.

Finding Median:
- If `len(max_heap) > len(min_heap)`: median is `-max_heap[0]`.
- If sizes are equal: median is `(-max_heap[0] + min_heap[0]) / 2.0`.

Time Complexity:
- `add_num`: O(log n)
- `find_median`: O(1)

Space Complexity:
- O(n) to store numbers.
"""

import heapq


class MedianFinder:
    """Finds median of a data stream in O(log n) insertion and O(1) query."""

    def __init__(self):
        # max_heap stores the smaller half (negated for Python heapq)
        self.max_heap: list[int] = []
        # min_heap stores the larger half
        self.min_heap: list[int] = []

    def add_num(self, num: int) -> None:
        """Adds a number into the data structure."""
        # 1. Always push to max_heap first
        heapq.heappush(self.max_heap, -num)

        # 2. Balance property: max of lower half must be <= min of upper half
        if (
            self.max_heap
            and self.min_heap
            and (-self.max_heap[0]) > self.min_heap[0]
        ):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # 3. Balance sizes: max_heap can have at most 1 more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self) -> float:
        """Returns the median of current numbers."""
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5

    mf.add_num(3)
    assert mf.find_median() == 2.0

    mf.add_num(4)
    assert mf.find_median() == 2.5

    print("All Two Heaps tests passed successfully.")
