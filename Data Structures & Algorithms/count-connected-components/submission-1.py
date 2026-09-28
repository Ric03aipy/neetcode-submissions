class Solution:
    
    """APPROCCIO UNION FIND"""
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        n_conn_comp = 0

        parent = list(range(n))
        ranks = [1] * n

        # Se un nodo non è genitore di se stesso allora non è un capogruppo: appiattisco l'albero fino al capogruppo
        def find(node) -> int: 
            """Resituisce il leader del gruppo a cui il nodo in input appartiene."""
            if parent[node] != node: 
                parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2) -> bool: 
            """Unisce i gruppi dei due nodi."""
            p1, p2 = find(n1), find(n2)
            
            # La presenza di un ciclo non è un problema per questo esercizio. Comunque devo uscire per non fare cose strane.
            if p1 == p2: return False
            
            if ranks[p1] > ranks[p2]: 
                parent[p2] = p1
            elif ranks[p2] > ranks[p1]:
                parent[p1] = p2
            else: 
                parent[p2] = p1
                ranks[p1] += 1
            return True

        for u, v in edges: 
            union(u, v)
        
        # Per sapere quante componenti connesse ci sono, ho bisogno di sapere quanti capogruppi unici ci sono
        # Prima mi assicuro che l'albero sia perfettamente appiattito per ogni gruppo
        for i in range(n): find(i)
        
        return len(set(parent))



