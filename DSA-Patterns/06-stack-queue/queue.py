"""
Queue Data Structure

What it is:
A linear data structure following the FIFO (First-In, First-Out) principle.
The first element added is the first element to be removed.

When it is used:
- Breadth-First Search (BFS) in trees and graphs.
- Task scheduling and buffering (print queues, web request pipelines).
- Producer-Consumer workflows.

The Key Idea:
NEVER use a standard Python `list` with `pop(0)` as a queue because `pop(0)` takes O(n)
time to shift all remaining elements.
ALWAYS use `collections.deque` in Python for queues, which provides true O(1) pops and appends.

Core Operations:
- `enqueue`: `deque.append(val)` (O(1))
- `dequeue`: `deque.popleft()` (O(1))
- `peek`: `deque[0]` (O(1))
- `is_empty`: `len(deque) == 0` (O(1))

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)

Space Complexity:
- O(n) to store n elements.

Common Pitfalls / Edge Cases:
- Using `list.pop(0)` in BFS leads to hidden O(V^2) or O(N^2) timeouts on LeetCode.
"""

from collections import deque
from typing import Any


class Queue:
    """A standard FIFO queue implementation using collections.deque."""

    def __init__(self):
        self._items: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Adds an item to the back of the queue. O(1)."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Removes and returns the front item. Raises IndexError if empty. O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        return self._items.popleft()

    def peek(self) -> Any:
        """Returns the front item without removing it. Raises IndexError if empty. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self._items[0]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty. O(1)."""
        return len(self._items) == 0

    def size(self) -> int:
        """Returns the number of elements in the queue. O(1)."""
        return len(self._items)


if __name__ == "__main__":
    q = Queue()
    assert q.is_empty() is True

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    assert q.size() == 3
    assert q.peek() == "A"

    assert q.dequeue() == "A"
    assert q.dequeue() == "B"
    assert q.peek() == "C"

    assert q.dequeue() == "C"
    assert q.is_empty() is True

    try:
        q.dequeue()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass

    print("All Queue tests passed successfully.")
