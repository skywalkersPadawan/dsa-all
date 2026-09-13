# Python `heapq` (Priority Queue / Binary Heap)

## Overview
The `heapq` module provides a **min-heap** implementation using standard Python lists. The smallest element is always maintained at index `0` (`heap[0]`).

---

## Key Functions and Complexities

| Function | What it does | Time Complexity |
| :--- | :--- | :--- |
| `heapq.heapify(nums)` | Converts a list into a valid min-heap in-place | `O(n)` |
| `heapq.heappush(heap, item)` | Pushes `item` onto the heap and restores heap order | `O(log n)` |
| `heapq.heappop(heap)` | Pops and returns the smallest item (`heap[0]`) | `O(log n)` |
| `heapq.heappushpop(heap, item)` | Pushes `item`, then pops and returns smallest | `O(log n)` (faster than separate push + pop) |
| `heap[0]` | Inspects the minimum item without popping | `O(1)` |
| `heapq.nlargest(k, iterable)` | Returns k largest elements | `O(n log k)` |
| `heapq.nsmallest(k, iterable)` | Returns k smallest elements | `O(n log k)` |

---

## How to Implement a Max-Heap in Python
`heapq` only implements a min-heap natively. To create a **max-heap**, negate the values:

```python
import heapq

max_heap = []
# Push elements negated
heapq.heappush(max_heap, -val)

# Peek max value
max_val = -max_heap[0]

# Pop max value
max_val = -heapq.heappop(max_heap)
```

---

## Storing Tuples (Custom Priority)
If tuples `(priority, item)` are stored, `heapq` orders by the first element of the tuple. If priorities are equal, it compares the second element.

```python
# Priority queue with Dijkstra's algorithm:
heap = []
heapq.heappush(heap, (distance, node))
curr_dist, curr_node = heapq.heappop(heap)
```

If the item is not directly comparable, add a unique counter:
```python
heapq.heappush(heap, (priority, count, item))
```

---

## The Top-K Pattern
To find the k largest elements in a stream or large array:
Maintain a **min-heap of size k**:
```python
import heapq


def find_k_largest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap  # Contains the k largest elements; heap[0] is the k-th largest
```
- **Time:** `O(n log k)` (much faster than sorting `O(n log n)` when `k << n`).
- **Space:** `O(k)`.
