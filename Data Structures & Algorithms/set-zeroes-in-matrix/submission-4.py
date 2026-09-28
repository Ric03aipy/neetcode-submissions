class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        if not matrix: return 

        ROWS, COLS = len(matrix), len(matrix[0])

        # Una singola variabile che mi dice se la prima riga contiene uno 0 (speculare con colonna va bene lo stesso)
        # Però conviene la riga poiché leggo sempre per riga (per sfruttare cache hit per memoria sequenziale)
        rowZero = False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    # Marco i bordi per azzerare poi: distinguo tra caso riga == 0 e altri valori 
                    if i > 0: matrix[i][0] = 0
                    else: rowZero = True 
                    matrix[0][j] = 0

        # Controllo righe e colonne tranne quella sensibile a sovrapposizione delle variabile marcatore (0 ai bordi)
        for i in range(1, ROWS):
            for j in range(1, COLS): 
                # Se uno dei due bordi è 0 allora questa cella va azzerata
                if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0

        # Poiché ho scelto che la variabile rowZero si ricorda se la riga ha 0 se è attiva...
        # Se ho il valore a 0 sicuramente la colonna va azzerata
        if matrix[0][0] == 0:
            for i in range(ROWS): matrix[i][0] = 0
        # Se ho anche il valore rowZero a zero anche la riga va cancellata
        if rowZero: 
            for j in range(COLS): matrix[0][j] = 0
            
