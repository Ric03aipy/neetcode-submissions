# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ==================
        # ripetizione #2 bfs
        # ==================

        if not root: return []

        from collections import deque

        res = []
        q = deque()
        q.append(root)

        while q: 
            lv_len = len(q)
            for i in range(lv_len):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            # sfrutto la caratteristica di python per lo scope
            res.append(node.val)
        
        return res
                

            


