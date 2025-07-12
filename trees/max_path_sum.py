from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, helper) -> int:
        if root is None:
            return 0
        
        left = self.dfs(root.left, helper)
        right = self.dfs(root.right, helper)

        temp = max(max(left, right) + root.val, root.val)
        helper[0] = max(helper[0], left + right + root.val, temp)

        return temp

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        helper = [root.val]
        self.dfs(root, helper)
        return helper[0]
