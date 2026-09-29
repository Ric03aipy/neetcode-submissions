class Solution:
    
    # Un altro approccio è una BFS pura limitata a k + 1 livelli

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Inizializzo la coda
        from collections import deque
        q = deque()

        # Costruisco la lsita di adiacenza e la struttura di supporto per il costo minimo
        adj_list = defaultdict(list)
        min_cost_to_reach_node = {}
        for u, v, p in flights: 
            adj_list[u].append((p, v)) # {from: (price, to)}
            min_cost_to_reach_node[u] = float('inf')
            min_cost_to_reach_node[v] = float('inf')

        # Sorgente in coda con indicazione di profondità e costo di percorso
        q.append((src, 0, 0))

        min_cost = float('inf')

        while q: 
            node, depth, cumulative_cost = q.popleft()
            
            # dst può essere al più a distanza k + 1 (0-src, k-intermedi, k+1-dst). Se lo supero non va bene. 
            # Il limitatore di profondità è anche una garanzia di "cicli limitati". 
            if depth > k + 1: continue

            if node == dst: min_cost = min(min_cost, cumulative_cost)

            for child_cost, child,  in adj_list[node]: 
                child_cumulative_cost = cumulative_cost + child_cost
                if child_cumulative_cost < min_cost_to_reach_node[child]: 
                    # Aggiorno la struttura dati 
                    min_cost_to_reach_node[child] = child_cumulative_cost
                    q.append((child, depth + 1, child_cumulative_cost))

        # Casi di fallimento: coda vuota o coda non vuota ma non ci sono elementi meno profondi di k
        return -1 if min_cost == float('inf') else min_cost





