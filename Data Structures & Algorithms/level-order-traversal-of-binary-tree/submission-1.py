# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []
        deq = deque([root]) # Coda che contiene solo i nodi
        
        while deq:
            level_len = len(deq)
            level_vals = []
            
            # Svuoto ESATTAMENTE i nodi del livello corrente
            for _ in range(level_len):
                node = deq.popleft()
                level_vals.append(node.val)
                
                if node.left: deq.append(node.left)
                if node.right: deq.append(node.right)
                
            res.append(level_vals)
            
        return res