class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac_cells = set()
        atl_cells = set()

        def dfs(r, c, ocean_set): 

            if (r, c) in ocean_set: return 
            
            ocean_set.add((r, c))

            if r + 1 < ROWS and heights[r][c] <= heights[r + 1][c]: dfs(r + 1, c, ocean_set)
            if r - 1 >= 0 and heights[r][c] <= heights[r - 1][c]: dfs(r - 1, c, ocean_set)
            if c + 1 < COLS and heights[r][c] <= heights[r][c + 1]: dfs(r, c + 1, ocean_set)
            if c - 1 >= 0 and heights[r][c] <= heights[r][c - 1]: dfs(r, c - 1, ocean_set)


        for i in range(ROWS): 
            dfs(i, 0, pac_cells)
            dfs(i, COLS - 1, atl_cells)

        for j in range(COLS): 
            dfs(0, j, pac_cells)
            dfs(ROWS - 1, j, atl_cells)

        intersection = pac_cells & atl_cells
        return list(list(cell) for cell in intersection)


