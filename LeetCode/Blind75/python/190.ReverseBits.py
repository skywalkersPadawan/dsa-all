class Solution:
    def reverseBits(self, n: int) -> int:
        # Reverse bits of a given 32 bits signed integer.
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result
