class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def is_attacking(r1, c1, r2, c2): # - O(1) ma deve essere chiamata fino a (n-1) volte per ogni inserimento
            # Stessa riga
            if r1 == r2: return True
            # Stessa colonna
            if c1 == c2: return True
            # Stessa diagonale: distanza orizzontale == distanza verticale
            if abs(r1 - r2) == abs(c1 - c2): return True
            # Altrimenti non si stanno attaccando
            return False

        res = [] 

        def dfs(path, c): # scorro su una sola dimensione, qui per colonna (le scacchiere non dipendono da questa logica - basta ruotare di 90° la scacchiera per ottenere le soluzioni per riga e viceversa)
            """
            path: contiene la lista delle posizioni. Per esempio [3,1,4,2] ovvero le regine si trovano in posizioni (3,1), (1,2), (4,3), (2,4)
            r: row index
            c: columns index
            """

            # Condizione di non validità - O(n)
            for i in range(len(path)-1):
                q_r, q_c = path[i]
                if is_attacking(q_r, q_c, *path[-1]): return 

            # Condizione di fine: ho piazzato una regina per colonna
            if len(path) == n: 
                res.append(path[:])
                return 

            # Le colonne le devo vedere tutte senza saltare nessuna, ma le righe posso scegliere di iniziare in modo 
            # Arbitrario, quindi devo farci un ciclo
            for i in range(n): # come in 'Permutations' io devo partire da 0, devo vederle tutte le righe

                # Mossa
                path.append((i, c))
                
                # Ricorsione
                dfs(path, c + 1)

                # Passo indietro
                path.pop()


        dfs([], 0)

        # input n = 4
        # res = [[(1, 0), (3, 1), (0, 2), (2, 3)], [(2, 0), (0, 1), (3, 2), (1, 3)]]

        # Qui costruisco il vero risutlato formattato come richiesto, tanto un costo (n^2) per un algoritmo esponenziale è contorno
        out = []
        for result in res: # result:List[tuple[int,int]] es. [(1, 0), (3, 1), (0, 2), (2, 3)]
            string_res = []
            for i in range(n): 
                row_string = ["Q" if row_val == i else "." for row_val, col_val in result]
                string_res.append("".join(row_string))
            out.append(string_res)
        return out

