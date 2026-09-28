class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        win = set()
        max_len = 0
        for idx, c in enumerate(s): 
            while c in win:
                win.discard(s[i])
                i += 1
            win.add(c)
            max_len = max(max_len, len(win))
        return max_len
