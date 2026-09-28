class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        win = set()
        max_len = 0
        for idx, c in enumerate(s): 
            if c not in win: 
                win.add(c)
                max_len = max(len(win), max_len)
            else: 
                while c in win:
                    win.discard(s[i])
                    i += 1
                win.add(c)
        return max_len
