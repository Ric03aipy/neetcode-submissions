"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # =============
        # ripetizione #1
        # =============

        if not node: return None

        clones = {}

        def dfs(curr) -> Optional['Node']: 
            
            if curr in clones: return clones[curr]

            clones[curr] = Node(val=curr.val)
            for neig in curr.neighbors: 
                clones[curr].neighbors.append(dfs(neig))

            return clones[curr]

        return dfs(node)