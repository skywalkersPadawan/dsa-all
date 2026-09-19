"""
Remove Nth Node From End of List

What it is:
Removes the n-th node from the end of a singly linked list and returns the head of the modified list,
achieved in a single pass using two pointers.

When it is used:
- LeetCode 19 (Remove Nth Node From End of List).
- Any single-pass lookup of the k-th element from the end of a stream or list.

The Key Idea:
Fast and Slow Pointer with a Dummy Node:
1. Create a `dummy = ListNode(0, head)` to cleanly handle removing the original head node.
2. Advance `fast` pointer by `n + 1` steps starting from `dummy`. This creates a gap of `n` nodes
   between `fast` and `slow`.
3. Move both `fast` and `slow` forward one step at a time until `fast` reaches None.
4. Now, `slow` is pointing directly at the node PRECEDING the node to be removed.
5. Delete the target node: `slow.next = slow.next.next`.
6. Return `dummy.next`.

Time Complexity:
- O(L) where L is the length of the linked list (single pass).

Space Complexity:
- O(1) auxiliary space.

Common Pitfalls / Edge Cases:
- Removing the head node (e.g. n == length): dummy node completely prevents edge-case logic.
- Single node list with n = 1: dummy.next becomes None.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Removes the n-th node from the end in a single pass.

    Time: O(L), Space: O(1).
    """
    dummy = ListNode(0, head)
    fast: Optional[ListNode] = dummy
    slow: Optional[ListNode] = dummy

    # Advance fast by n + 1 steps to create gap
    for _ in range(n + 1):
        if fast is not None:
            fast = fast.next

    # Move both until fast hits the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # Delete target node
    if slow and slow.next:
        slow.next = slow.next.next

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
    # Test case 1: [1, 2, 3, 4, 5], n = 2 -> [1, 2, 3, 5]
    ll1 = from_list([1, 2, 3, 4, 5])
    assert to_list(remove_nth_from_end(ll1, 2)) == [1, 2, 3, 5]

    # Test case 2: Remove head [1, 2], n = 2 -> [2]
    ll2 = from_list([1, 2])
    assert to_list(remove_nth_from_end(ll2, 2)) == [2]

    # Test case 3: Single node [1], n = 1 -> []
    ll3 = from_list([1])
    assert to_list(remove_nth_from_end(ll3, 1)) == []

    # Test case 4: Remove tail [1, 2, 3], n = 1 -> [1, 2]
    ll4 = from_list([1, 2, 3])
    assert to_list(remove_nth_from_end(ll4, 1)) == [1, 2]

    print("All Remove Nth Node tests passed successfully.")
