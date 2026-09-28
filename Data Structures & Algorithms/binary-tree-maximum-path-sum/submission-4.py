# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # DOPPIA RESPONSABILITà - VEDI DIAMETER

        # questa è l'informazione gloabale - lista solo per non creare una variabile di istanza (SW Eng, Thread Safety)
        tot_sum = [-float('inf')]

        def local_sum(root: Optional[TreeNode]) -> int: 

            # passo base
            if not root: return 0

            # calcolo sui sottoalberi
            left_sub_sum = local_sum(root.left)
            if left_sub_sum < 0: left_sub_sum = 0
            right_sub_sum = local_sum(root.right)
            if right_sub_sum < 0: right_sub_sum = 0

            # aggiornamento dell'informazione globale: non so quali pezzi aumentano e quali abbassano
            tot_sum[0] = max(   
                                tot_sum[0], 
                                root.val + left_sub_sum + right_sub_sum
                            )

            # restituisco l'informazione **locale** : la massima **somma di percorso** da qui fino alle foglie
            return root.val + max(left_sub_sum, right_sub_sum)

        # side effect sulla variabile locale di questa funzione - contenente risultato globale
        local_sum(root)

        return tot_sum[0]