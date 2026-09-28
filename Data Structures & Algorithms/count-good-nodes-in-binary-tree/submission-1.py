# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodesAux(root, curr_max) -> int:
            if not root: return 0
            add = 1 if curr_max <= root.val else 0 
            nxt_max = max(curr_max, root.val)
            return add + goodNodesAux(root.left, nxt_max) + goodNodesAux(root.right, nxt_max)

        return goodNodesAux(root, root.val)

