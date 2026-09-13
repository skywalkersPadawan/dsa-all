"""
Merge Two Sorted Lists

What it is:
Merges two already sorted singly linked lists into a single sorted linked list by splicing
together the nodes of the original lists (in-place).

When it is used:
- LeetCode 21 (Merge Two Sorted Lists).
- The merge subroutine in Merge Sort on Linked Lists (LeetCode 148).
- Merge k Sorted Lists (LeetCode 23) using divide-and-conquer pairing.

The Key Idea:
1. Create a sentinel `dummy` node to anchor the beginning of the merged list.
2. Maintain a `tail` pointer starting at `dummy`.
3. Compare `list1.val` and `list2.val`:
   - Point `tail.next` to the smaller node and advance that list's pointer.
   - Advance `tail = tail.next`.
4. Once one list is exhausted, directly attach the non-empty list to `tail.next`.
5. Return `dummy.next`.

Time Complexity:
- O(n + m) where n and m are lengths of the two lists.

Space Complexity:
- O(1) auxiliary space (modifies existing pointers in-place).

Common Pitfalls / Edge Cases:
- One or both lists are empty: directly returns the other list.
- Forgetting to attach the remainder of the non-empty list at the end.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """Merges two sorted linked lists in O(n + m) time and O(1) space."""
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach whichever list still has nodes remaining
    tail.next = list1 if list1 else list2

    return dummy.next


# Helpers
def to_list(head: Optional[ListNode]) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def from_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    l1 = from_list([1, 2, 4])
    l2 = from_list([1, 3, 4])
    merged = merge_two_lists(l1, l2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]

    # One empty list
    assert to_list(merge_two_lists(None, from_list([0]))) == [0]

    # Both empty lists
    assert merge_two_lists(None, None) is None

    print("All Merge Sorted Lists tests passed successfully.")
