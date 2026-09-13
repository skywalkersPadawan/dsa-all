"""
Recursion Basics

What it is:
A programming technique where a function calls itself to solve smaller instances
of the same problem until a base condition is met.

When it is used:
- Problems that have a natural hierarchical or self-similar structure (trees, graphs).
- Divide-and-conquer algorithms (Merge Sort, Quick Sort, Binary Search).
- Backtracking problems (subsets, permutations, path finding).

The Key Idea:
Every recursive function requires two essential parts:
1. Base Case: The condition under which the function terminates without recursing.
2. Recursive Step: The progress made by calling itself with a strictly smaller subproblem.

Time Complexity:
O(number of recursive calls * work done per call)

Space Complexity:
O(maximum recursion depth) due to Python's call stack memory.

Common Pitfalls:
- Forgetting the base case causes RecursionError (stack overflow in Python, default limit 1000).
- Redundant overlapping subproblems (e.g., naive Fibonacci) lead to O(2^n) exponential time.
- Passing large list slices (e.g., arr[1:]) in recursive calls uses O(n) extra space per call.
  Pass pointers/indices instead.
"""


def factorial(n: int) -> int:
    """Calculates n! = n * (n - 1) * ... * 1."""
    # Base case
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)


def sum_of_array(nums: list[int], index: int = 0) -> int:
    """Calculates array sum using pointer-based recursion (avoids list slicing)."""
    # Base case
    if index == len(nums):
        return 0
    # Recursive step
    return nums[index] + sum_of_array(nums, index + 1)


def fibonacci_with_memo(n: int, memo: dict[int, int] | None = None) -> int:
    """
    Computes n-th Fibonacci number using top-down recursion + memoization.
    Time: O(n), Space: O(n).
    """
    if memo is None:
        memo = {}

    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Check memo cache
    if n in memo:
        return memo[n]

    # Recursive step and memoize
    memo[n] = fibonacci_with_memo(n - 1, memo) + fibonacci_with_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    # Test factorial
    assert factorial(5) == 120
    assert factorial(0) == 1
    print("Factorial tests passed.")

    # Test sum of array
    test_nums = [1, 2, 3, 4, 5]
    assert sum_of_array(test_nums) == 15
    assert sum_of_array([]) == 0
    print("Sum of array tests passed.")

    # Test Fibonacci
    assert fibonacci_with_memo(0) == 0
    assert fibonacci_with_memo(1) == 1
    assert fibonacci_with_memo(10) == 55
    print("Fibonacci tests passed.")
