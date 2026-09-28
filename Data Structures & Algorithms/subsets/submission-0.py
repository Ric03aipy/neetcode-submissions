class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Tutti i possibili sottoinsiemi di nums (insieme delle parti)
        # Il fatto che sia una lista - mutabile - è in accordo con l'ingegneria del sofware: non sto creando una
        # variabile di istanza
        res = []

        def backtrack(current_path, start_idx):
            
            # Condizione di goal ? Nessuna di goal, ma di terminazione: non posso andare oltre la lunghezza di nums
            if start_idx == len(nums): 
                res.append(current_path[:])
                return 

            if start_idx < len(nums): 
                res.append(current_path[:])

            for i in range(start_idx, len(nums)): # vedo ogni numero in nums dall'indice start_idx 

                # Prendo il numero in considerazione
                current_path.append(nums[i])

                # Prossima mossa: start_idx mi fa new_choies (alternativamente dovrebbe essere nums[idx+1:] ma è uno spreco 
                # di memoria)
                backtrack(current_path, i + 1)

                # Ripristino delle condizioni
                current_path.pop()


        backtrack([], 0)
        return res