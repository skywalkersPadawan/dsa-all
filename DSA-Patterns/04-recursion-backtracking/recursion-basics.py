"""
Recursion Basics

What it is:
A method of solving problems where the solution depends on solutions to smaller
instances of the same problem. A recursive function consists of:
1. Base Case: stops recursion and directly returns an answer.
2. Recursive Call: invokes itself with reduced arguments.

When it is used:
- Naturally recursive structures: trees, graphs, linked lists, nested JSON/structures.
- Divide-and-conquer algorithms.
- Combinatorial search / backtracking.

The Key Idea:
Trust the recursive leap of faith: assume the function correctly solves smaller subproblems,
and focus solely on:
1. Handling the trivial base cases.
2. Combining or transforming the subproblem solution for the current step.

Time Complexity:
- O(branches^depth) in worst-case naive recursion, reduced to O(states) with memoization.

Space Complexity:
- O(max_call_stack_depth).

Common Pitfalls / Edge Cases:
- Missing base case leads to `RecursionError: maximum recursion depth exceeded`.
- Overlapping subproblems without memoization leads to exponential slowdown.
"""


def factorial(n: int) -> int:
    """Calculates n! recursively."""
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def power(base: float, exponent: int) -> float:
    """Computes base^exponent in O(log exponent) time using divide-and-conquer recursion."""
    if exponent == 0:
        return 1.0

    if exponent < 0:
        return 1.0 / power(base, -exponent)

    half = power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    else:
        return half * half * base


def is_palindrome_recursive(s: str, left: int = 0, right: int | None = None) -> bool:
    """Checks if string s is a palindrome using pointer-based recursion."""
    if right is None:
        right = len(s) - 1

    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return is_palindrome_recursive(s, left + 1, right - 1)


if __name__ == "__main__":
    assert factorial(5) == 120
    assert factorial(0) == 1

    assert power(2.0, 10) == 1024.0
    assert power(2.0, -2) == 0.25

    assert is_palindrome_recursive("racecar") is True
    assert is_palindrome_recursive("hello") is False
    assert is_palindrome_recursive("") is True
    print("All Recursion Basics tests passed successfully.")
