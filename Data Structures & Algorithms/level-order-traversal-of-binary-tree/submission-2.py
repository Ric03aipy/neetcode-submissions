# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # =================
        # ripetizione #1
        # =================

        from collections import deque

        if not root: return []

        que = deque([root])
        res = []

        while que: 
            # Conto quanti nodi ci sono ora nella coda: sono quelli di questo livello grazie a quanto segue
            layer_len = len(que)
            layer = []

            # Svuoto la coda dei nodi correnti e la popolo con i figli di ciascun nodo (livello + 1)
            for _ in range(layer_len):
                node = que.popleft()
                layer.append(node.val)
                if node.left: 
                    que.append(node.left)
                if node.right: 
                    que.append(node.right)

            res.append(layer)
        
        return res
            
            
