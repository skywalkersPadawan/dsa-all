"""
Cycle Detection in Linked List (Floyd's Tortoise and Hare)

What it is:
Detects whether a linked list contains a cycle (a node whose next pointer points back
to a previously visited node), and optionally finds the node where the cycle begins.

When it is used:
- Linked List Cycle I (LeetCode 141).
- Linked List Cycle II - Find entry point (LeetCode 142).
- Find the Duplicate Number in array (LeetCode 287 - cycle detection on array values).

The Key Idea:
Part 1: Detecting Cycle
- Initialize `slow = head` and `fast = head`.
- Move `slow` by 1 and `fast` by 2.
- If `fast` or `fast.next` becomes None, there is no cycle.
- If `slow == fast`, a cycle exists.

Part 2: Finding Cycle Start Node
- Mathematical insight: When slow and fast meet, the distance from `head` to the cycle start
  equals the distance from the `meeting point` to the cycle start (modulo cycle length).
- Reset one pointer to `head` and keep the other at the `meeting point`.
- Move both pointers 1 step at a time: the node where they meet is the start of the cycle!

Time Complexity:
- O(n) time.

Space Complexity:
- O(1) auxiliary space (no hash set of visited nodes needed).

Common Pitfalls / Edge Cases:
- Moving `fast` before checking `fast` and `fast.next` causes `AttributeError`.
- No cycle list returns `False` or `None`.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def has_cycle(head: Optional[ListNode]) -> bool:
    """Returns True if the linked list has a cycle, False otherwise."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """Returns the node where the cycle begins, or None if there is no cycle."""
    slow = head
    fast = head

    # Phase 1: Determine if a cycle exists
    has_loop = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_loop = True
            break

    if not has_loop:
        return None

    # Phase 2: Find cycle entry node
    # Reset slow to head, advance both 1 step at a time
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == "__main__":
    # 1. List without cycle: 1 -> 2 -> 3 -> 4 -> None
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    assert has_cycle(n1) is False
    assert detect_cycle_start(n1) is None

    # 2. List with cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle starts at node 2)
    n4.next = n2
    assert has_cycle(n1) is True
    entry = detect_cycle_start(n1)
    assert entry is not None and entry.val == 2

    # 3. Single self-looping node: 1 -> 1
    solo = ListNode(10)
    solo.next = solo
    assert has_cycle(solo) is True
    assert detect_cycle_start(solo) == solo

    # 4. Empty list
    assert has_cycle(None) is False
    assert detect_cycle_start(None) is None
    print("All Cycle Detection tests passed successfully.")
