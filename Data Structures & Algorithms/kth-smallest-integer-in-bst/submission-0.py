# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def aux(root: Optional[TreeNode], k:int, flat:list) -> None: 
            if not root: return
            # visita simmetrica 
            aux(root.left, k, flat)
            flat.append(root.val)
            aux(root.right, k, flat)

        flat = [] 
        aux(root, k, flat) # flat è una lista, viene passata per puntatore, quindi viene modificata
        print(flat)
        return flat[k-1]

            

