# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ==============
        # ripetizione #2
        # ==============

        # Idea: diametro in un nodo = somma delle altezze (# link) dei rami destro e sinistro
        # Per avere il massimo diametro bisogna trovare il massimo tra tutti i diametri tra quello 
        # del nodo corrente e quello dei sottorami. Infatti diametro e altezza non coincidono, per questo non 
        # è detto che il massimo diametro contemli la radice

        max_diameter = [0]

        def dfs(node: Optional[TreeNode]) -> int:

            # Caso base: nodo nullo oppure foglia
            if not node: return 0

            # Calcolo del diametro corrente e aggiornamento del massimo
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            diameter = left_h + right_h
            max_diameter[0] = max(max_diameter[0], diameter)

            # Ritorno l'altezza massima
            return 1 + max(left_h, right_h)
        
        dfs(root)
        return max_diameter[0]
