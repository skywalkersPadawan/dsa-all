"""
Sliding Window Pattern

What it is:
An algorithmic technique used to perform operations on a contiguous subsegment
(window) of an array or string. The window moves smoothly from left to right,
adding one element at the right and removing one element from the left,
avoiding repetitive recomputation.

When it is used:
1. Fixed-Size Window: Maximum/minimum sum or average of any subarray of size k.
2. Variable-Size Window: Longest or shortest contiguous substring/subarray that
   satisfies a given condition (e.g. at most k distinct characters, sum >= target).

The Key Idea:
- Fixed-size window of length k:
  Initialize window sum of first k elements.
  Then for i from k to n-1: add nums[i], subtract nums[i - k], update max/min.
- Variable-size window:
  Expand right boundary to include nums[right].
  While the window condition is violated (or can be shrunk):
    shrink from left by incrementing left and removing nums[left].
  Update optimal answer with current valid window (right - left + 1).

Time Complexity:
- O(n) time: each element enters the window once (via right) and leaves at most once (via left).

Space Complexity:
- O(1) to O(k) auxiliary space depending on auxiliary frequency map.

Common Pitfalls / Edge Cases:
- Empty array or k > len(nums).
- Shrinking condition: ensure left <= right.
- Forgetting to update state when shrinking left.
"""


def max_sum_subarray_fixed(nums: list[int], k: int) -> int:
    """Finds maximum sum of any contiguous subarray of fixed size k.

    Time: O(n), Space: O(1).
    """
    if len(nums) < k or k <= 0:
        return 0

    # Initialize the first window of size k
    window_sum = sum(nums[:k])
    max_sum = window_sum
    # Slide window across the rest of the array
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def length_of_longest_substring_without_repeating(s: str) -> int:
    """Finds length of longest contiguous substring without repeating characters.

    (LeetCode 3 - Longest Substring Without Repeating Characters)
    Time: O(n), Space: O(min(n, alphabet_size)).
    """
    char_index_map: dict[str, int] = {}
    max_length = 0
    left = 0
    for right, char in enumerate(s):
        # If char was seen within the current window, move left past its previous index
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1

        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    # Fixed window test
    assert max_sum_subarray_fixed([2, 1, 5, 1, 3, 2], 3) == 9  # [5, 1, 3]
    assert max_sum_subarray_fixed([2, 3, 4, 1, 5], 2) == 7  # [3, 4]
    assert max_sum_subarray_fixed([], 2) == 0

    # Variable window test
    assert length_of_longest_substring_without_repeating("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring_without_repeating("bbbbb") == 1  # "b"
    assert length_of_longest_substring_without_repeating("pwwkew") == 3  # "wke"
    assert length_of_longest_substring_without_repeating("") == 0
    print("All Sliding Window tests passed successfully.")
