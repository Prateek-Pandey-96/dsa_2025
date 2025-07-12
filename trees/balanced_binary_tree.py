from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        l = self.height(root.left)
        r = self.height(root.right)

        return abs(l-r)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
