# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # caso base: se non esiste la radice
        if not root: return None

        # scesi fino ad essere foglia
        if not root.left and not root.right: return TreeNode(root.val)

        # logica per nodi interni 

        inv_root = TreeNode(root.val)
        inv_root.left = self.invertTree(root.right)
        inv_root.right = self.invertTree(root.left)

        return inv_root 

        # Ho sempre creato nuovi nodi perché nella traccia lascia intendere che vuole un albero nuovo (come anche giusto
        # ingegneristicamente), piuttosto che fare side-effect

        