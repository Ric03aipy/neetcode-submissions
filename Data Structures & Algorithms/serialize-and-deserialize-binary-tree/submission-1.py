# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # la mia idea è quella di segnare una stringa che possa essere splittata per diventare un array ed essere 
        # comodamente letta

        # per esempio [1,2,3,null,null,4,5]
        # in "1,2,/,/,3,4,/,/,5" leggibile in fase di deserializzazione per ottenere il preorder
        # 1 è la radice
        # poi sempre a sinistra finché non incontri "/", poi se ha un figlio a destra ripeti, altrimenti è una foglia
        # allora devi riprendere l'ultimo nodo non esplorato -> usare una stack? 

        serialized = []
        
        # ausiliaria per costruizione stringa in pre-ordine
        def dfs_fill(root): 
            if not root: 
                serialized.append("/") 
                return 
            # serialized.append(str(root.val))
            # dfs_fill(root.left)
            # dfs_fill(root.right)
            
            # se volessi la rappresentazione al contrario per non togliere da sinistra ma togliere da destra (pop su lista invece che su deque)

            dfs_fill(root.right)
            dfs_fill(root.left)

            serialized.append(str(root.val))
            
        
        dfs_fill(root)

        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # from collections import deque
        
        # deq = deque(data.split(","))    # mutabile
        # print(deq)
        queue = data.split(",")

        def des_aux(): 
            val = queue.pop()
            # print(f"estratto valore = {val}")
            if val == "/": return None
            node = TreeNode(val)
            node.left = des_aux()
            node.right = des_aux()
            return node

        return des_aux()












