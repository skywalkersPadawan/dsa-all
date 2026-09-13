"""
Lowest Common Ancestor (LCA)

What it is:
The Lowest Common Ancestor between two nodes p and q in a tree T is the lowest (deepest)
node in T that has both p and q as descendants (where a node can be a descendant of itself).

When it is used:
- LCA in a General Binary Tree (LeetCode 236).
- LCA in a Binary Search Tree (LeetCode 235).
- Distance between two tree nodes: dist(p, q) = depth(p) + depth(q) - 2 * depth(LCA).

The Key Idea:
- General Binary Tree (Postorder DFS):
  Base Case: If `root is None` or `root == p` or `root == q`, return `root`.
  Recurse:
  `left = lowest_common_ancestor(root.left, p, q)`
  `right = lowest_common_ancestor(root.right, p, q)`
  Decision:
  - If both `left` and `right` are non-null: `root` is the split point -> return `root`!
  - Otherwise, return whichever child returned a non-null node.

- Binary Search Tree (BST) Optimization:
  Leverage ordering:
  - If both p.val and q.val < root.val: LCA must be in left subtree.
  - If both p.val and q.val > root.val: LCA must be in right subtree.
  - Otherwise: `root` is the split point (LCA)! O(h) time, O(1) space iterative.

Time Complexity:
- Binary Tree: O(n)
- BST: O(h) where h is tree height

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


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Finds LCA in a general binary tree (LeetCode 236)."""
    # Base cases: if root is None or matches p or q
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both left and right return a node, p and q are on different branches -> root is LCA
    if left and right:
        return root

    # Otherwise return the non-null result
    return left if left else right


def lowest_common_ancestor_bst(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Finds LCA in a Binary Search Tree in O(h) time and O(1) space (LeetCode 235)."""
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            # We found the split point
            return current

    return None


if __name__ == "__main__":
    # General Binary Tree:
    #         3
    #        / \
    #       5   1
    #      / \
    #     6   2
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n5 = TreeNode(5, n6, n2)
    n1 = TreeNode(1)
    root = TreeNode(3, n5, n1)

    # LCA of 5 and 1 is 3
    assert lowest_common_ancestor(root, n5, n1) == root
    # LCA of 6 and 2 is 5
    assert lowest_common_ancestor(root, n6, n2) == n5
    # LCA of 5 and 6 is 5
    assert lowest_common_ancestor(root, n5, n6) == n5

    # BST:
    #        6
    #       / \
    #      2   8
    bst_root = TreeNode(6, TreeNode(2), TreeNode(8))
    p_node = bst_root.left  # 2
    q_node = bst_root.right  # 8
    assert lowest_common_ancestor_bst(bst_root, p_node, q_node) == bst_root

    print("All Lowest Common Ancestor tests passed successfully.")
