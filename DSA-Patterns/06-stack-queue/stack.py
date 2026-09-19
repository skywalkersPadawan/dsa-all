"""
Stack Data Structure

What it is:
A linear data structure following the LIFO (Last-In, First-Out) principle.
The last element added is the first element removed.

When it is used:
- Function call stack / recursion management.
- Expression evaluation (postfix, infix parsing).
- Undo / Redo mechanics.
- Backtracking state management.
- Parentheses matching and syntax parsing.

The Key Idea:
In Python, a standard `list` is the idiomatic, high-performance stack:
- `push`: `list.append(x)` (O(1) amortized)
- `pop`: `list.pop()` (O(1))
- `peek`: `list[-1]` (O(1))
- `is_empty`: `len(list) == 0` (O(1))

Time Complexity:
- Push: O(1) amortized
- Pop: O(1)
- Peek: O(1)
- Size / IsEmpty: O(1)

Space Complexity:
- O(n) where n is the number of elements in the stack.

Common Pitfalls / Edge Cases:
- Calling `pop()` or `peek()` on an empty stack raises `IndexError`.
  Always check `if stack:` before popping or peeking.
"""

from typing import Any


class Stack:
    """A clean, standard LIFO stack implementation in Python."""

    def __init__(self):
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """Adds an item to the top of the stack. O(1)."""
        self._items.append(item)

    def pop(self) -> Any:
        """Removes and returns the top item. Raises IndexError if empty. O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")

        return self._items.pop()

    def peek(self) -> Any:
        """Returns the top item without removing it. Raises IndexError if empty. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self._items[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack has no items. O(1)."""
        return len(self._items) == 0

    def size(self) -> int:
        """Returns number of elements in stack. O(1)."""
        return len(self._items)


if __name__ == "__main__":
    s = Stack()
    assert s.is_empty() is True

    s.push(10)
    s.push(20)
    s.push(30)
    assert s.size() == 3
    assert s.peek() == 30

    assert s.pop() == 30
    assert s.pop() == 20
    assert s.peek() == 10
    assert s.size() == 1

    assert s.pop() == 10
    assert s.is_empty() is True

    # Empty pop check
    try:
        s.pop()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass

    print("All Stack tests passed successfully.")
