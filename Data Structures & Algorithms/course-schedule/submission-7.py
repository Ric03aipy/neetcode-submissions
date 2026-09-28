class Solution:

    """SOLUZIONE CON STATI/COLORE"""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Nodo - Corso | Arco - Prerequisiti (altri corsi)

        # Dichiarazione degli stati possibili per ogni nodo del grafo - Anche BIANCO, GRIGIO, NERO
        UNEXPLORED, VISITING, VISITED = 0, 1, 2

        adj_list = {course:[] for course in range(numCourses)}
        for course, pre in prerequisites: adj_list[course].append(pre)

        # All'inizio tutti i nodi sono non esplorati. Visto che sappiamo il loro numero e sappiamo indicizzarli usiamo 
        # una lista. Altrimenti anche un dizionario andava bene. 
        state = [0] * numCourses 

        def dfs(node:int): 

            # Per essere VISITING vuol dire che sono tornato indietro nel loop, quindi c'è un CICLO
            if state[node] == VISITING: return False

            # Se il nodo è completamente esplorato significa che ho potuto vedere il suo percorso fino alla fine senza cicli.
            # è un nodo valido, ovvero un corso che può essere completato
            if state[node] == VISITED: return True

            # Marco il nodo corrente come in visita per rami che discendono da questo: servirà a vedere se esiste un ciclo
            # che comprende questo nodo
            state[node] = VISITING
            for child in adj_list[node]: 
                if not dfs(child): return False

            # Una volta che visto tutti i possibili rami con questo nodo lo segno come definitivamente esplorato. 
            # Non ci torno più. 
            state[node] = VISITED

            return True


        for course in adj_list: 
            if state[course] == UNEXPLORED: 
                if not dfs(course): return False
            
        return True