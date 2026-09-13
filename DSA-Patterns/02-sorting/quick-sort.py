"""
Quick Sort

What it is:
A widely used divide-and-conquer comparison sorting algorithm.
It picks an element as a 'pivot' and partitions the array around the pivot,
such that elements smaller than the pivot are placed before it and
elements greater than the pivot are placed after it.

When it is used:
- General-purpose in-place sorting.
- Quickselect (finding the k-th smallest/largest element in O(n) average time).
- When average-case O(n log n) speed and O(log n) call stack space are preferred.

The Key Idea (Lomuto Partition Scheme):
1. Choose a pivot (commonly the last element `nums[high]`).
2. Maintain a boundary pointer `i` starting at `low - 1`.
3. Iterate `j` from `low` to `high - 1`. If `nums[j] <= pivot`, increment `i` and swap `nums[i]` with `nums[j]`.
4. Finally, swap `nums[i + 1]` with `nums[high]` (places pivot in its final position).
5. Recursively sort the subarrays to the left and right of the pivot index.

Time Complexity:
- Best/Average Case: O(n log n) when partitions are balanced.
- Worst Case: O(n^2) when array is already sorted and pivot is always chosen as first or last element.
  (Mitigated in practice with random pivot or median-of-three).

Space Complexity:
- O(log n) average auxiliary space due to recursion call stack; O(n) worst-case.

Stability:
- Not stable in standard in-place implementations due to long-distance swaps.

Common Pitfalls / Edge Cases:
- Selecting a poor pivot on already sorted arrays (e.g., last element) causes O(n^2) recursion.
- Off-by-one errors in partition bounds (`low <= high` vs `low < high`).
"""


def quick_sort(
    nums: list[int], low: int = 0, high: int | None = None
) -> list[int]:
    """In-place Quick Sort on nums[low..high]. Returns nums."""
    if high is None:
        high = len(nums) - 1

    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

    return nums


def partition(nums: list[int], low: int, high: int) -> int:
    """Lomuto partition scheme: places nums[high] at its correct sorted position."""
    pivot = nums[high]
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    # Place pivot in its correct sorted position
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


if __name__ == "__main__":
    test_cases = [
        [10, 80, 30, 90, 40, 50, 70],
        [5, 2, 3, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 3],
        [42],
        [],
    ]

    for nums in test_cases:
        expected = sorted(nums)
        assert quick_sort(nums[:]) == expected

    print("All Quick Sort tests passed successfully.")
