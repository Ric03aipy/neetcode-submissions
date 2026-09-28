class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # Identifico un nodo con le sue cordinate (r, c) nella griglia. 
        # Costuisco la lista di adiacenza e la popolo con le connessioni. 
        adj_list = {(r, c): [] for r in range(rows) for c in range(cols) if grid[r][c] == "1" }
        for (r, c) in adj_list: 
            # Controllo le 4 direzioni : un nodo può avere al più 4 neighbour lungo le 2 direzioni 
            # Invece di fare il controllo su griglia che mi costringe a verificare i Bounds cerco solo tra i nodi "1"
            # che sono tutti segnati nel "grafo" adj_list
            if (r + 1, c) in adj_list: adj_list[(r, c)].append((r + 1, c))
            if (r - 1, c) in adj_list: adj_list[(r, c)].append((r - 1, c))
            if (r, c + 1) in adj_list: adj_list[(r, c)].append((r, c + 1))
            if (r, c - 1) in adj_list: adj_list[(r, c)].append((r, c - 1))
        
        # Ora adj_list è un grafo non diretto. 
        
        # dfs - serve letteralmente solo a marcare un nodo come visto o meno; il numero di dfs è il numero di "isole"
        visited = set()
        counter = 0
        def dfs(node:tuple[int, int]):
            
            if node in visited: return 
            visited.add(node)

            for neighbour in adj_list[node]: 
                dfs(neighbour)
        
        
        for node in adj_list: 
            if node not in visited: 
                counter += 1
                dfs(node)

        return counter