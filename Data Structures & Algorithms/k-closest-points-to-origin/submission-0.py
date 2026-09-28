class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import heapq
        from math import sqrt

        # # Ha senso aggiungere ai k elementi qualcosa solo se la distanza di un nuovo punto è minore del massimo
        # # della collezione attuale
        # max_dist = -float('inf')

        # distanza euclidea (x,y) = sqrt((x1 - x2)^2 + (y1 - y2)^2))
        # ma dall'origine y = (0, 0)
        # la distanza diventa d(x, 0) = sqrt(x1^2 + y1^2)

        def dist_from_origin(x:List[int]) -> int: return sqrt(x[0] ** 2 + x[1] ** 2)

        # Creo un array di dimensione k - predisposto per MaxHeap: il più grande minimo si ottiene in O(1) e non serve
        # una variabile max_dist per tracciare la distanza del punto più lontano dei primi k (garantito len(points) >= k)
        # Nella struttura dati conservo distanza e punti per poter mantenere un parallelismo
        d_arr = [(-dist_from_origin(points[i]), points[i]) for i in range(k)]

        # Rendo l'array un MaxHeap
        heapq.heapify(d_arr)

        # Controllo gli altri valori 
        for i in range(k, len(points)): # completa il costo del ciclo di prima -> O(n)
            # Un punto entra solo se ha distanza minore del k-esimo massmo, ovvero la radice
            point = points[i]
            dist = -dist_from_origin(point)
            # Se la distanza negativa è maggiore allora la distanza è minore
            if dist > d_arr[0][0]:  # operazione 'peek' in O(1) per controllo, se passa operazioni di costo O(log k)
                                    # d_arr[0] primo elemento --> d_arr[0][0] distanza del primo elemento
                heapq.heappop(d_arr)
                heapq.heappush(d_arr, (dist, point))
        
        # La richiesta dice che non è importante l'ordine dei k elementi
        return [point for _, point in d_arr]
            