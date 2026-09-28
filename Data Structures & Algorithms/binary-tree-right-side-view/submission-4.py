# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ==================
        # ripetizione #1 bfs
        # ==================

        if not root: return []

        from collections import deque

        q = deque([root])
        res = []
        while q: 
            # Svuoto la coda a ogni livello, così che a ogni turno la coda contine un intero livello
            layer_len = len(q)
            res.append(q[-1].val)
            # Estraggo quelli del layer precedente e preparo il layer successivo con i loro figli
            for i in range(layer_len): 
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            

            # print([n.val for n in q])

        return res
            
            
                

            


