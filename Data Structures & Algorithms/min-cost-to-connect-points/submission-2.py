class Solution:

    # Soluzione con Prim
    # Per memoria, visto che il grafo viene generato al volo, in questo caso Prim > Kruskal

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # MinHeap per estrarre sempre l'arco a costo minimo
        import heapq 

        # Il primo punto, di inizializzazione, dista 0 da se stesso; (distanza, indice)
        prim_q = [] 

        # Quando questo contiene n-1 elementi ho toccato tutti i punti
        visited = set()
        
        # Inizializzo facendo una passata di calcoli di distanze
        for i in range(1, len(points)): 
            a, b = points[0], points[i]
            manhattan_distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
            heapq.heappush(prim_q, (manhattan_distance, 0, i))
        visited.add(0) # Ho già fatto tutti i calcoli possibili per il primo punto, non voglio più vederlo

        tot_dist = 0
        while prim_q: 
            dist, src_idx, dst_idx = heapq.heappop(prim_q)
            if len(visited) == len(points): break
            if dst_idx in visited: continue
            tot_dist += dist
            visited.add(dst_idx)
            # Propago dalla destinazione 
            for i in range(len(points)): 
                # Salto i nodi già visti (evito cicli) e la destinazione stessa (evito cose con costo 0 e perciò cicliche)
                if i in visited: continue
                a, b = points[dst_idx], points[i]
                manhattan_distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
                heapq.heappush(prim_q, (manhattan_distance, dst_idx, i))

            
        return tot_dist

