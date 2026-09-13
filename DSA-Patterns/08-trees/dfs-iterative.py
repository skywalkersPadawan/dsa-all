"""
Depth-First Search (DFS) - Iterative on Binary Trees

What it is:
Simulates recursive depth-first search using an explicit LIFO `stack` in Python.
Eliminates recursion overhead and prevents stack overflow on deep/skewed trees.

When it is used:
- Interview questions explicitly requesting "solve without recursion".
- Extremely deep trees where Python's recursion limit (default 1000) would be exceeded.
- Tree iterators (BSTIterator - LeetCode 173).

The Key Idea:
- Preorder (Root, Left, Right):
  Push `root` to stack. Pop `node`. Process `node.val`.
  Push `node.right` first, then `node.left` (so left is popped and processed first).
- Inorder (Left, Root, Right):
  Keep pushing `current` and moving `current = current.left` until hitting None.
  Then pop from stack, process value, and move to `current = node.right`.

Time Complexity:
- O(n) visiting all n nodes.

Space Complexity:
- O(h) auxiliary space for the stack.
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def preorder_iterative(root: Optional[TreeNode]) -> list[int]:
    """Iterative preorder traversal (Root -> Left -> Right) using a stack."""
    if not root:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so that left is popped and processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_iterative(root: Optional[TreeNode]) -> list[int]:
    """Iterative inorder traversal (Left -> Root -> Right) using a stack."""
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root

    while current or stack:
        # Reach the leftmost node of the current subtree
        while current:
            stack.append(current)
            current = current.left

        # Current must be None at this point; pop top node
        current = stack.pop()
        result.append(current.val)

        # We have visited the node and its left subtree; now visit right subtree
        current = current.right

    return result


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert preorder_iterative(root) == [1, 2, 4, 5, 3]
    assert inorder_iterative(root) == [4, 2, 5, 1, 3]

    assert preorder_iterative(None) == []
    assert inorder_iterative(None) == []

    print("All DFS Iterative tests passed successfully.")
