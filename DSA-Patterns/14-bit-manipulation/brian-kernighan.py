"""
Brian Kernighan's Algorithm

What it is:
A bit manipulation technique to CLEAR THE LOWEST (RIGHTMOST) SET BIT of a number in O(1):
`n = n & (n - 1)`

When it is used:
- Counting set bits in optimal time O(k) where k is number of 1-bits.
- Power of two verification (`n & (n - 1) == 0`).
- Isolating the lowest set bit: `lowest_bit = n & (-n)`.
- Bitmask search and bitboard games (Chess programming).

The Key Idea:
Why `n & (n - 1)` clears the lowest set bit:
- Subtracting 1 from a binary number flips all the bits after the rightmost set bit
  (which are all 0s) to 1s, and flips the rightmost set bit itself to 0.
- All bits to the left of the rightmost set bit remain completely untouched.
- Taking the bitwise AND of `n` and `n - 1` leaves the left bits identical, but zeroes
  out the rightmost set bit and all bits to its right!

Example:
n = 12 (binary: 1100)
n - 1 = 11 (binary: 1011)
n & (n - 1) = 1100 & 1011 = 1000 (8) -> lowest set bit is cleared!

Time Complexity:
- O(1) per step.

Space Complexity:
- O(1).
"""


def clear_lowest_set_bit(n: int) -> int:
    """Clears the lowest set bit in n."""
    return n & (n - 1)


def isolate_lowest_set_bit(n: int) -> int:
    """Isolates the lowest set bit of n (returns a power of 2)."""
    return n & (-n)


if __name__ == "__main__":
    # Clear lowest bit
    assert clear_lowest_set_bit(12) == 8  # 1100 -> 1000
    assert clear_lowest_set_bit(8) == 0  # 1000 -> 0000
    assert clear_lowest_set_bit(7) == 6  # 0111 -> 0110

    # Isolate lowest bit (n & -n)
    assert isolate_lowest_set_bit(12) == 4  # lowest set bit of 1100 is 4 (0100)
    assert isolate_lowest_set_bit(10) == 2  # lowest set bit of 1010 is 2 (0010)
    assert isolate_lowest_set_bit(16) == 16  # 10000

    print("All Brian Kernighan's tests passed successfully.")
