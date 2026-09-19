"""
Binary Search on Answer (Predicate / Feasibility Search)

What it is:
A powerful algorithmic pattern where binary search is applied not to a sorted array,
but to the RANGE OF POSSIBLE ANSWERS [low, high]. A monotonic feasibility function
`is_possible(mid)` is used to decide whether to search left or right.

When it is used:
- The problem asks for the "minimum possible maximum" or "maximum possible minimum".
- Checking if a specific answer works is easy (e.g. O(n)), but finding the optimal directly is hard.
- The condition is monotonic:
  e.g., If speed `x` works, all speeds `> x` also work.
  e.g., If capacity `c` works, all capacities `> c` also work.
- Classic Problems: Koko Eating Bananas, Capacity To Ship Packages, Split Array Largest Sum.

The Key Idea:
1. Define the search space [left, right] based on problem limits (e.g. min speed to max pile).
2. Write a helper function `is_possible(candidate_answer) -> bool`.
3. If `is_possible(mid)` is True, record mid as a possible answer and try to find a better one:
   - For minimization: right = mid - 1 (or search left).
   - For maximization: left = mid + 1 (or search right).
4. Return the optimal feasible answer.

Time Complexity:
- O(cost_of_check * log(search_space_range))

Space Complexity:
- O(1) auxiliary space.

Common Pitfalls / Edge Cases:
- Setting left and right bounds improperly (e.g., left = 0 causing division by zero).
- Inverting the monotonicity direction.
"""

import math


def min_eating_speed(piles: list[int], hours: int) -> int:
    """Finds the minimum integer eating speed k (bananas/hour) to eat all piles within `hours`.

    (LeetCode 875 - Koko Eating Bananas)
    """

    def can_finish(speed: int) -> bool:
        total_hours_needed = 0
        for pile in piles:
            # Ceiling division: math.ceil(pile / speed) or (pile + speed - 1) // speed
            total_hours_needed += math.ceil(pile / speed)

        return total_hours_needed <= hours

    # Search space: speed must be between 1 and max(piles)
    left = 1
    right = max(piles)
    optimal_speed = right
    while left <= right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            optimal_speed = mid  # mid is valid, try to find a slower speed
            right = mid - 1
        else:
            left = mid + 1  # too slow, must increase speed

    return optimal_speed


if __name__ == "__main__":
    # Test case 1: piles = [3, 6, 7, 11], hours = 8
    # Speed 4: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8 -> feasible
    assert min_eating_speed([3, 6, 7, 11], 8) == 4

    # Test case 2: piles = [30, 11, 23, 4, 20], hours = 5
    # Must finish each pile in 1 hour -> speed must be max(piles) = 30
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30

    # Test case 3: piles = [30, 11, 23, 4, 20], hours = 6
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23

    print("All Binary Search on Answer tests passed successfully.")
