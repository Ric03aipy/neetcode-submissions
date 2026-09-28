class Solution:

    # SOLUZIONE: dfs multi sorgente con logica inversa - dall'oceano alle vette invece che da vette a oceano

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])

        # Tutti i punti a cui arrivo facendo straripare i 2 oceani
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_h):
            """Popola il set visitati: se visito un nodo partendo da celle pacifico so tutte le celle che sfociano in esso""" 
            
            # Conidizoni di invalidità: 1) invalidità cella 2) già visti 3) vincolo specifico sull'altezza
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r, c) in visited or 
                heights[r][c] < prev_h):
                return

            # Una cella valida qui è una cella che può arrivare all'oceano rispettivo
            visited.add((r, c))

            # Propagazione nelle 4 direzioni
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        # Scorrendo le righe posso vedere i bordi sx e dx 
        for i in range(ROWS): 
            dfs(i, 0, pacific, -1)
            dfs(i, COLS - 1, atlantic, -1)

        # Scorrendo le colonne posso vedere i bordi top e bottom 
        for j in range(COLS): 
            dfs(0, j, pacific, -1)
            dfs(ROWS - 1, j, atlantic, -1)

        # Per avere le celle toccate da entrambi serve l'intersezione tra quelle che sfociano in uno dei due singolarmente
        both = pacific & atlantic

        return [list(pair) for pair in both]


