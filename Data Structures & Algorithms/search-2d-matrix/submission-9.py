class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # =====================
        # ripetizione #2
        # =====================

        # Definisco numero di righe e di colonne 
        m = len(matrix)
        n = len(matrix[0])

        # Ricerca binaria sulle righe per cercare la riga che contiene il target
        left, right = 0, m - 1
        target_row = None
        while left <= right: 
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target: 
                left = mid + 1
                target_row = mid
            else: right = mid - 1

        # Se non l'ho trovata allora so già che non c'è quel valore 
        if target_row is None: return False

        # Ricerca binaria sulla riga scelta
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target: return True
            if matrix[target_row][mid] < target: left = mid + 1
            else: right = mid - 1
        
        # Fallback
        return False
 
        
            