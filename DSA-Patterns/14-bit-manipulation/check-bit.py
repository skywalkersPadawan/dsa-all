"""
Check Bit (Is i-th Bit Set?)

What it is:
Checks whether the bit at position `i` (0-indexed from right/least significant bit)
of an integer `n` is 1 (set) or 0 (unset).

When it is used:
- Bitmask state inspection.
- Testing parity / odd-even check.
- Binary number representations and IP address masking.

The Key Idea:
Two Standard Techniques:
1. Right Shift and Mask:
   `((n >> i) & 1) == 1`
   Shifts the target bit down to position 0, then extracts it with `& 1`.
2. Left Shift Mask:
   `(n & (1 << i)) != 0`
   Creates a bitmask with only the i-th bit set to 1, then tests with `&`.

Time Complexity:
- O(1).

Space Complexity:
- O(1).
"""


def is_bit_set(n: int, i: int) -> bool:
    """Returns True if the i-th bit of n is set (1), False otherwise (0-indexed)."""
    return ((n >> i) & 1) == 1


def is_even(n: int) -> bool:
    """Checks if n is even using lowest bit test."""
    return (n & 1) == 0


def is_odd(n: int) -> bool:
    """Checks if n is odd using lowest bit test."""
    return (n & 1) == 1


if __name__ == "__main__":
    # 13 in binary: 1101
    # Bit 0: 1 (set)
    # Bit 1: 0 (unset)
    # Bit 2: 1 (set)
    # Bit 3: 1 (set)
    assert is_bit_set(13, 0) is True
    assert is_bit_set(13, 1) is False
    assert is_bit_set(13, 2) is True
    assert is_bit_set(13, 3) is True

    # Even / Odd
    assert is_even(10) is True
    assert is_even(7) is False
    assert is_odd(7) is True
    assert is_odd(0) is False

    print("All Check Bit tests passed successfully.")
