from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev1 = prev2 = 0
            for money in houses:
                prev1, prev2 = max(prev2 + money, prev1), prev1

            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
