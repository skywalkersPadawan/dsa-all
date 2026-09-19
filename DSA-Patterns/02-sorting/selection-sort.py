"""
Selection Sort

What it is:
An in-place comparison sort that divides the input into two parts: a sorted subarray
at the left and an unsorted subarray at the right. In each pass, it finds the smallest
element in the unsorted portion and swaps it with the leftmost unsorted element.

When it is used:
- When auxiliary memory write operations are extremely costly (selection sort makes
  at most O(n) swaps, fewer than any other elementary sort).
- Small lists where simplicity is preferred.

The Key Idea:
For each index i from 0 to n-1:
Find the index of the minimum element in nums[i...n-1].
Swap nums[i] with nums[min_index].

Time Complexity:
- Best, Average, and Worst Case: O(n^2) because it always scans the remaining unsorted
  portion regardless of whether the array is sorted.

Space Complexity:
- O(1) auxiliary space (in-place).

Stability:
- Not stable in standard array implementation (swapping across long distances can reorder equal keys).

Common Pitfalls / Edge Cases:
- Initializing min_index to i at the start of each outer loop.
- No early exit is possible without extra checks because it always seeks the global minimum of the suffix.
"""


def selection_sort(nums: list[int]) -> list[int]:
    """Sorts nums in non-decreasing order using in-place selection sort and returns it."""
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted segment
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


if __name__ == "__main__":
    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [9, -3, 5, 2, 6, 8, -6, 1, 3],
        [7],
        [],
    ]
    for nums in test_cases:
        expected = sorted(nums)
        assert selection_sort(nums) == expected

    print("All Selection Sort tests passed successfully.")
