"""
Longest Common Subsequence (LCS)

What it is:
Given two strings `text1` and `text2`, returns the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

When it is used:
- LeetCode 1143 (Longest Common Subsequence).
- File diff tools (git diff) and DNA sequence comparison / bioinformatics.

The Key Idea:
Let `dp[i][j]` be the length of LCS of `text1[0..i-1]` and `text2[0..j-1]`.
1. If `text1[i - 1] == text2[j - 1]`:
   Characters match! `dp[i][j] = 1 + dp[i - 1][j - 1]`.
2. If `text1[i - 1] != text2[j - 1]`:
   Take max of skipping a char from text1 or text2:
   `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`.

Time Complexity:
- O(m * n) where m = len(text1) and n = len(text2).

Space Complexity:
- O(m * n) for 2D DP table (can be space-optimized to O(min(m, n))).
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    """Computes length of longest common subsequence."""
    m = len(text1)
    n = len(text2)

    # dp[i][j] stores LCS of text1[0..i-1] and text2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3  # "ace"
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0

    print("All Longest Common Subsequence tests passed successfully.")
