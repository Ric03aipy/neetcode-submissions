# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node: return 0, 0
            left_h, left_d = dfs(node.left)
            right_h, right_d = dfs(node.right)
            curr_h = 1 + max(left_h, right_h) 
            curr_d = left_h + right_h 
            return (curr_h, max(curr_d, left_d, right_d))
            
        _, d = dfs(root)
        return d