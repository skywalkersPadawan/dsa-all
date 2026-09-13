"""
Climbing Stairs Pattern

What it is:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

When it is used:
- LeetCode 70 (Climbing Stairs).
- Counting paths/arrangements with local step choices.

The Key Idea:
To reach step `i`, you must come from either:
- Step `i - 1` (by taking 1 step)
- Step `i - 2` (by taking 2 steps)
Total distinct ways to reach step `i`:
`ways[i] = ways[i - 1] + ways[i - 2]` (identical recurrence to Fibonacci).

Base cases:
`ways[1] = 1`, `ways[2] = 2`.

Time Complexity:
- O(n) time.

Space Complexity:
- O(1) auxiliary space using two variables.
"""


def climb_stairs(n: int) -> int:
    """Calculates distinct ways to climb n stairs in O(n) time and O(1) space."""
    if n <= 2:
        return n

    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3  # (1+1+1), (1+2), (2+1)
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8

    print("All Climbing Stairs tests passed successfully.")
