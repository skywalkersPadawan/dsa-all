"""
Middle of a Linked List

What it is:
Finds the middle node of a singly linked list in a single pass.
If there are two middle nodes (even length), it typically returns the second middle node
(standard LeetCode 876 convention).

When it is used:
- Subroutine in Merge Sort on Linked Lists (splitting list in half).
- Subroutine in Palindrome Linked List and Reorder List.
- LeetCode 876 (Middle of the Linked List).

The Key Idea:
Fast and Slow Pointer Pattern (Tortoise and Hare):
- Initialize `slow = head` and `fast = head`.
- In each step, move `slow` by 1 step (`slow = slow.next`) and `fast` by 2 steps (`fast = fast.next.next`).
- When `fast` reaches the end (either `fast is None` or `fast.next is None`), `slow` is guaranteed
  to be at the middle.

Even vs Odd Length:
- Odd length [1 -> 2 -> 3]: fast lands on 3 (fast.next is None); slow lands on 2 (exact mid).
- Even length [1 -> 2 -> 3 -> 4]: fast lands on None; slow lands on 3 (second middle).
- If first middle is needed for even length, loop while `fast.next and fast.next.next`.

Time Complexity:
- O(n) single pass (n / 2 steps).

Space Complexity:
- O(1) auxiliary space (only two pointers).

Common Pitfalls / Edge Cases:
- Checking `while fast and fast.next` ensures `fast.next.next` never raises AttributeError.
- Empty list: returns None. Single node: returns the node.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Returns the second middle node for even-length lists (LeetCode 876)."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_first_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Returns the first middle node for even-length lists (useful for list split in merge sort)."""
    if not head or not head.next:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Helpers
def from_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next

    return dummy.next


if __name__ == "__main__":
    # Odd length: [1, 2, 3, 4, 5] -> middle is 3
    odd_list = from_list([1, 2, 3, 4, 5])
    mid_odd = find_middle_node(odd_list)
    assert mid_odd is not None and mid_odd.val == 3

    # Even length: [1, 2, 3, 4, 5, 6] -> second middle is 4
    even_list = from_list([1, 2, 3, 4, 5, 6])
    mid_even = find_middle_node(even_list)
    assert mid_even is not None and mid_even.val == 4

    # First middle on even list: [1, 2, 3, 4] -> 2
    first_mid = find_first_middle_node(from_list([1, 2, 3, 4]))
    assert first_mid is not None and first_mid.val == 2

    # Single node
    single = from_list([10])
    assert find_middle_node(single).val == 10

    # Empty
    assert find_middle_node(None) is None

    print("All Middle of Linked List tests passed successfully.")
