class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        # O(1) lookup per le zone sotto attacco
        used_rows = set()
        used_pos_diag = set() # (r + c)
        used_neg_diag = set() # (r - c)
        
        # Invece di tuple, salviamo solo l'indice della colonna per ogni riga
        # (ci faciliterà la stampa finale)
        board = [["."] * n for _ in range(n)]

        def backtrack(c):
            # OBIETTIVO: Abbiamo piazzato una regina in ogni colonna
            if c == n:
                res.append(["".join(row) for row in board])
                return
            
            # ESPLORA: Provo tutte le righe per questa colonna
            for r in range(n):
                # PRUNING: Se la casella è sotto tiro, la salto immediatamente (O(1))
                if r in used_rows or (r + c) in used_pos_diag or (r - c) in used_neg_diag:
                    continue
                
                # FAI LA MOSSA: Segno la scacchiera e aggiorno i Set
                used_rows.add(r)
                used_pos_diag.add(r + c)
                used_neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # SCENDI
                backtrack(c + 1)
                
                # ANNULLA LA MOSSA (Backtrack)
                used_rows.remove(r)
                used_pos_diag.remove(r + c)
                used_neg_diag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res