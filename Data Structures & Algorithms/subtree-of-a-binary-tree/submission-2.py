# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False # sotto un AND, un OR diventa uno XOR
        is_same_left = self.isSameTree(p.left, q.left)
        is_same_right = self.isSameTree(p.right, q.right)
        return p.val == q.val and is_same_left and is_same_right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        is_sub = is_sub_left = is_sub_right = False
        
        # Logica eplicita
        # if root.val == subRoot.val: 
        #     is_sub = self.isSameTree(root, subRoot)
        # is_sub_left = self.isSubtree(root.left, subRoot)
        # is_sub_right = self.isSubtree(root.right, subRoot)
        # return any((is_sub, is_sub_left, is_sub_right))

        # Logica veloce
        if self.isSameTree(root, subRoot): # questo è l'equivalente del primo if
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)