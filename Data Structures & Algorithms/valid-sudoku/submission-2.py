class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(l: List[str]): 
            counter = set()
            for el in l: 
                if el in counter and el != ".": return False
                counter.add(el)
            return True

        for i in range(9): 
            # row i     
            row = board[i]

            # col i
            col = [row[i] for row in board]

            # block i: order 1-2-3 ; 4-5-6 ; 7-8-9
            block = []
            block_row = i // 3
            block_col = i % 3
            for j in range(3): 
                for k in range(3): 
                    block.append(board[3*block_row+j][3*block_col+k])
            # print(f"i={i}")
            # print(f"row={row}")
            # print(f"col={col}")
            # print(f"block={block}")
            
            if not (is_valid(row) and is_valid(col) and is_valid(block)):
                return False


        return True
