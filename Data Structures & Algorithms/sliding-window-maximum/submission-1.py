class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        maxs = []
        deq:deque[int] = deque() # dentro contiene indici, tanto il valore è nums[indice] quindi non serve conservarlo
        # process first k elements
        print(deq)
        for right in range(len(nums)): 
            left = right - k + 1 # elemento per cui nums[left] vale, mentre la finestra è nums[left-1:right]

            # deq[0] contiene il massimo più recentemente trovato, deq[-1] è il minimo (monotonia) 
            # [6,3,2,5] -> vedrò prima 6 -> [6], poi più deboli -> [6,3,2], poi 5 -> [6,5], se k=4 per es.
            while deq and nums[right] > nums[deq[-1]]:
                # elimino candidati che non potranno mai essere il massimo della finestra 
                deq.pop()

            deq.append(right)
            
            # esce un numero con indice superiore, ovvero deq[0] è scaduto, è fuori finestra
            if left > deq[0]: 
                v = deq.popleft()
            # ad ogni iterazione il massimo della finestra si troverà in deq[0]
            
            # le prime iterazioni in cui la finestra non ha dimensione k non possono essere contate
            if left >= 0:
                maxs.append(nums[deq[0]])


        return maxs
