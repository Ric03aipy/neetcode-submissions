class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current_path, start_idx):
            # 1. OBIETTIVO: Per i Sottoinsiemi, OGNI nodo dell'albero è una soluzione valida.
            # Non ci sono "vicoli ciechi", quindi salviamo la path ad ogni singola chiamata.
            res.append(current_path[:])

            # 2. ESPLORA LE OPZIONI: Dai numeri successivi fino alla fine
            for i in range(start_idx, len(nums)):
                
                # 3. FAI LA MOSSA
                current_path.append(nums[i])
                
                # 4. SCENDI NEL RAMO (nota: i + 1, non start_idx + 1)
                backtrack(current_path, i + 1)
                
                # 5. ANNULLA LA MOSSA
                current_path.pop()

        backtrack([], 0)
        return res