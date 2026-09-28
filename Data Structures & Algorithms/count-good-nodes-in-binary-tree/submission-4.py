# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # ==============
        # ripetizione #1
        # ==============

        def dfs(x, max_val_so_far) -> int: 
            if x == None: return 0
            add = 0
            if x.val >= max_val_so_far: 
                add = 1
            return add + dfs(x.left, max(x.val, max_val_so_far)) + dfs(x.right, max(x.val, max_val_so_far))
        
        return dfs(root, float("-inf"))
