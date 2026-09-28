# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def aux(node: Optional[TreeNode], th:int, flat:list) -> None:
            if not node or len(flat) == th: return # mi fermo a k inserimenti
            # visita simmetrica 
            aux(node.left, th, flat)
            # qui devo fare un controllo: il ramo sinistro potrebbe saturare i k spazi
            if len(flat) == th: return 
            flat.append(node.val)
            aux(node.right, th, flat)

        flat = [] 
        aux(root, k, flat) # flat è una lista, viene passata per puntatore, quindi viene modificata
        return flat[-1]

            

