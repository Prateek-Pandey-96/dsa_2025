from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode], mn: int, mx: int) -> bool:
        if root is None:
            return True
        if root.val > mn and root.val < mx:
            return True
        if self.helper(root.left, mn, root.val) and self.helper(root.right, root.val, mx):
            return True
        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -1001, 1001)
