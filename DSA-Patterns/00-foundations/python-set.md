# Python `set` (Hash Set)

## Overview

A Python `set` is an unordered collection of unique, hashable elements implemented using an open-addressing hash table (similar to a `dict` without values).

---

## Complexity Reference

| Operation                | Average Case               | Worst Case | Notes                                    |
| :----------------------- | :------------------------- | :--------- | :--------------------------------------- |
| `val in s` (Membership)  | `O(1)`                     | `O(n)`     | Much faster than `val in list`           |
| `s.add(val)`             | `O(1)`                     | `O(n)`     | Hashes item and stores it                |
| `s.remove(val)`          | `O(1)`                     | `O(n)`     | Raises `KeyError` if item is missing     |
| `s.discard(val)`         | `O(1)`                     | `O(n)`     | Removes if present; does NOT raise error |
| `len(s)`                 | `O(1)`                     | `O(1)`     | Size is stored directly                  |
| `s1 & s2` (Intersection) | `O(min(len(s1), len(s2)))` | `O(n * m)` | Iterates smaller set                     |
| `s1 \| s2` (Union)       | `O(len(s1) + len(s2))`     | `O(n + m)` | Combines both sets                       |
| `s1 - s2` (Difference)   | `O(len(s1))`               | `O(n * m)` | Elements in s1 but not s2                |

---

## Essential Interview Patterns

### 1. Removing Duplicates from a List

```python
unique_elements = list(set(nums))  # Order is NOT preserved!
```

If order must be preserved, use dictionary keys:

```python
unique_ordered = list(dict.fromkeys(nums))  # O(n) and maintains order
```

### 2. Fast `O(1)` Lookup vs `O(n)` List Lookup

```python
# SLOW: O(n^2)
seen_list = []
for num in nums:
    if num in seen_list:  # O(n) per check!
        pass
    seen_list.append(num)

# FAST: O(n) total
seen_set = set()
for num in nums:
    if num in seen_set:  # O(1) check!
        pass
    seen_set.add(num)
```

### 3. Track Visited States in Graphs / DFS / BFS

```python
visited = set()
visited.add((row, col))
if (row, col) in visited:
    continue
```
