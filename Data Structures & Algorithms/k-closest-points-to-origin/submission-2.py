class Solution:

    # stesso codice della soluzione 1 ma con 2 ottimizzazioni: 
    # 1) sqrt(x) < sqrt(y) => x < y matematicamente quindi 
    # 2) heappop seguito da heappush per leggibilità può essere rimpiazzato da heapreplace

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        from math import sqrt

        def dist_squared_from_origin(x:List[int]) -> int: return x[0] ** 2 + x[1] ** 2

        # Creo un array di dimensione k - predisposto per MaxHeap: il più grande minimo si ottiene in O(1) e non serve
        # una variabile max_dist per tracciare la distanza del punto più lontano dei primi k (garantito len(points) >= k)
        # Nella struttura dati conservo distanza e punti per poter mantenere un parallelismo
        d_arr = [(-dist_squared_from_origin(points[i]), points[i]) for i in range(k)]

        # Rendo l'array un MaxHeap
        heapq.heapify(d_arr)

        # Controllo gli altri valori 
        for i in range(k, len(points)): # completa il costo del ciclo di prima -> O(n)
            # Un punto entra solo se ha distanza minore del k-esimo massmo, ovvero la radice
            point = points[i]
            dist = -dist_squared_from_origin(point)
            # Se la distanza negativa è maggiore allora la distanza è minore
            if dist > d_arr[0][0]:  heapq.heapreplace(d_arr, (dist, point))
        
        # La richiesta dice che non è importante l'ordine dei k elementi
        return [point for _, point in d_arr]
            