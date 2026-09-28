# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_index_map = {val:idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def buildTreeAux(left:int, right:int) -> Optional[TreeNode]:
            """
            left, right: puntatori in stile binary search;
            left: inizio della parte sinistra o inizio della parte destra a seconda del sottoalbero
            right: fine della parte destra o inizio della parte sinistra a seconda del sottoalbero
            """            
            # Condizione di uscita: se non ci sono elementi smette di avere senso logico
            if left > right: return None
        
            nonlocal preorder_idx
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root_idx = inorder_index_map[root_val]  # "mid" di una binary search

            return TreeNode(
                root_val,
                buildTreeAux(left, root_idx - 1),
                buildTreeAux(root_idx + 1, right)
            )

        return buildTreeAux(0, len(preorder) - 1)
        
        