# Python `list` (Dynamic Array)

## Overview

A Python `list` is implemented internally as a contiguous, dynamic array of pointers to objects (similar to `std::vector` in C++ or `ArrayList` in Java).

---

## Complexity Reference

| Operation                | Time Complexity  | Notes                                           |
| :----------------------- | :--------------- | :---------------------------------------------- |
| `list[i]` (Access)       | `O(1)`           | Direct pointer offset calculation               |
| `list[i] = val` (Update) | `O(1)`           | In-place reference replacement                  |
| `list.append(val)`       | `O(1)` amortized | Appends at end; resizes geometrically when full |
| `list.pop()`             | `O(1)`           | Removes from end                                |
| `list.pop(0)` / `pop(i)` | `O(n)`           | Shifts all elements after i one position left   |
| `list.insert(0, val)`    | `O(n)`           | Shifts all existing elements one position right |
| `val in list` (Search)   | `O(n)`           | Linear scan from left to right                  |
| `len(list)`              | `O(1)`           | Size is stored directly in array struct         |
| `list.reverse()`         | `O(n)`           | In-place two-pointer swap                       |
| `list.sort()`            | `O(n log n)`     | Timsort (adaptive, stable sort)                 |
| `list[a:b]` (Slice)      | `O(b - a)`       | Allocates a brand new list and copies pointers  |
| `list.extend(other)`     | `O(k)`           | Where `k = len(other)`                          |

---

## Essential Patterns in Interviews

### 1. Using a List as a Stack (LIFO)

Always push and pop from the end for `O(1)` operations:

```python
stack = []
stack.append(10)  # push O(1)
top = stack[-1]  # peek O(1)
val = stack.pop()  # pop O(1)
```

### 2. Never Use `list` as a Queue (FIFO)

```python
# BAD: O(n) per pop(0)
queue = []
queue.append(1)
queue.pop(0)  # O(n) penalty!

# GOOD: Use collections.deque for O(1) pops
from collections import deque

queue = deque()
queue.append(1)
queue.popleft()  # O(1)
```

### 3. List Comprehensions vs Loops

List comprehensions run faster than manual `.append()` in Python because they bypass bytecode overhead:

```python
# Preferred & idiomatic:
squares = [x * x for x in range(10) if x % 2 == 0]
```
