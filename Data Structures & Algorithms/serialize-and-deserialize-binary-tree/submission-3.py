# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Tolgo subito di mezzo il caso base
        if not root: return ""

        code = []

        # Visita in pre-ordine
        def dfs(node): 
            if not node: 
                code.append("/")
                return 
            code.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(code)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Se entra ""
        if not data: return None

        data = data.split(",")
        print(data)
            
        # Indice globale 
        idx = 0

        # Provo a costruire al contrario
        def dfs() -> Optional[TreeNode]:
            nonlocal idx
            val = data[idx]
            if val == "/": return None
            node = TreeNode(val)
            idx += 1
            node.left = dfs()
            idx += 1
            node.right = dfs()
            return node            


        return dfs()

