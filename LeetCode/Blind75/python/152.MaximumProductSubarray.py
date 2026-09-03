from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = cur_min = nums[0]
        for num in nums[1:]:
            prev_max = cur_max
            prev_min = cur_min
            cur_max = max(num, prev_max * num, prev_min * num)
            cur_min = min(num, prev_max * num, prev_min * num)
            res = max(res, cur_max)

        return res
