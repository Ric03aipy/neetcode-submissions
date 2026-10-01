class Solution:

    # Come Soluzione precedente ma con space ottimization

    def rob(self, nums: List[int]) -> int:
        # Caso base
        n = len(nums)
        if n == 1: return nums[0]

        # Inizializzazione struttura
        prev2 = 0 # distanza 2 dal corrente
        prev1 = nums[0] # distanza 1 dal corrente

        # Ciclo
        for i in range(2, n + 1): 
            curr = max(prev2 + nums[i-1], prev1)
            prev2 = prev1
            prev1 = curr

        return prev1