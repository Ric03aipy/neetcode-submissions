class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(current_path, remain, start_idx):
            if remain == 0:
                res.append(current_path[:])
                return

            for i in range(start_idx, len(candidates)):
                # Pruning anticipato: se il candidato supera il residuo, 
                # essendo l'array ordinato, tutti i successivi saranno peggiori
                if candidates[i] > remain:
                    break
                
                # Salto i duplicati solo sullo stesso livello di ricorsione
                if i > start_idx and candidates[i] == candidates[i-1]:
                    continue

                current_path.append(candidates[i])
                backtrack(current_path, remain - candidates[i], i + 1)
                current_path.pop()

        backtrack([], target, 0)
        return res