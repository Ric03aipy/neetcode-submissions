class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Matrice quadrata
        N = len(matrix)

        # Flip orizzontale
        for i in range(N // 2):
            matrix[i], matrix[N-1-i] = matrix[N-1-i], matrix[i]
        
        # Trasposizione
        for i in range(N): 
            for j in range(N):
                # Voglio trasporre solo mezza matrice
                if j < i: 
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            

