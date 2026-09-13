"""
Linear Search

What it is:
A sequential search algorithm that starts at the beginning of a collection and
inspects every element one by one until the target is found or the end is reached.

When it is used:
- When the data is unsorted.
- Small arrays where the overhead of sorting or hashing is not justified.
- Linked lists where random access is not available.

The Key Idea:
Iterate index by index. If current element equals target, return its index.
If the loop finishes without finding the target, return -1.

Time Complexity:
- Best Case: O(1) when target is at the first position.
- Average/Worst Case: O(n) when target is at the end or not present.

Space Complexity:
- O(1) auxiliary space (uses only a loop counter).

Common Pitfalls / Edge Cases:
- Empty array: loop does not execute; returns -1.
- Duplicate targets: typically returns the first matching index.
- Negative numbers or float values: use exact equality checks.

Related Patterns:
- Binary Search (when array is sorted, improves time to O(log n)).
- Hash Map Lookup (when multiple queries are needed, improves query time to O(1) average).
"""


def linear_search(nums: list[int], target: int) -> int:
    """Returns the index of target in nums, or -1 if not found."""
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    test_array = [4, 2, 7, 1, 9, 3]

    # Target present
    assert linear_search(test_array, 7) == 2
    assert linear_search(test_array, 4) == 0
    assert linear_search(test_array, 3) == 5

    # Target not present
    assert linear_search(test_array, 100) == -1

    # Empty array
    assert linear_search([], 5) == -1

    print("All Linear Search tests passed successfully.")
