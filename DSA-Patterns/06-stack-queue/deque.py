"""
Deque (Double-Ended Queue)

What it is:
A sequence data structure that supports efficient O(1) insertions and deletions
from both the front and the back ends.

When it is used:
- Sliding Window Maximum / Minimum problems (monotonic deque).
- Breadth-First Search (BFS) where items are added to one end and popped from the other.
- Palindrome validation (popping simultaneously from both ends).
- Work-stealing scheduling algorithms.

The Key Idea:
`collections.deque` is implemented as a doubly linked list of fixed-size contiguous blocks.
It provides:
- `append(x)`: add to right end O(1)
- `appendleft(x)`: add to left end O(1)
- `pop()`: remove and return from right end O(1)
- `popleft()`: remove and return from left end O(1)
- `deque[0]`: inspect leftmost element O(1)
- `deque[-1]`: inspect rightmost element O(1)

Time Complexity:
- Appends and Pops from both ends: O(1).
- Random access by index in middle: O(n) (not an array).

Space Complexity:
- O(n) memory.
"""

from collections import deque


def is_palindrome_deque(s: str) -> bool:
    """Demonstrates deque usage by checking palindrome from both ends."""
    char_deque: deque[str] = deque(s.lower())

    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            return False

    return True


if __name__ == "__main__":
    # Basic operations
    d: deque[int] = deque()

    # Append to both ends
    d.append(2)  # [2]
    d.append(3)  # [2, 3]
    d.appendleft(1)  # [1, 2, 3]
    d.appendleft(0)  # [0, 1, 2, 3]

    assert list(d) == [0, 1, 2, 3]
    assert d[0] == 0
    assert d[-1] == 3

    # Pop from both ends
    assert d.popleft() == 0  # [1, 2, 3]
    assert d.pop() == 3  # [1, 2]
    assert list(d) == [1, 2]

    # Palindrome demonstration
    assert is_palindrome_deque("radar") is True
    assert is_palindrome_deque("hello") is False
    assert is_palindrome_deque("a") is True

    print("All Deque tests passed successfully.")
