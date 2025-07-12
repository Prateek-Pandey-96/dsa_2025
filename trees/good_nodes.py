from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, -101))

        count = 0

        while queue:
            size = len(queue)

            while size > 0:
                curr, mx_till_now = queue.popleft()
                if curr.val >= mx_till_now:
                    count += 1
                mx_till_now = max(mx_till_now, curr.val)
                
                if curr.left:
                    queue.append((curr.left, mx_till_now))
                if curr.right:
                    queue.append((curr.right, mx_till_now))

                size -= 1

        return count
