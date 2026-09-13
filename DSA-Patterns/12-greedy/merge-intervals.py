"""
Merge Intervals Pattern

What it is:
Given an array of intervals where `intervals[i] = [start, end]`, merges all overlapping
intervals, and returns an array of the non-overlapping intervals that cover all the
intervals in the input.

When it is used:
- LeetCode 56 (Merge Intervals).
- Calendar scheduling, booking consolidation, disjoint memory range tracking.

The Key Idea:
1. Sort intervals by their START time in ascending order.
2. Initialize `merged = [intervals[0]]`.
3. For each subsequent interval `[curr_start, curr_end]`:
   - Let `last_end = merged[-1][1]`.
   - If `curr_start <= last_end` (Overlap!):
     Merge them by updating `merged[-1][1] = max(last_end, curr_end)`.
   - If `curr_start > last_end` (No overlap):
     Append `[curr_start, curr_end]` as a new independent interval to `merged`.

Time Complexity:
- O(n log n) sorting time, followed by O(n) single merge pass.

Space Complexity:
- O(n) auxiliary space to store the merged intervals.
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merges all overlapping intervals.

    Time: O(n log n), Space: O(n).
    """
    if not intervals:
        return []

    # Sort primarily by start time
    intervals.sort(key=lambda x: x[0])

    merged: list[list[int]] = [intervals[0]]

    for current in intervals[1:]:
        previous = merged[-1]
        # Overlap: current starts before or at the moment previous ends
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    return merged


if __name__ == "__main__":
    test_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected_1 = [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals(test_1) == expected_1

    test_2 = [[1, 4], [4, 5]]
    expected_2 = [[1, 5]]
    assert merge_intervals(test_2) == expected_2

    assert merge_intervals([]) == []
    assert merge_intervals([[1, 2]]) == [[1, 2]]

    print("All Merge Intervals tests passed successfully.")
