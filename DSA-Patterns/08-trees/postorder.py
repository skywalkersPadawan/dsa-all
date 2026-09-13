"""
Binary Tree Postorder Traversal

What it is:
A depth-first traversal where each node is visited AFTER both of its subtrees:
Left -> Right -> Root.

When it is used:
- Bottom-up Tree Dynamic Programming: evaluating expressions, computing subtree sizes/heights,
  deleting trees from leaves up (e.g. garbage collection).
- Binary Tree Maximum Path Sum (LeetCode 124).
- Diameter of Binary Tree (LeetCode 543).
- Lowest Common Ancestor (LeetCode 236).

The Key Idea:
- Recursive: `postorder(node.left)`, `postorder(node.right)`, visit `node.val`.
- Iterative:
  A clean, standard trick is to perform a modified preorder (Root -> Right -> Left),
  and then reverse the resulting list to obtain (Left -> Right -> Root).

Time Complexity:
- O(n) visiting all n nodes.

Space Complexity:
- O(h) auxiliary space.
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


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Iterative postorder traversal (Left -> Right -> Root).

    Uses the Root -> Right -> Left preorder reversal technique.
    """
    if not root:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    # Traverses: Root -> Right -> Left
    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push left first so right is popped first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Reversing [Root, Right, Left] yields [Left, Right, Root]
    return result[::-1]


if __name__ == "__main__":
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    assert postorder_traversal(root) == [3, 2, 1]
    assert postorder_traversal(None) == []

    print("All Postorder tests passed successfully.")
