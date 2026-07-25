# given a positive integer n, write a function that returns the number of set bits
# important —> learn only Brian Kernighans solution for this problem ignore others and keep the attempted brute force solution in a note
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count
