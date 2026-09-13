"""
Counting Sort

What it is:
A non-comparison-based sorting algorithm that operates on integer collections
within a known, bounded range [min_val, max_val]. It counts the frequency of each
distinct value, then computes positions in the sorted output.

When it is used:
- When the range of elements (k = max - min + 1) is not significantly greater than
  the number of elements (n).
- Sorting elements like character frequencies, ages, test scores, or as a subroutine
  in Radix Sort.

The Key Idea:
1. Find min_val and max_val to determine range k.
2. Build a frequency array `counts` of size k, where `counts[x - min_val]` stores
   the count of occurrences of x.
3. Overwrite the original array (or populate an output array) by placing each value
   according to its frequency count.

Time Complexity:
- Best, Average, and Worst Case: O(n + k), where n is len(nums) and k is (max_val - min_val + 1).
  Linear when k = O(n).

Space Complexity:
- O(k) auxiliary space for the counting array.

Stability:
- Can be implemented as stable (iterating backwards using cumulative prefix sums of counts).
  The standard interview in-place overwrite version shown below is straightforward for basic types.

Common Pitfalls / Edge Cases:
- Huge range k (e.g. nums = [1, 1_000_000_000]) causes MemoryError and extreme slowness O(k).
  Do NOT use counting sort when range k is large.
- Negative numbers: handled by offsetting with `min_val`.
- Empty array: return immediately.
"""


def counting_sort(nums: list[int]) -> list[int]:
    """Sorts an array of integers within a reasonable range in O(n + k) time."""
    if not nums:
        return nums

    min_val = min(nums)
    max_val = max(nums)
    range_span = max_val - min_val + 1

    # Count array
    counts = [0] * range_span
    for num in nums:
        counts[num - min_val] += 1

    # Overwrite nums with sorted elements
    write_index = 0
    for value_offset, count in enumerate(counts):
        value = min_val + value_offset
        for _ in range(count):
            nums[write_index] = value
            write_index += 1

    return nums


if __name__ == "__main__":
    test_cases = [
        [4, 2, 2, 8, 3, 3, 1],
        [-5, -10, 0, -3, 8, 5, -1, 10],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [0],
        [],
    ]

    for nums in test_cases:
        expected = sorted(nums)
        assert counting_sort(nums[:]) == expected

    print("All Counting Sort tests passed successfully.")
