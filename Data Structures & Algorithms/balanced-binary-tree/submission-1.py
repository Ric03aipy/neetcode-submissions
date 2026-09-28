# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # -> [is_balanced, height]
        def dfs(root) -> tuple[bool, int]:
            if not root: return (True, 0)
            is_balanced_left, height_left = dfs(root.left)
            is_balanced_right, height_right = dfs(root.right)
            is_balanced = (abs(height_left - height_right) <= 1) and is_balanced_left and is_balanced_right
            curr_height =  1 + max(height_left, height_right)
            return (is_balanced, curr_height)

        return dfs(root)[0]

