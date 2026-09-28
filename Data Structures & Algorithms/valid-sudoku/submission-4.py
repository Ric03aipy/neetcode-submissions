class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # chiave: tupla (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                
                if cell == ".":
                    continue
                
                # Check 1: Esiste già in questa riga, colonna o quadrato?
                if (cell in rows[r] or 
                    cell in cols[c] or 
                    cell in squares[(r // 3, c // 3)]):
                    return False
                
                # Update: Aggiungiamo il valore ai rispettivi Set
                cols[c].add(cell)
                rows[r].add(cell)
                squares[(r // 3, c // 3)].add(cell)

        return True