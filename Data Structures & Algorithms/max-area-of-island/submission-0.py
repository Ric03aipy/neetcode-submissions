class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        m, n = len(grid), len(grid[0])

        # Calcola l'area di un'isola
        def dfs(r, c, curr_area) -> int: 
            
            if r < 0 or r >= m or c < 0 or c >= n: return 0
            if grid[r][c] != 1: return 0

            grid[r][c] = "#" # se è un "1" lo marco come visto

            # L'area è data dalla cella corrente (un 1) sommata all'area nei 4 versi possibili
            area =  dfs(r + 1, c, curr_area + 1) + \
                    dfs(r - 1, c, curr_area + 1) + \
                    dfs(r, c + 1, curr_area + 1) + \
                    dfs(r, c - 1, curr_area + 1) + \
                    1 

            return area

        for i in range(m):
            for j in range(n):  
                if grid[i][j] == 1: 
                    max_area = max(max_area, dfs(i, j, 0))

        return max_area

