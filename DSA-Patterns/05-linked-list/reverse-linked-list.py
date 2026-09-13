"""
Reverse a Linked List

What it is:
Reverses the direction of pointers in a singly linked list so that the original tail
becomes the new head and the original head points to None.

When it is used:
- Reversing a linked list (LeetCode 206).
- Subroutine in Palindrome Linked List (reverse second half).
- Reorder List (reverse second half and merge).
- Reverse Nodes in k-Group (LeetCode 25).

The Key Idea:
Maintain three pointers:
- `previous`: initially None
- `current`: initially head
- `next_node`: temporary pointer to save `current.next` before overwriting it

Loop invariant:
While `current` is not None:
1. `next_node = current.next` (save next)
2. `current.next = previous` (reverse pointer)
3. `previous = current` (advance previous)
4. `current = next_node` (advance current)
At loop termination, `previous` is the new head.

Time Complexity:
- O(n) single pass through the list.

Space Complexity:
- Iterative: O(1) auxiliary space.
- Recursive: O(n) auxiliary space due to call stack.

Common Pitfalls / Edge Cases:
- Empty list (`head is None`) or single node list: returns `head`.
- Forgetting to save `next_node` before pointing `current.next` to `previous` causes losing the rest of the list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list iteratively in O(n) time and O(1) space."""
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list recursively in O(n) time and O(n) space."""
    if not head or not head.next:
        return head

    # Reverse the rest of the list
    new_head = reverse_list_recursive(head.next)

    # Put head at the end of reversed sublist
    head.next.next = head
    head.next = None

    return new_head


# Helper for testing
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
    # Test iterative reverse
    head1 = from_list([1, 2, 3, 4, 5])
    rev1 = reverse_list(head1)
    assert to_list(rev1) == [5, 4, 3, 2, 1]

    # Test single element & empty
    assert to_list(reverse_list(from_list([42]))) == [42]
    assert reverse_list(None) is None

    # Test recursive reverse
    head2 = from_list([10, 20, 30])
    rev2 = reverse_list_recursive(head2)
    assert to_list(rev2) == [30, 20, 10]

    print("All Reverse Linked List tests passed successfully.")
