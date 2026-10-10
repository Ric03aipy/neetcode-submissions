class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # ==============
        # ripetizione #1
        # ==============

        from collections import deque

        q = deque()

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(ROWS): 
            for j in range(COLS): 
                # metto in coda al livello 0 le sorgenti
                if grid[i][j] == 0: 
                    q.append((i, j))

        while q: 
            r, c = q.popleft()
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647: continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))


