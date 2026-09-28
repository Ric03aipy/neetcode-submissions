class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Anche se dalla versinoe 3.14 funzioni specifiche per MaxHeap sono implementate, 
        # preferisco complicare un pochino con il metodo che si usava fino a poco fa, retrocompatibile e più robusto.
        import heapq
        # Dentro heapq è implmentato un MinHeap. Per avere un MaxHeap cambio il segno - O(n)
        stones = [-stone for stone in stones]
        heapq.heapify(stones) 
        while len(stones) > 1: # O(n) * O(logn) - ciclo * costo delle operazioni dominanti
            # Estraggo 2 pietre e le riporto al segno originale per applicare la logica in modo chiaro: sono i due 
            # minimi negativi, ovvero i due massimi positivi, quindi sicuramente y <= x
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            # Regola di scontro
            if x > y: 
                new_weight = x - y
                # Aggiungo con cambio di segno per coerenza con MaxHeap
                heapq.heappush(stones, -new_weight)
        # Anche quando si estrae, per ottenere il valore coerente con l'array iniziale bisogna cambiare il segno
        return -stones[0] if stones else 0