# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # ===============
        # ripetizione #1
        # ===============
        
        max_path_sum = float('-inf')
        def dfs(node): 
             
            if not node: return 0

            # Se un sottoramo è negativo non mi deve ridurre la somma corrente
            left_path_sum = max(dfs(node.left), 0)
            right_path_sum = max(dfs(node.right), 0)

            # 2 scenari: il path si ferma qui o va propagato
            # Se si ferma qui devo considerare come totale = radice + sx + dx | Qui è dove faccio il controllo
            # Se va propagato devo *restituire* radice + massimo

            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, node.val + left_path_sum + right_path_sum)

            return node.val + max(left_path_sum, right_path_sum)

        dfs(root)
        return max_path_sum



