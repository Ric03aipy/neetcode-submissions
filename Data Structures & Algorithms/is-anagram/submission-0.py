class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = sorted(list(s)) 
        t = sorted(list(t))
        for idx, c in enumerate(s): 
            if c != t[idx]: return False
        return True