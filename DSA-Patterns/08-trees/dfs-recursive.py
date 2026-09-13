"""
Depth-First Search (DFS) - Recursive on Binary Trees

What it is:
A traversal technique that explores as deep as possible along each branch before backtracking.
On binary trees, DFS encompasses three primary traversal orders:
1. Preorder: Root -> Left -> Right
2. Inorder: Left -> Root -> Right
3. Postorder: Left -> Right -> Root

When it is used:
- Path finding, tree cloning, height/depth computation, subtree validations.
- Preorder: serialization, creating copies of trees.
- Inorder: retrieving sorted values from a Binary Search Tree (BST).
- Postorder: bottom-up tree DP (diameter, max path sum, subtree deletion).

The Key Idea:
Trust the recursive sub-call.
Base Case: `if not root: return`
Process `root.val`, recurse `dfs(root.left)`, recurse `dfs(root.right)` in the desired order.

Time Complexity:
- O(n) where n is the number of nodes in the tree (visits every node once).

Space Complexity:
- O(h) auxiliary space on call stack where h is tree height.
  - Balanced tree: O(log n).
  - Skewed tree: O(n).
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
    """Root -> Left -> Right."""
    result: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        result.append(node.val)  # Visit Root
        dfs(node.left)  # Visit Left
        dfs(node.right)  # Visit Right

    dfs(root)
    return result


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Left -> Root -> Right."""
    result: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)  # Visit Left
        result.append(node.val)  # Visit Root
        dfs(node.right)  # Visit Right

    dfs(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Left -> Right -> Root."""
    result: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)  # Visit Left
        dfs(node.right)  # Visit Right
        result.append(node.val)  # Visit Root

    dfs(root)
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

    assert preorder_traversal(root) == [1, 2, 4, 5, 3]
    assert inorder_traversal(root) == [4, 2, 5, 1, 3]
    assert postorder_traversal(root) == [4, 5, 2, 3, 1]

    print("All DFS Recursive tests passed successfully.")
