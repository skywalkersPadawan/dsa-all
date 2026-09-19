"""
Fractional Knapsack Problem

What it is:
Given weights and values of n items, put these items in a knapsack of capacity W
to get the MAXIMUM total value. Unlike 0/1 knapsack, we CAN take arbitrary fractions of an item.

When it is used:
- Resource blending (liquids, chemicals, grains, financial portfolio weightings).
- Demonstrates why Greedy solves Fractional Knapsack in O(n log n), but FAILS for 0/1 Knapsack
  (which requires Dynamic Programming).

The Key Idea:
Greedy by Value-to-Weight Ratio:
1. Calculate ratio `value / weight` for every item.
2. Sort items in descending order of their ratio.
3. Iterate through sorted items:
   - If the knapsack can accommodate the entire item, take all of it.
   - If not, take the fraction `remaining_capacity / item_weight` and stop.

Time Complexity:
- O(n log n) sorting time.

Space Complexity:
- O(1) auxiliary space.
"""


def fractional_knapsack(capacity: float, items: list[tuple[float, float]]) -> float:
    """Finds maximum value achievable within capacity.

    items format: [(weight, value), ...]
    """
    # Sort items by value / weight in descending order
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for weight, value in sorted_items:
        if remaining_capacity <= 0:
            break

        if weight <= remaining_capacity:
            # Take whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0

    return total_value


if __name__ == "__main__":
    # Items: (weight, value)
    # Item 1: (10, 60) -> ratio 6.0
    # Item 2: (20, 100) -> ratio 5.0
    # Item 3: (30, 120) -> ratio 4.0
    # Capacity = 50
    # Take all of item 1 (10kg, $60), all of item 2 (20kg, $100), 20kg of item 3 ($80)
    # Total = 60 + 100 + 80 = 240
    test_items = [(10, 60), (20, 100), (30, 120)]
    assert fractional_knapsack(50, test_items) == 240.0

    print("All Fractional Knapsack tests passed successfully.")
