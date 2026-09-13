"""
Intersection of Two Linked Lists

What it is:
Finds the node at which the intersection of two singly linked lists begins (i.e. the shared reference).
If the two linked lists have no intersection at all, returns None.

When it is used:
- LeetCode 160 (Intersection of Two Linked Lists).
- Detecting shared paths or convergent references in singly-linked structures.

The Key Idea (Two-Pointer Equalizer Trick):
Let length of list A be `a + c` and list B be `b + c`, where `c` is the length of the shared part.
- Pointer `pA` starts at `headA`, and `pB` starts at `headB`.
- When `pA` reaches the end of list A, redirect it to `headB`.
- When `pB` reaches the end of list B, redirect it to `headA`.
- Both pointers travel exactly `(a + c + b)` and `(b + c + a)` steps!
- Because total distances are identical, they will collide at the intersection node
  on the second pass, or both hit `None` simultaneously if no intersection exists.

Time Complexity:
- O(m + n) where m and n are the lengths of the two lists.

Space Complexity:
- O(1) auxiliary space.

Common Pitfalls / Edge Cases:
- Comparing node values (`pA.val == pB.val`) instead of node references (`pA == pB`).
  Intersection means shared identical memory nodes, not merely equal values.
- No intersection: both pointers will become None and `pA == pB` evaluates to True (returns None).
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def get_intersection_node(
    headA: Optional[ListNode], headB: Optional[ListNode]
) -> Optional[ListNode]:
    """Finds intersection node using two-pointer redirection.

    Time: O(m + n), Space: O(1).
    """
    if not headA or not headB:
        return None

    pointer_a = headA
    pointer_b = headB

    # Loop terminates when pointers meet (either at intersection node or both None)
    while pointer_a != pointer_b:
        pointer_a = pointer_a.next if pointer_a else headB
        pointer_b = pointer_b.next if pointer_b else headA

    return pointer_a


if __name__ == "__main__":
    # Create shared segment: 8 -> 4 -> 5
    shared = ListNode(8, ListNode(4, ListNode(5)))

    # List A: 4 -> 1 -> (shared: 8 -> 4 -> 5)
    headA = ListNode(4, ListNode(1, shared))

    # List B: 5 -> 6 -> 1 -> (shared: 8 -> 4 -> 5)
    headB = ListNode(5, ListNode(6, ListNode(1, shared)))

    result = get_intersection_node(headA, headB)
    assert result == shared
    assert result.val == 8

    # No intersection
    non_intersect_1 = ListNode(1, ListNode(2))
    non_intersect_2 = ListNode(3, ListNode(4))
    assert get_intersection_node(non_intersect_1, non_intersect_2) is None

    # One list empty
    assert get_intersection_node(None, headA) is None

    print("All Intersection of Two Linked Lists tests passed successfully.")
