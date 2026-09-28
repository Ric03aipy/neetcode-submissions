class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        arr = [0] * 26
        for c in s1: arr[ord(c) - ord('a')] += 1
        
        arr2 = [0] * 26
        for right in range(len(s2)): 
            left = right - len(s1) + 1
            arr2[ord(s2[right]) - ord('a')] += 1
            if arr == arr2: return True
            if left < 0: continue
            arr2[ord(s2[left]) - ord('a')] -= 1
        
        return False
        