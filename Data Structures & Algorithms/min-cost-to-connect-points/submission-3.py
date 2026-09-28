class Solution:
    
    # Soluzione con Kruskal

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Ho bisogno di conoscere tutte le distanze per poter unire con la minima distanza - O(n^2) con n=len(points)
        distances = []
        for i in range(len(points)): 
            for j in range(i + 1, len(points)): 
                a, b = points[i], points[j]
                manhattan_distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
                # Registro gli indici perché più piccoli e intuitivi qui - posso accedere ai valori in ogni momento 
                distances.append((i, j, manhattan_distance)) 

        # Ora devo ordinare le distanze in modo crescente - O((n^2)log(n^2)) <=> O((n^2)log(n)) - è il collo di bottiglia
        distances.sort(key=lambda x: x[2])
        
        # Definizione di parent e rank: ogni nodo è parent di se stesso, ogni gruppo (albero) è alto 1
        parent = list(range(len(points)))
        rank = [1] * len(points)

        # Definizione delle funzioni union e find
        def find(node) -> int:
            """Ritorna il capogruppo, appiatendo la struttura nel mentre. Il capogruppo è l'indice di un punto.
            node: indice del punto""" 
            if node != parent[node]: # è vero solo per il capogruppo o per nodi già appiatiti
                parent[node] = find(parent[node]) # per tutti gli altri nodi appiatisco
            return parent[node] # node qui punta al capogruppo
        
        def union(n1, n2) -> bool: 
            p1, p2 = find(n1), find(n2)
            # Se sono nello stesso gruppo l'unione significa creare un arco inter-grouppo quindi un ciclo: non deve accadere
            if p1 == p2: return False
            # Unisco con la logica del bilanciamento
            if rank[p1] > rank[p2]: 
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else: # tie -> arbitrario ma cambia il rango 
                parent[p2] = p1
                rank[p1] += 1
            return True
        
        # Una volta disposti i pezzi applico l'union find
        mst_cost = 0
        edges_unified = 0
        for i, j, dist in distances:
            if edges_unified == len(points) - 1: break 
            if union(i, j): 
                mst_cost += dist
                edges_unified += 1
        return mst_cost







