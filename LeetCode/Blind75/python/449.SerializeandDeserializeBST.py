import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = collections.deque(map(int, data.split(",")))

        def build(lower, upper):
            if not vals or vals[0] < lower or vals[0] > upper:
                return None

            val = vals.popleft()
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)

            return node

        return build(float("-inf"), float("inf"))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
