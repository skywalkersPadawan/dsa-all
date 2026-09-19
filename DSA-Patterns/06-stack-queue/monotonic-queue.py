"""
Monotonic Queue Pattern

What it is:
A double-ended queue (deque) where elements are kept in strictly monotonic order
(usually monotonic decreasing from front to back). It supports `push`, `pop`, and `get_max`
in O(1) amortized time while processing a sliding window.

When it is used:
- Sliding Window Maximum (LeetCode 239).
- Constrained Subsequence Sum (LeetCode 1425).
- Shortest Subarray with Sum at Least K (LeetCode 862).

The Key Idea:
To maintain maximums in a sliding window:
1. When pushing a new element `val`:
   Remove all elements from the BACK of the deque that are smaller than `val`.
   (They can never be the maximum again because `val` is both larger and arrived later).
2. The FRONT of the deque (`deque[0]`) always holds the maximum element of the current window.
3. When an element slides out of the window:
   If the element being evicted equals `deque[0]`, pop it from the FRONT.

Time Complexity:
- O(1) amortized per push/pop/get_max.

Space Complexity:
- O(k) where k is the window size.
"""

from collections import deque


class MonotonicQueue:
    """Maintains maximum element in a sliding window in O(1) amortized time."""

    def __init__(self):
        self._deque: deque[int] = deque()

    def push(self, val: int) -> None:
        """Pushes val, removing all smaller elements from the back."""
        while self._deque and self._deque[-1] < val:
            self._deque.pop()

        self._deque.append(val)

    def pop(self, val: int) -> None:
        """Evicts val from the front only if it matches current max."""
        if self._deque and self._deque[0] == val:
            self._deque.popleft()

    def get_max(self) -> int:
        """Returns the maximum element in the window in O(1)."""
        return self._deque[0]


if __name__ == "__main__":
    mq = MonotonicQueue()

    # Window 1: [1, 3, -1]
    mq.push(1)
    mq.push(3)
    mq.push(-1)
    assert mq.get_max() == 3

    # Slide window: evict 1, add -3 -> [3, -1, -3]
    mq.pop(1)
    mq.push(-3)
    assert mq.get_max() == 3

    # Slide window: evict 3, add 5 -> [-1, -3, 5]
    mq.pop(3)
    mq.push(5)
    assert mq.get_max() == 5

    print("All Monotonic Queue tests passed successfully.")
