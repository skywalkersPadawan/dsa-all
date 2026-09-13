"""
Gas Station (Circular Tour Pattern)

What it is:
There are n gas stations along a circular route. You are given two integer arrays
`gas` and `cost`. You begin the journey with an empty tank at one of the stations.
Return the starting station's index if you can travel around the circuit once in the
clockwise direction, otherwise return -1.

When it is used:
- LeetCode 134 (Gas Station).
- Resource-constrained circular tours and pipeline balancing.

The Key Idea:
Two Vital Insights:
1. Feasibility: If `sum(gas) < sum(cost)`, it is mathematically impossible to complete
   the circuit regardless of where you start -> return -1 immediately!
2. Greedy Start Pruning:
   If you start at station `A` and run out of gas at station `B`, then NO station
   between `A` and `B` could possibly be the start either (because starting at any
   intermediate station would arrive at B with even less fuel).
   Therefore, greedily reset the starting candidate to `B + 1` and reset `tank = 0`!

Time Complexity:
- O(n) single pass.

Space Complexity:
- O(1) auxiliary space.
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """Returns starting gas station index, or -1 if impossible."""
    if sum(gas) < sum(cost):
        return -1

    total_tank = 0
    start_station = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        # If tank dips below 0, station i cannot be part of the successful prefix
        if total_tank < 0:
            start_station = i + 1
            total_tank = 0

    return start_station


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    # Start at station 3 (index 3, gas[3]=4, cost[3]=1)
    assert can_complete_circuit(gas, cost) == 3

    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    # sum(gas) = 9 < sum(cost) = 10 -> impossible
    assert can_complete_circuit(gas2, cost2) == -1

    print("All Gas Station tests passed successfully.")
