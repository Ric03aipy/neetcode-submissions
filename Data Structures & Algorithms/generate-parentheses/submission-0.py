class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # You should aim for a solution as good or better than O(4^n / sqrt(n)) time and O(n) space, where n is the number of parenthesis pairs in the string.

        # COME SI CONTA UNA TALE COMLPESSITà COMPUTAZIONALE? (IN GENERALE è MOLTO STRANA IN TUTTI I PROBLEMI DI BACKTRACKING)


        res = [] 





        def backtrack(path, can_open, can_close): 

            if can_open == 0 and can_close == 0: 
                res.append(path[:])
                return 
 
            # condizione di invalidità 
            if can_close < can_open: return

            if can_open > 0 :
                path.append("(")
                backtrack(path, can_open - 1, can_close)
                path.pop()
            if can_close > 0: 
                path.append(")")
                backtrack(path, can_open, can_close - 1)
                path.pop()

        backtrack([], n, n)
        res = ["".join(el) for el in res]
        return res


