"""
Binary Search

What it is:
An efficient search algorithm that finds the position of a target value within
a sorted array by repeatedly dividing the search interval in half.

When it is used:
- The input array is already sorted in non-decreasing order.
- Checking for the existence or index of an element in O(log n) time.

The Key Idea:
Maintain two pointers, left and right. Compare the middle element to the target:
- If nums[mid] == target: found, return mid.
- If nums[mid] < target: target lies in the right half -> left = mid + 1.
- If nums[mid] > target: target lies in the left half -> right = mid - 1.

Time Complexity:
- Best Case: O(1) when target is in the exact middle.
- Worst/Average Case: O(log n) since search space halves each iteration.

Space Complexity:
- Iterative: O(1) auxiliary space.
- Recursive: O(log n) auxiliary space due to call stack.

Common Pitfalls / Edge Cases:
- Using `while left < right` instead of `while left <= right`: misses the last single-element range.
- Integer overflow in other languages: `mid = left + (right - left) // 2` (Python handles arbitrarily large ints,
  but this is good universal practice).
- Forgetting that the array MUST be sorted.

Related Patterns:
- Lower Bound / Upper Bound.
- Binary Search on Answer space.
"""


def binary_search(nums: list[int], target: int) -> int:
    """Returns the index of target in sorted nums, or -1 if not found."""
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(
    nums: list[int], target: int, left: int = 0, right: int | None = None
) -> int:
    """Recursive variant of binary search."""
    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    sorted_nums = [1, 3, 5, 7, 9, 11, 13]

    # Iterative tests
    assert binary_search(sorted_nums, 1) == 0
    assert binary_search(sorted_nums, 7) == 3
    assert binary_search(sorted_nums, 13) == 6
    assert binary_search(sorted_nums, 6) == -1
    assert binary_search([], 5) == -1

    # Recursive tests
    assert binary_search_recursive(sorted_nums, 1) == 0
    assert binary_search_recursive(sorted_nums, 7) == 3
    assert binary_search_recursive(sorted_nums, 13) == 6
    assert binary_search_recursive(sorted_nums, 6) == -1
    assert binary_search_recursive([], 5) == -1

    print("All Binary Search tests passed successfully.")
