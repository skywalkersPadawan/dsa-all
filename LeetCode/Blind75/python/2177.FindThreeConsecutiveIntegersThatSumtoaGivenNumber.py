class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:
            return []
        
        middle_number = num // 3
        return [middle_number - 1, middle_number, middle_number + 1]