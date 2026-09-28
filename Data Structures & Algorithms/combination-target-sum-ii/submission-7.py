class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # ================
        # ripetizione #1
        # ================

        # Preliminare per saltare i duplicati
        candidates.sort()

        # Risultato da riempire
        res = []

        def dfs(path, start_idx, curr_sum): 
            """
            path: lista di valori
            start_idx: primo indice da controllare per il nuovo ciclo - serve a evitare permutazioni
            curr_sum: sum(path), evita un costo O(n) inutile
            """

            # Condizione di successo prima perché altrimenti salta l'ultimo
            if curr_sum == target: res.append(path[:])

            # Pruning intelligente
            if curr_sum > target: return 

            for i in range(start_idx, len(candidates)): 

                if i > start_idx and candidates[i] == candidates[i-1]: continue

                path.append(candidates[i])
                dfs(path, i + 1, curr_sum + candidates[i])
                path.pop()  

        dfs([], 0, 0)

        return res

        # [9,2,2,4,6,1,5]
        # [1,2,2,4,5,6,9]


