class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Creazione della lista di adiacenza        
        adj_list = {i:[] for i in range(n)}
        for src, dst in edges: 
            # Doppie connessioni
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # Stati
        UNEXPLORED, VISITING, VISITED = 0, 1, 2
        state = [UNEXPLORED] * n

        # Idea: se una dfs non rileva cicli ed è sufficiente a marcare tutto il grafo allora il grafo è un albero unico
        def dfs(node) -> bool:  
            # Se trovo un nodo percorrendo un'altra direzione vuol dire che ho trovato un ciclo
            if state[node] == VISITED: return False
            # Se torno su un nodo che sto visitando lo accetto perché il ciclo è artificiale, è dovuto alla bidirezionalità
            # if state[node] == VISITING: 
            #     # Se ritorno true significa che il ciclo artificiale viene fatto passare
            #     # E solo il nodo marcato come completamente visitato che viene nuovamente visto fa scattare l'allarme
            #     # (Logica opposta a grafo diretto)
            #     return True
            
            state[node] = VISITING
            # Marco tutti i sottoposti
            for child in adj_list[node]: 
                if state[child] != VISITING:
                    if not dfs(child): return False
            # Marco il nodo corrente come trovato percorrendo una direzione
            state[node] = VISITED
            return True

        # Se è un albero, visto che è un grafo non diretto, allora dovrebbe rappresentare un'unica componente connessa, 
        # dunque non è rilevante quale nodo viene usato per fare da root
        if not dfs(0): return False
        print(state)
        return all(state)