class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # ===============
        # ripetizione #1
        # ===============

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c): 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1": return 
            grid[r][c] = "#"
            
            for dr, dc in directions: 
                dfs(r + dr, c + dc)

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1": 
                    res += 1
                    dfs(i, j)

        return res