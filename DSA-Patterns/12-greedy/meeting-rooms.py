"""
Meeting Rooms Patterns

What it is:
1. Meeting Rooms I (LeetCode 252): Can one person attend all meetings without overlap?
2. Meeting Rooms II (LeetCode 253): What is the MINIMUM number of conference rooms required?

When it is used:
- Resource scheduling, CPU thread pooling, classroom assignments.
- Foundation for interval overlap counting.

The Key Idea:
- Meeting Rooms I (Boolean Check):
  Sort intervals by start time. Check if any `intervals[i][0] < intervals[i - 1][1]`.
- Meeting Rooms II (Min Rooms Required):
  Chronological Event Separation (Sweep-line):
  1. Separate start times and end times into two independent arrays and sort both:
     `starts.sort()` and `ends.sort()`.
  2. Use two pointers `s` and `e`:
     - If `starts[s] < ends[e]`: a new meeting started before the earliest meeting ended.
       Allocate a new room! `rooms += 1`, `s += 1`.
     - Else: a meeting ended and freed a room.
       `rooms -= 1`, `e += 1`.
     Track `max_rooms = max(max_rooms, rooms)`.

Time Complexity:
- O(n log n) sorting.

Space Complexity:
- O(n) to store separate start and end arrays.
"""


def can_attend_all_meetings(intervals: list[list[int]]) -> bool:
    """Returns True if a person could attend all meetings without conflict (LeetCode 252)."""
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Finds minimum conference rooms needed (LeetCode 253).

    Time: O(n log n), Space: O(n).
    """
    if not intervals:
        return 0

    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    start_ptr = 0
    end_ptr = 0
    current_rooms = 0
    max_rooms = 0

    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
            start_ptr += 1
        else:
            current_rooms -= 1
            end_ptr += 1

    return max_rooms


if __name__ == "__main__":
    # Meeting Rooms I
    assert can_attend_all_meetings([[0, 30], [5, 10], [15, 20]]) is False
    assert can_attend_all_meetings([[7, 10], [2, 4]]) is True

    # Meeting Rooms II
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0

    print("All Meeting Rooms tests passed successfully.")
