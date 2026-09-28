# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBSTAux(node, upper, lower) -> bool: 
            if not node: return True
            cond = lower < node.val < upper
            return  cond and isValidBSTAux(node.left, node.val, lower) and isValidBSTAux(node.right, upper, node.val)

        return isValidBSTAux(root, float('inf'), -float('inf'))




