"""
Kadane's Algorithm (Maximum Subarray)

What it is:
An optimal greedy / dynamic programming algorithm that finds the contiguous subarray
within a one-dimensional array of numbers which has the largest sum.

When it is used:
- Maximum Subarray Problem (LeetCode 53).
- Stock buy/sell maximum single-trade profit (transforming into daily price difference array).
- Maximum Circular Subarray Sum (max of standard Kadane vs total_sum - min_Kadane).

The Key Idea:
At each index `i`, we decide whether to:
1. Extend the existing subarray sum: `current_sum + nums[i]`
2. Start a new subarray fresh from `nums[i]`: `nums[i]`
Therefore: `current_sum = max(nums[i], current_sum + nums[i])`
We track `max_sum = max(max_sum, current_sum)`.

If `current_sum` becomes negative, it cannot help any future subarray, so starting
fresh at the next positive element is always better.

Time Complexity:
- O(n) single pass over the array.

Space Complexity:
- O(1) auxiliary space (tracks only two scalar variables: current_sum and max_sum).

Common Pitfalls / Edge Cases:
- All negative numbers: initializing `max_sum = 0` incorrectly returns 0 when the
  answer should be the largest negative number (e.g. `[-3, -2, -5]` -> `-2`).
  Always initialize `max_sum = nums[0]` and `current_sum = nums[0]`.
- Empty array: check and return 0.
"""


def max_subarray_sum(nums: list[int]) -> int:
    """Returns the maximum sum of any contiguous non-empty subarray in O(n) time."""
    if not nums:
        return 0

    current_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        # Decide: extend previous subarray or start new from current element
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """Returns (max_sum, start_index, end_index) of the maximum subarray."""
    if not nums:
        return (0, -1, -1)

    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return (max_sum, start, end)


if __name__ == "__main__":
    # Standard mixed array
    test_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(test_1) == 6  # [4, -1, 2, 1]

    # All negative numbers
    test_2 = [-5, -2, -8, -1, -4]
    assert max_subarray_sum(test_2) == -1  # [-1]

    # All positive numbers
    test_3 = [1, 2, 3, 4]
    assert max_subarray_sum(test_3) == 10

    # Index tracking verification
    max_val, s, e = max_subarray_with_indices(test_1)
    assert max_val == 6
    assert test_1[s : e + 1] == [4, -1, 2, 1]
    print("All Kadane's Algorithm tests passed successfully.")
