"""
Largest Rectangle in Histogram

What it is:
Given an array of integers `heights` representing the histogram's bar height where
the width of each bar is 1, finds the area of the largest rectangle in the histogram.

When it is used:
- LeetCode 84 (Largest Rectangle in Histogram).
- LeetCode 85 (Maximal Rectangle in 2D Binary Matrix - using LeetCode 84 row by row).

The Key Idea:
For each bar at index `i`, what is the largest rectangle where bar `i` is the SHORTEST bar?
Width extends:
- Leftwards until the first bar strictly shorter than `heights[i]`.
- Rightwards until the first bar strictly shorter than `heights[i]`.

Monotonic Increasing Stack:
Maintain indices of bars in strictly increasing height order.
When a bar of height `heights[i]` arrives that is shorter than `heights[stack[-1]]`:
1. Pop the top bar: `height = heights[stack.pop()]`.
2. The right boundary for this popped bar is `i`.
3. The left boundary is the new `stack[-1]` (or -1 if stack is now empty).
4. `width = i - left_boundary - 1`
5. `area = height * width`.
Append a sentinel height of 0 at the end to automatically flush out all remaining bars in the stack.

Time Complexity:
- O(n) single pass: each index is pushed once and popped once.

Space Complexity:
- O(n) auxiliary space for the stack.

Common Pitfalls / Edge Cases:
- Empty array returns 0.
- All bars of same height: width calculation handles correctly.
- Forgetting to process remaining bars on stack (sentinel `0` solves this cleanly).
"""


def largest_rectangle_area(heights: list[int]) -> int:
    """Computes the largest rectangle area in a histogram in O(n) time and O(n) space."""
    if not heights:
        return 0

    max_area = 0
    # Append 0 to flush all bars from the stack at the end
    extended_heights = heights + [0]
    stack: list[int] = []

    for current_index, current_height in enumerate(extended_heights):
        while stack and current_height < extended_heights[stack[-1]]:
            popped_height = extended_heights[stack.pop()]
            # If stack is empty, left boundary is -1
            left_boundary = stack[-1] if stack else -1
            width = current_index - left_boundary - 1
            max_area = max(max_area, popped_height * width)

        stack.append(current_index)

    return max_area


if __name__ == "__main__":
    # Standard case
    assert (
        largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    )  # bars 5 and 6: min_height 5, width 2
    assert largest_rectangle_area([2, 4]) == 4

    # Single bar
    assert largest_rectangle_area([5]) == 5

    # Strictly increasing
    assert largest_rectangle_area([1, 2, 3, 4, 5]) == 9  # min 3 * width 3

    # Empty
    assert largest_rectangle_area([]) == 0

    print("All Largest Rectangle tests passed successfully.")
