# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # upper e lower sono gli estremi superiore e inferiore che un nodo non può sforare -> servono per garantire per esempio che un nodo root->right->left non sia minore della root
        def isValidBSTAux(node, upper, lower) -> bool: 
            if not node: return True
            cond = lower < node.val < upper
            return  cond & isValidBSTAux(node.left, node.val, lower) & isValidBSTAux(node.right, upper, node.val)

        return isValidBSTAux(root, float('inf'), -float('inf'))




