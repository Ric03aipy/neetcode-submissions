class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        import heapq

        que = [(0, 0, 0)] # (costo temporale finora, riga, colonna)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        min_time = 0
        while que: 
            costo_di_spostamento, r, c = heapq.heappop(que)
            if r == c == len(grid) - 1: return max(min_time, grid[r][c])
            if (r, c) in visited: continue
            visited.add((r, c))
            min_time = max(min_time, grid[r][c])
            # Esplorazione dei vicini su griglia: 4 direzioni
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS: continue
                # Lazy deletion: metto i nodi nuovi anche se sono già in coda usufruendo della proprietò di priorità
                costo = max(grid[r][c], grid[nr][nc])
                heapq.heappush(que, (costo, nr, nc))
        return min_time


