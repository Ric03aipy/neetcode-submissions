class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        import heapq
        tot_time = 0

        # Costruisco la lista di adiacenza, portando anche l'informazione temporale
        adj_list = {idx: [] for idx in range(n + 1)}
        for src, dst, time in times: adj_list[src].append((time, dst))
        
        # Inizializzo la coda di priorità con la radice. Info nella coda (cumulative_time, node).
        priority_queue = [(0, k)]

        # Struttura per sapere chi è stato già estratto
        visited = set()

        # Dijkstra (BFS con coda di priorità)
        while priority_queue: # Costo: O(E) - quanti elementi possono entrare? 1 per ogni arco | senza stati è il costo in spazio che non viene soddisftto
            curr_time, node = heapq.heappop(priority_queue)
            if node in visited: continue
            if len(visited) == n: break # in coda rimangono solo nodi già visti con costo più alto di quello scelto
            tot_time = max(tot_time, curr_time)
            visited.add(node)

            for time_node2child, child in adj_list[node]: 
                if child not in visited: 
                    heapq.heappush(priority_queue, (curr_time + time_node2child, child))

        # è impossibile risolvere il problema se c'è più di 1 componente connessa, ovvero se la sorgente k non può 
        # fisicamente trasmettere a qualche nodo
        if len(visited) != n: return -1

        return tot_time    

