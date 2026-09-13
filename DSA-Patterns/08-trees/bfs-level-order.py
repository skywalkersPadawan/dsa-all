"""
Breadth-First Search (BFS) / Level-Order Traversal on Binary Trees

What it is:
Visits nodes of a binary tree level by level from top to bottom, and left to right within each level.

When it is used:
- Binary Tree Level Order Traversal (LeetCode 102).
- Binary Tree Right/Left Side View (LeetCode 199).
- Shortest path / minimum depth in unweighted trees (LeetCode 111).
- Populating next right pointers (LeetCode 116).

The Key Idea:
Use a FIFO Queue (`collections.deque`):
1. Push `root` to queue.
2. While queue is not empty:
   - Determine `level_size = len(queue)` (number of nodes in current level).
   - Loop `level_size` times:
     - Pop `node = queue.popleft()`.
     - Append `node.val` to `current_level` list.
     - Enqueue `node.left` and `node.right` if they exist.
   - Append `current_level` to `result`.

Time Complexity:
- O(n) visiting all n nodes.

Space Complexity:
- O(w) auxiliary space where w is the maximum width of the tree.
  For a full binary tree, the last level contains n/2 nodes -> O(n) space.
"""

from collections import deque
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


def level_order_traversal(root: Optional[TreeNode]) -> list[list[int]]:
    """Returns level-by-level list of node values using a queue."""
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        current_level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    """Returns the values of the nodes visible from the right side.

    (LeetCode 199)
    """
    if not root:
        return []

    right_view: list[int] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # If it's the last element of this level, it's visible from the right
            if i == level_size - 1:
                right_view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_view


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

    assert level_order_traversal(root) == [[3], [9, 20], [15, 7]]
    assert right_side_view(root) == [3, 20, 7]
    assert level_order_traversal(None) == []

    print("All BFS Level Order tests passed successfully.")
