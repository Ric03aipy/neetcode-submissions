# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # =============
        # ripetizione #1
        # =============

        def dfs(node, upper, lower) -> bool:
            """
            Il nodo corrente deve essere sempre compreso tra upper e lower.
            """

            # Se non ci sono nodi la condizione è vera perché non ci sono nodi per violarla            
            if not node: return True

            # Condizione di validità per il nodo corrente
            curr_cond = lower < node.val < upper
            
            # Corto-Circuitando con l'AND sui sottorami: 
            # I nodi a sinistra non possono superare il nodo corrente, i nodi a destra non possono scendervi sotto
            return  curr_cond and \
                    dfs(node.left, node.val, lower) and \
                    dfs(node.right, upper, node.val)

        return dfs(root, float('inf'), -float("inf"))