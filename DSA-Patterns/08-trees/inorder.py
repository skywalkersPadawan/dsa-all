"""
Binary Tree Inorder Traversal

What it is:
A depth-first traversal where each node is visited between its left and right subtrees:
Left -> Root -> Right.

When it is used:
- In a Binary Search Tree (BST), inorder traversal yields all values in STRICTLY ASCENDING ORDER!
- Validating a Binary Search Tree (LeetCode 98).
- Finding the k-th smallest element in a BST (LeetCode 230).
- LeetCode 94 (Binary Tree Inorder Traversal).

The Key Idea:
- Recursive: Recurse `inorder(node.left)`, visit `node.val`, recurse `inorder(node.right)`.
- Iterative: Push all left children onto stack until hitting None. Pop node, record value,
  then move pointer to `node.right`.

Time Complexity:
- O(n) visiting every node.

Space Complexity:
- O(h) auxiliary call stack/explicit stack space.
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


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Iterative inorder traversal (Left -> Root -> Right)."""
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def kth_smallest_in_bst(root: Optional[TreeNode], k: int) -> int:
    """Finds the k-th smallest element (1-indexed) in a BST using early-stop inorder traversal.

    (LeetCode 230)
    """
    stack: list[TreeNode] = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val

        current = current.right

    return -1


if __name__ == "__main__":
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    assert inorder_traversal(root) == [1, 2, 3, 4, 5]
    assert kth_smallest_in_bst(root, 1) == 1
    assert kth_smallest_in_bst(root, 3) == 3
    assert kth_smallest_in_bst(root, 5) == 5

    print("All Inorder tests passed successfully.")
