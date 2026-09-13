# Python `collections.deque` (Double-Ended Queue)

## Overview
A `collections.deque` (pronounced "deck") is implemented internally as a doubly linked list of fixed-size memory blocks. It provides `O(1)` appends and pops from **both ends**.

---

## Complexity Comparison: `list` vs `deque`

| Operation | `list` | `collections.deque` |
| :--- | :--- | :--- |
| Append to right (`append`) | `O(1)` amortized | `O(1)` |
| Pop from right (`pop`) | `O(1)` | `O(1)` |
| Append to left (`appendleft`) | `O(n)` (slow!) | `O(1)` (fast!) |
| Pop from left (`popleft`) | `O(n)` (slow!) | `O(1)` (fast!) |
| Access by index (`d[i]`) | `O(1)` | `O(n)` (must walk blocks) |
| Search by value (`x in d`) | `O(n)` | `O(n)` |

---

## When to Use `deque` in Interviews

1. **Breadth-First Search (BFS):**
   Queues require FIFO (First-In, First-Out). Always use `deque` for BFS queues.
   ```python
   from collections import deque

   queue = deque([root])
   while queue:
       node = queue.popleft()  # O(1) FIFO pop
       if node.left:
           queue.append(node.left)
       if node.right:
           queue.append(node.right)
   ```

2. **Sliding Window Problems:**
   Monotonic queues use `popleft()` and `pop()` to maintain extremes in `O(1)` amortized time.

3. **Fixed-Size Rolling Buffer:**
   `deque(maxlen=k)` automatically discards elements from the opposite end when full.
   ```python
   window = deque(maxlen=3)
   window.append(1)
   window.append(2)
   window.append(3)
   window.append(4)  # 1 is automatically evicted: deque([2, 3, 4], maxlen=3)
   ```
