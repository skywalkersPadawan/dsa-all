"""
Prefix Sum + Hash Map Pattern

What it is:
A combined pattern where a running prefix sum is tracked alongside a hash map
storing earlier prefix sum values (and their frequencies or first-seen indices).

When it is used:
- Subarray Sum Equals K (LeetCode 560): Count number of subarrays whose sum equals k.
- Contiguous Array (LeetCode 525): Maximum length of contiguous subarray with equal number of 0s and 1s.
- Continuous Subarray Sum (LeetCode 523): Subarray sum is a multiple of k.
- Subarray sums divisible by k (LeetCode 974).

The Key Idea:
Let `prefix_sum[i]` be the sum of elements from 0 to i.
The sum of subarray `nums[j..i]` is `prefix_sum[i] - prefix_sum[j - 1]`.
We want: `prefix_sum[i] - prefix_sum[j - 1] == k`
Rearranging: `prefix_sum[j - 1] == prefix_sum[i] - k`.
As we compute `current_sum`, we check how many times `(current_sum - k)` has occurred previously.

Crucial Initialization:
- To count subarrays starting at index 0, initialize map with `{0: 1}` (a prefix sum of 0 has occurred once).
- For maximum length queries, initialize `{0: -1}` (a prefix sum of 0 occurs before index 0 at index -1).

Time Complexity:
- O(n) single pass.

Space Complexity:
- O(n) auxiliary space for the hash map.
"""


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """Counts total number of subarrays summing to k.

    (LeetCode 560)
    Time: O(n), Space: O(n).
    """
    count = 0
    current_sum = 0
    # Map stores: prefix_sum -> frequency of occurrence
    prefix_counts: dict[int, int] = {0: 1}

    for num in nums:
        current_sum += num
        needed_prefix = current_sum - k

        if needed_prefix in prefix_counts:
            count += prefix_counts[needed_prefix]

        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count


def max_length_equal_zeros_and_ones(nums: list[int]) -> int:
    """Finds maximum length of contiguous subarray with equal number of 0 and 1.

    (LeetCode 525 - Contiguous Array)
    Treat 0 as -1 and find longest subarray with sum 0.
    """
    # Map stores: prefix_sum -> first index where it was seen
    first_seen: dict[int, int] = {0: -1}
    max_len = 0
    current_sum = 0

    for i, num in enumerate(nums):
        # Treat 0 as -1
        current_sum += 1 if num == 1 else -1

        if current_sum in first_seen:
            # We have seen this same prefix sum before at first_seen[current_sum]
            subarray_len = i - first_seen[current_sum]
            max_len = max(max_len, subarray_len)
        else:
            first_seen[current_sum] = i

    return max_len


if __name__ == "__main__":
    # Subarray sum equals k
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3

    # Equal zeros and ones
    assert max_length_equal_zeros_and_ones([0, 1]) == 2
    assert max_length_equal_zeros_and_ones([0, 1, 0]) == 2
    assert max_length_equal_zeros_and_ones([0, 1, 1, 0, 1, 1, 1, 0]) == 4

    print("All Prefix Sum + Hash Map tests passed successfully.")
