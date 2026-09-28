class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(current_path): 
            # OBIETTIVO: Abbiamo usato tutti i numeri?
            if len(current_path) == len(nums): res.append(current_path[:])

            #  ESPLORO: Parti SEMPRE da 0. Ogni numero è un candidato potenziale.
            for j in range(0, len(nums)): 
                
                # PRUNING: Se il numero è già nel percorso, non posso riusarlo!
                if nums[j] in current_path: continue

                current_path.append(nums[j])
                backtrack(current_path)
                current_path.pop()

        backtrack([])

        return res