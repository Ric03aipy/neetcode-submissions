class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # =================
        # ripetizione #1
        # =================

        s1_freq = [0] * 26
        for c in s1: s1_freq[ord(c) - ord('a')] += 1

        k = len(s1) # lunghezza della finestra
        for left in range(len(s2) - k + 1): 
            arr = [0] * 26
            right = left + k
            for c in s2[left:right]: arr[ord(c) - ord('a')] += 1
            if arr == s1_freq: return True
        return False