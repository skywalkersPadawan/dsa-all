# Space Complexity Analysis

## What is Space Complexity?

Space complexity quantifies the total amount of memory an algorithm needs relative to the input size n.

`Total Space = Auxiliary Space (extra memory used) + Input Space`

In coding interviews, **auxiliary space** (extra memory allocated by your algorithm) is usually what interviewers care about most.

---

## Types of Memory Usage

### 1. Variables & Pointers -> `O(1)`

```python
left = 0
right = len(nums) - 1
total = 0
```

Fixed number of variables regardless of n.

### 2. Explicit Data Structures -> `O(n)`

```python
seen = set(nums)  # O(n) space
counts = [0] * n  # O(n) space
```

### 3. Call Stack Space (Recursion) -> `O(max depth)`

Every active function call adds a frame to Python's call stack.

```python
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)
```

Max call stack depth is n -> `O(n)` auxiliary space.

---

## Recursion Call Stack Depth vs Number of Calls

A common interview trap:

- **Time** depends on the **total number of function calls**.
- **Space** depends on the **maximum recursion depth** (deepest branch active at any single moment).

### Example: Balanced Tree Traversal (DFS)

- Total nodes: n
- Tree height: `h ≈ log n`
- **Time:** `O(n)` (visits all nodes)
- **Auxiliary Space:** `O(log n)` (call stack holds at most h frames)

---

## In-Place vs Out-of-Place

- **In-place (`O(1)` auxiliary space):** The algorithm modifies the input directly without allocating significant extra structures (e.g., Two-pointer reverse, in-place quick sort partition).
- **Out-of-place:** Allocates auxiliary buffers, arrays, or copies of the input (e.g., standard Merge Sort creates temporary left and right halves -> `O(n)` space).

---

## Common Python Space Pitfalls

1. **List Slicing `nums[a:b]`:** Creates a **new copy** in memory. Slicing in a loop or recursion uses `O(n)` extra space. Use two pointers/indices instead.
2. **String Concatenation in a Loop:** Strings in Python are immutable. `s += char` in a loop copies the string every step (`O(n^2)` time and `O(n)` extra space). Use `"".join(list_of_chars)` instead.
