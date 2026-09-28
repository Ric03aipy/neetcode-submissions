class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # DAL TESTO: 
        # You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and 
        # consisted of n-1 edges.
        # --> inizialmente era un albero
        # two different vertices --> l'arco aggiunto non è un cappio

        # Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple
        # answers, return the edge that appears last in the input edges.
        # --> devo ritornare l'ultimo arco che mi da false nell'union, ovvero l'ultimo arco che mi forma un ciclo
        # (è evidente nella foto a quadrato che anche se c'è 1 arco di troppo, poi possono diventare motli gli archi che 
        # formano un ciclo)

        # A differenza dei precedenti che si risolvono facilmente con dfs pure, questo non mi sembra altrettanto multi risoluzione.

        # Gli archi sono da 1 a n quindi stavolta alloco n + 1 valori, tanto il costo è sempre O(V) - [0] è inutilizzato
        # ma è un'inefficienza assolutamente microscopica a favore della leggibilità
        
        n = len(edges) 
        parent = list(range(n + 1))
        ranks = [1] * (n + 1)

        def find(node): 
            if parent[node] != node: 
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2): 
            p1, p2 = find(node1), find(node2)
            if p1 == p2: return False   # Ciclo     
            if parent[p1] > parent[p2]: 
                parent[p2] = p1
            elif parent[p2] > parent[p1]: 
                parent[p1] = p2
            else: 
                parent[p2] = p1
                ranks[p1] += 1
            return True
        
        last = None
        for u, v in edges: 
            if not union(u, v): last = [u, v]
        return last
        

