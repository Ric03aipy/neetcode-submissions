import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        
        # Trasformiamo l'array in un Min-Heap valido in tempo O(N)
        heapq.heapify(self.min_heap)
        
        # Riduciamo il Min-Heap finché non contiene esattamente i K elementi più grandi
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Inseriamo il nuovo numero nel Min-Heap
        heapq.heappush(self.min_heap, val)
        
        # Se abbiamo superato la capienza K, cacciamo il più piccolo
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # Il K-esimo elemento più grande è garantito essere in cima al Min-Heap
        return self.min_heap[0]
