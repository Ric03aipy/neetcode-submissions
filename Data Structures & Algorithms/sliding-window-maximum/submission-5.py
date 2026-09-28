class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ===============
        # ripetizione #1 
        # ===============

        # SOLUZIONE NAIVE 1 LINE: return [max(nums[right-k:right]) for right in range(k, len(nums)+1)]

        from collections import deque
        deq = deque()
        res = []

        for right in range(len(nums)): 
            left = right - k + 1
        
            # mantenimento di monotonia
            while deq and nums[right] > nums[deq[-1]]: 
                deq.pop()

            deq.append(right)
            
            # se la scadenza è arrivata
            if deq[0] < left: 
                deq.popleft()

            # se è grande abbastanza 
            if right >= k - 1: 
                res.append(nums[deq[0]])

        return res 
            

