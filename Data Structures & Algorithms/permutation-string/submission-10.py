class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # =================
        # ripetizione #2
        # =================

        k = len(s1)

        # conto le frequenze di c
        f = {}
        for c in s1: f[c] = f.get(c, 0) + 1
        
        curr_win = {}
        n_match = 0
        for right, c in enumerate(s2): 
            left = right - k + 1
            curr_win[c] = curr_win.get(c, 0) + 1
            if c in f and curr_win[c] == f[c]: n_match += 1
            if n_match == len(f): return True
            if left < 0: continue
            was_eq = s2[left] in f and curr_win[s2[left]] == f[s2[left]]
            curr_win[s2[left]] -= 1
            if was_eq and curr_win[s2[left]] != f[s2[left]]: n_match -= 1

            # print(f, curr_win, f == curr_win, s2[left:right + 1])
            
        
        return False