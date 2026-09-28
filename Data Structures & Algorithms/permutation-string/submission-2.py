class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Building frequency of chars in s1 - O(26) = O(1) in space, O(n) time
        freq = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"}
        for c in s1: freq[c] += 1 
        
        # Sliding window pattern - processing the first window -> required to build the initial map
        window = {} # observed chars 
        left = 0
        k = len(s1) # fixed size of a window - a substring is a consecutive sequence of chars
        sub = s2[left:left + k]
        sub_freq = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"} # O(1) in space as above
        for c in sub: sub_freq[c] += 1 
        if sub_freq == freq: return True
        
        # Sliding window pattern - sliding the window
        print(sub, sub_freq)
        for left in range(1, len(s2) - k + 1):
            right = left + k
            entering = s2[right - 1]
            leaving = s2[left - 1]
            sub_freq[leaving] -= 1
            sub_freq[entering] = sub_freq.get(entering, 0) + 1
            # check only leaving and entering freqs
            if sub_freq == freq: return True
            
            
        return False
