class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        import heapq
        from collections import defaultdict

        # Costruisco la lsita di adiacenza
        adj_list = defaultdict(list)
        for u, v, p in flights: adj_list[u].append((p, v)) # {from: (price, to)}

        q = [(0, 0, src)]   # (cumulative price, number of intermediate stops, destination airport)
        intermediate_stop = 0 
        visited = dict()

        while q: 
            # print(q, visited)
            cumulative_price, n_stops, node = heapq.heappop(q)
            
            # Vincolo di fermate intermedie (stop sulla profondità)
            if n_stops > k + 1: continue # k + 1 perché la desinazione non conta nei k

            # Se sono a una profondità ammissibile il primo percorso che mi porta alla soluzione è a costo minimo
            if node == dst: return cumulative_price

            # Questo controllo permette di saltare i cicli senza 3 stati: per la coda di priorità, un nodo che viene visto 
            # una seconda volta non ha senso di essere considerato, in quanto, se facesse parte della soluzione, sarebbe
            # sempre preferibile la prima visita. A questo però bisogna aggiungere il vincolo sulle fermate...
            if node in visited: 
                if n_stops >= visited[node]: continue
                # ... se invece è un percorso più corto magari lo voglio vedere di nuovo
            visited[node] = n_stops

            # Aggiungo i figli
            for child_price, child_to in adj_list[node]: 
                heapq.heappush(q, (cumulative_price + child_price, n_stops + 1, child_to))

        return -1




