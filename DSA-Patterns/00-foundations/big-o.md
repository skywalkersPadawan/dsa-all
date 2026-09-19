# Big-O Notation

## What is Big-O?

Big-O notation describes the upper bound (worst-case scenario) of an algorithm's growth rate in terms of time or space as the input size n increases towards infinity.

---

## Order of Common Growth Rates (Fastest to Slowest)

| Notation     | Name         | Typical Example                                   | When n = 1000 Operations |
| ------------ | ------------ | ------------------------------------------------- | ------------------------ |
| `O(1)`       | Constant     | Accessing array by index, hash map lookup         | ~ 1                      |
| `O(log n)`   | Logarithmic  | Binary search, balanced BST operations            | ~ 10                     |
| `O(n)`       | Linear       | Linear search, single loop through array          | ~ 1,000                  |
| `O(n log n)` | Linearithmic | Merge sort, heap sort, quick sort (average)       | ~ 10,000                 |
| `O(n^2)`     | Quadratic    | Nested loops, bubble sort, selection sort         | ~ 1,000,000              |
| `O(n^3)`     | Cubic        | Matrix multiplication (standard 3 loops)          | ~ 1,000,000,000          |
| `O(2^n)`     | Exponential  | Generating all subsets, naive recursive Fibonacci | ~ 10^301                 |
| `O(n!)`      | Factorial    | Generating all permutations                       | Gigantic                 |

---
