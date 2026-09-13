"""
Bitwise Operations Overview in Python

What it is:
Operations that manipulate numbers at the level of their individual bits (binary digits 0 and 1).

The 6 Fundamental Bitwise Operators in Python:
1. AND `&`: `1 & 1 = 1`, all other pairs = `0`
2. OR `|`: `0 | 0 = 0`, all other pairs = `1`
3. XOR `^`: `1 ^ 0 = 1`, `0 ^ 1 = 1`, identical bits = `0`
4. NOT `~`: Bitwise invert: `~x = -(x + 1)` in two's complement
5. Left Shift `<<`: `x << k` multiplies x by 2^k
6. Right Shift `>>`: `x >> k` integer divides x by 2^k

Python-Specific Note on Integers:
Python integers have ARBITRARY PRECISION (infinite bits), so they do not naturally overflow
at 32 or 64 bits.
To simulate 32-bit signed integers in Python (e.g. LeetCode 371):
- Use 32-bit mask: `MASK = 0xFFFFFFFF`
- Wrap arithmetic: `(x) & MASK`
- Handle negative sign: `x if x <= 0x7FFFFFFF else ~(x ^ MASK)`

Time Complexity:
- O(1) for all standard bitwise operations.

Space Complexity:
- O(1).
"""


def bitwise_and(a: int, b: int) -> int:
    return a & b


def bitwise_or(a: int, b: int) -> int:
    return a | b


def bitwise_xor(a: int, b: int) -> int:
    return a ^ b


def bitwise_not(a: int) -> int:
    return ~a


def left_shift(a: int, shift_by: int) -> int:
    return a << shift_by


def right_shift(a: int, shift_by: int) -> int:
    return a >> shift_by


if __name__ == "__main__":
    # 5 in binary is 101, 3 is 011
    assert bitwise_and(5, 3) == 1  # 101 & 011 = 001
    assert bitwise_or(5, 3) == 7  # 101 | 011 = 111
    assert bitwise_xor(5, 3) == 6  # 101 ^ 011 = 110
    assert bitwise_not(5) == -6  # ~5 = -(5 + 1) = -6
    assert left_shift(5, 1) == 10  # 5 * 2 = 10
    assert right_shift(5, 1) == 2  # 5 // 2 = 2

    print("All Bit Operations tests passed successfully.")
