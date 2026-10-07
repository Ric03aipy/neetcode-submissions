class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # =============
        # ripetizione #1
        # =============
        
        if digits == "": return [] 

        vocab = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def dfs(path:List, digit_idx:int): 

            if digit_idx == len(digits): 
                res.append("".join(path))
                return 

            for n in vocab[digits[digit_idx]]:
                path.append(n) 
                dfs(path, digit_idx + 1)
                path.pop()

        dfs([], 0)
        return res