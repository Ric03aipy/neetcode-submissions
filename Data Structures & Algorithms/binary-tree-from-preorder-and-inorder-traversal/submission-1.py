# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Mappa degli indici "globale" per efficienza nella ricerca degli elementi 
        inorder_map = {val:idx for idx, val in enumerate(inorder)}

        # Indice globale - uso una lista per evitare di creare un attributo di istanza self.pre_idx
        preord_index = [0] 

        # Funzione ausiliaria - divide et impera
        def aux(left:int, right:int) -> Optional[TreeNode]:
            
            # Se left > right smette di avere senso la suddivisione - "qualcosa di più piccolo" > "qualcosa di più grande" 
            if left > right: return None
            
            # La radice è sempre il primo nodo della lista in preordine (radice -> sottoalbero sx -> sottoalbero dx)
            root_val = preorder[preord_index[0]]
            root = TreeNode(root_val)
            preord_index[0] += 1

            # L'informazione su come "dividere" le due liste
            # N.B: per efficienza non divido fisicamente le liste - lo splicing costa O(n) in memoria - , ma passo puntatori
            mid = inorder_map[root_val]

            # Ricorsione + Divide (chimata ricorsiva) and Conquer (assegnazione dei nodi alla radice)
            root.left = aux(left, mid - 1) 
            root.right = aux(mid + 1, right)

            return root

        return aux(0, len(preorder) - 1)



