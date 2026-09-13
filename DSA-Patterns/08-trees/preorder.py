"""
Binary Tree Preorder Traversal

What it is:
A depth-first traversal where each node is visited BEFORE its subtrees:
Root -> Left -> Right.

When it is used:
- Creating a complete duplicate/clone of a binary tree.
- Serializing a tree structure to a string/list.
- Prefix expression evaluation in expression trees.
- LeetCode 144 (Binary Tree Preorder Traversal).

The Key Idea:
- Recursive: Visit `node.val`, recurse `preorder(node.left)`, recurse `preorder(node.right)`.
- Iterative: Use a stack. Push `root`. Pop `node`, record `node.val`, then push `node.right`
  followed by `node.left` (so left is popped and processed next).

Time Complexity:
- O(n) visiting all n nodes.

Space Complexity:
- O(h) where h is tree height.
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


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Standard interview preorder traversal using an explicit stack."""
    if not root:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Right child pushed first so left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


if __name__ == "__main__":
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    assert preorder_traversal(root) == [1, 2, 3]
    assert preorder_traversal(None) == []

    print("All Preorder tests passed successfully.")
