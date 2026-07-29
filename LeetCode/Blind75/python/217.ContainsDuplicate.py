# straightforward solution is to use a hashset of O(1) lookup and O(n) complexity
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            # this step is necessary because without seen.add(num) the set never changes and duplicates cannot be found

        return False
