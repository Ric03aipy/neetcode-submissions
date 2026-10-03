class Solution:

    # L'idea qui è runnare da nums[0] a nums[n-2] e poi da nums[1] a nums[n-1] l'algoritmo precedente e prendere il massimo
    # Visto che il vincolo mi impedisce di prendere la prima E l'ultima allora tratto come 2 segmenti che si differenziano
    # solo per capo e coda

    def rob(self, nums: List[int]) -> int:
        
        # Caso base
        if len(nums) == 1: return nums[0]
        n = len(nums)

        def robAuxiliary(from_idx, to_idx) -> int:
            # Qui già sappiamo che la lunghezza è > 2

            # Inizializzazione struttura
            prev2 = 0 # distanza 2 dal corrente
            prev1 = nums[from_idx] # distanza 1 dal corrente

            # Ciclo
            for i in range(from_idx + 2, to_idx + 1): 
                curr = max(prev2 + nums[i-1], prev1)
                prev2 = prev1
                prev1 = curr

            return prev1
        
        max_left = robAuxiliary(0, n - 1)
        max_right = robAuxiliary(1, n)
        return max(max_left, max_right)