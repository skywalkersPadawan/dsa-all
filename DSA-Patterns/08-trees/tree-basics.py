"""
Binary Tree Basics

What it is:
A hierarchical, non-linear data structure where each node has at most two children,
referred to as the `left` child and the `right` child.

When it is used:
- Hierarchical data representation (file systems, DOM trees, organizational charts).
- Efficient search, insertion, and deletion (Binary Search Trees).
- Heap priority queues.
- Syntax trees in compilers.

The Key Idea:
A standard TreeNode definition in Python:
```python
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Core Properties:
- Root: The topmost node with no parent.
- Leaf: A node with no children (`node.left is None and node.right is None`).
- Height: The length of the longest downward path from the node to a leaf.
- Depth: The distance from the root to the node.

Time Complexity:
- Traversal: O(n) visiting all n nodes.
- Search/Insert/Delete in balanced BST: O(log n).
- Degenerate tree (skewed, like a linked list): O(n).

Space Complexity:
- O(h) auxiliary call stack space where h is tree height (log n for balanced, n for skewed).
"""

from typing import Optional


class TreeNode:
    """Standard Binary Tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: Optional[TreeNode]) -> int:
    """Counts total number of nodes in binary tree. O(n) time, O(h) space."""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaf_nodes(root: Optional[TreeNode]) -> int:
    """Counts number of leaf nodes in binary tree."""
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


if __name__ == "__main__":
    # Construct tree:
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

    assert count_nodes(root) == 5
    assert count_leaf_nodes(root) == 3  # nodes 4, 5, 3
    assert count_nodes(None) == 0

    print("All Binary Tree Basics tests passed successfully.")
