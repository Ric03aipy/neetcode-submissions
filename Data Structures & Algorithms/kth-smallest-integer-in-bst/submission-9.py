# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # ===============
        # ripetizione #1 - con stack iterativo (prima volta per questo esercizio)
        # ===============

        stack = []
        curr = root
        seen = 0
        while stack or curr:
            while curr: 
                stack.append(curr)
                curr = curr.left
            # Qui curr is None 
            curr = stack.pop()
            seen += 1
            if seen == k: return curr.val
            curr = curr.right

        return -1 # Non arriva mai qui per i vincoli del problema




