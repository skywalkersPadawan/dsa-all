"""
Bitmask Subsets Pattern

What it is:
Uses integer bitmasks from `0` to `2^n - 1` to generate all 2^n subsets of an array of size n.
The i-th bit of integer `mask` indicates whether `nums[i]` is included in the current subset.

When it is used:
- Non-recursive power set generation.
- Bitmask Dynamic Programming (Traveling Salesperson, Assignment problem).
- Checking all combinations of up to n <= 20 elements iteratively.

The Key Idea:
For an array of size n:
Total subsets = `1 << n` (which is 2^n).
For each integer `mask` from 0 to `(1 << n) - 1`:
  Construct subset:
  For each bit position `i` from 0 to n-1:
    If `(mask >> i) & 1 == 1`:
      Include `nums[i]` in the current subset.

Time Complexity:
- O(n * 2^n) time.

Space Complexity:
- O(1) auxiliary space (excluding generated subsets).
"""


def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    """Generates all subsets using bit manipulation."""
    n = len(nums)
    total_subsets = 1 << n  # 2^n
    all_subsets: list[list[int]] = []

    for mask in range(total_subsets):
        current_subset: list[int] = []
        for i in range(n):
            # Check if i-th bit is set in mask
            if (mask >> i) & 1:
                current_subset.append(nums[i])
        all_subsets.append(current_subset)

    return all_subsets


if __name__ == "__main__":
    res = subsets_bitmask([1, 2, 3])
    assert len(res) == 8  # 2^3 = 8
    assert [] in res
    assert [1] in res
    assert [1, 2, 3] in res

    assert subsets_bitmask([]) == [[]]

    print("All Bitmask Subsets tests passed successfully.")
