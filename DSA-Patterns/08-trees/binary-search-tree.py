"""
Binary Search Tree (BST) Operations

What it is:
A binary tree where for every node:
- All values in the LEFT subtree are strictly LESS than the node's value.
- All values in the RIGHT subtree are strictly GREATER than the node's value.

When it is used:
- O(log n) dynamic search, insertion, and deletion.
- Inorder traversal yields elements in sorted order.
- Validating BST (LeetCode 98).
- BST operations (LeetCode 700 - Search, LeetCode 701 - Insert, LeetCode 450 - Delete).

The Key Idea:
- Search: if target < node.val, go left; if target > node.val, go right; else found!
- Insert: walk down until hitting None, then attach new node.
- Delete:
  - Node has 0 children: return None.
  - Node has 1 child: return the non-null child.
  - Node has 2 children: replace node's value with its in-order successor
    (minimum value in the right subtree), then delete the successor from right subtree.
- Validation: DFS with lower and upper bound constraints: `low < node.val < high`.

Time Complexity:
- Search/Insert/Delete: O(h) where h is tree height (O(log n) balanced, O(n) worst-case).

Space Complexity:
- O(h) recursion stack space.
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


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Searches for val in BST in O(h) time."""
    current = root
    while current:
        if current.val == val:
            return current
        elif val < current.val:
            current = current.left
        else:
            current = current.right
    return None


def insert_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """Inserts val into BST and returns root."""
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)

    return root


def delete_bst(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Deletes key from BST and returns modified root (LeetCode 450)."""
    if not root:
        return None

    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Node has 2 children -> find in-order successor (min in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left

        root.val = successor.val
        # Delete successor from right subtree
        root.right = delete_bst(root.right, successor.val)

    return root


def is_valid_bst(
    root: Optional[TreeNode],
    low: float = float("-inf"),
    high: float = float("inf"),
) -> bool:
    """Validates if a binary tree satisfies BST invariants (LeetCode 98)."""
    if not root:
        return True

    if not (low < root.val < high):
        return False

    return is_valid_bst(root.left, low, root.val) and is_valid_bst(
        root.right, root.val, high
    )


if __name__ == "__main__":
    # Build BST:
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3
    root = TreeNode(4)
    for v in [2, 7, 1, 3]:
        insert_bst(root, v)

    assert is_valid_bst(root) is True

    # Search
    assert search_bst(root, 2) is not None
    assert search_bst(root, 99) is None

    # Delete leaf
    delete_bst(root, 1)
    assert search_bst(root, 1) is None
    assert is_valid_bst(root) is True

    # Delete node with two children (4)
    root = delete_bst(root, 4)
    assert search_bst(root, 4) is None
    assert is_valid_bst(root) is True

    # Invalid BST test
    #     5
    #    / \
    #   1   4 (invalid right child: 4 < 5)
    bad_root = TreeNode(5, TreeNode(1), TreeNode(4))
    assert is_valid_bst(bad_root) is False

    print("All Binary Search Tree tests passed successfully.")
