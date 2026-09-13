"""
Bubble Sort

What it is:
A comparison-based sorting algorithm that repeatedly steps through the list,
compares adjacent elements, and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

When it is used:
- Primarily for educational purposes and conceptual understanding.
- Detecting if an array is already sorted in O(n) time with an early-exit flag.

The Key Idea:
In each pass, the largest unsorted element "bubbles up" to its correct position at the end.
After k passes, the last k elements are guaranteed to be in their final sorted positions.
An early-exit boolean flag (`swapped`) stops execution if no swaps occur in a pass.

Time Complexity:
- Best Case: O(n) when array is already sorted (using the `swapped` flag).
- Average/Worst Case: O(n^2) when array is reverse sorted.

Space Complexity:
- O(1) auxiliary space (in-place sort).

Stability:
- Stable (adjacent elements with equal keys are never swapped).

Common Pitfalls / Edge Cases:
- Forgetting the `swapped` flag degrades best-case time to O(n^2).
- Inner loop range: elements after `n - 1 - i` are already sorted and don't need rechecking.
"""


def bubble_sort(nums: list[int]) -> list[int]:
    """Sorts nums in non-decreasing order using in-place bubble sort and returns it."""
    n = len(nums)

    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # If no two elements were swapped in this pass, the array is sorted
        if not swapped:
            break

    return nums


if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],  # already sorted
        [5, 4, 3, 2, 1],  # reverse sorted
        [3],  # single element
        [],  # empty
    ]

    for nums in test_cases:
        expected = sorted(nums)
        assert bubble_sort(nums) == expected

    print("All Bubble Sort tests passed successfully.")
