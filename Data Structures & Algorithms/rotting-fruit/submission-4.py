class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # =================
        # ripetizione #1
        # =================

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0 
        fresh = 0
        from collections import deque
        q = deque()
        for i in range(ROWS):
            for j in range(COLS): 
                if grid[i][j] == 2: q.append((i, j, minutes))
                if grid[i][j] == 1: fresh += 1

        while q: 
            r, c, time = q.popleft()
            minutes = max(minutes, time)

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS: continue
            
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, time + 1))
            
        return minutes if fresh == 0 else -1
