"""
Two Pointers Pattern

What it is:
A technique where two index pointers traverse one or two sequences simultaneously.
The pointers can move in opposite directions (converging from ends toward each other)
or in the same direction at different speeds (fast and slow pointers).

When it is used:
- Converging Pointers:
  - Sorted array target pair search (Two Sum II).
  - 3Sum / 4Sum problems.
  - Palindrome verification / in-place array reversal.
  - Trapping Rain Water / Container With Most Water.
- Fast & Slow Pointers:
  - Cycle detection in linked lists.
  - In-place duplicate removal from sorted arrays.

The Key Idea:
- Converging: Start with `left = 0`, `right = len(nums) - 1`.
  Compute total = nums[left] + nums[right].
  If total == target: match found!
  If total < target: since nums is sorted, increment `left` to increase the sum.
  If total > target: decrement `right` to decrease the sum.
- Eliminates one entire row or column of potential pairs at every step in O(1).

Time Complexity:
- O(n) time: each element is visited at most once.

Space Complexity:
- O(1) auxiliary space (in-place pointers).

Common Pitfalls / Edge Cases:
- The array must be sorted for the converging sum pattern to work.
- Off-by-one errors: `left < right` (distinct elements) vs `left <= right`.
- Duplicate elements in 3Sum: remember to skip adjacent identical elements to avoid duplicate triplets.
"""


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Finds 1-based indices of two numbers in sorted array that add up to target.

    (LeetCode 167 - Two Sum II)
    Time: O(n), Space: O(1).
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def reverse_array_in_place(nums: list[int]) -> list[int]:
    """Reverses an array in-place using two converging pointers.

    Time: O(n), Space: O(1).
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


def remove_duplicates_sorted(nums: list[int]) -> int:
    """Removes duplicates from a sorted array in-place and returns length of unique portion.

    (LeetCode 26 - Remove Duplicates from Sorted Array)
    Fast & slow pointer technique.
    Time: O(n), Space: O(1).
    """
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


if __name__ == "__main__":
    # Two sum sorted
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]

    # Reverse array in-place
    arr = [1, 2, 3, 4, 5]
    assert reverse_array_in_place(arr) == [5, 4, 3, 2, 1]

    # Remove duplicates
    sorted_arr = [1, 1, 2, 2, 3, 4, 4]
    new_length = remove_duplicates_sorted(sorted_arr)
    assert new_length == 4
    assert sorted_arr[:new_length] == [1, 2, 3, 4]
    print("All Two Pointers tests passed successfully.")
