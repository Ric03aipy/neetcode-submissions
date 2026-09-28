class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque
        
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2

        q = deque()
        for i in range(ROWS): 
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    q.append((i, j, 0)) # Segno nel nodo in coda il tempo di entrata in coda

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        minutes = 0
        while q: 
            
            # Estraggo dalla coda
            r, c, t = q.popleft()
            # Il tempo è il massimo che tiro fuori 
            minutes = max(minutes, t)

            # Vedo i figli 
            for dir_row, dir_col in directions: 

                # Seleziono il figlio da mettere potenzialmente in coda
                n_row, n_col = r + dir_row, c + dir_col

                # Controllo di esistenza del figlio
                if n_row < 0 or n_row >= ROWS or n_col < 0 or n_col >= COLS: continue

                # FRESH -> modifico in place poi "propago l'onda" == aggiungo in coda
                # EMPTY -> non faccio niente e non propago
                # ROTTEN -> non faccio niente e non progago: sono già in coda a turno 0
                if grid[n_row][n_col] == FRESH: 
                    grid[n_row][n_col] = ROTTEN
                    q.append((n_row, n_col, t + 1)) # Ci vuole 1 minuto partendo da ROTTEN, 2 se a distanza 2 e così via

        for i in range(ROWS): 
            for j in range(COLS):
                if grid[i][j] == FRESH: return -1

        return minutes

