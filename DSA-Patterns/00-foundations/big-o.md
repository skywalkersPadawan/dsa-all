# Big-O Notation

## What is Big-O?
Big-O notation describes the upper bound (worst-case scenario) of an algorithm's growth rate in terms of time or space as the input size n increases towards infinity.

---

## Order of Common Growth Rates (Fastest to Slowest)

| Notation | Name | Typical Example | When n = 1000 Operations |
| :--- | :--- | :--- | :--- |
| `O(1)` | Constant | Accessing array by index, hash map lookup | ~ 1 |
| `O(log n)` | Logarithmic | Binary search, balanced BST operations | ~ 10 |
| `O(n)` | Linear | Linear search, single loop through array | ~ 1,000 |
| `O(n log n)` | Linearithmic | Merge sort, heap sort, quick sort (average) | ~ 10,000 |
| `O(n^2)` | Quadratic | Nested loops, bubble sort, selection sort | ~ 1,000,000 |
| `O(n^3)` | Cubic | Matrix multiplication (standard 3 loops) | ~ 1,000,000,000 |
| `O(2^n)` | Exponential | Generating all subsets, naive recursive Fibonacci | ~ 10^301 |
| `O(n!)` | Factorial | Generating all permutations | Gigantic |

---

## The Rule of Thumb for Coding Interviews (10^8 Rule)
Modern online judges (LeetCode, HackerRank, Codeforces) can execute roughly **10^7 to 10^8 operations per second** in Python.

Use the problem's constraint n to deduce the expected time complexity:

| Input Constraint (n) | Required Target Complexity |
| :--- | :--- |
| n <= 10 to 12 | `O(n!)` or `O(n * 2^n)` (Backtracking, Permutations) |
| n <= 20 to 25 | `O(2^n)` (Subsets, Bitmask DP) |
| n <= 100 | `O(n^4)` or `O(n^3)` (Floyd-Warshall, 3D DP) |
| n <= 1,000 | `O(n^2)` (Nested loops, 2D DP) |
| n <= 100,000 (10^5) | `O(n log n)` or `O(n)` (Sorting, Heaps, Two Pointers) |
| n <= 1,000,000 (10^6) | `O(n)` or `O(n log n)` (Linear scans, Sliding window) |
| n > 10^9 | `O(log n)` or `O(1)` (Binary search, Math) |

---

## Three Simplification Rules
1. **Drop Constants:** `O(2n + 5)` -> `O(n)`
2. **Drop Lower-Order Terms:** `O(n^2 + 100n + log n)` -> `O(n^2)`
3. **Multi-Variable Inputs:** If there are two independent inputs m and n, preserve both: `O(m * n)` or `O(m + n)`.
