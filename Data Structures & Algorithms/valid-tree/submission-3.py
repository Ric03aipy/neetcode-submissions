class Solution:

    """APPROCCIO DFS PER COMPONENTI CONNESSE SU GRAFI NON DIRETTI. NIENTE 3 STATI. I 3 STATI SI USANO PER GRAFI DIRETTI."""

    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Un albero DEVE avere ESATTAMENTE n-1 archi
        if len(edges) != n-1: return False

        # Costruzione della lista di adiacenza con doppia connessione per ogni arco non diretto        
        adj_list = {i:[] for i in range(n)}
        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Struttura per tracciare nodi visti
        visited = set()

        def dfs(node, prev): 
            
            # Se un nodo è stato già visitato allora ho un ciclo. Sono sicuro che non è un passo all'indietro per 
            # la condizione pre ricorsione che scarta l'ipotesi.
            if node in visited: return False

            # Segno questo nodo come toccato
            visited.add(node)

            # Voglio vedere solo figli "in avanti"
            for child in adj_list[node]: 
                if child != prev: 
                    if not dfs(child, node): return False
                
            return True

        if not dfs(0, None): return False

        # Se ho visitato tutti i nodi allora formano un unica componente connessa
        return len(visited) == n

        