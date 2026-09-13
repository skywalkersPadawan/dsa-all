"""
Max-Heap Implementation from Scratch

What it is:
A complete binary tree stored in an array where every parent node satisfies the
Max-Heap property: `parent >= left_child` and `parent >= right_child`.
The maximum element is always at the root (`heap[0]`).

When it is used:
- Finding largest elements in streams.
- Two Heaps pattern (e.g. median finder lower half).
- Priority queues where higher numbers represent higher priority.

The Key Idea:
Symmetric to Min-Heap:
- `_sift_up`: swap with parent while `heap[index] > heap[parent]`.
- `_sift_down`: swap with the largest of its children if child > parent.

Time Complexity:
- Push: O(log n)
- Pop: O(log n)
- Peek: O(1)

Space Complexity:
- O(n) storage space.
"""


class MaxHeap:
    """A standard Binary Max-Heap implemented from scratch."""

    def __init__(self):
        self.heap: list[int] = []

    def push(self, val: int) -> None:
        """Pushes val onto the max-heap. O(log n)."""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        """Pops and returns the maximum element. Raises IndexError if empty. O(log n)."""
        if not self.heap:
            raise IndexError("pop from empty heap")

        max_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)

        return max_val

    def peek(self) -> int:
        """Returns the maximum element without removing it. O(1)."""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _sift_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index],
            )
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index: int) -> None:
        n = len(self.heap)
        while 2 * index + 1 < n:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )
                index = largest
            else:
                break

    def __len__(self) -> int:
        return len(self.heap)


if __name__ == "__main__":
    mh = MaxHeap()
    elements = [5, 3, 8, 1, 2, 9]
    for x in elements:
        mh.push(x)

    assert mh.peek() == 9
    sorted_desc = []
    while len(mh) > 0:
        sorted_desc.append(mh.pop())

    assert sorted_desc == sorted(elements, reverse=True)

    print("All Max-Heap tests passed successfully.")
