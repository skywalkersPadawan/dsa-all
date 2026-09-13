"""
Subsets (Power Set) Pattern

What it is:
Generates all possible subsets (the power set) of a given collection of elements.
For an array of n distinct elements, there are exactly 2^n subsets.

When it is used:
- Combinatorial search problems where decisions are binary: "include or exclude".
- Generating power sets (LeetCode 78 - Subsets, LeetCode 90 - Subsets II).
- Knapsack search / bitmask iteration.

The Key Idea:
Mental Model: Choose -> Explore -> Undo (Backtracking).
At each recursive step starting from index `start`:
1. Add a copy of current `path` to `result` (every prefix of choices forms a valid subset).
2. For each element from `start` to `len(nums) - 1`:
   - Choose: `path.append(nums[i])`
   - Explore: `backtrack(i + 1, path)` (move to next index to avoid duplicate usage)
   - Undo: `path.pop()`

Time Complexity:
- O(n * 2^n): there are 2^n subsets, and copying each takes O(n).

Space Complexity:
- O(n) auxiliary space for recursion stack and current path (excluding result output).

Common Pitfalls / Edge Cases:
- Forgetting to copy the path: `result.append(path[:])` vs `result.append(path)`.
  Appending `path` directly stores a reference to a mutable list that gets cleared by later pops.
- Duplicates in input (Subsets II): sort the array first, and skip `if i > start and nums[i] == nums[i - 1]`.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    """Generates all subsets of unique elements nums.

    Time: O(n * 2^n), Space: O(n).
    """
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        # Every state reached is a valid subset
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])  # Choose
            backtrack(i + 1, path)  # Explore (i + 1 enforces forward progress)
            path.pop()  # Undo

    backtrack(0, [])
    return result


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """Generates all unique subsets of nums that may contain duplicates.

    (LeetCode 90)
    """
    result: list[list[int]] = []
    nums.sort()  # Sort to bring duplicates together

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])

        for i in range(start, len(nums)):
            # Skip duplicate elements at the same tree level
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    all_subsets = subsets(nums)
    assert len(all_subsets) == 8  # 2^3 = 8
    assert [] in all_subsets
    assert [1] in all_subsets
    assert [1, 2, 3] in all_subsets

    # Subsets with duplicates
    dup_nums = [1, 2, 2]
    unique_subsets = subsets_with_dup(dup_nums)
    assert len(unique_subsets) == 6
    # [1, 2] appears once, [2, 2] appears once, etc.
    assert unique_subsets.count([2]) == 1
    assert unique_subsets.count([1, 2]) == 1

    print("All Subsets tests passed successfully.")
