class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            count += self.expandAroundCenter(s, i, i)
            count += self.expandAroundCenter(s, i, i + 1)

        return count

    # helper function to expand around the center of the substring
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


# the name of the functions are not pythonic preferable to be expand_around_center and count_substrings, but leetcode wants to it to be like this.
