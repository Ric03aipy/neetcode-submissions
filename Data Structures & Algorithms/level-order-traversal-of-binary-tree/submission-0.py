# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        from collections import deque
        res = []
        deq = deque()
        # initialize the queue
        deq.append((root, 0)) # node, index/level
        # other levels
        while deq: 
            node, idx = deq.popleft()
            if node.left: deq.append((node.left, idx + 1))
            if node.right: deq.append((node.right, idx + 1))
            if idx == len(res): 
                res.append([])
            res[idx].append(node.val)
        return res
