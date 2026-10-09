# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ================
        # ripetizione #3
        # ================

        max_h = [0]

        # h_left + h_right + 1 se mi fermo altrimenti propago l'altezza 

        def dfs(node) -> int: 

            if not node: return 0

            h_left = dfs(node.left)
            h_right = dfs(node.right)
            
            path_h = h_left + h_right 

            max_h[0] = max(max_h[0], path_h)
            return max(h_left, h_right) + 1

        dfs(root)
        return max_h[0]