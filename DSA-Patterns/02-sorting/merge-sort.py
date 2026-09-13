"""
Merge Sort

What it is:
A classic divide-and-conquer, comparison-based sorting algorithm.
It divides the input array into two halves, recursively sorts them,
and then merges the two sorted halves into a single sorted array.

When it is used:
- When a guaranteed O(n log n) worst-case time complexity is required.
- When stable sorting is essential.
- Sorting linked lists (can be done with O(1) extra space on linked lists).
- External sorting (sorting data too large to fit in RAM).

The Key Idea:
1. Divide: Split the array at mid = len(nums) // 2 until base case (length <= 1).
2. Conquer: Recursively merge_sort both halves.
3. Combine: Merge the two sorted subarrays with two pointers into a merged list.

Time Complexity:
- Best, Average, and Worst Case: O(n log n).
  Array splits into log n levels; each level does O(n) merging work.

Space Complexity:
- O(n) auxiliary space to store temporary merged arrays during the combine step.

Stability:
- Stable (when elements are equal, take from left subarray first: `left[i] <= right[j]`).

Common Pitfalls / Edge Cases:
- Using `<` instead of `<=` when comparing left and right elements destroys stability.
- Base case: array of length 0 or 1 is already sorted.
"""


def merge_sort(nums: list[int]) -> list[int]:
    """Returns a new sorted list containing all elements of nums in non-decreasing order."""
    # Base case
    if len(nums) <= 1:
        return nums

    # Divide
    mid = len(nums) // 2
    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])

    # Conquer (Merge)
    return merge(left_sorted, right_sorted)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merges two sorted lists into one sorted list."""
    merged = []
    i = 0  # pointer for left
    j = 0  # pointer for right

    while i < len(left) and j < len(right):
        # Use <= to maintain stability
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


if __name__ == "__main__":
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [1],
        [],
        [-5, -10, 0, 15, 7, 2],
    ]

    for nums in test_cases:
        expected = sorted(nums)
        assert merge_sort(nums) == expected

    print("All Merge Sort tests passed successfully.")
