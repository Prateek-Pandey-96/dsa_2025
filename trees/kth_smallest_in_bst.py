from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root, inorder):
        if root is None:
            return
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.traverse(root, inorder)

        return inorder[k-1]



