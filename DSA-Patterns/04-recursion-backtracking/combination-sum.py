"""
Combination Sum Pattern

What it is:
Finds all unique combinations of candidate numbers where the chosen numbers sum up to a target.
Each number may be chosen an unlimited number of times.

When it is used:
- Making change problems (listing all coin combinations).
- Partitioning a target sum using available denominations.
- LeetCode 39 (Combination Sum), LeetCode 40 (Combination Sum II).

The Key Idea:
Backtracking with state `(start_index, remaining_target, current_path)`.
1. Base Cases:
   - If `remaining == 0`: found a valid combination, append `path[:]` to result.
   - If `remaining < 0`: target exceeded, stop exploring this branch.
2. For each index `i` from `start` to `len(candidates) - 1`:
   - If sorted, stop early when `candidates[i] > remaining`.
   - Choose: `path.append(candidates[i])`.
   - Explore: `backtrack(i, remaining - candidates[i], path)`.
     CRUCIAL: pass `i` (not `i + 1`) because candidate elements may be REUSED!
   - Undo: `path.pop()`.

Time Complexity:
- O(N^(T/M)) where N is number of candidates, T is target, and M is minimal candidate value.

Space Complexity:
- O(T / M) maximum recursion depth.

Common Pitfalls / Edge Cases:
- Passing `i + 1` instead of `i`: accidentally forbids reusing elements.
- Forgetting to sort candidates: misses the `candidates[i] > remaining` early break optimization.
- Forgetting `start` index: generates permutations instead of combinations (e.g. both [2, 3] and [3, 2]).
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Returns all unique combinations in candidates summing to target (elements reusable).

    Time: O(N^(T/M)), Space: O(T/M).
    """
    result: list[list[int]] = []
    candidates.sort()  # Sort to enable early pruning

    def backtrack(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            # Since candidates are sorted, all subsequent elements will also exceed remaining
            if candidates[i] > remaining:
                break

            path.append(candidates[i])  # Choose
            backtrack(
                i, remaining - candidates[i], path
            )  # Explore (same index i -> reuse allowed)
            path.pop()  # Undo

    backtrack(0, target, [])
    return result


if __name__ == "__main__":
    # Test case 1
    cands1 = [2, 3, 6, 7]
    target1 = 7
    res1 = combination_sum(cands1, target1)
    assert [2, 2, 3] in res1
    assert [7] in res1
    assert len(res1) == 2

    # Test case 2
    cands2 = [2, 3, 5]
    target2 = 8
    res2 = combination_sum(cands2, target2)
    assert [2, 2, 2, 2] in res2
    assert [2, 3, 3] in res2
    assert [3, 5] in res2
    assert len(res2) == 3

    # Test case 3: impossible target
    assert combination_sum([2], 1) == []

    print("All Combination Sum tests passed successfully.")
