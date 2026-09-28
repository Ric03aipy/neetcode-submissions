class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # log(m*n)=log(m)+log(n) --> Opzione 2. 1 sola ricerca binaria immaginando l'array flat
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        # L'unica attenzione da fare è che come beccare l'elemento: 
        # Supponiamo [[ , , , , ], [ , , , , ], [ , , , , ], [ , , , , pippo]]
        # target = pippo
        # m = 4, n = 5
        # pippo è matrix[3][4], ma è l'elemento mid=19 in un array flat, 3 = mid // n, 4 = mid % n
        # Ricorda che: // qui è valido perché i numeri sono positivi, int(a / b) arrotonda a zero sempre

        while left <= right: 
            mid = left + (right - left) // 2
            if matrix[mid // n][mid % n] == target: return True
            elif target > matrix[mid // n][mid % n]: left = mid + 1
            else: right = mid - 1
        
        return False
