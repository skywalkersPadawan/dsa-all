"""
Linked List Basics

What it is:
A linear data structure in which elements (nodes) are stored non-contiguously in memory.
Each node contains a data value and a pointer (reference) to the next node in the sequence.

When it is used:
- When constant-time insertions or deletions from the beginning or at a known pointer are needed.
- Implementing queues, stacks, or chaining in hash tables.
- LRU Cache (with doubly linked lists).

The Key Idea:
A standard singly linked list node has two attributes:
- `val`: data value
- `next`: reference to next ListNode (or None)
To prevent special-casing empty lists or head modifications, a `dummy` (sentinel) node
is frequently used: `dummy = ListNode(0, head)`.

Time Complexity:
- Prepend (insert at head): O(1)
- Append (insert at tail): O(n) without tail pointer, O(1) with tail pointer
- Search: O(n)
- Delete node given previous pointer: O(1)

Space Complexity:
- O(n) total space (one node per item).
"""

from typing import Optional


class ListNode:
    """Standard singly-linked list node."""

    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def create_linked_list(values: list[int]) -> Optional[ListNode]:
    """Helper to construct a linked list from a Python list."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Helper to convert a linked list into a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def insert_at_head(head: Optional[ListNode], val: int) -> ListNode:
    """Inserts a new node at the head in O(1) time."""
    return ListNode(val, head)


def delete_node_by_value(
    head: Optional[ListNode], target: int
) -> Optional[ListNode]:
    """Deletes the first node with value == target using a dummy node."""
    dummy = ListNode(0, head)
    current = dummy

    while current.next:
        if current.next.val == target:
            current.next = current.next.next
            break
        current = current.next

    return dummy.next


if __name__ == "__main__":
    # Test creation and conversion
    ll = create_linked_list([1, 2, 3, 4])
    assert linked_list_to_list(ll) == [1, 2, 3, 4]

    # Test insert at head
    ll = insert_at_head(ll, 0)
    assert linked_list_to_list(ll) == [0, 1, 2, 3, 4]

    # Test delete node
    ll = delete_node_by_value(ll, 2)
    assert linked_list_to_list(ll) == [0, 1, 3, 4]

    # Delete head
    ll = delete_node_by_value(ll, 0)
    assert linked_list_to_list(ll) == [1, 3, 4]

    # Empty list
    assert create_linked_list([]) is None
    assert linked_list_to_list(None) == []

    print("All Linked List Basics tests passed successfully.")
