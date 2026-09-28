class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ================
        # ripetizione # 1
        # ================

        res = []

        def dfs(path, opened, closed): 

            # Condizione di errore
            if closed > opened: return 
            # Condizione di successo
            if closed == n: res.append("".join(path))

            # Se posso aprire faccio la mossa
            if opened < n: 
                path.append("(")
                dfs(path, opened + 1, closed)
                path.pop()
            # Posso sempre chiudere, al massimo esco dopo per errore - tanto comunque mi serve anche se metto if closed < n
            path.append(")")
            dfs(path, opened, closed + 1)
            path.pop()

        dfs([], 0, 0)

        return res
