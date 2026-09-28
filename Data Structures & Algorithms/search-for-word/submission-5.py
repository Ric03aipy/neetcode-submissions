class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ================
        # ripetizione #1 
        # ================

        

        def dfs(word_idx, r, c, seen): 

            # I contronti si fanno da 0 a len(word) - 1, se li passa tutti allora la parola c'è
            if word_idx == len(word): return True

            # Condizioni di non validità
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])): return False
            if (r, c) in seen: return False
            if word[word_idx] != board[r][c]: return False

            # Esplorazione dei passi successivi
            seen.add((r, c))
            res =   dfs(word_idx + 1, r + 1, c, seen) or \
                    dfs(word_idx + 1, r - 1, c, seen) or \
                    dfs(word_idx + 1, r, c + 1, seen) or \
                    dfs(word_idx + 1, r, c - 1, seen) 
            seen.remove((r, c))
            return res


        # Il punto di partenza deve essere una cella qualunque
        for i in range(len(board)): 
            for j in range(len(board[0])):
                if dfs(0, i, j, set()): return True
        return False