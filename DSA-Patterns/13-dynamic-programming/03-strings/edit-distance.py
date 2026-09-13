"""
Edit Distance (Levenshtein Distance)

What it is:
Given two strings `word1` and `word2`, return the minimum number of operations required
to convert `word1` to `word2`.
Permitted operations:
1. Insert a character
2. Delete a character
3. Replace a character

When it is used:
- LeetCode 72 (Edit Distance - Hard).
- Spell checkers, autocomplete suggestions, fuzzy string search.

The Key Idea:
Let `dp[i][j]` be the minimum operations to convert `word1[0..i-1]` to `word2[0..j-1]`.
Base cases:
- `dp[i][0] = i` (delete all i characters from word1).
- `dp[0][j] = j` (insert all j characters into word1).

State Transitions:
If `word1[i - 1] == word2[j - 1]`:
  No operation needed: `dp[i][j] = dp[i - 1][j - 1]`.
Else:
  `dp[i][j] = 1 + min(`
    `dp[i][j - 1],`      # Insert
    `dp[i - 1][j],`      # Delete
    `dp[i - 1][j - 1]`   # Replace
  `)`

Time Complexity:
- O(m * n) where m = len(word1) and n = len(word2).

Space Complexity:
- O(m * n) (can be reduced to O(min(m, n)) with two rolling rows).
"""


def min_distance(word1: str, word2: str) -> int:
    """Calculates Levenshtein edit distance between word1 and word2."""
    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: converting to/from empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # Insert
                    dp[i - 1][j],  # Delete
                    dp[i - 1][j - 1],  # Replace
                )

    return dp[m][n]


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (remove 'r')
    # rose -> ros (remove 'e')

    assert min_distance("intention", "execution") == 5
    assert min_distance("", "a") == 1
    assert min_distance("abc", "abc") == 0

    print("All Edit Distance tests passed successfully.")
