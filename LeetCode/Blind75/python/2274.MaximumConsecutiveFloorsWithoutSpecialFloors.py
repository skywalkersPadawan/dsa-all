class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        prev = bottom - 1
        max_gap = 0
        for floor in special:
            gap = floor - prev - 1
            max_gap = max(max_gap, gap)
            prev = floor

        gap = top - prev
        max_gap = max(max_gap, gap)

        return max_gap