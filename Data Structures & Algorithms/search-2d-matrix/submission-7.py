class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # =====================
        # ripetizione #1
        # =====================
        
        # binary search on answer
        left, right = 0, len(matrix) - 1
        target_row = None
        while left <= right: 
            mid = left + (right - left) // 2
            # scansiono solo gli elementi [0] di ogni riga
            # la più stretta valida è quella che non supera il target visto l'ordine
            if matrix[mid][0] <= target: 
                target_row = mid
                left = mid + 1
            else: 
                right = mid - 1

        if target_row is None: return False

        # binary search
        left, right = 0, len(matrix[0]) - 1
        while left <= right: 
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target: return True
            if matrix[target_row][mid] > target: right = mid -1
            else: left = mid + 1
        
        return False