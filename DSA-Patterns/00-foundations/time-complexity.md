# Time Complexity Analysis

## What is Time Complexity?
Time complexity quantifies the amount of computational operations an algorithm performs as a function of the input size n. It does not measure wall-clock seconds (which depend on hardware), but rather the number of elementary operations executed.

---

## How to Determine Time Complexity in Python

### 1. Single Loops -> `O(n)`
```python
for item in nums:  # runs n times
    print(item)  # O(1) operation
```
**Total:** `O(n)`

### 2. Nested Loops -> `O(n^2)`
```python
for i in range(len(nums)):  # n times
    for j in range(len(nums)):  # n times
        pass  # O(1)
```
**Total:** `n * n = O(n^2)`

### 3. Dependent Nested Loops -> `O(n^2)`
```python
for i in range(n):
    for j in range(i + 1, n):
        pass
```
Number of operations: `(n - 1) + (n - 2) + ... + 1 = n * (n - 1) / 2 = O(n^2)`

### 4. Halving or Doubling Loop Variables -> `O(log n)`
```python
while n > 1:
    n = n // 2
```
Divides n by 2 at each step. Takes `log2(n)` steps.

### 5. Loop with Logarithmic Step -> `O(n log n)`
```python
for i in range(n):
    step = n
    while step > 1:
        step //= 2
```
Outer loop runs n times; inner loop runs `log n` times -> `O(n log n)`.

---

## Time Complexity in Recursion

Use the formula:
`Time Complexity = Total Recursive Calls * Work per Call`

### Example 1: Binary Search (Divide and Conquer)
- Calls at each level: 1
- Depth of tree: `log n`
- Work per call: `O(1)`
- **Total:** `O(log n)`

### Example 2: Naive Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
- Each call branches into 2 calls.
- Tree depth: n.
- Number of calls: `2^0 + 2^1 + 2^2 + ... + 2^n ≈ 2^n`.
- **Total:** `O(2^n)`.

---

## Hidden Time Complexities in Python
Watch out for operations that look simple but take linear time:

| Operation | Looks Like | Actual Time Complexity | Why? |
| :--- | :--- | :--- | :--- |
| `item in my_list` | `O(1)` | `O(n)` | Scans entire list sequentially |
| `my_list.pop(0)` | `O(1)` | `O(n)` | Shifts all elements left by 1 |
| `my_list.insert(0, x)` | `O(1)` | `O(n)` | Shifts all elements right by 1 |
| `my_list[i:j]` | `O(1)` | `O(j - i)` | Copies slice elements into new list |
| `string1 + string2` | `O(1)` | `O(len1 + len2)` | Creates an entirely new immutable string |
| `min(my_list)` / `max(...)` | `O(1)` | `O(n)` | Inspects every element |
