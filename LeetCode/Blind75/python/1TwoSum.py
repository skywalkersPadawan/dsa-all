from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numberDict = {}
        for i, number in enumerate(numbers):
            if target - number in numberDict:
                return [numberDict[target - number], i]
            numberDict[number] = i

        return []
