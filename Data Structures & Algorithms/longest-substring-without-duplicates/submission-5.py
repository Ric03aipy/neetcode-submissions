class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)): 
            # print(left, right, s[left], s[right], right-left+1, s[left: right+1])
            
            # ===== extend the window (for loop) =====
            if s[right] not in seen: 
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)
            else: 
                # ===== shrink the window ======
                # skip to the next equal character
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                # go to the first non equal character
                left += 1

        return max_len
        