class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq 
        
        # (distanza_per_raggiungerlo, indice_del_punto)
        # Partiamo dal nodo 0 a costo 0
        prim_q = [(0, 0)] 
        visited = set()
        tot_dist = 0
        
        while prim_q: 
            dist, node = heapq.heappop(prim_q)
            
            if node in visited: continue

            visited.add(node)
            tot_dist += dist
            
            if len(visited) == len(points): break
                
            # Propaga verso tutti gli altri nodi non ancora nel cluster
            for i in range(len(points)): 
                if i not in visited: 
                    d = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    heapq.heappush(prim_q, (d, i))
                    
        return tot_dist