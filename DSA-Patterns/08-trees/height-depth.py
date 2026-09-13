"""
Height and Depth of Binary Tree

What it is:
- Maximum Depth / Height: Number of nodes along the longest path from the root down to the farthest leaf.
  (LeetCode 104 - Maximum Depth of Binary Tree).
- Minimum Depth: Number of nodes along the shortest path from the root down to the nearest leaf.
  (LeetCode 111 - Minimum Depth of Binary Tree).

The Key Idea:
- Max Depth:
  Base case: `if not root: return 0`
  Recursive case: `1 + max(max_depth(root.left), max_depth(root.right))`
- Min Depth:
  Be careful! A node with only one child is NOT a leaf. The path must reach a true leaf
  (a node with neither left nor right child).
  If `not root.left`: return `1 + min_depth(root.right)`
  If `not root.right`: return `1 + min_depth(root.left)`
  Otherwise: return `1 + min(min_depth(root.left), min_depth(root.right))`

Time Complexity:
- O(n) visiting each node once.

Space Complexity:
- O(h) auxiliary call stack space.
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


def max_depth(root: Optional[TreeNode]) -> int:
    """Returns the maximum depth (height in node count) of a binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root: Optional[TreeNode]) -> int:
    """Returns the minimum depth to a leaf node in a binary tree."""
    if not root:
        return 0

    # If left child is None, must explore right child
    if not root.left:
        return 1 + min_depth(root.right)
    # If right child is None, must explore left child
    if not root.right:
        return 1 + min_depth(root.left)

    return 1 + min(min_depth(root.left), min_depth(root.right))


if __name__ == "__main__":
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert max_depth(root) == 3
    assert min_depth(root) == 2  # leaf 9 is at depth 2

    # Skewed tree: 1 -> 2 -> 3
    skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert max_depth(skewed) == 3
    assert min_depth(skewed) == 3  # not 1, because node 1 is not a leaf!

    assert max_depth(None) == 0
    assert min_depth(None) == 0

    print("All Height and Depth tests passed successfully.")
