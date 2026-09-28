class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ===============
        # ripetizione #1
        # ===============

        # L'input è una matrice di adiacenza tra nodi, quindi una singola dfs è O(V^2), qui O(m*n)
        
        ROWS, COLS = len(heights), len(heights[0])

        pac_cells = set()
        atl_cells = set()

        def dfs(r, c, ocean_set, prev): 

            if r >= ROWS or c >= COLS or r < 0 or c < 0 or \
                (r, c) in ocean_set or \
                heights[r][c] < prev: return 
            
            ocean_set.add((r, c))

            dfs(r + 1, c, ocean_set, heights[r][c])
            dfs(r, c + 1, ocean_set, heights[r][c])
            dfs(r - 1, c, ocean_set, heights[r][c])
            dfs(r, c - 1, ocean_set, heights[r][c])


        for i in range(ROWS): 
            dfs(i, 0, pac_cells, 0)
            dfs(i, COLS - 1, atl_cells, 0)

        for j in range(COLS): 
            dfs(0, j, pac_cells, 0)
            dfs(ROWS - 1, j, atl_cells, 0)

        intersection = pac_cells & atl_cells
        return list(list(cell) for cell in intersection)


