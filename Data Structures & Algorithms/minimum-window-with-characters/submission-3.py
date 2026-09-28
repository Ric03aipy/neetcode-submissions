class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ======================
        # ripetizione #1
        # ======================
        res = ""

        t_freq = {}
        for c in t: t_freq[c] = t_freq.get(c, 0) + 1

        need = len(t_freq) # numero di caratteri unici
        have = 0 # aumenta solo quando un carattere utile ha raggiunto la frequenza giusta

        win = {} # qui invece conto la frequenza dei caratteri sotto osservazione

        left = 0
        min_len = float('inf')
        for right in range(len(s)): 

            # accumulo caratteri
            right_char = s[right]
            win[right_char] = win.get(right_char, 0) + 1
            # print(win)
            if right_char in t_freq and win[right_char] == t_freq[right_char]: 
                have += 1
                # if have == need: print(f"soddisfatta con {win}")

            while have == need:
            
                # calcola la lunghezza solo quando è valida
                if right-left < min_len:
                    res = s[left:right+1]
                    min_len = right-left
                # print(f"attuale res = {res}")

                # restringi
                left_char = s[left]
                win[left_char] = win.get(left_char, 0) - 1
                if left_char in t_freq and win[left_char] < t_freq[left_char]: have -= 1
                left += 1
        
        return res

                
                

                


            


            
