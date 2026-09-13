"""
Next Greater Element Pattern

What it is:
For each element in an array, finds the first element to its right that is strictly greater
than itself. If no greater element exists, output -1 for that position.

When it is used:
- LeetCode 496 (Next Greater Element I).
- LeetCode 503 (Next Greater Element II - Circular Array).
- Daily Temperatures (LeetCode 739).
- Stock Span (previous greater element variation).

The Key Idea:
Use a Monotonic Decreasing Stack.
Iterate through the array from left to right:
- While `stack` is not empty and `nums[i] > nums[stack[-1]]`:
  The element `nums[i]` is the "next greater element" for the index at `stack[-1]`.
  Pop the index and record: `result[popped_index] = nums[i]`.
- Push current index `i` onto the stack.
- Any indices remaining in the stack at the end have no greater element to their right (default -1).

For Circular Arrays:
- Iterate through the array twice (`2 * n - 1` iterations) using `i % n`.

Time Complexity:
- O(n) linear time: each index is pushed once and popped at most once.

Space Complexity:
- O(n) auxiliary space for the stack and output array.

Common Pitfalls / Edge Cases:
- Circular vs non-circular array requirements.
- Strictly greater (`>`) vs greater than or equal (`>=`).
"""


def next_greater_element(nums: list[int]) -> list[int]:
    """Finds next greater element for every item in nums. Returns -1 if none exists.

    Time: O(n), Space: O(n).
    """
    n = len(nums)
    result = [-1] * n
    # Stack stores indices of elements waiting for their next greater element
    stack: list[int] = []

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            smaller_index = stack.pop()
            result[smaller_index] = nums[i]

        stack.append(i)

    return result


def next_greater_element_circular(nums: list[int]) -> list[int]:
    """Finds next greater element in a circular array (LeetCode 503)."""
    n = len(nums)
    result = [-1] * n
    stack: list[int] = []

    # Loop twice through the array to simulate circular wrap-around
    for i in range(2 * n):
        current_val = nums[i % n]
        while stack and current_val > nums[stack[-1]]:
            smaller_index = stack.pop()
            result[smaller_index] = current_val

        if i < n:
            stack.append(i)

    return result


if __name__ == "__main__":
    # Standard array
    arr = [2, 1, 2, 4, 3]
    assert next_greater_element(arr) == [4, 2, 4, -1, -1]

    # Decreasing array
    assert next_greater_element([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]

    # Increasing array
    assert next_greater_element([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]

    # Circular array test: [1, 2, 1] -> [2, -1, 2]
    assert next_greater_element_circular([1, 2, 1]) == [2, -1, 2]

    print("All Next Greater Element tests passed successfully.")
