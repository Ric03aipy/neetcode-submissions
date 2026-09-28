class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # ================
        # ripetizione #1
        # ================

        def is_palindrome(seq) -> bool: return seq == seq[::-1]

        res:List[List[str]] = []

        def dfs(path:List[str], cut_idx):
            # path è una lista di sezioni palindrome
            if cut_idx == len(s): res.append(path[:])   
            
            for i in range(cut_idx, len(s)):
                candidate = s[cut_idx: i+1]
                if is_palindrome(candidate): 
                    path.append(candidate)
                    dfs(path, i + 1)
                    path.pop()

        dfs([], 0)
        return res
        