"""
Activity Selection Problem

What it is:
Given a set of activities with start and finish times `[start, finish]`, select the
MAXIMUM number of activities that can be performed by a single person/resource,
assuming that a person can only work on a single activity at a time.

When it is used:
- Resource allocation, classroom scheduling, CPU task scheduling.
- Foundation for interval scheduling algorithms.

The Key Idea:
Greedy Choice Rule:
ALWAYS select the activity that FINISHES EARLIEST!
Why? Finishing earlier leaves the maximum possible remaining time for subsequent activities.
1. Sort all activities in non-decreasing order of their FINISH times.
2. Select the first activity. Set `last_finish_time = activity.finish`.
3. For each subsequent activity:
   If `activity.start >= last_finish_time`:
     Select this activity and update `last_finish_time = activity.finish`.

Time Complexity:
- O(n log n) to sort activities by finish time, followed by O(n) single scan.

Space Complexity:
- O(1) auxiliary space (excluding sorted array/output).
"""


def max_activities(activities: list[list[int]]) -> list[list[int]]:
    """Selects maximum number of non-overlapping activities.

    activities format: [[start, finish], ...]
    """
    if not activities:
        return []

    # Sort primarily by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    selected = [sorted_activities[0]]
    last_finish_time = sorted_activities[0][1]

    for start, finish in sorted_activities[1:]:
        if start >= last_finish_time:
            selected.append([start, finish])
            last_finish_time = finish

    return selected


if __name__ == "__main__":
    # Activities: [[start, finish]]
    test_acts = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 9]]
    chosen = max_activities(test_acts)
    # Optimal set: [1, 4], [5, 7], [8, 9] (size 3)
    assert len(chosen) == 3
    assert chosen == [[1, 4], [5, 7], [8, 9]]

    assert max_activities([]) == []

    print("All Activity Selection tests passed successfully.")
