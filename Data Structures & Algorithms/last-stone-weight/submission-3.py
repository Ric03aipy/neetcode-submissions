class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # ====================
        # ripetizione #1
        # ====================

        import heapq

        # Per ottenere un max heap mi serve un minheap a valori negativi
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            x = -heapq.heappop(stones)  
            y = -heapq.heappop(stones)
            # x è stata pescata per prima, quindi è necessariamente x >= y per costuzione della struttura dati
            if x != y: heapq.heappush(stones, -(x-y))
    
        return -stones[0] if stones else 0

