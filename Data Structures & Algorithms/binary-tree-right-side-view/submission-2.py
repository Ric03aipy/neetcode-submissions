# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ===============
        # ripetizione #1
        # ===============
        
        res = []


        def dfs(node: Optional[TreeNode], depth:int):
            # ritorna l'altezza
            if not node: return 0

            # idea: aggiungo il primo di una certa profondità
            if depth == len(res): res.append(node.val)

            # chiamo prima a destra per garantire che siano sempre i nodi destri a essere visti 
            if node.right: dfs(node.right, depth + 1)
            if node.left: dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res