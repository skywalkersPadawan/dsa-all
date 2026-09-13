"""
Insertion Sort

What it is:
A simple comparison-based sorting algorithm that builds the final sorted array
one item at a time by repeatedly taking the next element and inserting it into
its proper position among the previously sorted elements.

When it is used:
- Small datasets (often used as the base-case sort in hybrid algorithms like Timsort).
- Nearly sorted / partially sorted data (runs in near O(n) time).
- Online algorithms where data arrives in a stream one element at a time.

The Key Idea:
Maintain a sorted subarray on the left [0...i-1].
Pick the element at index i (current_value) and shift all elements in the sorted
portion that are greater than current_value one position to the right, then place
current_value in the vacated spot.

Time Complexity:
- Best Case: O(n) when array is already sorted (only 1 comparison per element, 0 shifts).
- Average/Worst Case: O(n^2) when array is randomly ordered or reversed.

Space Complexity:
- O(1) auxiliary space (in-place).

Stability:
- Stable (does not shift equal elements).

Common Pitfalls / Edge Cases:
- Shifting elements requires careful index bounds (`while j >= 0 and nums[j] > current_val`).
- Empty or single-element lists require no work.
"""


def insertion_sort(nums: list[int]) -> list[int]:
    """Sorts nums in non-decreasing order using in-place insertion sort and returns it."""
    for i in range(1, len(nums)):
        current_value = nums[i]
        j = i - 1

        # Shift elements of nums[0..i-1] that are greater than current_value to one position ahead
        while j >= 0 and nums[j] > current_value:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current_value

    return nums


if __name__ == "__main__":
    test_cases = [
        [12, 11, 13, 5, 6],
        [4, 3, 2, 10, 12, 1, 5, 6],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [42],
        [],
    ]

    for nums in test_cases:
        expected = sorted(nums)
        assert insertion_sort(nums) == expected

    print("All Insertion Sort tests passed successfully.")
