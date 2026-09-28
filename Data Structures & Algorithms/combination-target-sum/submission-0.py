class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
         
        def backtrack(current_path, start_idx): 
            
            # Condizione di terminazione
            if sum(current_path) == target:
                res.append(current_path.copy())
                return 
                # Constraint: 2 <= nums[i] <= 30 ; se ci potesse essere stato 0 dopo non potevo ritornare
                # o avrei mancato delle combinazioni
            
            # Ciclo sui candidati da entrare nel path corrente
            for i in range(start_idx, len(nums)): 
                
                # Condizione di non validità (dipende dal constraint di avere numeri strettamente positivi)
                if sum(current_path) > target: continue

                # Faccio un passo 
                current_path.append(nums[i])

                # Chiamata ricorsiva - NON i+1, ma i perché "The same number may be chosen from nums an unlimited number of times"
                backtrack(current_path, i)

                # Ritiro il passo
                current_path.pop()


        backtrack([], 0)
        return res