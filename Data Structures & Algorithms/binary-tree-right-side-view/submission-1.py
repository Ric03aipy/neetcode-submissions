# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # APPROCCIO BFS OTTIMIZZATA

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        from collections import deque

        res = []
        deq = deque([root])

        while deq:
            deq_curr_len = len(deq)
            for _ in range(deq_curr_len):
                node = deq.popleft()
                if node.left: deq.append(node.left)
                if node.right: deq.append(node.right)
            # alla fine node sarà quello più a destra
            res.append(node.val)
        return res
