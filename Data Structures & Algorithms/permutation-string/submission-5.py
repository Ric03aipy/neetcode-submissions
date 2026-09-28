class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2): return False
        
        # Building frequency of chars in s1 - O(26) = O(1) in space, O(n) time
        freq = [0]*26
        for c in s1: freq[ord(c)-ord('a')] += 1 
        
        # Sliding window pattern - processing the first window -> required to build the initial map
        window = {} # observed chars 
        left = 0
        k = len(s1) # fixed size of a window - a substring is a consecutive sequence of chars
        sub = s2[left:left + k]
        sub_freq = [0]*26 # O(1) in space as above
        for c in sub: sub_freq[ord(c)-ord('a')] += 1 
        if sub_freq == freq: return True

        # Sliding window pattern - sliding the window
        for left in range(1, len(s2) - k + 1):
            right = left + k
            entering = s2[right - 1]
            leaving = s2[left - 1]
            sub_freq[ord(leaving) - ord('a')] -= 1
            sub_freq[ord(entering) - ord('a')] += 1
            # check only leaving and entering freqs
            if sub_freq == freq: return True
            
        return False
