"""
Balanced Binary Tree

What it is:
A binary tree in which the depth of the two subtrees of every node never differs
by more than one: `abs(height(left) - height(right)) <= 1`.

When it is used:
- LeetCode 110 (Balanced Binary Tree).
- AVL and Red-Black tree invariant checks.

The Key Idea (Bottom-Up Postorder Check):
A naive top-down approach computes height at every node, resulting in O(n^2) runtime.
The optimal bottom-up approach checks balance while computing height in O(n):
- Return the node's height if balanced.
- Return `-1` as a sentinel if any subtree is unbalanced.
- If left or right subtree returns `-1`, or `abs(left_h - right_h) > 1`, propagate `-1` up immediately!

Time Complexity:
- O(n) single postorder pass with early termination.

Space Complexity:
- O(h) call stack space.
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


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Returns True if the tree is height-balanced, False otherwise."""

    def check_height(node: Optional[TreeNode]) -> int:
        """Returns height of subtree if balanced, or -1 if unbalanced."""
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        # Check balance condition for current node
        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1


if __name__ == "__main__":
    # Balanced tree:
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    balanced_root = TreeNode(3)
    balanced_root.left = TreeNode(9)
    balanced_root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert is_balanced(balanced_root) is True

    # Unbalanced tree:
    #         1
    #        /
    #       2
    #      /
    #     3
    unbalanced_root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert is_balanced(unbalanced_root) is False

    # Empty tree is balanced
    assert is_balanced(None) is True

    print("All Balanced Binary Tree tests passed successfully.")
