"""
Two Sum Pattern (Hash Map Lookup)

What it is:
Given an array of integers `nums` and an integer `target`, returns the indices of the
two numbers such that they add up to `target`.

When it is used:
- LeetCode 1 (Two Sum).
- Foundation for 3Sum, 4Sum, and target complement problems.
- Finding pairs with a given difference or product.

The Key Idea:
Single-Pass Hash Map:
Instead of testing every pair with two nested loops in O(n^2), we store each element's
value and its index in a hash map as we iterate.
For each element `num` at index `i`:
1. Calculate its complement: `complement = target - num`.
2. Check if `complement` is already in the hash map:
   - If YES: return `[seen[complement], i]`.
   - If NO: store current number: `seen[num] = i`.
Because complement lookup is O(1) average, the entire search takes linear time O(n).

Time Complexity:
- O(n) single pass through the array.

Space Complexity:
- O(n) auxiliary space to store elements in the hash map.

Common Pitfalls / Edge Cases:
- Using the same element twice (e.g. target = 6, nums = [3, 2, 4]; picking index 0 twice).
  The single-pass approach naturally avoids this because we check `seen` BEFORE adding `nums[i]`.
- Duplicate numbers in input: the map stores the most recent index, which is fine since
  a valid pair will trigger before or during duplicate overwrite.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Returns indices of two numbers that add up to target in O(n) time and O(n) space."""
    seen: dict[int, int] = {}  # maps value -> index

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 10) == []

    print("All Two Sum tests passed successfully.")
