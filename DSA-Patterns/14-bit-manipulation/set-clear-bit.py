"""
Set, Clear, and Toggle Bit

What it is:
Techniques to modify individual bits at position `i` (0-indexed from right):
1. Set bit: Turn i-th bit to 1.
2. Clear bit: Turn i-th bit to 0.
3. Toggle bit: Flip i-th bit (0 -> 1, 1 -> 0).

When it is used:
- Bitmask manipulation.
- Flags, permissions (read/write/execute bitmasks in Unix).
- State compression in DP.

The Key Idea:
- Set bit: `n | (1 << i)`
  OR with 1 forces the bit to 1; OR with 0 leaves other bits unchanged.
- Clear bit: `n & ~(1 << i)`
  NOT `(1 << i)` creates a mask of all 1s except a 0 at position i. AND forces i-th bit to 0.
- Toggle bit: `n ^ (1 << i)`
  XOR with 1 flips the bit; XOR with 0 leaves other bits unchanged.

Time Complexity:
- O(1).

Space Complexity:
- O(1).
"""


def set_bit(n: int, i: int) -> int:
    """Sets the i-th bit of n to 1."""
    return n | (1 << i)


def clear_bit(n: int, i: int) -> int:
    """Clears the i-th bit of n to 0."""
    return n & ~(1 << i)


def toggle_bit(n: int, i: int) -> int:
    """Toggles (inverts) the i-th bit of n."""
    return n ^ (1 << i)


if __name__ == "__main__":
    # 9 in binary is 1001
    # Set bit 1 -> 1011 (11)
    assert set_bit(9, 1) == 11
    assert set_bit(9, 0) == 9  # already set

    # Clear bit 3 from 9 (1001) -> 0001 (1)
    assert clear_bit(9, 3) == 1
    assert clear_bit(9, 1) == 9  # already clear

    # Toggle bit 1 of 9 (1001 -> 1011 = 11)
    assert toggle_bit(9, 1) == 11
    # Toggle again -> back to 9
    assert toggle_bit(11, 1) == 9

    print("All Set/Clear/Toggle Bit tests passed successfully.")
