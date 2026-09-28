# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # l'idea è prendere l'esercizio di prima e prendere sempre il più a destra: per costruzione inserisco sempre 
        # il nodo di destra dopo, quindi per ogni livello il primo non nullo partendo da destra è il primo visto

        from collections import deque
        if not root: return []
        from collections import deque
        lv_order = []
        # res = []
        deq = deque()
        # initialize the queue
        deq.append((root, 0)) # node, index/level
        # other levels
        while deq: 
            node, idx = deq.popleft()
            if node.left: deq.append((node.left, idx + 1))
            if node.right: deq.append((node.right, idx + 1))
            if idx == len(lv_order): 
                lv_order.append([])
            lv_order[idx].append(node.val)
        # print(lv_order)
        
        return [el[-1] for el in lv_order]