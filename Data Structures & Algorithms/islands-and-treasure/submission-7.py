class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
    
        APPROCCIO PIù EFFICIENTE CON PATTERN MULTI-SOURCE. 
        METTO NELLA CODA SUBITO TUTTI I TESORI E POI PROPAGO TUTTE LE ONDE INSIEME 1 LIVELLO ALLA VOLTA. 
        IN QUESTO MODO - E USNDO LO STESSO MECCANISMO DI DISTANZA SALVATA IN CODA - 
        UN NODO VERRà SEMPRE AGGIUNTO ALLA CODA DAL NODO TESORO PIù VICINO. 
        QUINDI IL CONTROLLO SARà: 'SE IL NODO è IN CODA O è 0 O è -1 ALLORA NON è VALIDO'
        """

        from collections import deque

        # Inizializzo la coda ai soli tesori - distanza 0 da se stessi
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    q.append((i, j, 0))

        # Eseguo la bfs: i nodi del livello 0 sono quelli
        seen = set() 
        while q: 
            r, c, d = q.popleft()
            seen.add((r, c))
            
            # Per la regola dedotta all'inizio "se viene modificato viene settato subito al minimo perché la dfs assegna la shallowest depth" allora posso non propagare su un nodo modificato
            if grid[r][c] not in (0, 2147483647) or grid[r][c] == -1: continue
            grid[r][c] = d
            
            # Condizioni di validità: 1) esiste la cella 2) non ho mai visto il nodo 3) mi conviene aggiornare 
            # Ma la 2) potrebbe essere assorbita dal controllo precedente
            if  r + 1 < len(grid) \
                and grid[r+1][c] > d+1: q.append((r+1,c,d+1))
            if  r - 1 >= 0 \
                and grid[r-1][c] > d+1: q.append((r-1,c,d+1))
            if  c + 1 < len(grid[0]) \
                and grid[r][c+1] > d+1: q.append((r,c+1,d+1))
            if  c - 1 >= 0 \
                and grid[r][c-1] > d+1: q.append((r,c-1,d+1))




    


