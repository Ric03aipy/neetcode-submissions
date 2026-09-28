class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0
        max_len = 0
        p = 0 # counter
        win = dict()
        while p < len(s): 
            # print(f"Inzio iter #{p}: {win}")
            if s[p] not in win or win[s[p]] == 0: 
                j += 1
                win[s[p]] = 1
                max_len = max(max_len, len([k for k in win if win[k] == 1]))
            else: 
                win[s[p]] += 1
                while win[s[p]] > 1: 
                    win[s[i]] -= 1
                    # print(f"modifiche: {win}")
                    i += 1
            # print(f"Fine iter #{p}: {win}")

            p += 1
            
        return max_len
        