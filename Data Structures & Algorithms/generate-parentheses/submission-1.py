class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(path, count_open, count_close): 

            if count_open == n and count_close == n:
                res.append(path[:])

            if count_close > count_open: return 

            # niente for perché la decisione è binaria
            if count_open < n: 
                path.append("(")
                backtrack(path, count_open + 1, count_close)
                path.pop()
            
            if count_close < n: 
                path.append(")")
                backtrack(path, count_open, count_close + 1)
                path.pop()

        backtrack([], 0, 0)
        res = ["".join(el) for el in res]
        return res


