"""
Top-K Frequent Elements Pattern

What it is:
Given an integer array `nums` and an integer `k`, returns the `k` most frequent elements.
The answer can be returned in any order.

When it is used:
- LeetCode 347 (Top K Frequent Elements).
- Trending topics, search term suggestions, frequency analysis.

The Key Idea:
1. Count frequencies using `collections.Counter` in O(n).
2. Maintain a min-heap of size `k` storing `(frequency, num)`.
3. For each `(num, freq)`:
   - `heapq.heappush(min_heap, (freq, num))`
   - If `len(min_heap) > k`: `heapq.heappop(min_heap)`
4. The remaining `k` elements in the heap are the top-k most frequent.

Time Complexity:
- O(n log k) using a heap of size k.

Space Complexity:
- O(n) for frequency map + O(k) for heap.
"""

from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Finds top k most frequent elements using Counter + min-heap."""
    counts = Counter(nums)
    # Min-heap stores tuples of (frequency, number)
    min_heap: list[tuple[int, int]] = []

    for num, freq in counts.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    res = top_k_frequent(nums, 2)
    assert sorted(res) == [1, 2]

    assert top_k_frequent([1], 1) == [1]

    print("All Top-K tests passed successfully.")
