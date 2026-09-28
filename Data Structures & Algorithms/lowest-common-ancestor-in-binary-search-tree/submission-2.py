# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # ====================
        # ripetizione #1 (senza "root.val in interavllo")
        # ====================

        if not root: return None

        if p.val < root.val and q.val < root.val: return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val: return self.lowestCommonAncestor(root.right, p, q)

        # se arriva qui ci sono 2 ipotesi: 
        # - uno è maggiore e l'altro minore, allora il nodo corrente è il LCA
        # - uno è esattamente questo nodo, l'altro è un figlio (non potrebbe essere un padre per il ripetersi 
        # del dilemma ai nodi precedenti), quindi il nodo corrente è il LCA & è anche uno tra p e q
        return root