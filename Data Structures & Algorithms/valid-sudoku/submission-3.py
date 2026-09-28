class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n^2) is linear for this problem!

        # idea: check for existance, if a value already exists then it's doubled and invalid

        # check for rows and cols
        
        for i in range(9):
            seen_col = set()
            seen_row = set()
            for j in range(9): 
                cell_row = board[i][j]
                if cell_row != ".":
                    if cell_row in seen_row: return False
                    else: seen_row.add(cell_row)
              
                cell_col = board[j][i]
                if cell_col != ".": 
                    if cell_col in seen_col: return False
                    else: seen_col.add(cell_col)

            # print(f"row{i} = {seen_row}")
            # print(f"col{i} = {seen_col}")


        # check for boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for a in range(3):
                    for b in range(3):
                        cell = board[i+a][j+b]
                        if cell != ".": 
                            if cell in box: return False
                            else: box.add(cell)
                # print(f"box ({i}, {j}) = {box}")
        return True
                