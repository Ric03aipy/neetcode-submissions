class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Caso base
        if not matrix or not matrix[0]: return []
        
        res = []

        # Definisco i limiti
        right, down, left, up = len(matrix[0]) - 1, len(matrix) - 1, 0, 0
        
        while left <= right and up <= down: 

            # Leggo dal limite sinistro al limite destro 
            c = left
            while c <= right:     
                res.append(matrix[up][c])
                c += 1
            up += 1

            # Leggo dal limite alto a quello basso 
            c = up
            while c <= down: 
                res.append(matrix[c][right])
                c += 1
            right -= 1 

            """
            Anche cambiando il while con and, il codice fallisce comunque sulle matrici non quadrate (rettangolari) perché i 
            4 movimenti interni vengono eseguiti tutti di fila senza verificare se la matrice è finita a metà del giro.
            """

            if not (up <= down and left <= right): break



            # Leggo dal limite destro a quello sinistro
            c = right
            while c >= left: 
                res.append(matrix[down][c])
                c -= 1 
            down -= 1

            # Leggo dal limite basso a quello alto - unico caso in cui non voglio l'ugualianza perché è il punto di partenza
            c = down 
            while c >= up: 
                res.append(matrix[c][left])
                c -= 1
            left += 1

        return res


