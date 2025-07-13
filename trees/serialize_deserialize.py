from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def formTree(self, q) -> Optional[TreeNode]:
        front = q.popleft()
        if front == 'null':
            return None
        left = self.formTree(q)
        right = self.formTree(q)
        root = TreeNode(int(front))
        root.left = left
        root.right = right

        return root
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "null"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + '*' + left + '*' + right
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue = deque()
        curr = []
        for ch in data:
            if ch == '*':
                queue.append(''.join(curr))
                curr = []
                continue
            curr.append(ch)
        queue.append(''.join(curr))
        return self.formTree(queue)

 
