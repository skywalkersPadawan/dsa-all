# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(rootOne, rootTwo):
            if not rootOne and not rootTwo:
                return True
            if not rootOne and rootTwo:
                return False
            if rootOne and not rootTwo:
                return False
            if rootOne.val != rootTwo.val:
                return False
            return solve(rootOne.left, rootTwo.left) and solve(
                rootOne.right, rootTwo.right
            )

        return solve(p, q)
