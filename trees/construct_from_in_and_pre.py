from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, pre_idx, preorder, inorder, in_start, in_end, mp):
        if pre_idx == len(preorder) or in_start > in_end:
            return None
        
        root = TreeNode(preorder[pre_idx[0]])
        pos = mp[preorder[pre_idx[0]]]
        pre_idx[0] += 1
        
        root.left = self.helper(pre_idx, preorder, inorder, in_start, pos-1, mp)
        root.right = self.helper(pre_idx, preorder, inorder, pos+1, in_end, mp)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        pre_idx = [0]
        return self.helper(pre_idx, preorder, inorder, 0, len(inorder)-1, mp)
