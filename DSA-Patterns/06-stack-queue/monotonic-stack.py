"""
Monotonic Stack Pattern

What it is:
A stack whose elements are maintained in strictly monotonic order (either strictly
increasing or strictly decreasing from bottom to top).

When it is used:
- Finding the "Next Greater Element" or "Next Smaller Element" for every item in an array in O(n) time.
- Daily Temperatures (LeetCode 739).
- Largest Rectangle in Histogram (LeetCode 84).
- Trapping Rain Water (LeetCode 42).
- Online Stock Span (LeetCode 901).

The Key Idea:
- To find Next Greater Element: Maintain a monotonic decreasing stack (storing elements or indices).
  When a new element `nums[i]` arrives that is greater than `nums[stack[-1]]`, it "resolves" the
  elements on the stack:
  We pop `stack[-1]` and record `nums[i]` as its next greater element!
  Once smaller elements are cleared, push `i`.
- Each index is pushed once and popped at most once -> O(n) total amortized time!

Time Complexity:
- O(n) amortized time for processing entire array.

Space Complexity:
- O(n) auxiliary space for the stack.

Common Pitfalls / Edge Cases:
- Storing indices instead of values: usually essential because you need to compute distances
  or access original positions.
- Strict vs non-strict monotonicity (`nums[i] > stack[-1]` vs `nums[i] >= stack[-1]`).
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Given daily temperatures, returns an array answer such that answer[i] is the number of days

    you have to wait after the i-th day to get a warmer temperature. If none, answer[i] = 0.
    (LeetCode 739)
    """
    n = len(temperatures)
    answer = [0] * n
    # Stack stores indices of temperatures in decreasing order
    stack: list[int] = []

    for current_index, current_temp in enumerate(temperatures):
        # While current day is warmer than the day at the top of stack
        while stack and current_temp > temperatures[stack[-1]]:
            previous_index = stack.pop()
            answer[previous_index] = current_index - previous_index

        stack.append(current_index)

    return answer


if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures(temps) == expected

    # Strictly decreasing (no warmer day)
    assert daily_temperatures([30, 20, 10]) == [0, 0, 0]

    # Strictly increasing
    assert daily_temperatures([10, 20, 30]) == [1, 1, 0]

    print("All Monotonic Stack tests passed successfully.")
