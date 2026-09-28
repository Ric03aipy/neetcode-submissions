class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # log(m*n)=log(m)+log(n) --> Opzione 1. 2 ricerche binarie consecutive

        # 1. Ricerca binaria per trovare la riga giusta: 
        # - guardo il primo e l'ultimo elemento di una riga, se target è compreso tra essi ok
        # - altrimenti usa il principio della ricerca binaria per scremare il 50% alla volta
        up, down = 0, len(matrix) - 1 
        target_row = None
        while up <= down:
            mid = up + (down - up) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]: 
                target_row = mid
                break
            if target > matrix[mid][-1]: up = mid + 1
            elif target < matrix[mid][0]: down = mid - 1 
        # print(f"found at row: {target_row}")
        if target_row is None: return False
        # 2. Ricerca binaria per trovare la colonna giusta: la classica su array 1D
        left, right = 0, len(matrix[0]) - 1
        while left <= right: 
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target: return True
            elif matrix[target_row][mid] > target: right = mid - 1
            else: left = mid + 1

        return False
