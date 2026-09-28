class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Idea più elegante:
        # Posso lanciare una dfs da tutti gli 1 per segnarli visited. 
        # Ogni volta che faccio partire 1 dfs aggiungo 1 al contatore globale del risultato. 
        # Posso risparmiare il set visited in memoria applicando il trucco della modifica dell'input

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c): 
            
            if r < 0 or r >= rows or c < 0 or c >= cols: return 

            if grid[r][c] != "1": return 
            
            grid[r][c] = "#"
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        counter = 0
        for i in range(rows):
            for j in range(cols):  
                if grid[i][j] == "1": 
                    counter += 1
                    dfs(i, j)

        return counter




