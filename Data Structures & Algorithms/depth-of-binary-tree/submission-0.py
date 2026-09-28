# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Soluzione con DFS ricorsiva

    def maxDepthAux(self, root, curr_depth) -> int:
        if not root: return curr_depth  
        return max(
                self.maxDepthAux(root.left, curr_depth + 1), 
                self.maxDepthAux(root.right, curr_depth + 1)
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.maxDepthAux(root, 0)    # non 1 qui, perché il root non è stato processato; 
                                            # per essere 1 dovrebbe essere max(aux(left, 1), aux(right, 1))