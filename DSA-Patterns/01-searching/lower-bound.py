"""
Lower Bound

What it is:
Finds the index of the first (leftmost) element in a sorted array that is
GREATER THAN OR EQUAL TO (>=) a given target. Equivalent to bisect.bisect_left.

When it is used:
- Finding the starting index of a target in an array with duplicates.
- Finding the insertion position to maintain sorted order.
- Range queries on sorted arrays (e.g., number of elements >= target).

The Key Idea:
Keep a search interval [left, right] where right = len(nums).
If nums[mid] >= target, mid could be the answer, but there could be an earlier one to the left,
so right = mid.
If nums[mid] < target, mid is strictly too small, so left = mid + 1.
When left == right, left is the lower bound index.

Time Complexity:
- O(log n) because the search space halves every iteration.

Space Complexity:
- O(1) auxiliary space.

Common Pitfalls / Edge Cases:
- Target larger than all elements in nums: returns len(nums).
- Empty array: returns 0.
- Duplicates: correctly returns the index of the first occurrence.
"""


def lower_bound(nums: list[int], target: int) -> int:
    """Returns the smallest index where nums[index] >= target.

    If all elements are smaller than target, returns len(nums).
    """
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    nums = [1, 2, 4, 4, 4, 6, 7]

    # Target present multiple times -> returns first occurrence
    assert lower_bound(nums, 4) == 2

    # Target not present -> returns index of first element >= target
    assert lower_bound(nums, 3) == 2  # first element >= 3 is 4 at index 2
    assert lower_bound(nums, 5) == 5  # first element >= 5 is 6 at index 5

    # Target smaller than all elements
    assert lower_bound(nums, 0) == 0

    # Target larger than all elements -> returns len(nums)
    assert lower_bound(nums, 10) == len(nums)

    # Empty array
    assert lower_bound([], 5) == 0

    print("All Lower Bound tests passed successfully.")
