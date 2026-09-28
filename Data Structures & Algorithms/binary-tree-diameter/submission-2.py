# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # Questa è la lavagna globale che conterrà il record del diametro
        
        def dfs(node):
            if not node:
                return 0 # L'altezza di un nodo inesistente è 0
                
            # 1. Chiedo le altezze ai miei figli (BOTTOM-UP)
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # 2. CALCOLO GLOBALE: Il diametro che passa per QUESTO nodo.
            # E se è maggiore del record attuale, aggiorno la lavagna!
            self.res = max(self.res, left_height + right_height)
            
            # 3. RISPOSTA AL GENITORE: Ritorno la MIA altezza per i calcoli di chi sta sopra
            return 1 + max(left_height, right_height)
            
        dfs(root)
        
        return self.res




