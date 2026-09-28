# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ================
        # ripetizione #1
        # ================

        global_counter = [0]

        def dfs(node: Optional[TreeNode]):
            
            # Usando None come valore di fallimento è necessario il controllo esplicito "is not None" per evitare
            # che la condizione sia vero per node.val = 0 come risultato richiesto
            if not node: return None 
            
            # Prima vai tutto a sinistra dove ci sono i più piccoli in assoluto 
            found_left = dfs(node.left)
            if found_left is not None: return found_left

            # Aumenti il contatore solo dopo essere andato a sinistra 
            global_counter[0] += 1

            # Fai il controllo dopo l'aggiornamento per l'1-indexing, così il primo controllo lo fa il nodo più a sx e idx 1
            if global_counter[0] == k: return node.val

            # Se il controllo non ha avuto successo puoi provare a destra
            found_right = dfs(node.right)            
            if found_right is not None: return found_right

        return dfs(root)
