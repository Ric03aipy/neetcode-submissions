# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # =================
        # ripetizione #2
        # =================
        
        if not root: return []

        from collections import deque

        q = deque()
        q.append(root)

        res = []
        while q: 
            nodes_at_current_lv = len(q)
            new_lv = []
            for _ in range(nodes_at_current_lv): 
                node = q.popleft()
                new_lv.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(new_lv)
        return res
    