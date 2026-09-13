"""
Permutations Pattern

What it is:
Generates all possible orderings of a given collection of elements.
For an array of n distinct elements, there are n! (n factorial) permutations.

When it is used:
- Traveling Salesperson Problem (brute-force).
- Anagram generation.
- LeetCode 46 (Permutations), LeetCode 47 (Permutations II).

The Key Idea:
Unlike subsets/combinations where order does not matter and we only move forward (`start -> i + 1`),
permutations care about order. Any unused element from the entire collection can be chosen next.

Standard Backtracking with a `used` boolean array:
1. Base Case: if `len(path) == len(nums)`, record `path[:]`.
2. For each index `i` from 0 to `len(nums) - 1`:
   - If `used[i]` is True, skip.
   - Choose: `used[i] = True`, `path.append(nums[i])`.
   - Explore: `backtrack(path, used)`.
   - Undo: `path.pop()`, `used[i] = False`.

Time Complexity:
- O(n * n!): there are n! permutations, each taking O(n) to construct/copy.

Space Complexity:
- O(n) auxiliary space for recursion stack, path, and boolean array.

Common Pitfalls / Edge Cases:
- Duplicates in input (Permutations II): sort nums first; skip if `used[i]` or
  `(i > 0 and nums[i] == nums[i - 1] and not used[i - 1])`.
"""


def permute(nums: list[int]) -> list[list[int]]:
    """Generates all permutations of distinct integers nums.

    Time: O(n * n!), Space: O(n).
    """
    result: list[list[int]] = []
    used = [False] * len(nums)

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True  # Choose
            path.append(nums[i])

            backtrack(path)  # Explore

            path.pop()  # Undo
            used[i] = False

    backtrack([])
    return result


def permute_unique(nums: list[int]) -> list[list[int]]:
    """Generates all unique permutations of nums that may contain duplicates.

    (LeetCode 47)
    """
    result: list[list[int]] = []
    nums.sort()  # Sort to group duplicate values
    used = [False] * len(nums)

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # If current duplicate has already been processed in this same position
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result


if __name__ == "__main__":
    # Distinct permutations
    res = permute([1, 2, 3])
    assert len(res) == 6  # 3! = 6
    assert [1, 2, 3] in res
    assert [3, 2, 1] in res

    # Single element
    assert permute([1]) == [[1]]

    # Duplicates
    dup_res = permute_unique([1, 1, 2])
    assert len(dup_res) == 3  # [1, 1, 2], [1, 2, 1], [2, 1, 1]
    assert [1, 1, 2] in dup_res
    assert [1, 2, 1] in dup_res
    assert [2, 1, 1] in dup_res

    print("All Permutations tests passed successfully.")
