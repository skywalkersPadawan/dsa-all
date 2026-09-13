"""
Difference Array Pattern

What it is:
A technique used to apply multiple range updates (e.g. "add value val to all elements
in index range [left, right]") in O(1) time per update. Once all updates are recorded,
a single prefix sum pass reconstructs the final array in O(n) time.

When it is used:
- Multiple offline range addition operations:
  e.g., LeetCode 370 (Range Addition), LeetCode 1109 (Corporate Flight Bookings),
  LeetCode 1094 (Car Pooling).
- Sweep-line interval overlap counting.

The Key Idea:
Let `diff[i] = nums[i] - nums[i - 1]` (with `diff[0] = nums[0]`).
To add `val` to every element in `nums[left..right]`:
1. `diff[left] += val` (shifts all reconstructed values from left onwards up by val).
2. `diff[right + 1] -= val` (cancels the shift for indices strictly past right).
After all updates, the running prefix sum of `diff` yields the final updated array.

Time Complexity:
- Each range update: O(1) time.
- Final reconstruction: O(n) time.
- Total for k updates on array of size n: O(n + k), compared to naive O(n * k).

Space Complexity:
- O(n) auxiliary space for the difference array.

Common Pitfalls / Edge Cases:
- Index bounds: if `right + 1 == n`, do not update `diff[right + 1]` (out of bounds).
"""


class DifferenceArray:
    """Manages an array of size n and supports O(1) range updates."""

    def __init__(self, initial: list[int]):
        self.n = len(initial)
        # diff array of size n + 1 simplifies avoiding out-of-bounds check for right + 1
        self.diff = [0] * (self.n + 1)

        # Initialize diff from the initial array
        if initial:
            self.diff[0] = initial[0]
            for i in range(1, self.n):
                self.diff[i] = initial[i] - initial[i - 1]

    def update_range(self, left: int, right: int, val: int) -> None:
        """Adds val to all elements in range [left, right] (inclusive, 0-indexed) in O(1)."""
        self.diff[left] += val
        self.diff[right + 1] -= val

    def get_result(self) -> list[int]:
        """Reconstructs the updated array in O(n) using prefix sum."""
        result = [0] * self.n
        if self.n == 0:
            return result

        result[0] = self.diff[0]
        for i in range(1, self.n):
            result[i] = result[i - 1] + self.diff[i]

        return result


if __name__ == "__main__":
    # Start with an array of zeros of length 5
    initial_array = [0, 0, 0, 0, 0]
    da = DifferenceArray(initial_array)

    # Operations:
    # Add 2 to range [1, 3] -> [0, 2, 2, 2, 0]
    da.update_range(1, 3, 2)
    # Add 3 to range [2, 4] -> [0, 2, 5, 5, 3]
    da.update_range(2, 4, 3)
    # Add -2 to range [0, 2] -> [-2, 0, 3, 5, 3]
    da.update_range(0, 2, -2)

    assert da.get_result() == [-2, 0, 3, 5, 3]

    # Test with non-zero initial array
    da2 = DifferenceArray([1, 2, 3, 4, 5])
    da2.update_range(0, 4, 10)  # Add 10 to all
    assert da2.get_result() == [11, 12, 13, 14, 15]

    print("All Difference Array tests passed successfully.")
