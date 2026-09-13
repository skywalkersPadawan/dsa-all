"""
Python `heapq` Guide and Interview Idioms

What it is:
Demonstrates idiomatic usage of Python's built-in `heapq` module, which implements
a binary min-heap on top of standard Python lists.

When it is used:
- Standard tool for priority queues in coding interviews.
- Dijkstra's shortest path, Prim's MST, A* search.
- Top-K elements, finding median from data stream, merging k sorted streams.

The Key Idea:
- Min-Heap: `heapq.heappush(heap, val)` and `heapq.heappop(heap)`.
- Peek: `heap[0]` in O(1).
- Max-Heap: Push negated values `heapq.heappush(heap, -val)` and negate on pop `-heapq.heappop(heap)`.
- Tuples: `(priority, data)`. Orders by first element of tuple.
- `heapq.heapify(nums)`: in-place O(n) construction.
- `heapq.nlargest(k, nums)` and `heapq.nsmallest(k, nums)` in O(n log k).

Time Complexity:
- `heapify`: O(n)
- `heappush` / `heappop`: O(log n)
- `nlargest` / `nsmallest`: O(n log k)
"""

import heapq


def demonstrate_min_heap() -> list[int]:
    nums = [5, 1, 8, 3, 2]
    heapq.heapify(nums)  # O(n) in-place min-heap

    sorted_out = []
    while nums:
        sorted_out.append(heapq.heappop(nums))
    return sorted_out


def demonstrate_max_heap(nums: list[int]) -> list[int]:
    """Demonstrates max-heap behavior using negated numbers."""
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    sorted_desc = []
    while max_heap:
        sorted_desc.append(-heapq.heappop(max_heap))
    return sorted_desc


if __name__ == "__main__":
    # Min-heap
    assert demonstrate_min_heap() == [1, 2, 3, 5, 8]

    # Max-heap
    assert demonstrate_max_heap([5, 1, 8, 3, 2]) == [8, 5, 3, 2, 1]

    # Top-K using nlargest
    raw = [10, 2, 50, 100, 3, 90]
    assert heapq.nlargest(3, raw) == [100, 90, 50]
    assert heapq.nsmallest(2, raw) == [2, 3]

    print("All Python heapq tests passed successfully.")
