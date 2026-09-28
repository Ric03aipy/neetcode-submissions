class Solution:

    """SOLUZIONE DA O(1) IN MEMORIA. TRUCCO DI POLLICINO."""

    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r:int, c:int):

            # Condizioni di non validità
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O': 
                return 

            # Qui arrivano solo 'O' che sono connesse in un percorso ai bordi 
            board[r][c] = "#" # marcatore temporaneo

            # Propago la dfs nelle 4 direzioni
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][COLS - 1] == 'O': dfs(i, COLS - 1)
        for j in range(COLS): 
            if board[0][j] == 'O': dfs(0, j)
            if board[ROWS - 1][j] == 'O': dfs(ROWS - 1, j)

        # Tutto ciò che non è safe non si salva
        for i in range(ROWS):
            for j in range(COLS): 
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '#': board[i][j] = 'O'