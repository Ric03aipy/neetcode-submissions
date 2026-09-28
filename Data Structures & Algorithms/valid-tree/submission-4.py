class Solution:

    """APPROCCIO CON UNION-FIND. UNION-FIND NON USA LA LISTA DI ADIACENZA."""

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Un albero DEVE avere ESATTAMENTE n-1 archi
        if len(edges) != n-1: return False

        # Per le 2 strutture dati Union/Find uso array perché so che gli indici vanno da 0 a n-1

        # Tracciamento dei nodi genitore; All'inizio ogni nodo è parent di se stesso
        parent_map = list(range(n))
        # Tracciamento dell'altezza dell'albero con parent il nodo i-esimo
        ranks = [1] * n

        # ======================== Funzioni ausiliarie ========================

        def find(node_id): 
            # Appiattisco mentre salgo al leader grazie alla chiamata ricorsiva. Il nodo deve essere genitore di se stesso 
            # per essere il capogrupo che cerco.
            if node_id != parent_map[node_id]:
                # Il capogruppo del figlio è uguale al capogruppo del padre
                parent_map[node_id] = find(parent_map[node_id])
            return parent_map[node_id]

        def union(node_id1, node_id2) -> bool:
            """Ritorna l'esito dell'operazione. False se trova un ciclo (stesso gruppo), True se avviene l'unione.""" 
            
            parent1, parent2 = find(node_id1), find(node_id2)

            # Se sto cercando di mettere un arco tra due nodi dello stesso gruppo allora sto formando un ciclo
            if parent1 == parent2: return False

            # Altrimenti faccio l'unione in modo che l'albero si mantengo bilanciato: aggancio l'albero più basso al 
            # capogruppo (quindi come sottoalbero del capogruppo) dell'albero più alto
            if ranks[node_id1] > ranks[node_id2]: 
                parent_map[parent2] = parent1
            elif ranks[node_id1] < ranks[node_id2]: 
                parent_map[parent1] = parent2
            else: 
                # Se hanno la stessa grandezza arbitrariamente uno si sottomette all'altro e l'altezza cresce solo 
                # del capogruppo quindi di 1
                parent_map[parent2] = parent1
                ranks[parent1] += 1

            return True

        # ==========================================================================

        # Per ogni arco provo a fare l'unione. Se riesco a unire tutto senza trovare cicli allora è un albero
        for u,v in edges: 
            if not union(u, v): return False
        return True
            

            












        """
        PROBLEMA PER NODI CHE COMPAIONO IN PIù LISTE DI ADIACENZA
        
        # Stati
        UNEXPLORED, VISITING, VISITED = 0, 1, 2
        state = [UNEXPLORED] * n

        # Idea: se una dfs non rileva cicli ed è sufficiente a marcare tutto il grafo allora il grafo è un albero unico
        def dfs(node) -> bool:  
            print("visito", node)
            # Va bene se sto puntando a un nodo già visitato
            if state[node] == VISITED: return True
            # Non va bene se c'è un ciclo
            if state[node] == VISITING: 
                print("dsfsfgdas")
                return False
            
            state[node] = VISITING
            # Marco tutti i sottoposti
            for child in adj_list[node]: 
                if not dfs(child): return False
            # Marco il nodo corrente
            state[node] = VISITED
            return True

        # Se è un albero, visto che è un grafo non diretto, allora dovrebbe rappresentare un'unica componente connessa, 
        # dunque non è rilevante quale nodo viene usato per fare da root
        if not dfs(0): return False
        print(state)
        return all(state)
        """