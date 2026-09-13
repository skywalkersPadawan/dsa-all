"""
Min-Heap Implementation from Scratch

What it is:
A complete binary tree stored in an array where every parent node satisfies the
Min-Heap property: `parent <= left_child` and `parent <= right_child`.
The minimum element is always at the root (`heap[0]`).

When it is used:
- Understanding internal mechanics of priority queues.
- Heap Sort.
- Custom heaps with tracking handles or mutable elements.

The Key Idea:
Array Indexing (0-indexed):
- Parent of `i`: `(i - 1) // 2`
- Left child of `i`: `2 * i + 1`
- Right child of `i`: `2 * i + 2`

Operations:
- `push(val)`: append `val` to end of array, then `_sift_up(len - 1)`.
- `pop()`: swap root with last element, pop last element, then `_sift_down(0)`.
- `peek()`: return `heap[0]` in O(1).

Time Complexity:
- Push: O(log n)
- Pop: O(log n)
- Peek: O(1)
- Build heap (heapify): O(n)

Space Complexity:
- O(n) to store elements.
"""


class MinHeap:
    """A standard Binary Min-Heap implemented from scratch."""

    def __init__(self):
        self.heap: list[int] = []

    def push(self, val: int) -> None:
        """Pushes val onto the min-heap. O(log n)."""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        """Pops and returns the minimum element. Raises IndexError if empty. O(log n)."""
        if not self.heap:
            raise IndexError("pop from empty heap")

        # Swap root with last element
        min_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)

        return min_val

    def peek(self) -> int:
        """Returns the minimum element without removing it. O(1)."""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _sift_up(self, index: int) -> None:
        """Restores min-heap property upwards from index."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index],
            )
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index: int) -> None:
        """Restores min-heap property downwards from index."""
        n = len(self.heap)
        while 2 * index + 1 < n:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break

    def __len__(self) -> int:
        return len(self.heap)


if __name__ == "__main__":
    h = MinHeap()
    elements = [5, 3, 8, 1, 2, 9]
    for x in elements:
        h.push(x)

    assert h.peek() == 1
    sorted_out = []
    while len(h) > 0:
        sorted_out.append(h.pop())

    assert sorted_out == sorted(elements)

    print("All Min-Heap tests passed successfully.")
