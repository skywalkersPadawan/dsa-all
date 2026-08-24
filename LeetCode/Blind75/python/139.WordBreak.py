from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # learn the optimal dp solution and then go the deque or memoization appraoch after learning more
        word_set = set(wordDict)
        n = len(s)
        max_len = max(len(word) for word in wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# most common optimised accepted solution the common optimisation is done with max_len restricting the inner loop understand how can be derived and used in a real problem setting
