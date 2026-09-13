"""
Serialize and Deserialize Binary Tree

What it is:
Serialization is the process of converting a binary tree data structure into a string of values
so that it can be stored in a file or memory buffer, or transmitted across a network.
Deserialization is the reverse process, reconstructing the tree structure from the string.

When it is used:
- LeetCode 297 (Serialize and Deserialize Binary Tree - Hard).
- Tree persistence and RPC transmissions.

The Key Idea:
Preorder Traversal with Sentinel Null Markers:
1. Serialization:
   Perform DFS preorder traversal. If node is None, record a sentinel marker (e.g. `'#'`).
   Separate values with commas.
   Example: [1, 2, null, null, 3, 4, null, null, 5, null, null]
2. Deserialization:
   Split string by comma into a queue/iterator.
   Reconstruct recursively:
   - Pop next value.
   - If value is `'#'`, return None.
   - Otherwise, create `node = TreeNode(int(val))`, then:
     `node.left = deserialize_helper()`
     `node.right = deserialize_helper()`
   - Return `node`.

Time Complexity:
- O(n) for both serialize and deserialize.

Space Complexity:
- O(n) memory to store the string and recursion stack.
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


class Codec:
    """Encodes a tree to a single string and decodes a string back to a tree."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using preorder traversal."""
        values: list[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                values.append("#")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes string representation back to tree."""
        if not data:
            return None

        tokens = iter(data.split(","))

        def dfs() -> Optional[TreeNode]:
            val = next(tokens)
            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


if __name__ == "__main__":
    codec = Codec()

    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    original_root = TreeNode(1)
    original_root.left = TreeNode(2)
    original_root.right = TreeNode(3, TreeNode(4), TreeNode(5))

    serialized = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized)

    # Re-serializing the deserialized root should yield the exact same string
    assert codec.serialize(deserialized_root) == serialized

    # Empty tree check
    assert codec.deserialize(codec.serialize(None)) is None

    print("All Serialize and Deserialize tests passed successfully.")
