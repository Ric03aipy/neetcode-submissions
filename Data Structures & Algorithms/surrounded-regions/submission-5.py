class Solution:

    """SOLUZIONE: ATTACCHIAMO DAI BORDI"""
    
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r:int, c:int, safe:set):

            # Condizioni di non validità
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in safe or board[r][c] == 'X': return False

            # Qui arrivano solo 'O' che sono connesse in un percorso ai bordi 
            safe.add((r, c))

            # Propago la dfs nelle 4 direzioni
            dfs(r + 1, c, safe)
            dfs(r - 1, c, safe)
            dfs(r, c + 1, safe)
            dfs(r, c - 1, safe)

        safe = set()
        for i in range(ROWS):
            if board[i][0] == 'O': 
                dfs(i, 0, safe)
            if board[i][COLS - 1] == 'O':
                dfs(i, COLS - 1, safe)
        for j in range(COLS): 
            if board[0][j] == 'O':
                dfs(0, j, safe)
            if board[ROWS - 1][j] == 'O':
                dfs(ROWS - 1, j, safe)

        # Tutto ciò che non è safe non si salva
        for i in range(1, ROWS-1):
            for j in range(1, COLS-1): 
                if (i, j) not in safe and board[i][j] == 'O': board[i][j] = 'X'
