"""
Divide and Conquer Pattern

What it is:
A recursive paradigm that breaks down a problem into two or more subproblems of the
same or related type, until these become simple enough to be solved directly (base case).
The solutions to the subproblems are then combined to give a solution to the original problem.

Three Steps:
1. Divide: Break problem into smaller subproblems.
2. Conquer: Recursively solve the subproblems.
3. Combine: Merge the subproblem solutions into the overall solution.

When it is used:
- Merge Sort, Quick Sort, Binary Search.
- Fast Matrix Multiplication (Strassen), Fast Fourier Transform (FFT).
- Maximum Subarray (alternative to Kadane), Closest Pair of Points.

The Key Idea:
Reducing problem size by a constant fraction (e.g., n/2) at each level gives a recursion
depth of O(log n). If the combine step takes O(n), total runtime is O(n log n) by Master Theorem.

Time Complexity:
- T(n) = a * T(n/b) + f(n) (governed by Master Theorem).

Space Complexity:
- O(log n) call stack space.

Common Pitfalls / Edge Cases:
- Uneven division of subproblems.
- Inefficient combine step dominating overall time.
"""


def max_subarray_divide_and_conquer(
    nums: list[int], left: int = 0, right: int | None = None
) -> int:
    """Finds maximum subarray sum using divide-and-conquer.

    Time: O(n log n), Space: O(log n).
    """
    if right is None:
        right = len(nums) - 1

    if left > right:
        return float("-inf")
    if left == right:
        return nums[left]

    mid = left + (right - left) // 2

    # 1. Conquer left and right halves
    left_max = max_subarray_divide_and_conquer(nums, left, mid)
    right_max = max_subarray_divide_and_conquer(nums, mid + 1, right)

    # 2. Find max crossing subarray crossing the midpoint
    cross_max = max_crossing_sum(nums, left, mid, right)

    # 3. Combine: maximum of all three
    return max(left_max, right_max, cross_max)


def max_crossing_sum(nums: list[int], left: int, mid: int, right: int) -> int:
    """Finds max sum of subarray starting in left half and ending in right half."""
    # Max sum starting at mid and going left
    left_sum = float("-inf")
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += nums[i]
        left_sum = max(left_sum, current_sum)

    # Max sum starting at mid + 1 and going right
    right_sum = float("-inf")
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += nums[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_divide_and_conquer(nums) == 6

    assert max_subarray_divide_and_conquer([1, 2, 3, 4]) == 10
    assert max_subarray_divide_and_conquer([-1, -2, -3]) == -1

    print("All Divide and Conquer tests passed successfully.")
