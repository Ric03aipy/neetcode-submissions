class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ===============
        # ripetizione #4
        # ===============

        from collections import deque

        d = deque() # indici
        res = []
        
        for right in range(len(nums)): 
            
            left = right - k + 1

            # controllo sulla scadenza e aggiornamento risultato
            if d and left > d[0]: d.popleft()
            
            # aggiungo un elemento più piccolo oppure se è più grande pulisco tutti i più piccoli
            while d and nums[d[-1]] < nums[right]: d.pop()
            d.append(right)

            if right >= k - 1: res.append(nums[d[0]])

        return res
            


