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

        counter = 0 # Numero di good nodes

        def dfs(x, max_val_so_far) -> None: 
            if x == None: return 
            if x.val >= max_val_so_far: 
                nonlocal counter
                counter += 1
            dfs(x.left, max(x.val, max_val_so_far))
            dfs(x.right, max(x.val, max_val_so_far))
            return 
        
        dfs(root, float("-inf"))
        return counter