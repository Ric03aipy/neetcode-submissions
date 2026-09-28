class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Edge case che non viene risolto dall'algoritmo di backtrack (restituirebbe [""])
        if digits == "": return [] 

        letters = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

        res = [] 

        def dfs(path, start_idx):

            # Condizione di uscita: ho messo una lettera per ogni cifra
            if len(path) == len(digits): 
                res.append("".join(path)) # Creo la stringa solo quando ho una soluzione, invece della hconcatenazione 
                return 

            # Per ogni cifra devo fare una scelta del carattere da selezionare oppure no
            for i in range(start_idx, len(digits)): # --- CICLO DA TEMPLATE QUANDO HO n POSSIBILITà (cifre)

                for char in letters[digits[i]]: 
                    
                    # Faccio la mossa
                    path.append(char)

                    # Ricorsione
                    dfs(path, i + 1)

                    # Torno indietro per provare un altra lettera associata alla stessa cifra
                    path.pop()

            # se M è il massimo numero di caratteri associati a un numero (M=4) allora il costo di questo algoritmo 
            # dovrebbe essere 4^n a cui aggiungere il costo del join che alle brutte è n, quindi i conti tornano con la 
            # richiesta O(n*(M^n)) = O(n*(4^n))


        dfs([], 0)

        return res



