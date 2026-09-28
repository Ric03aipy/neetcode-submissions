class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_c = {}
        for c in s: 
            seen_s[c] = seen_s.get(c, 0) + 1
        for c in t: 
            seen_c[c] = seen_c.get(c, 0) + 1
        return seen_s.items() == seen_c.items()

        