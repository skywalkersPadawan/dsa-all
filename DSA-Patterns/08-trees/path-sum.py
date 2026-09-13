"""
Path Sum Patterns on Binary Trees

What it is:
Techniques for validating and finding root-to-leaf paths and arbitrary paths
that sum to a given target.

Key Variations:
1. Path Sum I (LeetCode 112): Does ANY root-to-leaf path sum equal target?
2. Path Sum II (LeetCode 113): Return ALL root-to-leaf paths that sum to target.
3. Binary Tree Maximum Path Sum (LeetCode 124): Longest path between ANY two nodes.

The Key Idea:
- Root-to-Leaf (Path Sum I):
  At each node, subtract `node.val` from remaining target.
  If at a leaf node (`not node.left and not node.right`), check if `target_sum == 0`.
- Max Path Sum (Any-to-Any, LeetCode 124):
  Postorder traversal:
  Each node returns to parent: `node.val + max(0, max(left_gain, right_gain))`.
  Global maximum is updated with: `node.val + max(0, left_gain) + max(0, right_gain)`.

Time Complexity:
- O(n) visiting all nodes.

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


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """Returns True if there is a root-to-leaf path summing to target_sum.

    (LeetCode 112)
    """
    if not root:
        return False

    target_sum -= root.val

    # Check if this is a leaf node
    if not root.left and not root.right:
        return target_sum == 0

    return has_path_sum(root.left, target_sum) or has_path_sum(
        root.right, target_sum
    )


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Finds maximum path sum of any non-empty path between any two nodes.

    (LeetCode 124 - Hard)
    Time: O(n), Space: O(h).
    """
    global_max = float("-inf")

    def max_gain(node: Optional[TreeNode]) -> int:
        nonlocal global_max
        if not node:
            return 0

        # Max gain from left and right subtrees (ignore negatives by taking max with 0)
        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))

        # Price of the path where current node is the highest point (turning point)
        price_newpath = node.val + left_gain + right_gain
        global_max = max(global_max, price_newpath)

        # For recursion to parent, can only pick ONE branch (left or right)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return int(global_max)


if __name__ == "__main__":
    #       5
    #      / \
    #     4   8
    #    /
    #   11
    #  /  \
    # 7    2
    root = TreeNode(5)
    root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    root.right = TreeNode(8)

    # Path 5 -> 4 -> 11 -> 2 = 22
    assert has_path_sum(root, 22) is True
    # Path 5 -> 8 = 13
    assert has_path_sum(root, 13) is True
    # Non-existent sum
    assert has_path_sum(root, 100) is False

    # Max path sum test: [-10, 9, 20, null, null, 15, 7]
    # Path: 15 -> 20 -> 7 = 42
    tree_124 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(tree_124) == 42

    print("All Path Sum tests passed successfully.")
