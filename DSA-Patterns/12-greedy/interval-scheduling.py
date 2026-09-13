"""
Interval Scheduling (Non-overlapping Intervals)

What it is:
Given an array of intervals `intervals` where `intervals[i] = [start, end]`,
returns the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

When it is used:
- LeetCode 435 (Non-overlapping Intervals).
- Video Stitching (LeetCode 1024).
- Scheduling appointments on a single calendar.

The Key Idea:
Equivalent to Activity Selection:
"Minimizing intervals removed" is mathematically identical to "Maximizing non-overlapping intervals kept"!
1. Sort intervals by their END time in ascending order.
2. Maintain `count_removed = 0` and `prev_end = float('-inf')`.
3. For each `[start, end]`:
   - If `start < prev_end`: this interval overlaps with our kept interval.
     Because intervals are sorted by end time, the current interval ends later or equal to prev_end,
     so we GREEDILY REMOVE current interval: `count_removed += 1`.
   - Otherwise: no overlap! Keep it: `prev_end = end`.

Time Complexity:
- O(n log n) sorting time.

Space Complexity:
- O(1) auxiliary space (excluding sort).
"""


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """Returns minimum number of intervals to remove to eliminate all overlaps."""
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    removed_count = 0
    previous_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < previous_end:
            # Overlap detected -> greedily remove current interval
            removed_count += 1
        else:
            # No overlap -> update previous_end
            previous_end = end

    return removed_count


if __name__ == "__main__":
    # Remove [1, 3] to leave [1, 2] and [2, 3]
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

    # Identical intervals: remove all but 1
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2

    # Already non-overlapping
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0

    print("All Interval Scheduling tests passed successfully.")
