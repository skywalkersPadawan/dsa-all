"""
Minimum Platforms for Railway Station

What it is:
Given arrival and departure times of all trains that reach a railway station,
find the minimum number of platforms required for the railway station so that
no train is kept waiting.

When it is used:
- Railway / flight gate assignment.
- Identical algorithmic pattern to Meeting Rooms II.

The Key Idea:
Sweep-line / Event Sorting:
1. Sort both `arrivals` and `departures` independently in ascending order.
2. Maintain two pointers `i = 0` (arrivals) and `j = 0` (departures).
3. If `arrivals[i] <= departures[j]`:
   A train has arrived before the earlier train left.
   Increment `platforms_needed += 1`, advance `i += 1`.
4. Otherwise:
   A train has departed, freeing up a platform.
   Decrement `platforms_needed -= 1`, advance `j += 1`.
5. Max value of `platforms_needed` at any point in time is the answer.

Time Complexity:
- O(n log n) sorting.

Space Complexity:
- O(1) auxiliary space (if sorting input arrays in-place).
"""


def find_platform(arrivals: list[int], departures: list[int]) -> int:
    """Calculates minimum platforms required at station."""
    arrivals.sort()
    departures.sort()

    platforms_needed = 0
    max_platforms = 0
    i = 0  # pointer for arrival
    j = 0  # pointer for departure
    n = len(arrivals)

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return max_platforms


if __name__ == "__main__":
    # Times in 24-hr format (e.g. 900 = 09:00, 910 = 09:10)
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    # At 9:50, trains 2 and 3 are on platforms, train 1 has departed -> 3 platforms max
    assert find_platform(arr, dep) == 3

    assert find_platform([900, 1100, 1235], [1000, 1200, 1240]) == 1

    print("All Minimum Platforms tests passed successfully.")
