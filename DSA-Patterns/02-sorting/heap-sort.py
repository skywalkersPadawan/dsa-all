"""
Heap Sort

What it is:
A comparison-based sorting algorithm based on a Binary Heap data structure.
It builds a Max-Heap from the input array, then repeatedly extracts the maximum
element and places it at the end of the array.

When it is used:
- When guaranteed O(n log n) runtime is required with strictly O(1) auxiliary space.
- Embedded systems with strict memory limits where Quick Sort's recursion stack or
  Merge Sort's O(n) buffer is unacceptable.

The Key Idea:
1. Build a Max-Heap from the array in O(n) time using `heapify` from bottom up.
2. In a Max-Heap, the root (`nums[0]`) is always the largest element.
3. Swap `nums[0]` with `nums[i]` (where i ranges from n-1 down to 1), effectively
   placing the largest element in its final sorted position at the end.
4. Call `heapify` on the reduced heap of size `i` to restore the Max-Heap property.

Time Complexity:
- Best, Average, and Worst Case: O(n log n).
  Building the heap takes O(n), and each of the n extractions takes O(log n).

Space Complexity:
- O(1) auxiliary space (in-place).

Stability:
- Not stable (heap operations reorder equal keys across branches).

Common Pitfalls / Edge Cases:
- Index math for zero-indexed binary heap:
  - Parent: `(i - 1) // 2`
  - Left child: `2 * i + 1`
  - Right child: `2 * i + 2`
- Bottom-up heap construction starts at `n // 2 - 1` down to 0.
"""


def heap_sort(nums: list[int]) -> list[int]:
    """Sorts nums in non-decreasing order using in-place Heap Sort and returns it."""
    n = len(nums)
    # Step 1: Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Step 2: One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum) to the end
        nums[0], nums[i] = nums[i], nums[0]
        # Call max heapify on the reduced heap
        heapify(nums, i, 0)

    return nums


def heapify(nums: list[int], heap_size: int, root_index: int) -> None:
    """Restores the max-heap property for subtree rooted at root_index in a heap of size heap_size."""
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    # If left child exists and is greater than root
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # If right child exists and is greater than the current largest
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If largest is not root
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Recursively heapify the affected sub-tree
        heapify(nums, heap_size, largest)


if __name__ == "__main__":
    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [9],
        [],
    ]
    for nums in test_cases:
        expected = sorted(nums)
        assert heap_sort(nums) == expected

    print("All Heap Sort tests passed successfully.")
