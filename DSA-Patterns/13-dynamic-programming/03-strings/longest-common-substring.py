"""
Longest Common Substring

What it is:
Given two strings `text1` and `text2`, finds the length of the longest CONTIGUOUS
substring shared by both strings. Unlike LCS, characters must be contiguous.

When it is used:
- Plagiarism detection.
- Substring pattern matching.

The Key Idea:
Let `dp[i][j]` be the length of the longest common suffix of `text1[0..i-1]` and `text2[0..j-1]`.
1. If `text1[i - 1] == text2[j - 1]`:
   `dp[i][j] = 1 + dp[i - 1][j - 1]`.
   Update `max_length = max(max_length, dp[i][j])`.
2. If `text1[i - 1] != text2[j - 1]`:
   `dp[i][j] = 0` (Reset! The contiguous streak is broken).

Time Complexity:
- O(m * n).

Space Complexity:
- O(m * n) or O(min(m, n)) space.
"""


def longest_common_substring(text1: str, text2: str) -> int:
    """Finds length of longest contiguous substring common to both strings."""
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    return max_length


if __name__ == "__main__":
    assert longest_common_substring("abcde", "abfce") == 2  # "ab"
    assert longest_common_substring("GeeksforGeeks", "GeeksQuiz") == 5  # "Geeks"
    assert longest_common_substring("abc", "xyz") == 0

    print("All Longest Common Substring tests passed successfully.")
