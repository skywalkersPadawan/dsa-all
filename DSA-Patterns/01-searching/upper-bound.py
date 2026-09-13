"""
Upper Bound

What it is:
Finds the index of the first element in a sorted array that is
STRICTLY GREATER THAN (>) a given target. Equivalent to bisect.bisect_right.

When it is used:
- Finding the ending index of a target in an array with duplicates:
  last_index = upper_bound(nums, target) - 1 (if target exists).
- Counting occurrences of a target:
  count = upper_bound(nums, target) - lower_bound(nums, target).
- Insertion position after any existing duplicates.

The Key Idea:
Keep a search interval [left, right] where right = len(nums).
If nums[mid] > target, mid could be the answer, so search left: right = mid.
If nums[mid] <= target, mid is not strictly greater, so search right: left = mid + 1.
When left == right, left is the upper bound index.

Time Complexity:
- O(log n) time.

Space Complexity:
- O(1) auxiliary space.

Common Pitfalls / Edge Cases:
- Target larger than or equal to all elements: returns len(nums).
- Empty array: returns 0.
- Comparing nums[mid] > target (upper bound) vs nums[mid] >= target (lower bound).
"""


def upper_bound(nums: list[int], target: int) -> int:
    """Returns the smallest index where nums[index] > target.

    If no such element exists, returns len(nums).
    """
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left


def count_occurrences(nums: list[int], target: int) -> int:
    """Counts how many times target appears in sorted array nums.

    Uses lower_bound and upper_bound in O(log n) time.
    """
    # Inline lower_bound for self-containment
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if nums[m] >= target:
            r = m
        else:
            l = m + 1
    first_index = l

    last_index = upper_bound(nums, target)
    return last_index - first_index


if __name__ == "__main__":
    nums = [1, 2, 4, 4, 4, 6, 7]

    # Target present multiple times -> returns index right after last occurrence
    assert upper_bound(nums, 4) == 5  # index 5 has value 6 (> 4)

    # Target not present -> returns index of first element > target
    assert upper_bound(nums, 3) == 2  # first element > 3 is 4 at index 2
    assert upper_bound(nums, 5) == 5  # first element > 5 is 6 at index 5

    # Target smaller than all elements
    assert upper_bound(nums, 0) == 0

    # Target larger than or equal to all elements
    assert upper_bound(nums, 7) == len(nums)
    assert upper_bound(nums, 10) == len(nums)

    # Counting occurrences
    assert count_occurrences(nums, 4) == 3
    assert count_occurrences(nums, 2) == 1
    assert count_occurrences(nums, 9) == 0

    print("All Upper Bound tests passed successfully.")
