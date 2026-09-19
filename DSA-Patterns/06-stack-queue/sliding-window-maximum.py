"""
Sliding Window Maximum

What it is:
Given an array `nums` and a sliding window of size `k` moving from left to right,
computes the maximum value in each window position.

When it is used:
- LeetCode 239 (Sliding Window Maximum).
- Moving maximum/minimum filters in signal and data stream processing.

The Key Idea (Monotonic Deque of Indices):
Maintain a `deque` storing INDICES of elements in strictly decreasing order of their values:
For each element `nums[i]`:
1. Evict Outdated: Remove indices from the front of the deque if `deque[0] <= i - k`
   (they have slid out of the current window).
2. Maintain Monotonicity: Remove indices from the back while `nums[deque[-1]] <= nums[i]`
   (they are smaller than the incoming element and can never be the maximum).
3. Append Current Index: `deque.append(i)`.
4. Record Window Maximum: Once `i >= k - 1` (the first full window is formed),
   `nums[deque[0]]` is guaranteed to be the maximum of the current window.

Time Complexity:
- O(n) linear time: each index is added to deque once and removed at most once.

Space Complexity:
- O(k) auxiliary space for the deque (stores at most k indices).

Common Pitfalls / Edge Cases:
- Storing values instead of indices in deque makes it impossible to know when an element
  has slid outside the current window of size k. Always store indices!
- k = 1: output is identical to nums.
"""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Finds maximum value in each sliding window of size k in O(n) time."""
    if not nums or k <= 0:
        return []

    if k == 1:
        return nums

    result: list[int] = []

    # Deque stores indices; values at indices are strictly decreasing
    window_deque: deque[int] = deque()
    for i, val in enumerate(nums):
        # 1. Remove indices that are outside the current window
        if window_deque and window_deque[0] <= i - k:
            window_deque.popleft()

        # 2. Maintain monotonic decreasing order in deque
        while window_deque and nums[window_deque[-1]] <= val:
            window_deque.pop()

        # 3. Add current index
        window_deque.append(i)

        # 4. Add to result once the first window is complete
        if i >= k - 1:
            result.append(nums[window_deque[0]])

    return result


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7]
    assert max_sliding_window(nums, k) == expected

    # Single element / k = 1
    assert max_sliding_window([1], 1) == [1]

    # k equals array length
    assert max_sliding_window([4, 2, 7, 1], 4) == [7]

    print("All Sliding Window Maximum tests passed successfully.")
