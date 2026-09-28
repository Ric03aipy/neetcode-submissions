"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Edge case
        if not node: return node

        # Dai CONSTRAINT: There are no duplicate edges and no self-loops in the graph.

        old_to_new_map = {} # {nodo esistente: nodo copia}, destinata a essere O(2V)=O(V) in spazio

        # Faccio una dfs per popolare old_to_new_map
        visited = set() # O(V) in spazio
        def dfs(node): 
            if node in visited: return
            visited.add(node)
            old_to_new_map[node] = Node(val = node.val)
            for neighbor in node.neighbors: dfs(neighbor)
        
        dfs(node)

        # Ora che ho i corrispettivi devo solo creare la struttura. Questo ciclo domina il tempo O(V + E) 
        for old_node in old_to_new_map: 
            for old_neighbour in old_node.neighbors: 
                old_to_new_map[old_node].neighbors.append(old_to_new_map[old_neighbour])

        return old_to_new_map[node]
            
