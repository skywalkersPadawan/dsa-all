"""
K-th Largest Element in an Array

What it is:
Finds the k-th largest element in an unsorted array.
(e.g., in [3, 2, 1, 5, 6, 4], 2nd largest is 5).

When it is used:
- LeetCode 215 (Kth Largest Element in an Array).
- Real-time leaderboard rankings and quantile estimations.

The Key Idea:
Min-Heap of Size k:
1. Maintain a min-heap containing at most `k` elements.
2. For each number in the array:
   - `heapq.heappush(min_heap, num)`
   - If `len(min_heap) > k`: `heapq.heappop(min_heap)` (removes the smallest of the top k+1).
3. At the end, the heap contains the `k` largest elements of the entire array,
   and the root (`min_heap[0]`) is the k-th largest!

Time Complexity:
- O(n log k) where n is len(nums). Much faster than O(n log n) sorting when k << n.

Space Complexity:
- O(k) auxiliary space for the heap.
"""

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    """Finds the k-th largest element using a min-heap of size k.

    Time: O(n log k), Space: O(k).
    """
    min_heap: list[int] = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1

    print("All K-th Largest Element tests passed successfully.")
