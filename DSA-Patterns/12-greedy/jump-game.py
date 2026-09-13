"""
Jump Game (Greedy Reachability Pattern)

What it is:
Given an integer array `nums` where `nums[i]` represents your maximum jump length at index `i`,
determines if you are able to reach the last index starting from index 0.

When it is used:
- LeetCode 55 (Jump Game).
- LeetCode 45 (Jump Game II - minimum jumps).
- Video Stitching (LeetCode 1024).

The Key Idea:
Forward Greedy Reach:
Track the farthest index `max_reachable` you can reach so far.
Iterate through the array:
- If current index `i > max_reachable`: you are stranded! Cannot move forward -> return False.
- Update `max_reachable = max(max_reachable, i + nums[i])`.
- If `max_reachable >= len(nums) - 1`: destination reached -> return True.

Alternative (Backward Goal Tracking):
Start `goal = len(nums) - 1`.
Loop backwards from `n - 2` down to 0:
If `i + nums[i] >= goal`, shift `goal = i`.
At the end, return `goal == 0`.

Time Complexity:
- O(n) single pass.

Space Complexity:
- O(1) auxiliary space.
"""


def can_jump(nums: list[int]) -> bool:
    """Returns True if the last index is reachable, False otherwise (LeetCode 55)."""
    max_reachable = 0
    target = len(nums) - 1

    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False

        max_reachable = max(max_reachable, i + jump)
        if max_reachable >= target:
            return True

    return False


def jump_game_min_jumps(nums: list[int]) -> int:
    """Returns minimum number of jumps to reach the last index (LeetCode 45)."""
    jumps = 0
    current_jump_end = 0
    farthest = 0

    # Don't need to jump from the last index
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        # If we have reached the end of the current jump horizon
        if i == current_jump_end:
            jumps += 1
            current_jump_end = farthest

    return jumps


if __name__ == "__main__":
    # Can jump
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False  # stranded at index 3
    assert can_jump([0]) is True

    # Min jumps (Jump Game II)
    assert jump_game_min_jumps([2, 3, 1, 1, 4]) == 2
    assert jump_game_min_jumps([2, 3, 0, 1, 4]) == 2

    print("All Jump Game tests passed successfully.")
