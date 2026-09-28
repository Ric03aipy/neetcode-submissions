class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        # L'ordine iniziale non conta
        nums.sort()

        def backtrack(path, start_idx): 
            
            # Ogni path è valido purché non ci siano ripetizioni 
            res.append(path[:])

            # Non voglio permutazioni 
            for i in range(start_idx, len(nums)):

                # Non voglio i duplicati
                if i > start_idx and nums[i] == nums[i-1]: continue

                path.append(nums[i])

                backtrack(path, i + 1)
            
                path.pop()

        backtrack([], 0)
        
    
        return res