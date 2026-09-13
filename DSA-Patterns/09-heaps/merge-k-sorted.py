"""
Merge K Sorted Lists / Arrays

What it is:
Merges `k` sorted lists/arrays into a single sorted list.

When it is used:
- LeetCode 23 (Merge k Sorted Lists - Hard).
- External sorting (merging sorted runs from disk).
- Aggregating sorted search results from distributed shards.

The Key Idea:
Min-Heap of Size k:
1. Push the first element from each of the `k` lists into a min-heap: `(val, list_index, element_index)`.
2. Pop the smallest element `(val, i, j)` and append `val` to `result`.
3. If list `i` has a next element `j + 1`, push `(lists[i][j + 1], i, j + 1)` into the heap.
4. Repeat until the heap is empty.

Time Complexity:
- O(N log k) where N is total number of elements across all lists and k is number of lists.

Space Complexity:
- O(k) auxiliary space for the heap.
"""

import heapq


def merge_k_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    """Merges k sorted integer arrays in O(N log k) time and O(k) space."""
    min_heap: list[tuple[int, int, int]] = []  # (value, array_index, element_index)
    result = []

    # Insert the first element of each non-empty array
    for array_index, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], array_index, 0))

    while min_heap:
        val, array_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # If next element exists in the same array, push it
        if elem_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, array_idx, elem_idx + 1))

    return result


if __name__ == "__main__":
    k_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted_arrays(k_lists) == expected

    # With empty arrays
    assert merge_k_sorted_arrays([[], [1], []]) == [1]
    assert merge_k_sorted_arrays([]) == []

    print("All Merge K Sorted tests passed successfully.")
