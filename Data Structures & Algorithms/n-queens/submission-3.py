class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        row_used = set()
        pos_diag_used = set()
        neg_diag_used = set()

        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(c): 

            if c == n: 
                res_el = []
                for row in board: res_el.append("".join(row))
                res.append(res_el)
                return 

            for r in range(n): 
                if r in row_used or r + c in pos_diag_used or r - c in neg_diag_used: continue
                row_used.add(r)
                pos_diag_used.add(r + c)
                neg_diag_used.add(r - c)
                board[r][c] = "Q"
                
                dfs(c + 1)

                board[r][c] = "."
                row_used.remove(r)
                pos_diag_used.remove(r + c)
                neg_diag_used.remove(r - c)


        dfs(0)

        return res