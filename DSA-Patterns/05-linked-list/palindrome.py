"""
Palindrome Linked List

What it is:
Checks whether a singly linked list is a palindrome (reads identically forwards and backwards).

When it is used:
- LeetCode 234 (Palindrome Linked List).
- Verifying symmetric structures without copying to an array.

The Key Idea (O(1) Space In-Place Approach):
1. Find Middle: Use fast and slow pointers to locate the end of the first half.
2. Reverse Second Half: Reverse the linked list starting from `slow.next`.
3. Check Palindrome: Compare values node by node from `head` and the head of the reversed second half.
4. (Optional best practice): Restore list by reversing the second half back.

Time Complexity:
- O(n) total: O(n) to find middle + O(n) to reverse + O(n) to compare.

Space Complexity:
- O(1) auxiliary space (operates directly on node pointers).

Common Pitfalls / Edge Cases:
- Odd vs Even lengths: handled cleanly because the reversed second half is always <= first half length.
- Single node or empty list is always a palindrome.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def is_palindrome_linked_list(head: Optional[ListNode]) -> bool:
    """Checks if a singly linked list is a palindrome in O(n) time and O(1) space."""
    if not head or not head.next:
        return True

    # 1. Find the first middle node (slow)
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse the second half
    second_half_head = reverse_list(slow.next)

    # 3. Compare first half and reversed second half
    first_pointer = head
    second_pointer = second_half_head
    is_palindrome = True

    while second_pointer:
        if first_pointer.val != second_pointer.val:
            is_palindrome = False
            break
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    # 4. Optional: Restore second half
    slow.next = reverse_list(second_half_head)

    return is_palindrome


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Helper to reverse a linked list in-place."""
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


# Helpers
def from_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    # Even palindrome: 1 -> 2 -> 2 -> 1
    assert is_palindrome_linked_list(from_list([1, 2, 2, 1])) is True

    # Odd palindrome: 1 -> 2 -> 3 -> 2 -> 1
    assert is_palindrome_linked_list(from_list([1, 2, 3, 2, 1])) is True

    # Non-palindrome: 1 -> 2
    assert is_palindrome_linked_list(from_list([1, 2])) is False

    # Single node & empty
    assert is_palindrome_linked_list(from_list([1])) is True
    assert is_palindrome_linked_list(None) is True

    print("All Palindrome Linked List tests passed successfully.")
