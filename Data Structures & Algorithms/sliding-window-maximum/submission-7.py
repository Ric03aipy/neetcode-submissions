class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ===============
        # ripetizione #1 
        # ===============

        from collections import deque

        deq = deque() # qui gli elementi hanno una data di scadenza: è l'indice 
        maxs = []

        for right in range(len(nums)): 
            left = right - k + 1    # right=3, k=3, left deve essere 1 (indici 1,2,3) 

            while deq and deq[0] < left: # confronto tra indici: via ciò che è scaduto
                deq.popleft()

            while deq and nums[right] > nums[deq[-1]]: # [1,2,3,6] 6 scade dopo, non c'è verso che chi viene prima possa essere un massimo in una finestra a dimensione fissa
                deq.pop()

            deq.append(right)

            if right >= k - 1: # non left, perché gli inserimenti sono fatti su right, altrimenti ne perdi k 
                # alla fine di ogni giro, visto che la deq da sx a dx è strettamnte descrescente sui numeri, il massimo è 
                # nums[deq[0]]
                maxs.append(nums[deq[0]]) # (inoltre non può essere vuota a meno che nums lo sia)

        return maxs



            