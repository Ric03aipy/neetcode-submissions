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
