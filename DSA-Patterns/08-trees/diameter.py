"""
Diameter of Binary Tree

What it is:
The length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
(The length is measured in number of edges, which equals number of nodes on path - 1).

When it is used:
- LeetCode 543 (Diameter of Binary Tree).
- Tree DP / longest path problems in graphs and trees.

The Key Idea:
Postorder Tree DP:
For any node, the longest path passing THROUGH that node equals:
`left_height + right_height` (measuring edges).
At each node:
1. Recursively calculate `left_height` and `right_height`.
2. Update global `max_diameter = max(max_diameter, left_height + right_height)`.
3. Return `1 + max(left_height, right_height)` to the parent so the parent can extend the path.

Time Complexity:
- O(n) single postorder traversal.

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


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """Returns the length of the diameter (number of edges on longest path).

    Time: O(n), Space: O(h).
    """
    max_diameter = 0

    def get_height(node: Optional[TreeNode]) -> int:
        nonlocal max_diameter
        if not node:
            return 0

        left_height = get_height(node.left)
        right_height = get_height(node.right)

        # Diameter through this node is sum of left and right heights
        max_diameter = max(max_diameter, left_height + right_height)

        # Return height of this subtree to parent
        return 1 + max(left_height, right_height)

    get_height(root)
    return max_diameter


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # Longest path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3 (length 3 edges)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert diameter_of_binary_tree(root) == 3

    # Two-node tree: 1 -> 2 (length 1 edge)
    assert diameter_of_binary_tree(TreeNode(1, TreeNode(2))) == 1

    # Empty tree
    assert diameter_of_binary_tree(None) == 0

    print("All Diameter of Binary Tree tests passed successfully.")
