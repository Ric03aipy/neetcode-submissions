class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        # DFS
        def backtrack(path:set[str], r, c, i): 
            """
            r: indice di riga
            c: indice di colonna
            i: indice di word - da 0 a len(word) - 1, quindi quando la funzione viene chiamata con i == len(word)allora 
                tutta la parola è stata correttamente matchata carattere per carattere
            """
            
            # Condizione di successo - è la prima condizione perché word[len(word)] non è definita, è OOB
            if i == len(word): return True

            # Condizione di uscita per OOB
            if (not (0 <= r < rows)) or (not (0 <= c < cols)): return False
            
            # Condizione di uscita per fallimento di sotto-obiettivo: posizione corrente = carattere ricercato
            if board[r][c] != word[i]: return False

            # Condizione di uscita per visione della stessa cella
            if (r, c) in path: return False

            # Vista la negazione precedente, qui abbiamo board[r][c] == word[i]
            
            # Faccio la mossa
            path.add((r, c))

            # Ricorsione della DFS
            res =   backtrack(path, r + 1, c, i + 1) or \
                    backtrack(path, r - 1, c, i + 1) or \
                    backtrack(path, r, c + 1, i + 1) or \
                    backtrack(path, r, c - 1, i + 1) 

            # Ritiro la mossa
            path.discard((r, c))

            return res

        out = False
        for i in range(rows): 
            for j in range(cols):
                out = out or backtrack(set(), i, j, 0)
                if out: return True
        
        return out

        