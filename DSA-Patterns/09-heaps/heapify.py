"""
Heapify Algorithm (In-Place O(n) Heap Construction)

What it is:
Transforms an arbitrary unsorted array into a valid Binary Heap in linear O(n) time,
without using extra memory.

When it is used:
- Equivalent to Python's `heapq.heapify(list)`.
- First phase of Heap Sort.
- Initializing priority queues from existing arrays.

The Key Idea:
Why Bottom-Up is O(n), whereas repeated push is O(n log n):
- Leaves (the bottom half of nodes from `n // 2` to `n - 1`) are already valid 1-element heaps!
- We only need to call `_sift_down` starting from the lowest non-leaf node (`n // 2 - 1`)
  backwards up to the root index 0.
- Mathematical proof: most nodes are near the leaves and travel only 1 or 2 levels down.
  Sum of (nodes * height) converges to 2n = O(n).

Time Complexity:
- O(n) linear time.

Space Complexity:
- O(1) in-place auxiliary space.
"""


def heapify_min(nums: list[int]) -> None:
    """Converts nums into a min-heap in-place in O(n) time."""
    n = len(nums)
    # Start from last non-leaf node down to 0
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_min(nums, n, i)


def _sift_down_min(nums: list[int], n: int, index: int) -> None:
    """Pushes nums[index] down until min-heap property is satisfied."""
    while 2 * index + 1 < n:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and nums[left] < nums[smallest]:
            smallest = left
        if right < n and nums[right] < nums[smallest]:
            smallest = right

        if smallest != index:
            nums[index], nums[smallest] = nums[smallest], nums[index]
            index = smallest
        else:
            break


def is_valid_min_heap(nums: list[int]) -> bool:
    """Verifies that nums satisfies the min-heap property for all parent-child pairs."""
    n = len(nums)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[i] > nums[left]:
            return False
        if right < n and nums[i] > nums[right]:
            return False
    return True


if __name__ == "__main__":
    data = [9, 4, 7, 1, 2, 6, 3, 5]
    heapify_min(data)

    assert is_valid_min_heap(data) is True
    assert data[0] == 1  # root is global minimum

    # Empty and single element
    empty_arr = []
    heapify_min(empty_arr)
    assert empty_arr == []

    single = [42]
    heapify_min(single)
    assert single == [42]

    print("All Heapify tests passed successfully.")
