class Solution:

    """APPROCCIO DFS"""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Costruzione list di adiacenza
        adj_list = {i:[] for i in range(n)}
        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node, prev): 
            
            # Se è già visitato è un ciclo: non mi interessa ma devo terminare per evitare loop infiniti
            if node in visited: return

            # Segno il nodo come visitato
            visited.add(node)

            # Propago su tutti i figli che non sono il nodo da cui provengo 
            for child in adj_list[node]: 
                if child != prev: 
                    dfs(child, node)
            return

        n_conn_comp = 0
        for node in adj_list: 
            if node not in visited:
                n_conn_comp += 1
                dfs(node, None)


        return n_conn_comp