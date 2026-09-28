"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    """SI PUò FARE IN UNA SOLA PASSATA INVECE CHE DUE. LA FUZNIONE DFS DEVE RESTITUIRE IL CLONE E APPENDERE AL CLONE
    RISULTATI DI ALTRE CHIAMATE. POICHé TUTTE LE CHIAMATE DEVONO ARRIVARE IN FONDO PRIMA DI POTER APPENDERE, TUTTI GLI 
    APPEND POSSONO AVVENIRE CON SUCCESSO."""

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        clones = {} # Funge sia da mappa che da registro 'visited'

        def dfs(curr):
            if curr in clones:
                return clones[curr] # Ritorno la copia già esistente
            
            # Creo la copia e la registro SUBITO per evitare loop infiniti
            clone = Node(curr.val)
            clones[curr] = clone
            
            # Popolo i vicini chiamando la DFS (che mi restituirà sempre un nodo clonato)
            for neighbor in curr.neighbors:
                clone.neighbors.append(
                    dfs(neighbor) # QUESTO è IL TRUCCO DEI TRUCCHI DI QUESTO ESERCIZIO
                )
                
            return clone
            
        return dfs(node)