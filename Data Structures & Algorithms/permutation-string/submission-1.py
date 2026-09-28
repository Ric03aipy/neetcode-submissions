class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1) # fixed size of a window - a substring is a consecutive sequence of chars
        freq = {}
        for c in s1: freq[c] = freq.get(c, 0) + 1
        for i in range(len(s2) - k + 1):
            substring = s2[i:i+k]
            substring_freq = {}
            for c in substring: substring_freq[c] = substring_freq.get(c, 0) + 1
            if freq == substring_freq: return True
        return False
