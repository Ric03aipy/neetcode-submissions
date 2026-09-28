class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # =================
        # ripetizione #1
        # =================

        # Struttura per marcare i visitati
        # seen = set()
        max_area = 0

        def dfs(r, c): 
            # Se la cella non è valida o è stata già visitata non la prendo in considerazione
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):# or (r, c) in seen: 
                return 0
            
            # seen.add((r, c))
            val = grid[r][c]
            grid[r][c] = "#"
            if val != 1: return 0
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if (i, j) not in seen:
                if grid[i][j] != "#":
                    max_area = max(max_area, dfs(i, j))

        return max_area