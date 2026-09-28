# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Soluzione con DFS iterativa (e stack come struttura dati di supporto)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack:tuple[TreeNode, int] = [(root, 1)]    # registro per ogni nodo la profondità a cui si trova
        max_depth = 1
        while stack: 
            node, d = stack.pop()
            if node.left: stack.append((node.left, d + 1))
            if node.right: stack.append((node.right, d + 1))
            max_depth = max(max_depth, d)
        return max_depth