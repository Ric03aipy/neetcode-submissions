class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Rispetto al precedente esercizio che mi chiedeva se era possibile finire tutti i corsi qui mi chiede
        # una cosa in più, mi chiede di dare una sequenza se esiste. 

        # Mi sta chiedendo un ordinamento topologico. Io non so l'approccio di Kahn. Ma trovo intuitivo l'approccio 
        # dfs e poi inverti 

        # Definisco gli stati/colori (sono variabili che non servono ma aumentano la leggibilità)
        UNEXPLORED, VISITING, VISITED = 0, 1, 2
        state = [0] * numCourses    # Visto che sono da 0 a numCourses-1 posso usare il corso come id

        # Devo sapere chi è il prerequisito di chi; gli elementi sono coppie [a, b], so la dimensione
        adj_list = {course:[] for course in range(numCourses)}
        for course, pre in prerequisites: adj_list[course].append(pre)

        topological_order = []
        def dfs(node) -> bool: 
            # Se il nodo è stato esplorato completamente allora non fa parte di alcun ciclo
            if state[node] == VISITED: return True
            # Se ritorno su nodo mentre è ancora in esplorazione allora fa parte di un ciclo
            if state[node] == VISITING: return False

            # Marco il nodo corrente come aperto
            state[node] = VISITING

            for child in adj_list[node]: 
                if not dfs(child): return False

            state[node] = VISITED
            topological_order.append(node)
            return True


        # La dfs parte da più punti nel caso di componenti non connesse del grafo
        for course in adj_list: 
            if state[course] == UNEXPLORED: 
                # Se c'è un ciclo non ci può essere un ordinamento topologico
                if not dfs(course): return []

        return topological_order


        