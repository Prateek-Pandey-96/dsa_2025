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

        temp = max(left, right) + 1
        helper[0] = max(helper[0], left+right+1)
        return temp

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # helper for passing by reference
        helper = [0]
        self.dfs(root, helper)
        return helper[0]-1
        


