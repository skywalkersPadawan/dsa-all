"""
Combinations Pattern

What it is:
Generates all possible combinations of k numbers chosen out of 1..n (or from an array).
Order does not matter ([1, 2] is the same combination as [2, 1]).
The number of such combinations is given by the binomial coefficient C(n, k).

When it is used:
- Selecting team members, lottery numbers, committee problems.
- LeetCode 77 (Combinations).

The Key Idea:
Backtracking with a forward-moving `start` index:
1. Base Case: if `len(path) == k`, save `path[:]` and return.
2. For `i` from `start` to `n`:
   - Pruning Optimization: if the remaining available numbers `(n - i + 1)` is fewer
     than needed `(k - len(path))`, we can stop the loop early.
   - Choose: `path.append(i)`
   - Explore: `backtrack(i + 1, path)`
   - Undo: `path.pop()`

Time Complexity:
- O(k * C(n, k)) where C(n, k) = n! / (k! * (n - k)!).

Space Complexity:
- O(k) recursion call stack depth and path storage.

Common Pitfalls / Edge Cases:
- Missing the pruning check `i <= n - (k - len(path)) + 1` causes unnecessary recursion branches.
- k = 0 or k > n.
"""


def combine(n: int, k: int) -> list[list[int]]:
    """Generates all combinations of k numbers from range 1..n.

    Time: O(k * C(n, k)), Space: O(k).
    """
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        if len(path) == k:
            result.append(path[:])
            return

        # Prune: need (k - len(path)) more elements
        # Available numbers from i to n is (n - i + 1)
        # So we only iterate while i <= n - (k - len(path)) + 1
        needed = k - len(path)
        for i in range(start, n - needed + 2):
            path.append(i)  # Choose
            backtrack(i + 1, path)  # Explore (i + 1 enforces no reuse)
            path.pop()  # Undo

    backtrack(1, [])

    return result


if __name__ == "__main__":
    res = combine(4, 2)
    expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert len(res) == 6
    for c in expected:
        assert c in res

    # Single element
    assert combine(1, 1) == [[1]]

    # k == n
    assert combine(3, 3) == [[1, 2, 3]]
    print("All Combinations tests passed successfully.")
