# Python `dict` (Hash Map)

## Overview

A Python `dict` is a hash table that maps unique keys to values. In Python 3.7+, dictionaries are guaranteed to maintain **insertion order**.

---

## Complexity Reference

| Operation                             | Average Case | Worst Case | Notes                                          |
| :------------------------------------ | :----------- | :--------- | :--------------------------------------------- |
| `d[key]` (Get)                        | `O(1)`       | `O(n)`     | Hash collision chain traversal                 |
| `d[key] = val` (Set)                  | `O(1)`       | `O(n)`     | Dynamic resize occurs when table is ~ 2/3 full |
| `key in d` (Lookup)                   | `O(1)`       | `O(n)`     | Checks key presence via hash lookup            |
| `del d[key]` / `d.pop(key)`           | `O(1)`       | `O(n)`     | Removes key-value pair                         |
| `len(d)`                              | `O(1)`       | `O(1)`     | Tracked directly                               |
| `d.keys()`, `d.values()`, `d.items()` | `O(n)`       | `O(n)`     | Iterating over all entries                     |

_Note: Worst-case `O(n)` only occurs under pathological hash collision conditions._

---

## Hashable Keys

Keys must be immutable and hashable:

- **Valid keys:** `int`, `float`, `str`, `tuple` (if all elements inside are hashable), `frozenset`.
- **Invalid keys:** `list`, `dict`, `set` (will raise `TypeError: unhashable type`).

---

## Essential Idioms in Coding Interviews

### 1. `.get(key, default)`

Avoids `KeyError` when a key might not exist yet:

```python
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
```

### 2. `collections.defaultdict`

Automatically initializes missing keys on access:

```python
from collections import defaultdict

# Grouping items by key
graph = defaultdict(list)
graph["A"].append("B")  # initializes empty list automatically
```

### 3. `collections.Counter`

Quick frequency counts:

```python
from collections import Counter

freq = Counter(nums)
most_common_two = freq.most_common(2)  # [(elem, count), ...]
```
